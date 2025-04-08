from PySide6.QtWidgets import QTreeWidget

class CustomTreeWidget(QTreeWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setColumnCount(3)  # 设置三列：项目名称、下载图标、查看详情图标
        self.setHeaderHidden(True)
        self.downloaded_items = set()  # 存储已下载项目
        self.setColumnWidth(0, 250)  # 设置第一列宽度
        self.setColumnWidth(1, 30)   # 设置图标列宽度
        self.setColumnWidth(2, 30)   # 设置图标列宽度 