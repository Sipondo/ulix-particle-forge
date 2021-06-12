LISTBOX_MIMETYPE = "application/x-item"

OP_NODE_INPUT = 1
OP_NODE_OUTPUT = 2
OP_NODE_IMAGE = 3
OP_NODE_PARTICLE = 4
OP_NODE_CAMERA = 5
OP_NODE_DELAY = 6
OP_NODE_FILTER = 7
OP_NODE_STAGE = 8
OP_NODE_EMIT = 9
OP_NODE_SHIFT = 10
OP_NODE_TRIGGER = 11

CALC_NODES = {}


class ConfException(Exception):
    pass


class InvalidNodeRegistration(ConfException):
    pass


class OpCodeNotRegistered(ConfException):
    pass


def register_node_now(op_code, class_reference):
    if op_code in CALC_NODES:
        raise InvalidNodeRegistration(
            "Duplicite node registration of '%s'. There is already %s"
            % (op_code, CALC_NODES[op_code])
        )
    CALC_NODES[op_code] = class_reference


def register_node(op_code):
    def decorator(original_class):
        register_node_now(op_code, original_class)
        return original_class

    return decorator


def get_class_from_opcode(op_code):
    if op_code not in CALC_NODES:
        raise OpCodeNotRegistered("OpCode '%d' is not registered" % op_code)
    return CALC_NODES[op_code]


# import all nodes and register them
from nodes import *
