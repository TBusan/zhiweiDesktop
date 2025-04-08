import sys
import os
from PySide6.QtWidgets import (QMainWindow, QTableWidgetItem, QHeaderView)
from PySide6.QtCore import Qt
from PySide6.QtUiTools import QUiLoader

class DownloadManager(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # 加载UI文件
        loader = QUiLoader()
        ui_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "download_manager.ui")
        self.ui = loader.load(ui_path)
        self.setCentralWidget(self.ui.centralwidget)
        
        # 设置列宽
        header = self.ui.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Fixed)  # 序号
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)  # 项目
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)  # 任务
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.Fixed)  # 规格
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.Fixed)  # 大小
        header.setSectionResizeMode(5, QHeaderView.ResizeMode.Fixed)  # 进度
        header.setSectionResizeMode(6, QHeaderView.ResizeMode.Fixed)  # 操作
        
        self.ui.table.setColumnWidth(0, 60)  # 序号
        self.ui.table.setColumnWidth(3, 100)  # 规格
        self.ui.table.setColumnWidth(4, 80)  # 大小
        self.ui.table.setColumnWidth(5, 100)  # 进度
        self.ui.table.setColumnWidth(6, 80)  # 操作
        
        # 添加一些测试数据
        self.add_test_data()
    
    def add_test_data(self):
        """添加测试数据到表格"""
        self.ui.table.setRowCount(1)  # 设置行数
        
        # 添加一行测试数据
        row = 0
        self.ui.table.setItem(row, 0, QTableWidgetItem("1"))  # 序号
        self.ui.table.setItem(row, 1, QTableWidgetItem("正在下载"))  # 项目
        self.ui.table.setItem(row, 2, QTableWidgetItem(""))  # 任务
        self.ui.table.setItem(row, 3, QTableWidgetItem(""))  # 规格
        self.ui.table.setItem(row, 4, QTableWidgetItem(""))  # 大小
        self.ui.table.setItem(row, 5, QTableWidgetItem(""))  # 进度
        self.ui.table.setItem(row, 6, QTableWidgetItem(""))  # 操作

if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    app = QApplication(sys.argv)
    window = DownloadManager()
    window.show()
    sys.exit(app.exec()) 