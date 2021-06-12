from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from calc_conf import *
from nodeeditor.utils import dumpException


class InputBoxWrapper(QFrame):
    def __init__(self, node, binding, parent=None):
        super().__init__(parent)
        self.setFrameStyle(6)  # "border:1px solid rgb(90, 90, 90); ")
        self.layout = QVBoxLayout()
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        self.w_toggle = QPushButton(binding[1])
        self.w_toggle.setCheckable(True)
        self.w_toggle.toggle()

        self.w_toggle.clicked.connect(
            lambda: self.w_contents.show()
            if self.w_toggle.isChecked()
            else self.w_contents.hide()
        )

        self.layout.addWidget(self.w_toggle)

        self.w_contents = InputBox(node, binding[2])
        # self.w_contents.hide()
        self.layout.addWidget(self.w_contents)


class InputBox(QFrame):
    def __init__(self, node, binding, parent=None):
        super().__init__(parent)
        # self.setFrameStyle(6)  # "border:1px solid rgb(90, 90, 90); ")
        self.layout = QVBoxLayout()
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        for b in binding:
            self.layout.addWidget(INPUT_DICT[b[0]](node, b))


class MultiInputLine(QWidget):
    def __init__(self, node, binding, parent=None):
        super().__init__(parent)
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(5, 5, 5, 5)
        self.setLayout(self.layout)

        length = len(binding[2])
        self.layout.addWidget(QLabel(binding[1]))

        for i in range(length):
            b = binding[2][i]
            self.layout.addWidget(QLabel(b[0]))
            createInput(self.layout, node, b[1], b[2])


class MultiInputToggleLine(QWidget):
    def __init__(self, node, binding, parent=None):
        super().__init__(parent)
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(5, 5, 5, 5)
        self.setLayout(self.layout)

        length = len(binding[2])
        self.layout.addWidget(QLabel(binding[1]))

        for i in range(length - 1):
            b = binding[2][i]
            self.layout.addWidget(QLabel(b[0]))
            createInput(self.layout, node, b[1], b[2])

        b = binding[2][-1]
        value = node.getInputValue(b[1], b[2])
        self.layout.addWidget(QLabel(b[0]))
        widget = QCheckBox()
        widget.setChecked(bool(value))
        widget.stateChanged.connect(
            lambda x: node.setInputValue(b[1], widget.isChecked())
        )
        self.layout.addWidget(widget)


class InputLine(QWidget):
    def __init__(self, node, binding, parent=None):
        super().__init__(parent)
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(5, 5, 5, 5)
        self.setLayout(self.layout)

        self.layout.addWidget(QLabel(binding[1]))
        createInput(self.layout, node, binding[2], binding[3])


# class InputDropList(QWidget):
#     def __init__(self, node, binding, parent=None):
#         super().__init__(parent)
#         self.layout = QHBoxLayout()
#         self.layout.setContentsMargins(5, 5, 5, 5)
#         self.setLayout(self.layout)
#
#         self.layout.addWidget(QLabel(binding[1]))
#         createInput(self.layout, node, binding[2], binding[3])


class widgetContent(QWidget):
    def __init__(self, node, binding, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        for b in binding:
            self.layout.addWidget(INPUT_DICT[b[0]](node, b))


INPUT_DICT = {
    "line": InputLine,
    "multi": MultiInputLine,
    "multitoggle": MultiInputToggleLine,
    "box": InputBoxWrapper,
}


def createInput(layout, node, tag, base):
    value = node.getInputValue(tag, base)
    widget = QLineEdit(str(value))
    widget.textChanged.connect(lambda x: node.setInputValue(tag, widget.text()))
    layout.addWidget(widget)


class QDMPropListbox(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.list_items = []
        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignTop)
        self.setLayout(self.layout)

        self.setMinimumWidth(200)
        self.content = None

    def updateSelection(self, selected_items):
        if self.content:
            self.content.setParent(None)
        try:
            selected_items[0].content.fields
        except Exception:
            print("No fields!")
            return
        if len(selected_items) == 1:
            self.content = widgetContent(
                selected_items[0].content, selected_items[0].content.binding
            )
            self.layout.addWidget(self.content)
