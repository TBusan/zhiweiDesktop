import sys
from PySide6.QtWidgets import (QMainWindow, QApplication, QStyle, QPushButton, 
                              QLabel, QWidget, QHBoxLayout)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon
from PySide6.QtUiTools import QUiLoader
import os

class DetailWindow(QMainWindow):
    def __init__(self, item_name, parent=None):
        super().__init__(parent)
        self.item_name = item_name
        self.parent_window = parent
        
        # 设置为独立窗口
        self.setWindowFlags(Qt.Window)
        
        # 加载UI文件
        loader = QUiLoader()
        ui_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "detail_window.ui")
        self.ui = loader.load(ui_path)
        self.setCentralWidget(self.ui.centralwidget)
        
        # 设置窗口标题
        self.setWindowTitle(f"数据分析客户端 - {item_name}")
        
        # 添加图标到返回按钮
        self.ui.back_btn.setIcon(QApplication.style().standardIcon(QStyle.StandardPixmap.SP_ArrowBack))
        self.ui.back_btn.setIconSize(QSize(24, 24))
        self.ui.back_btn.clicked.connect(self.go_back)
        
        # 状态栏消息
        self.statusBar().showMessage("当前区块序号：1")
        
        # 添加导航按钮到状态栏
        nav_widget = QWidget()
        nav_layout = QHBoxLayout(nav_widget)
        nav_layout.setContentsMargins(0, 0, 0, 0)
        
        prev_btn = QPushButton("上一块")
        next_btn = QPushButton("下一块")
        prev_btn.setStyleSheet("""
            QPushButton {
                background-color: #f0f0f0;
                border: 1px solid #ccc;
                padding: 4px 12px;
                border-radius: 2px;
            }
        """)
        next_btn.setStyleSheet("""
            QPushButton {
                background-color: #f0f0f0;
                border: 1px solid #ccc;
                padding: 4px 12px;
                border-radius: 2px;
            }
        """)
        nav_layout.addWidget(prev_btn)
        nav_layout.addWidget(next_btn)
        
        self.statusBar().addPermanentWidget(nav_widget)

    def go_back(self):
        """返回到主窗口"""
        if self.parent_window:
            # 从父窗口的字典中移除自己
            if hasattr(self.parent_window, 'detail_windows'):
                self.parent_window.detail_windows.pop(self.item_name, None)
            self.parent_window.show()
        self.close()
        
    def closeEvent(self, event):
        """重写关闭事件，根据触发来源决定行为"""
        # 获取触发关闭事件的原因
        if self.sender() and self.sender().objectName() == "back_button":
            # 如果是通过返回按钮触发的关闭，显示主窗口
            if self.parent_window:
                self.parent_window.show()
        else:
            # 如果是通过关闭按钮触发的关闭，退出整个程序
            QApplication.quit()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DetailWindow("测试项目")
    window.show()
    sys.exit(app.exec()) 