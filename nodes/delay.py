from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from calc_conf import *
from calc_node_base import *


@register_node(OP_NODE_DELAY)
class Node_Delay(SystemNode):
    icon = "icon/delay.png"
    op_code = OP_NODE_DELAY
    op_title = "Delay"
    content_label_objname = "node_delay"

    def __init__(self, scene):
        super().__init__(scene, inputs=[0], outputs=[0])
        self.eval()
        self.setBinding()

    def setBinding(self):
        self.content.binding = [
            ["box", "General", [["line", "Duration", "duration", 1.0],],],
        ]
