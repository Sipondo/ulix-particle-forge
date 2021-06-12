from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from calc_conf import *
from calc_node_base import *


@register_node(OP_NODE_SHIFT)
class Node_Shift(SystemNode):
    icon = "icon/shift.png"
    op_code = OP_NODE_SHIFT
    op_title = "Shift"
    content_label_objname = "node_shift"

    def __init__(self, scene):
        super().__init__(scene, inputs=[1], outputs=[1])
        self.eval()
        self.setBinding()

    def setBinding(self):
        self.content.binding = [
            [
                "box",
                "General",
                [
                    [
                        "multitoggle",
                        "",
                        [
                            ["Life", "life", 0.0],
                            ["Life σ", "life_range", 0.0],
                            ["O", "abs_life", False],
                        ],
                    ],
                    [
                        "multitoggle",
                        "",
                        [
                            ["Size", "size", 0.0],
                            ["Size σ", "size_range", 0.0],
                            ["O", "abs_size", False],
                        ],
                    ],
                ],
            ],
            [
                "box",
                "Position",
                [
                    [
                        "multitoggle",
                        "Pos",
                        [
                            ["x", "pos_x", 0],
                            ["x σ", "pos_range_x", 0],
                            ["O", "abs_pos_x", False],
                        ],
                    ],
                    [
                        "multitoggle",
                        "Pos",
                        [
                            ["y", "pos_y", 0],
                            ["y σ", "pos_range_y", 0],
                            ["O", "abs_pos_y", False],
                        ],
                    ],
                    [
                        "multitoggle",
                        "Pos",
                        [
                            ["z", "pos_z", 0],
                            ["z σ", "pos_range_z", 0],
                            ["O", "abs_pos_z", False],
                        ],
                    ],
                ],
            ],
            [
                "box",
                "Velocity",
                [
                    [
                        "multitoggle",
                        "Vel",
                        [
                            ["x", "vel_x", 0],
                            ["x σ", "vel_range_x", 0],
                            ["O", "abs_vel_x", False],
                        ],
                    ],
                    [
                        "multitoggle",
                        "Vel",
                        [
                            ["y", "vel_y", 0],
                            ["y σ", "vel_range_y", 0],
                            ["O", "abs_vel_y", False],
                        ],
                    ],
                    [
                        "multitoggle",
                        "Vel",
                        [
                            ["z", "vel_z", 0],
                            ["z σ", "vel_range_z", 0],
                            ["O", "abs_vel_z", False],
                        ],
                    ],
                ],
            ],
            [
                "box",
                "Rotation",
                [
                    ["multi", "", [["Value", "rot", 0], ["Range", "rot_range", 0]]],
                    [
                        "multi",
                        "",
                        [["Velocity", "rot_vel", 0], ["Range", "rot_vel_range", 0]],
                    ],
                ],
            ],
            [
                "box",
                "Colour",
                [
                    [
                        "multitoggle",
                        "Red",
                        [
                            ["", "col_r", 0],
                            ["r σ", "col_range_r", 0],
                            ["O", "abs_col_r", False],
                        ],
                    ],
                    [
                        "multitoggle",
                        "Green",
                        [
                            ["", "col_g", 0],
                            ["g σ", "col_range_g", 0],
                            ["O", "abs_col_g", False],
                        ],
                    ],
                    [
                        "multitoggle",
                        "Blue",
                        [
                            ["", "col_b", 0],
                            ["b σ", "col_range_b", 0],
                            ["O", "abs_col_b", False],
                        ],
                    ],
                ],
            ],
        ]
