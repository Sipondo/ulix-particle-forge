from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from calc_conf import *
from calc_node_base import *


@register_node(OP_NODE_FILTER)
class Node_Filter(SystemNode):
    icon = "icon/filter.png"
    op_code = OP_NODE_FILTER
    op_title = "Filter"
    content_label_objname = "node_filter"

    def __init__(self, scene):
        super().__init__(scene, inputs=[1], outputs=[0])
        self.eval()
        self.setBinding()

    def setBinding(self):
        self.content.binding = [
            [
                "box",
                "General",
                [
                    [
                        "multi",
                        "",
                        [
                            ["Min life", "min_life", -1000],
                            ["Max life", "max_life", 1000],
                        ],
                    ],
                ],
            ],
            [
                "box",
                "Position",
                [
                    [
                        "multi",
                        "",
                        [["Min x", "min_x", -1000], ["Max x", "max_x", 1000]],
                    ],
                    [
                        "multi",
                        "",
                        [["Min y", "min_y", -1000], ["Max y", "max_y", 1000]],
                    ],
                    [
                        "multi",
                        "",
                        [["Min z", "min_z", -1000], ["Max z", "max_z", 1000]],
                    ],
                ],
            ],
            [
                "box",
                "Velocity",
                [
                    [
                        "multi",
                        "",
                        [["Min x", "min_vel_x", -1000], ["Max x", "max_vel_x", 1000]],
                    ],
                    [
                        "multi",
                        "",
                        [["Min y", "min_vel_y", -1000], ["Max y", "max_vel_y", 1000]],
                    ],
                    [
                        "multi",
                        "",
                        [["Min z", "min_vel_z", -1000], ["Max z", "max_vel_z", 1000]],
                    ],
                ],
            ],
        ]
