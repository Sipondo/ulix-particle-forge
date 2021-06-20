from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from calc_conf import *
from calc_node_base import *


@register_node(OP_NODE_ACTOR)
class Node_Actor(SystemNode):
    icon = "icon/shift.png"
    op_code = OP_NODE_ACTOR
    op_title = "Actor"
    content_label_objname = "node_actor"

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
                    ["toggle", "Continuous", "continuous", False],
                ],
            ],
            [
                "box",
                "User",
                [
                    ["toggle", "User Enabled", "user_enabled", ""],
                    ["toggle", "User Recover", "user_recover", True],
                    [
                        "multitoggle",
                        "",
                        [
                            ["User Speed", "user_speed", 1.0],
                            ["", "user_speed_enabled", True],
                        ],
                    ],
                    ["line", "x", "user_x", -1],
                    ["line", "y", "user_y", 0],
                    ["line", "z", "user_z", 0],
                ],
            ],
            [
                "box",
                "Target",
                [
                    ["toggle", "Target Enabled", "target_enabled", ""],
                    ["toggle", "Target Recover", "target_recover", True],
                    [
                        "multitoggle",
                        "",
                        [
                            ["Target Speed", "target_speed", 1.0],
                            ["", "target_speed_enabled", True],
                        ],
                    ],
                    ["line", "x", "target_x", 1],
                    ["line", "y", "target_y", 0],
                    ["line", "z", "target_z", 0],
                ],
            ],
        ]
