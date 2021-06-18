from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from calc_conf import *
from calc_node_base import *


@register_node(OP_NODE_CAMRAIL)
class Node_Camrail(SystemNode):
    icon = "icon/camera.png"
    op_code = OP_NODE_CAMRAIL
    op_title = "Camrail"
    content_label_objname = "node_camrail"

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
                    ["line", "Mirror", "mirror", "mirrornegative"],
                    ["line", "Delay", "delay", 0],
                    ["line", "Duration", "duration", 1.5],
                    ["line", "Source Angle", "source", 100],
                    ["line", "Target Angle", "target", 200],
                    ["line", "Equation", "equation", "x"],
                ],
            ],
        ]
