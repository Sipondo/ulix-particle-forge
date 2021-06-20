from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from calc_conf import *
from calc_node_base import *
from numpy.random import randint


@register_node(OP_NODE_STAGE)
class Node_Stage(SystemNode):
    icon = "icon/system.png"
    op_code = OP_NODE_STAGE
    op_title = "Stage"
    content_label_objname = "node_stage"

    def __init__(self, scene):
        super().__init__(scene, inputs=[], outputs=[0, 1, 2, 3])
        self.eval()
        self.setBinding()

    def setBinding(self):
        self.content.binding = [
            [
                "box",
                "General",
                [["line", "Stage ID", "stage", randint(100000000)]],
            ]  # TODO: replace as this is ugly but sufficient
        ]
