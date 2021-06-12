from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from calc_conf import *
from calc_node_base import *


@register_node(OP_NODE_PARTICLE)
class Node_Particle(SystemNode):
    icon = "icon/particle.png"
    op_code = OP_NODE_PARTICLE
    op_title = "Particle"
    content_label_objname = "node_particle"

    def __init__(self, scene):
        super().__init__(scene, inputs=[1, 2], outputs=[0, 1])
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
                "Acceleration",
                [
                    ["line", "x", "acc_x", 0],
                    ["line", "y", "acc_y", 0],
                    ["line", "z", "acc_z", 0],
                ],
            ],
            [
                "box",
                "Gravity",
                [
                    ["line", "x", "grav_x", 0],
                    ["line", "y", "grav_y", 0],
                    ["line", "z", "grav_z", 0],
                    ["line", "Force", "grav_force", 0.0],
                    ["line", "Exponent", "grav_exponent", 0.5],
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
