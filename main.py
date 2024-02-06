import sys

from PyQt6.QtWidgets import QApplication
from qfluentwidgets import FluentWindow, FluentTranslator, FluentIcon, NavigationItemPosition

import interfaces

__version__ = '1.0'


class Window(FluentWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(f'几何计算器 {__version__}')
        self.resize(800, 600)

        # 点的字典，键为名字，值为点的对象
        self.points = dict()
        # 所有条件，里面的表达式值都为0
        self.conditions = []
        # 所有符号的集合
        self.symbols = set()

        # 添加子界面
        self.ui_add = interfaces.InterfaceAdd(self)
        self.addSubInterface(self.ui_add, FluentIcon.ADD, '添加点和条件')
        self.ui_solve = interfaces.InterfaceSolve(self)
        self.addSubInterface(self.ui_solve, FluentIcon.EDIT, '求解')
        self.ui_help = interfaces.InterfaceHelp(self)
        self.addSubInterface(self.ui_help, FluentIcon.HELP, '帮助与关于', NavigationItemPosition.BOTTOM)


app = QApplication(sys.argv)
# 国际化
# 为啥translator不生效啊，我不理解啊啊啊啊啊
translator = FluentTranslator()
app.installTranslator(translator)
w = Window()
w.show()
sys.exit(app.exec())
