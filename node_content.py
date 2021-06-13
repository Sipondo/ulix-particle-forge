from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from calc_conf import *
from calc_node_base import *
from nodeeditor.utils import dumpException


class NodeContent(QDMNodeContentWidget):
    def initUI(self):
        self.fields = {}
        self.binding = []

    def getInputValue(self, tag, base):
        if tag in self.fields:
            return self.fields[tag]
        else:
            self.setInputValue(tag, base)
            return base

    def setInputValue(self, tag, value):
        self.fields[tag] = value

    def serialize(self):
        res = super().serialize()
        for field, value in self.fields.items():
            res[f"field_{field}"] = value

        return res

    def deserialize(self, data, hashmap={}):
        res = super().deserialize(data, hashmap)
        try:
            for key, value in data.items():
                if "field" in key:
                    print(key)
                    self.fields[key[6:]] = value

            return True & res
        except Exception as e:
            dumpException(e)
        return res
