from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from calc_conf import *
from calc_node_base import *


@register_node(OP_NODE_EQUATION)
class Node_Equation(SystemNode):
    icon = "icon/link.png"
    op_code = OP_NODE_EQUATION
    op_title = "Equation"
    content_label_objname = "node_equation"

    def __init__(self, scene):
        super().__init__(scene, inputs=[], outputs=[])
        self.eval()
        self.setBinding()

    def setBinding(self):
        self.content.binding = [
            [
                "box",
                "General",
                [
                    ["line", "Label", "label", "eq"],
                    ["line", "Equation", "equation", "t"],
                ],
            ],
        ]
