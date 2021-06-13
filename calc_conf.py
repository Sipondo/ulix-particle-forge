import math
import hashlib
from typing import Dict, List
from pathlib import Path


class Int4Hash:
    BYTES = 4
    BITS = BYTES * 8
    BITS_MINUS1 = BITS - 1
    MIN = -(2 ** BITS_MINUS1)
    MAX = 2 ** BITS_MINUS1 - 1

    @classmethod
    def as_dict(cls, texts: List[str]) -> Dict[int, str]:
        return {cls.as_int(text): text for text in texts}  # Intentionally reversed.

    @classmethod
    def as_int(cls, text: str) -> int:
        seed = text.encode()
        hash_digest = hashlib.shake_128(seed).digest(cls.BYTES)
        hash_int = int.from_bytes(hash_digest, byteorder="big", signed=True)
        assert cls.MIN <= hash_int <= cls.MAX
        return hash_int

    @classmethod
    def as_list(cls, texts: List[str]) -> List[int]:
        return [cls.as_int(text) for text in texts]


LISTBOX_MIMETYPE = "application/x-item"

OP_NODE_IMAGE = 3
OP_NODE_RENDER = 4
OP_NODE_CAMERA = 5
OP_NODE_DELAY = 6
OP_NODE_FILTER = 7
OP_NODE_STAGE = 8
OP_NODE_EMIT = 9
OP_NODE_SHIFT = 10
OP_NODE_TRIGGER = 11
OP_NODE_TRANSFORM = Int4Hash.as_int("transform")
print(OP_NODE_TRANSFORM)

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
        raise OpCodeNotRegistered(f"OpCode '{op_code}' is not registered")
    return CALC_NODES[op_code]


# import all nodes and register them
from nodes import *

from calc_node_base import *


binding = [
    [
        "box",
        "Acceleration",
        [
            ["line", "x", "acc_x", 0],
            ["line", "y", "acc_y", 0],
            ["line", "z", "acc_z", 0],
        ],
    ],
    [
        "box",
        "Gravity",
        [
            ["line", "x", "grav_x", 0],
            ["line", "y", "grav_y", 0],
            ["line", "z", "grav_z", 0],
            ["line", "Force", "grav_force", 0.0],
            ["line", "Exponent", "grav_exponent", 0.5],
        ],
    ],
]


# # creating class dynamically
# Node_Transform = type(
#     "Node_Transform",
#     (SystemNode,),
#     {
#         # constructor
#         # data members
#         "icon": "icon/particle.png",
#         "op_code": OP_NODE_TRANSFORM,
#         "op_title": "Transform",
#         "content_label_objname": "node_transform",
#         "binding": binding,
#     },
# )

# register_node_now(OP_NODE_TRANSFORM, Node_Transform)

GeoNodes = {}

for blockfile in Path("/resources/shader/p4geoblocks").glob("*.glsl"):
    with open(blockfile, "r") as infile:
        geoblock = infile.read()
    # print(blockfile.stem)
    constants = geoblock.split("// CONSTANTS")[1].split("// CONSTANTS_END")[0].strip()

    # print(constants.split("\n"))

    binding = []
    box = []

    for line in constants.split("\n"):
        if line[:5] == "// --":
            box = ["box", line[6:].strip(), []]
            binding.append(box)
            continue

        perc_parts = line.split("%")
        typ = perc_parts[0]
        varn = perc_parts[1]
        value = perc_parts[2].split("=")[1].split(";")[0].strip()

        if typ in ("float", "int",):
            box[2].append(["line", varn.replace("_", " ").capitalize(), varn, value])
        if typ == "vec3":
            value = value.split("(")[1].split(")")[0].strip().split(",")
            box[2].append(
                [
                    "line",
                    f'{varn.replace("_", " ").capitalize()} x',
                    f"{varn}_X",
                    value[0],
                ]
            )
            box[2].append(
                [
                    "line",
                    f'{varn.replace("_", " ").capitalize()} y',
                    f"{varn}_Y",
                    value[1],
                ]
            )
            box[2].append(
                [
                    "line",
                    f'{varn.replace("_", " ").capitalize()} z',
                    f"{varn}_Z",
                    value[2],
                ]
            )

    name = " ".join(
        [
            x.capitalize()
            for x in f"Geo {blockfile.stem.capitalize()}".replace("_", " ").split(" ")
        ]
    )
    system_name = name.replace(" ", "_")
    h = Int4Hash.as_int(blockfile.stem)

    GeoNodes[h] = type(
        system_name,
        (SystemNode,),
        {
            # constructor
            # data members
            "icon": "icon/geo.png"
            if "stage" not in name.lower()
            else "icon/filter.png",
            "op_code": h,
            "op_title": name,
            "content_label_objname": system_name,
            "binding": binding,
        },
    )
    register_node_now(h, GeoNodes[h])
