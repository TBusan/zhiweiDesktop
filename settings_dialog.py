from PySide6.QtWidgets import (QDialog, QTabWidget, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QLineEdit, QPushButton, QFileDialog)
from PySide6.QtCore import Qt

class SettingsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("设置")
        self.setMinimumSize(500, 300)
        
        # 创建主布局
        layout = QVBoxLayout(self)
        
        # 创建标签页
        tab_widget = QTabWidget()
        
        # FTP设置页
        ftp_tab = QWidget()
        ftp_layout = QVBoxLayout(ftp_tab)
        
        # 数据保存目录
        save_dir_widget = QWidget()
        save_dir_layout = QHBoxLayout(save_dir_widget)
        save_dir_layout.setContentsMargins(0, 0, 0, 0)
        
        save_dir_label = QLabel("数据保存目录:")
        self.save_dir_edit = QLineEdit()
        self.save_dir_edit.setText("RpDownload")
        self.save_dir_edit.setMinimumWidth(300)
        browse_btn = QPushButton("浏览")
        browse_btn.clicked.connect(self.browse_directory)
        
        save_dir_layout.addWidget(save_dir_label)
        save_dir_layout.addWidget(self.save_dir_edit)
        save_dir_layout.addWidget(browse_btn)
        
        ftp_layout.addWidget(save_dir_widget)
        ftp_layout.addStretch()
        
        # 功能设置页
        function_tab = QWidget()
        function_layout = QVBoxLayout(function_tab)
        function_layout.addStretch()
        
        # 软件版本页
        version_tab = QWidget()
        version_layout = QVBoxLayout(version_tab)
        version_layout.addStretch()
        
        # 添加标签页
        tab_widget.addTab(ftp_tab, "FTP设置")
        tab_widget.addTab(function_tab, "功能设置")
        tab_widget.addTab(version_tab, "软件版本")
        
        layout.addWidget(tab_widget)
        
        # 添加底部按钮
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        
        ok_button = QPushButton("确定")
        ok_button.clicked.connect(self.accept)
        cancel_button = QPushButton("取消")
        cancel_button.clicked.connect(self.reject)
        
        button_layout.addWidget(ok_button)
        button_layout.addWidget(cancel_button)
        
        layout.addLayout(button_layout)
        
        # 设置样式
        self.setStyleSheet("""
            QDialog {
                background-color: white;
            }
            QTabWidget::pane {
                border: 1px solid #ddd;
                background-color: white;
            }
            QTabBar::tab {
                background-color: #f0f0f0;
                border: 1px solid #ddd;
                padding: 8px 16px;
                margin-right: 2px;
            }
            QTabBar::tab:selected {
                background-color: white;
                border-bottom: none;
            }
            QPushButton {
                background-color: #f0f0f0;
                border: 1px solid #ddd;
                padding: 6px 16px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #e0e0e0;
            }
            QLineEdit {
                padding: 6px;
                border: 1px solid #ddd;
                border-radius: 4px;
            }
        """)
    
    def browse_directory(self):
        """打开目录选择对话框"""
        directory = QFileDialog.getExistingDirectory(
            self,
            "选择数据保存目录",
            self.save_dir_edit.text(),
            QFileDialog.Option.ShowDirsOnly
        )
        if directory:
            self.save_dir_edit.setText(directory) 