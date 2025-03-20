import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                              QHBoxLayout, QLineEdit, QLabel, QPushButton, 
                              QTreeWidget, QTreeWidgetItem, QSplitter, QMenu,
                              QStyle)
from PySide6.QtCore import Qt, QSize, Signal
from PySide6.QtGui import QIcon, QFont, QAction
from detail_window import DetailWindow  # 导入新创建的DetailWindow类

class CustomTreeWidget(QTreeWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setColumnCount(3)  # 设置三列：项目名称、下载图标、查看详情图标
        self.setHeaderHidden(True)
        self.downloaded_items = set()  # 存储已下载项目
        self.setColumnWidth(0, 250)  # 设置第一列宽度
        self.setColumnWidth(1, 30)   # 设置图标列宽度
        self.setColumnWidth(2, 30)   # 设置图标列宽度

class DataAnalysisClient(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("知微客户端")
        self.setMinimumSize(1000, 600)
        
        # 存储详情窗口的字典
        self.detail_windows = {}
        
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
        
        # 使用自定义树形列表
        self.test_tree = CustomTreeWidget()
        self.test_tree.itemClicked.connect(self.on_item_clicked)
        navigation_layout.addWidget(self.test_tree)
        
        # 测试类别
        test_category = QTreeWidgetItem(self.test_tree)
        test_category.setText(0, "测试")
        
        # 测试项目
        test_items = [
            "cs3", "cs2", "cs1", "华明路_测试", "华明路5", "华明路4", 
            "华明路3", "华明路2", "1111", "燕记温源", "华明路", "道路1"
        ]
        
        # 添加测试项目并设置图标
        for item_text in test_items:
            item = QTreeWidgetItem(test_category)
            item.setText(0, item_text)
            # 添加下载按钮
            download_btn = QPushButton()
            download_btn.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_ArrowDown))
            download_btn.setIconSize(QSize(20, 20))
            download_btn.setFixedSize(28, 28)
            download_btn.setStyleSheet("""
                QPushButton {
                    background-color: transparent;
                    border: none;
                    padding: 2px;
                }
                QPushButton:hover {
                    background-color: #e0e0e0;
                    border-radius: 4px;
                }
            """)
            download_btn.clicked.connect(lambda checked, name=item_text: self.download_item(name))
            self.test_tree.setItemWidget(item, 1, download_btn)
        
        test_category.setExpanded(True)
        
        # 321类别
        number_category = QTreeWidgetItem(self.test_tree)
        number_category.setText(0, "321")
        
        # 321项目
        number_item = QTreeWidgetItem(number_category)
        number_item.setText(0, "123")
        download_btn = QPushButton()
        download_btn.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_ArrowDown))
        download_btn.setIconSize(QSize(20, 20))
        download_btn.setFixedSize(28, 28)
        download_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;
                padding: 2px;
            }
            QPushButton:hover {
                background-color: #e0e0e0;
                border-radius: 4px;
            }
        """)
        download_btn.clicked.connect(lambda: self.download_item("123"))
        self.test_tree.setItemWidget(number_item, 1, download_btn)
        
        # 测试用和激活测试类别
        test_use_category = QTreeWidgetItem(self.test_tree)
        test_use_category.setText(0, "测试用")
        
        activated_category = QTreeWidgetItem(self.test_tree)
        activated_category.setText(0, "激活测试")
        activated_item = QTreeWidgetItem(activated_category)
        activated_item.setText(0, "测试456987")
        download_btn = QPushButton()
        download_btn.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_ArrowDown))
        download_btn.setIconSize(QSize(20, 20))
        download_btn.setFixedSize(28, 28)
        download_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;
                padding: 2px;
            }
            QPushButton:hover {
                background-color: #e0e0e0;
                border-radius: 4px;
            }
        """)
        download_btn.clicked.connect(lambda: self.download_item("测试456987"))
        self.test_tree.setItemWidget(activated_item, 1, download_btn)
        
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
    
    def download_item(self, item_name):
        """下载项目"""
        self.statusBar().showMessage(f"开始下载: {item_name}", 3000)
        self.selected_item_label.setText(f"正在下载 {item_name}...")
        
        # 模拟下载完成后的操作
        item = self.find_item_by_name(item_name)
        if item:
            # 移除下载按钮
            self.test_tree.removeItemWidget(item, 1)
            # 添加删除和查看详情按钮
            delete_btn = QPushButton()
            delete_btn.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_TrashIcon))
            delete_btn.setIconSize(QSize(20, 20))
            delete_btn.setFixedSize(28, 28)
            delete_btn.setStyleSheet("""
                QPushButton {
                    background-color: transparent;
                    border: none;
                    padding: 2px;
                }
                QPushButton:hover {
                    background-color: #e0e0e0;
                    border-radius: 4px;
                }
            """)
            delete_btn.clicked.connect(lambda: self.delete_item(item_name))
            
            view_btn = QPushButton()
            view_btn.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_FileDialogContentsView))
            view_btn.setIconSize(QSize(20, 20))
            view_btn.setFixedSize(28, 28)
            view_btn.setStyleSheet("""
                QPushButton {
                    background-color: transparent;
                    border: none;
                    padding: 2px;
                }
                QPushButton:hover {
                    background-color: #e0e0e0;
                    border-radius: 4px;
                }
            """)
            view_btn.clicked.connect(lambda: self.view_item_details(item_name))
            
            self.test_tree.setItemWidget(item, 1, delete_btn)
            self.test_tree.setItemWidget(item, 2, view_btn)
            
            # 添加到已下载集合
            self.test_tree.downloaded_items.add(item_name)

    def delete_item(self, item_name):
        """删除已下载的项目"""
        self.statusBar().showMessage(f"删除项目: {item_name}", 3000)
        item = self.find_item_by_name(item_name)
        if item:
            # 恢复为下载按钮
            for col in range(1, 3):
                self.test_tree.removeItemWidget(item, col)
            download_btn = QPushButton()
            download_btn.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_ArrowDown))
            download_btn.setIconSize(QSize(20, 20))
            download_btn.setFixedSize(28, 28)
            download_btn.setStyleSheet("""
                QPushButton {
                    background-color: transparent;
                    border: none;
                    padding: 2px;
                }
                QPushButton:hover {
                    background-color: #e0e0e0;
                    border-radius: 4px;
                }
            """)
            download_btn.clicked.connect(lambda: self.download_item(item_name))
            self.test_tree.setItemWidget(item, 1, download_btn)
            
            # 从已下载集合中移除
            self.test_tree.downloaded_items.remove(item_name)

    def find_item_by_name(self, name):
        """通过名称查找树形项目"""
        def search_items(parent):
            for i in range(parent.childCount()):
                child = parent.child(i)
                if child.text(0) == name:
                    return child
                result = search_items(child)
                if result:
                    return result
            return None
        
        for i in range(self.test_tree.topLevelItemCount()):
            root = self.test_tree.topLevelItem(i)
            if root.text(0) == name:
                return root
            result = search_items(root)
            if result:
                return result
        return None
    
    def view_item_details(self, item_name):
        """查看项目详情"""
        self.statusBar().showMessage(f"查看详情: {item_name}", 3000)
        
        # 如果该项目的窗口已经存在，就显示已有窗口
        if item_name in self.detail_windows:
            self.detail_windows[item_name].showMaximized()  # 使用最大化显示
            self.detail_windows[item_name].raise_()  
            self.detail_windows[item_name].activateWindow()
        else:
            # 创建新窗口并保存
            detail_window = DetailWindow(item_name)
            detail_window.setParent(None)  # 设置为无父窗口
            self.detail_windows[item_name] = detail_window
            detail_window.showMaximized()  # 使用最大化显示
        
        # 可选：隐藏主窗口
        self.hide()
    
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