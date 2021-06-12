from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from calc_conf import *
from calc_node_base import *


@register_node(OP_NODE_CAMERA)
class Node_Camera(SystemNode):
    icon = "icon/camera.png"
    op_code = OP_NODE_CAMERA
    op_title = "Camera"
    content_label_objname = "node_camera"

    def __init__(self, scene):
        super().__init__(scene, inputs=[0], outputs=[0])
        self.eval()
        self.setBinding()

    def setBinding(self):
        self.content.binding = [
            [
                "box",
                "General",
                [
                    ["line", "Duration", "duration", 1.5],
                    ["line", "Source Angle", "source", 100],
                    ["line", "Target Angle", "target", 200],
                    ["line", "Speed", "Speed", 10],
                    ["line", "Speed", "Friction", 3],
                ],
            ],
        ]
