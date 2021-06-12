import os
import sys
from PyQt5.QtWidgets import *
import calc_conf

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "node_main"))
# sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from calc_window import CalculatorWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # print(QStyleFactory.keys())
    app.setStyle("Fusion")

    wnd = CalculatorWindow()
    wnd.show()

    sys.exit(app.exec_())
