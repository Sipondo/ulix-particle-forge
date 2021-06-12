from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from calc_conf import *
from calc_node_base import *


@register_node(OP_NODE_INPUT)
class Node_Input(SystemNode):
    icon = "icon/in.png"
    op_code = OP_NODE_INPUT
    op_title = "Input"
    content_label_objname = "node_input"

    def __init__(self, scene):
        super().__init__(scene, inputs=[], outputs=[0])
        self.eval()
        self.setBinding()

    def setBinding(self):
        self.content.binding = [
            ["box", "General", [["line", "Duration", "duration", 1.0],],],
        ]
