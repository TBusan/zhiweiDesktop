import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLineEdit, QLabel, QPushButton, 
                             QMessageBox)
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QIcon, QFont
from data_analysis_client import DataAnalysisClient

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("数据分析客户端 - 登录")
        self.setFixedSize(500, 400)  # 增加窗口大小
        
        # 创建中央部件和布局
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setSpacing(25)  # 增加间距
        layout.setContentsMargins(60, 40, 60, 40)  # 增加边距
        
        # 添加标题
        title_label = QLabel("数据分析客户端")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 28px; font-weight: bold; color: #333; margin-bottom: 20px;")
        layout.addWidget(title_label)
        
        # 用户名输入框
        username_layout = QVBoxLayout()
        username_label = QLabel("用户名:")
        username_label.setStyleSheet("color: #333; font-size: 16px; margin-bottom: 5px;")
        self.username_edit = QLineEdit()
        self.username_edit.setPlaceholderText("请输入用户名")
        self.username_edit.setMinimumHeight(45)  # 设置最小高度
        self.username_edit.setStyleSheet("""
            QLineEdit {
                padding: 12px;
                border: 1px solid #ddd;
                border-radius: 6px;
                font-size: 16px;
                background-color: white;
            }
            QLineEdit:focus {
                border: 2px solid #3a3f51;
            }
        """)
        username_layout.addWidget(username_label)
        username_layout.addWidget(self.username_edit)
        layout.addLayout(username_layout)
        
        # 密码输入框
        password_layout = QVBoxLayout()
        password_label = QLabel("密码:")
        password_label.setStyleSheet("color: #333; font-size: 16px; margin-bottom: 5px;")
        self.password_edit = QLineEdit()
        self.password_edit.setPlaceholderText("请输入密码")
        self.password_edit.setEchoMode(QLineEdit.EchoMode.Password)  # 修正密码输入模式
        self.password_edit.setMinimumHeight(45)  # 设置最小高度
        self.password_edit.setStyleSheet("""
            QLineEdit {
                padding: 12px;
                border: 1px solid #ddd;
                border-radius: 6px;
                font-size: 16px;
                background-color: white;
            }
            QLineEdit:focus {
                border: 2px solid #3a3f51;
            }
        """)
        password_layout.addWidget(password_label)
        password_layout.addWidget(self.password_edit)
        layout.addLayout(password_layout)
        
        # 登录按钮
        self.login_button = QPushButton("登录")
        self.login_button.setMinimumHeight(45)  # 设置最小高度
        self.login_button.setStyleSheet("""
            QPushButton {
                background-color: #3a3f51;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 12px;
                font-size: 16px;
                min-width: 200px;
                margin-top: 20px;
            }
            QPushButton:hover {
                background-color: #2c3143;
            }
            QPushButton:pressed {
                background-color: #1f2532;
            }
        """)
        self.login_button.clicked.connect(self.login)
        layout.addWidget(self.login_button, alignment=Qt.AlignCenter)
        
        # 设置回车键触发登录
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
    
    # 设置全局样式
    app.setStyleSheet("""
        QMainWindow {
            background-color: #f5f5f5;
        }
        QMessageBox {
            background-color: white;
        }
        QMessageBox QPushButton {
            padding: 5px 15px;
            border-radius: 4px;
            background-color: #3a3f51;
            color: white;
            min-width: 80px;
            min-height: 25px;
        }
        QMessageBox QPushButton:hover {
            background-color: #2c3143;
        }
    """)
    
    window = LoginWindow()
    window.show()
    sys.exit(app.exec()) 