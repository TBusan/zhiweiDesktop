import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                              QHBoxLayout, QLineEdit, QLabel, QPushButton, 
                              QTreeWidget, QTreeWidgetItem, QSplitter, QMenu)
from PySide6.QtCore import Qt, QSize, Signal
from PySide6.QtGui import QIcon, QFont, QAction

class DataAnalysisClient(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("数据分析客户端")
        self.setMinimumSize(1000, 600)
        
        # 主分割器
        main_splitter = QSplitter(Qt.Horizontal)
        self.setCentralWidget(main_splitter)
        
        # 左侧导航面板
        navigation_panel = QWidget()
        navigation_layout = QVBoxLayout(navigation_panel)
        navigation_layout.setContentsMargins(0, 0, 0, 0)
        navigation_panel.setFixedWidth(350)
        
        # 搜索框
        search_widget = QWidget()
        search_layout = QHBoxLayout(search_widget)
        search_layout.setContentsMargins(10, 10, 10, 10)
        
        self.search_edit = QLineEdit()
        self.search_edit.setPlaceholderText("请输入要搜索的用户")
        # 添加搜索框交互
        self.search_edit.textChanged.connect(self.filter_items)
        self.search_edit.returnPressed.connect(self.search_items)
        search_layout.addWidget(self.search_edit)
        
        navigation_layout.addWidget(search_widget)
        
        # 云端测区任务标题
        task_title = QLabel("云端测区任务")
        task_title.setStyleSheet("background-color: #f0f0f0; padding: 10px; color: black; font-weight: bold;")
        navigation_layout.addWidget(task_title)
        
        # 测试树形列表
        self.test_tree = QTreeWidget()
        self.test_tree.setHeaderHidden(True)
        # 添加树形列表交互
        self.test_tree.itemClicked.connect(self.on_item_clicked)
        self.test_tree.itemDoubleClicked.connect(self.on_item_double_clicked)
        self.test_tree.setContextMenuPolicy(Qt.CustomContextMenu)
        self.test_tree.customContextMenuRequested.connect(self.show_context_menu)
        navigation_layout.addWidget(self.test_tree)
        
        # 测试类别
        test_category = QTreeWidgetItem(self.test_tree, ["测试"])
        
        # 测试项目
        test_items = [
            "cs3", "cs2", "cs1", "华明路_测试", "华明路5", "华明路4", 
            "华明路3", "华明路2", "1111", "燕记温源", "华明路", "道路1"
        ]
        
        # 添加测试项目并设置下载图标
        for item_text in test_items:
            item = QTreeWidgetItem(test_category, [item_text])
            item.setIcon(0, QIcon())  # 此处应设置图标，因为没有实际图标资源，留空
        
        test_category.setExpanded(True)
        
        # 321类别
        number_category = QTreeWidgetItem(self.test_tree, ["321"])
        
        # 321项目
        number_item = QTreeWidgetItem(number_category, ["123"])
        number_item.setIcon(0, QIcon())  # 此处应设置图标
        
        # 测试用和激活测试类别
        self.test_tree.addTopLevelItem(QTreeWidgetItem(["测试用"]))
        
        activated_category = QTreeWidgetItem(self.test_tree, ["激活测试"])
        activated_item = QTreeWidgetItem(activated_category, ["测试456987"])
        
        # 右侧内容区域（这里只是一个占位符）
        self.content_area = QWidget()
        self.content_layout = QVBoxLayout(self.content_area)
        self.content_area.setStyleSheet("background-color: #e6e9f0;")
        
        # 右侧显示选中项的标签
        self.selected_item_label = QLabel("请从左侧选择一个项目")
        self.selected_item_label.setAlignment(Qt.AlignCenter)
        self.selected_item_label.setStyleSheet("color: #666; font-size: 16px;")
        self.content_layout.addWidget(self.selected_item_label)
        
        # 添加到分割器
        main_splitter.addWidget(navigation_panel)
        main_splitter.addWidget(self.content_area)
        
        # 设置分割比例
        main_splitter.setSizes([350, 650])
        
        # 添加底部状态栏按钮
        self.statusBar().addPermanentWidget(self.create_status_button("在线任务"))
        self.statusBar().addPermanentWidget(self.create_status_button("下载管理"))
        
        # 存储原始树项目以便进行过滤
        self.store_original_items()
        
    def create_status_button(self, text):
        """创建状态栏按钮"""
        button = QPushButton()
        button.setText(text)
        button.setFixedSize(90, 30)
        button.clicked.connect(lambda: self.on_status_button_clicked(text))
        return button
    
    def store_original_items(self):
        """存储原始树项目以便搜索过滤"""
        self.original_items = []
        root_count = self.test_tree.topLevelItemCount()
        
        for i in range(root_count):
            root = self.test_tree.topLevelItem(i)
            root_text = root.text(0)
            
            children = []
            for j in range(root.childCount()):
                child = root.child(j)
                children.append((child.text(0), j))
            
            self.original_items.append((root_text, i, children))
    
    def filter_items(self, text):
        """根据输入文本过滤树项目"""
        if not text:
            # 如果搜索框为空，恢复原始项目
            for category, index, children in self.original_items:
                root = self.test_tree.topLevelItem(index)
                root.setHidden(False)
                for child_text, child_index in children:
                    if child_index < root.childCount():
                        root.child(child_index).setHidden(False)
            return
        
        text = text.lower()
        # 隐藏不匹配的项目
        for category, index, children in self.original_items:
            root = self.test_tree.topLevelItem(index)
            
            # 检查是否有任何子项匹配
            has_match = False
            for child_text, child_index in children:
                if child_index < root.childCount():
                    child = root.child(child_index)
                    if text in child_text.lower():
                        child.setHidden(False)
                        has_match = True
                    else:
                        child.setHidden(True)
            
            # 如果类别名称匹配或有匹配的子项，显示类别
            if text in category.lower() or has_match:
                root.setHidden(False)
                if text in category.lower():
                    # 如果类别名称匹配，显示其所有子项
                    for child_text, child_index in children:
                        if child_index < root.childCount():
                            root.child(child_index).setHidden(False)
            else:
                root.setHidden(True)
    
    def search_items(self):
        """按回车键进行搜索"""
        search_text = self.search_edit.text()
        if search_text:
            self.statusBar().showMessage(f"正在搜索: {search_text}", 3000)
            self.filter_items(search_text)
    
    def on_item_clicked(self, item, column):
        """树项目点击事件"""
        if item.parent():  # 仅处理子项目点击
            self.selected_item_label.setText(f"已选择: {item.text(0)}")
            self.statusBar().showMessage(f"选中项目: {item.text(0)}", 2000)
    
    def on_item_double_clicked(self, item, column):
        """树项目双击事件"""
        if item.parent():  # 仅处理子项目双击
            self.selected_item_label.setText(f"正在加载 {item.text(0)} 的数据...")
            self.statusBar().showMessage(f"加载项目: {item.text(0)}", 2000)
    
    def show_context_menu(self, position):
        """显示上下文菜单"""
        item = self.test_tree.itemAt(position)
        if not item:
            return
            
        context_menu = QMenu(self)
        
        if item.parent():  # 子项目菜单
            download_action = QAction("下载", self)
            download_action.triggered.connect(lambda: self.download_item(item.text(0)))
            context_menu.addAction(download_action)
            
            view_action = QAction("查看详情", self)
            view_action.triggered.connect(lambda: self.view_item_details(item.text(0)))
            context_menu.addAction(view_action)
        else:  # 类别菜单
            expand_action = QAction("展开全部", self)
            expand_action.triggered.connect(lambda: item.setExpanded(True))
            context_menu.addAction(expand_action)
            
            collapse_action = QAction("折叠全部", self)
            collapse_action.triggered.connect(lambda: item.setExpanded(False))
            context_menu.addAction(collapse_action)
        
        context_menu.exec_(self.test_tree.mapToGlobal(position))
    
    def download_item(self, item_name):
        """下载项目"""
        self.statusBar().showMessage(f"开始下载: {item_name}", 3000)
        self.selected_item_label.setText(f"正在下载 {item_name}...")
    
    def view_item_details(self, item_name):
        """查看项目详情"""
        self.statusBar().showMessage(f"查看详情: {item_name}", 3000)
        self.selected_item_label.setText(f"正在查看 {item_name} 的详细信息...")
    
    def on_status_button_clicked(self, button_text):
        """状态栏按钮点击事件"""
        if button_text == "在线任务":
            self.statusBar().showMessage("正在查看在线任务...", 2000)
        elif button_text == "下载管理":
            self.statusBar().showMessage("正在打开下载管理...", 2000)

if __name__ == "__main__":
    # 如果直接运行此文件，提示需要通过登录页面进入
    print("请运行 login_window.py 以启动程序！")
    sys.exit(1) 