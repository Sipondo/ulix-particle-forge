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
                    ["line", "Duration", "duration", 1.5],
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
                        [["Hit", "hit_strength", 0.0], ["", "hit_enabled", ""],],
                    ],
                    [
                        "multitoggle",
                        "",
                        [["Sound", "sound_path", ""], ["", "sound_enabled", ""],],
                    ],
                ],
            ],
        ]
