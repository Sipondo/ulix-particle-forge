from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from calc_conf import *
from calc_node_base import *


@register_node(OP_NODE_IMAGE)
class Node_Image(SystemNode):
    icon = "icon/image.png"
    op_code = OP_NODE_IMAGE
    op_title = "Image"
    content_label_objname = "node_image"

    def __init__(self, scene):
        super().__init__(scene, inputs=[], outputs=[2])
        self.eval()
        self.setBinding()

    def setBinding(self):
        self.content.binding = [
            ["box", "General", [["line", "Filename", "file", "scorch_01"]]]
        ]
