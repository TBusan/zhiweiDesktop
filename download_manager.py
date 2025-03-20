import sys
from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QTableWidget,
                             QTableWidgetItem, QHeaderView, QLabel)
from PySide6.QtCore import Qt

class DownloadManager(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # 创建中央部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(10, 10, 10, 10)
        
        # 创建标题标签
        title_label = QLabel("任务下载列表")
        title_label.setStyleSheet("""
            QLabel {
                font-size: 16px;
                font-weight: bold;
                color: #333;
                padding: 10px 0;
            }
        """)
        layout.addWidget(title_label)
        
        # 创建表格
        self.table = QTableWidget()
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(["序号", "项目", "任务", "规格", "大小", "进度", "操作"])
        
        # 设置表格样式
        self.table.setStyleSheet("""
            QTableWidget {
                background-color: white;
                border: 1px solid #ddd;
            }
            QHeaderView::section {
                background-color: #f0f0f0;
                padding: 5px;
                border: none;
                border-right: 1px solid #ddd;
                border-bottom: 1px solid #ddd;
            }
            QTableWidget::item {
                padding: 5px;
            }
        """)
        
        # 设置列宽
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Fixed)  # 序号
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)  # 项目
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)  # 任务
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.Fixed)  # 规格
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.Fixed)  # 大小
        header.setSectionResizeMode(5, QHeaderView.ResizeMode.Fixed)  # 进度
        header.setSectionResizeMode(6, QHeaderView.ResizeMode.Fixed)  # 操作
        
        self.table.setColumnWidth(0, 60)  # 序号
        self.table.setColumnWidth(3, 100)  # 规格
        self.table.setColumnWidth(4, 80)  # 大小
        self.table.setColumnWidth(5, 100)  # 进度
        self.table.setColumnWidth(6, 80)  # 操作
        
        # 设置表格其他属性
        self.table.setShowGrid(True)
        self.table.setGridStyle(Qt.PenStyle.SolidLine)
        self.table.verticalHeader().setVisible(False)
        self.table.setAlternatingRowColors(True)
        
        layout.addWidget(self.table)
        
        # 添加一些测试数据
        self.add_test_data()
        
        # 设置整体样式
        central_widget.setStyleSheet("""
            QWidget {
                background-color: #f5f5f5;
            }
        """)
    
    def add_test_data(self):
        """添加测试数据到表格"""
        self.table.setRowCount(1)  # 设置行数
        
        # 添加一行测试数据
        row = 0
        self.table.setItem(row, 0, QTableWidgetItem("1"))  # 序号
        self.table.setItem(row, 1, QTableWidgetItem("正在下载"))  # 项目
        self.table.setItem(row, 2, QTableWidgetItem(""))  # 任务
        self.table.setItem(row, 3, QTableWidgetItem(""))  # 规格
        self.table.setItem(row, 4, QTableWidgetItem(""))  # 大小
        self.table.setItem(row, 5, QTableWidgetItem(""))  # 进度
        self.table.setItem(row, 6, QTableWidgetItem(""))  # 操作

if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    app = QApplication(sys.argv)
    window = DownloadManager()
    window.show()
    sys.exit(app.exec()) 