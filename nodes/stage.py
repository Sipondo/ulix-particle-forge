from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from calc_conf import *
from calc_node_base import *


@register_node(OP_NODE_STAGE)
class Node_System(SystemNode):
    icon = "icon/system.png"
    op_code = OP_NODE_STAGE
    op_title = "Stage"
    content_label_objname = "node_stage"

    def __init__(self, scene):
        super().__init__(scene, inputs=[0], outputs=[0])
        self.eval()
        self.setBinding()

    def setBinding(self):
        self.content.binding = []
