from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from calc_conf import *
from calc_node_base import *


@register_node(OP_NODE_EMIT)
class Node_Emit(SystemNode):
    icon = "icon/emit.png"
    op_code = OP_NODE_EMIT
    op_title = "Emit"
    content_label_objname = "node_emit"

    def __init__(self, scene):
        super().__init__(scene, inputs=[0], outputs=[])
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
                        [["Life", "life", 5.0], ["Life σ", "life_range", 0.0]],
                    ],
                    [
                        "multi",
                        "",
                        [["Size", "size", 1.0], ["Size σ", "size_range", 0.0]],
                    ],
                ],
            ],
            [
                "box",
                "Emission",
                [
                    ["line", "Duration", "duration", 1.5],
                    ["line", "Count", "count", 100],
                ],
            ],
            [
                "box",
                "Position",
                [
                    ["multi", "Pos", [["x", "pos_x", -1], ["x σ", "pos_range_x", 0]],],
                    ["multi", "Pos", [["y", "pos_y", 0], ["y σ", "pos_range_y", 0]],],
                    ["multi", "Pos", [["z", "pos_z", 0], ["z σ", "pos_range_z", 0]],],
                ],
            ],
            [
                "box",
                "Velocity",
                [
                    ["multi", "Vel", [["x", "vel_x", 6], ["x σ", "vel_range_x", 0]],],
                    ["multi", "Vel", [["y", "vel_y", 0], ["y σ", "vel_range_y", 0]],],
                    ["multi", "Vel", [["z", "vel_z", 0], ["z σ", "vel_range_z", 0]],],
                ],
            ],
            [
                "box",
                "Rotation",
                [
                    ["multi", "", [["Value", "rot", 0], ["Range", "rot_range", 360]]],
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
                    ["multi", "Red", [["", "col_r", 1], ["r σ", "col_range_r", 0]],],
                    ["multi", "Green", [["", "col_g", 1], ["g σ", "col_range_g", 0]],],
                    ["multi", "Blue", [["", "col_b", 1], ["b σ", "col_range_b", 0]],],
                ],
            ],
        ]
