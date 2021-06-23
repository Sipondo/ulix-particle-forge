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
        super().__init__(scene, inputs=[], outputs=[])
        self.eval()
        self.setBinding()

    def setBinding(self):
        self.content.binding = [
            [
                "box",
                "Emission",
                [
                    ["line", "Delay", "delay", 0],
                    ["line", "Duration", "duration", 0.9],
                    ["line", "Count", "count", 1],
                ],
            ],
            [
                "box",
                "General",
                [
                    ["line", "Mirror", "mirror", "mirrornegative"],
                    ["line", "Target Angle", "target", 20],
                    ["line", "Speed", "speed", 1],
                    ["line", "Friction", "friction", 3],
                ],
            ],
        ]
