from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from calc_conf import *
from calc_node_base import *


@register_node(OP_NODE_OUTPUT)
class Node_Output(SystemNode):
    icon = "icon/out.png"
    op_code = OP_NODE_OUTPUT
    op_title = "Output"
    content_label_objname = "node_output"

    def __init__(self, scene):
        super().__init__(scene, inputs=[0], outputs=[])
        self.eval()
        self.setBinding()

    def setBinding(self):
        self.content.binding = []
