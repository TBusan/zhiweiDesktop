import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox, QLineEdit, QPushButton)
from PySide6.QtCore import Qt
from PySide6.QtUiTools import QUiLoader
from data_analysis_client import DataAnalysisClient

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # 加载UI文件
        loader = QUiLoader()
        self.ui = loader.load('login_window.ui')
        self.setCentralWidget(self.ui)
        
        # 获取UI控件
        self.username_edit = self.ui.findChild(QLineEdit, 'username_edit')
        self.password_edit = self.ui.findChild(QLineEdit, 'password_edit')
        self.login_button = self.ui.findChild(QPushButton, 'login_button')
        
        # 连接信号
        self.login_button.clicked.connect(self.login)
        self.password_edit.returnPressed.connect(self.login)
        self.username_edit.returnPressed.connect(lambda: self.password_edit.setFocus())
        
        # 存储主窗口实例
        self.main_window = None
    
    def login(self):
        """登录验证"""
        username = self.username_edit.text().strip()
        password = self.password_edit.text().strip()
        
        # 这里简单演示，实际应用中应该连接到后端进行验证
        if not username or not password:
            QMessageBox.warning(self, "提示", "用户名和密码不能为空！")
            return
        
        # 这里使用简单的用户名密码验证，实际应用中应该使用更安全的验证方式
        if username == "admin" and password == "123456":
            # 登录成功，显示主窗口
            self.main_window = DataAnalysisClient()
            self.main_window.show()
            self.close()
        else:
            QMessageBox.warning(self, "错误", "用户名或密码错误！")
            self.password_edit.clear()
            self.password_edit.setFocus()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    
    window = LoginWindow()
    window.show()
    sys.exit(app.exec()) 