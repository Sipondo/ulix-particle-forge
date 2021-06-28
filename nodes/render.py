from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from calc_conf import *
from calc_node_base import *


@register_node(OP_NODE_RENDER)
class Node_Render(SystemNode):
    icon = "icon/particle.png"
    op_code = OP_NODE_RENDER
    op_title = "Render"
    content_label_objname = "node_render"

    def __init__(self, scene):
        super().__init__(scene, inputs=[2], outputs=[])
        self.eval()
        self.setBinding()

    def setBinding(self):
        self.content.binding = [
            [
                "box",
                "General",
                [
                    ["line", "Filename", "file", "scorch_01"],
                    ["line", "Equation", "equation", "Add"],
                    ["line", "Noise", "noise", 1.0],
                    ["line", "Opacity", "opacity", 1.0],
                    ["toggle", "Rotation by Velocity", "rotvel", ""],
                ],
            ],
        ]
