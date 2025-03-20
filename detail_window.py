import sys
from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                              QLabel, QPushButton, QComboBox, QLineEdit,
                              QSpinBox, QDoubleSpinBox, QCheckBox)
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon

class DetailWindow(QMainWindow):
    def __init__(self, item_name):
        super().__init__()
        self.item_name = item_name  # 保存项目名称
        self.setWindowTitle(f"数据分析客户端 - {item_name}")
        self.setMinimumSize(1200, 800)
        
        # 创建中央部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        
        # 顶部工具栏
        toolbar = QWidget()
        toolbar_layout = QHBoxLayout(toolbar)
        toolbar_layout.setContentsMargins(10, 5, 10, 5)
        
        # 添加按钮
        add_btn = QPushButton("+")
        add_btn.setFixedSize(40, 40)
        add_btn.setStyleSheet("""
            QPushButton {
                background-color: #2E8B57;
                color: white;
                border-radius: 4px;
                font-size: 20px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #3CB371;
            }
        """)
        toolbar_layout.addWidget(add_btn)
        
        # 坐标输入框
        coord_widget = QWidget()
        coord_layout = QHBoxLayout(coord_widget)
        coord_layout.setSpacing(5)
        
        # X坐标
        x_label = QLabel("X")
        x_spin = QSpinBox()
        x_spin.setRange(0, 9999)
        coord_layout.addWidget(x_label)
        coord_layout.addWidget(x_spin)
        
        # Y坐标
        y_label = QLabel("Y")
        y_spin = QSpinBox()
        y_spin.setRange(0, 9999)
        coord_layout.addWidget(y_label)
        coord_layout.addWidget(y_spin)
        
        # 高度
        height_label = QLabel("高")
        height_spin = QSpinBox()
        height_spin.setRange(0, 9999)
        coord_layout.addWidget(height_label)
        coord_layout.addWidget(height_spin)
        
        # 深度
        depth_label = QLabel("深")
        depth_spin = QSpinBox()
        depth_spin.setRange(0, 9999)
        coord_layout.addWidget(depth_label)
        coord_layout.addWidget(depth_spin)
        
        toolbar_layout.addWidget(coord_widget)
        
        # 备注输入框
        note_edit = QLineEdit()
        note_edit.setPlaceholderText("请输入备注")
        note_edit.setFixedWidth(200)
        toolbar_layout.addWidget(note_edit)
        
        # 确认按钮
        confirm_btn = QPushButton("确认")
        confirm_btn.setStyleSheet("""
            QPushButton {
                background-color: #2E8B57;
                color: white;
                padding: 5px 15px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #3CB371;
            }
        """)
        toolbar_layout.addWidget(confirm_btn)
        
        # 添加弹性空间
        toolbar_layout.addStretch()
        
        # 右侧工具栏
        right_tools = QWidget()
        right_tools_layout = QHBoxLayout(right_tools)
        right_tools_layout.setSpacing(10)
        
        # 网格选项
        grid_check = QCheckBox("网格")
        right_tools_layout.addWidget(grid_check)
        
        # 颜色选择
        color_combo = QComboBox()
        color_combo.addItems(["黑白", "彩色"])
        right_tools_layout.addWidget(color_combo)
        
        # 亮度调节
        brightness_spin = QSpinBox()
        brightness_spin.setRange(0, 100)
        brightness_spin.setValue(17)
        right_tools_layout.addWidget(brightness_spin)
        
        # 数据处理按钮
        process_btn = QPushButton("数据处理")
        process_btn.setStyleSheet("""
            QPushButton {
                background-color: #2E8B57;
                color: white;
                padding: 5px 15px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #3CB371;
            }
        """)
        right_tools_layout.addWidget(process_btn)
        
        toolbar_layout.addWidget(right_tools)
        main_layout.addWidget(toolbar)
        
        # 添加图像显示区域（这里用标签代替）
        image_area = QLabel("雷达数据图像显示区域")
        image_area.setStyleSheet("""
            QLabel {
                background-color: white;
                border: 1px solid #ccc;
                padding: 10px;
            }
        """)
        image_area.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(image_area)
        
        # 底部状态栏
        self.statusBar().showMessage("当前区块序号：1")
        
        # 添加导航按钮到状态栏
        nav_widget = QWidget()
        nav_layout = QHBoxLayout(nav_widget)
        
        prev_btn = QPushButton("上一块")
        next_btn = QPushButton("下一块")
        nav_layout.addWidget(prev_btn)
        nav_layout.addWidget(next_btn)
        
        self.statusBar().addPermanentWidget(nav_widget)

    def closeEvent(self, event):
        """重写关闭事件，清理资源"""
        # 从父窗口的字典中移除自己
        parent = self.parent()
        if parent and hasattr(parent, 'detail_windows'):
            parent.detail_windows.pop(self.item_name, None)
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DetailWindow("测试项目")
    window.show()
    sys.exit(app.exec()) 