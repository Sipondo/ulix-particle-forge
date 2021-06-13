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
        super().__init__(scene, inputs=[1, 2], outputs=[])
        self.eval()
        self.setBinding()

    def setBinding(self):
        self.content.binding = [
            [
                "box",
                "General",
                [
                    ["line", "Equation", "equation", "Add"],
                    ["line", "Depth", "depth", 0],
                    ["line", "Max Count", "max_count", 10000],
                    ["line", "Opacity", "opacity", 1.0],
                    ["line", "Frequency", "render_frequency", 200],
                ],
            ],
            [
                "box",
                "Blur",
                [
                    ["line", "Count", "blur_count", 3],
                    ["line", "Delay", "blur_delay", 0.1],
                ],
            ],
        ]