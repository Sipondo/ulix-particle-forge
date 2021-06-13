# from PyQt5.QtCore import *
# from PyQt5 import QtWidgets
# from calc_conf import *
# from calc_node_base import *


# # @register_node(OP_NODE_TRANSFORM)
# class Node_Transform(SystemNode):
#     icon = "icon/particle.png"
#     op_code = OP_NODE_TRANSFORM
#     op_title = "Transform"
#     content_label_objname = "node_transform"

#     def __init__(self, scene):
#         super().__init__(scene, inputs=[1], outputs=[])
#         self.eval()
#         self.setBinding()

#     def setBinding(self):
#         self.content.binding = [
#             [
#                 "box",
#                 "Acceleration",
#                 [
#                     ["line", "x", "acc_x", 0],
#                     ["line", "y", "acc_y", 0],
#                     ["line", "z", "acc_z", 0],
#                 ],
#             ],
#             [
#                 "box",
#                 "Gravity",
#                 [
#                     ["line", "x", "grav_x", 0],
#                     ["line", "y", "grav_y", 0],
#                     ["line", "z", "grav_z", 0],
#                     ["line", "Force", "grav_force", 0.0],
#                     ["line", "Exponent", "grav_exponent", 0.5],
#                 ],
#             ],
#         ]
