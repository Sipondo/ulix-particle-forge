from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from calc_conf import *
from calc_node_base import *


@register_node(OP_NODE_TRIGGER)
class Node_Trigger(SystemNode):
    icon = "icon/trigger.png"
    op_code = OP_NODE_TRIGGER
    op_title = "Trigger"
    content_label_objname = "node_trigger"

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
                    [
                        "multitoggle",
                        "",
                        [["Hit", "hit", 0.0], ["", "hit_enabled", ""],],
                    ],
                    [
                        "multitoggle",
                        "",
                        [["Sound", "sound_path", ""], ["", "sound_enabled", ""],],
                    ],
                    [
                        "multitoggle",
                        "",
                        [["Shake", "shake", 0.5], ["", "shake_enabled", ""],],
                    ],
                ],
            ],
            [
                "box",
                "Darkness",
                [
                    ["toggle", "Dark Enabled", "dark_enabled", ""],
                    ["toggle", "Dark Recover", "dark_recover", True],
                    ["line", "Dark", "dark", 0.5],
                    [
                        "multitoggle",
                        "",
                        [
                            ["Dark Speed", "dark_speed", 1.0],
                            ["", "dark_speed_enabled", True],
                        ],
                    ],
                ],
            ],
        ]
