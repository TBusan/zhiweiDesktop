import sys
from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                              QLabel, QPushButton, QComboBox, QLineEdit,
                              QSpinBox, QDoubleSpinBox, QCheckBox, QApplication)
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QFont

class DetailWindow(QMainWindow):
    def __init__(self, item_name):
        super().__init__()
        self.item_name = item_name
        self.setWindowTitle(f"数据分析客户端")
        self.setMinimumSize(1200, 800)
        # 设置为独立窗口
        self.setWindowFlags(Qt.Window)
        
        # 创建中央部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(5)
        
        # 顶部工具栏
        toolbar = QWidget()
        toolbar_layout = QHBoxLayout(toolbar)
        toolbar_layout.setContentsMargins(0, 0, 0, 0)
        toolbar_layout.setSpacing(10)
        
        # 左侧工具组
        left_tools = QWidget()
        left_layout = QHBoxLayout(left_tools)
        left_layout.setSpacing(5)
        left_layout.setContentsMargins(0, 0, 0, 0)
        
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
        left_layout.addWidget(add_btn)
        
        # 坐标输入组
        coord_group = QWidget()
        coord_layout = QHBoxLayout(coord_group)
        coord_layout.setSpacing(5)
        coord_layout.setContentsMargins(0, 0, 0, 0)
        
        # X坐标
        x_label = QLabel("X")
        x_spin = QSpinBox()
        x_spin.setFixedWidth(60)
        x_spin.setValue(0)
        x_spin.setStyleSheet("QSpinBox { background-color: white; padding: 2px; }")
        
        # Y坐标
        y_label = QLabel("Y")
        y_spin = QSpinBox()
        y_spin.setFixedWidth(60)
        y_spin.setValue(0)
        y_spin.setStyleSheet("QSpinBox { background-color: white; padding: 2px; }")
        
        # 长度
        length_label = QLabel("长")
        length_spin = QSpinBox()
        length_spin.setFixedWidth(60)
        length_spin.setValue(0)
        length_spin.setStyleSheet("QSpinBox { background-color: white; padding: 2px; }")
        
        # 宽度
        width_label = QLabel("宽")
        width_spin = QSpinBox()
        width_spin.setFixedWidth(60)
        width_spin.setValue(0)
        width_spin.setStyleSheet("QSpinBox { background-color: white; padding: 2px; }")
        
        # 高度
        height_label = QLabel("高")
        height_spin = QSpinBox()
        height_spin.setFixedWidth(60)
        height_spin.setValue(0)
        height_spin.setStyleSheet("QSpinBox { background-color: white; padding: 2px; }")
        
        # 深度
        depth_label = QLabel("深")
        depth_spin = QSpinBox()
        depth_spin.setFixedWidth(60)
        depth_spin.setValue(0)
        depth_spin.setStyleSheet("QSpinBox { background-color: white; padding: 2px; }")
        
        # 添加所有坐标输入组件
        coord_layout.addWidget(x_label)
        coord_layout.addWidget(x_spin)
        coord_layout.addWidget(y_label)
        coord_layout.addWidget(y_spin)
        coord_layout.addWidget(length_label)
        coord_layout.addWidget(length_spin)
        coord_layout.addWidget(width_label)
        coord_layout.addWidget(width_spin)
        coord_layout.addWidget(height_label)
        coord_layout.addWidget(height_spin)
        coord_layout.addWidget(depth_label)
        coord_layout.addWidget(depth_spin)
        
        left_layout.addWidget(coord_group)
        
        # 备注输入框
        note_edit = QLineEdit()
        note_edit.setPlaceholderText("请输入备注")
        note_edit.setFixedWidth(150)
        note_edit.setStyleSheet("QLineEdit { background-color: white; padding: 4px; }")
        left_layout.addWidget(note_edit)
        
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
        left_layout.addWidget(confirm_btn)
        
        toolbar_layout.addWidget(left_tools)
        toolbar_layout.addStretch()
        
        # 右侧工具组
        right_tools = QWidget()
        right_layout = QHBoxLayout(right_tools)
        right_layout.setSpacing(10)
        right_layout.setContentsMargins(0, 0, 0, 0)
        
        # 网格选项
        grid_check = QCheckBox("网格")
        grid_check.setStyleSheet("QCheckBox { color: #333; }")
        right_layout.addWidget(grid_check)
        
        # 线条选项
        line_check = QCheckBox("线条")
        line_check.setStyleSheet("QCheckBox { color: #333; }")
        right_layout.addWidget(line_check)
        
        # 颜色选择
        color_combo = QComboBox()
        color_combo.addItems(["彩色"])
        color_combo.setFixedWidth(60)
        color_combo.setStyleSheet("QComboBox { background-color: white; }")
        right_layout.addWidget(color_combo)
        
        # 亮度调节
        brightness_spin = QSpinBox()
        brightness_spin.setRange(0, 100)
        brightness_spin.setValue(17)
        brightness_spin.setFixedWidth(50)
        brightness_spin.setStyleSheet("QSpinBox { background-color: white; }")
        right_layout.addWidget(brightness_spin)
        
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
        right_layout.addWidget(process_btn)
        
        # 剖面平滑度
        smoothness_label = QLabel("剖面平滑度")
        smoothness_label.setStyleSheet("QLabel { color: #333; }")
        right_layout.addWidget(smoothness_label)
        
        smoothness_spin = QDoubleSpinBox()
        smoothness_spin.setValue(1.6)
        smoothness_spin.setFixedWidth(50)
        smoothness_spin.setStyleSheet("QDoubleSpinBox { background-color: white; }")
        right_layout.addWidget(smoothness_spin)
        
        # 三维视图按钮
        view_3d_btn = QPushButton("三维视图")
        view_3d_btn.setStyleSheet("""
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
        right_layout.addWidget(view_3d_btn)
        
        # 坐标校正复选框
        coord_correction = QCheckBox("坐标校正")
        coord_correction.setStyleSheet("QCheckBox { color: #333; }")
        right_layout.addWidget(coord_correction)
        
        toolbar_layout.addWidget(right_tools)
        main_layout.addWidget(toolbar)
        
        # 添加图像显示区域
        image_area = QWidget()
        image_layout = QVBoxLayout(image_area)
        image_layout.setContentsMargins(0, 0, 0, 0)
        
        # 顶部图像
        top_image = QLabel()
        top_image.setStyleSheet("QLabel { background-color: white; border: 1px solid #ccc; }")
        top_image.setMinimumHeight(200)
        
        # 底部图像
        bottom_image = QLabel()
        bottom_image.setStyleSheet("QLabel { background-color: white; border: 1px solid #ccc; }")
        bottom_image.setMinimumHeight(200)
        
        image_layout.addWidget(top_image)
        image_layout.addWidget(bottom_image)
        main_layout.addWidget(image_area)
        
        # 底部状态栏
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

    def closeEvent(self, event):
        """重写关闭事件，清理资源"""
        parent = self.parent()
        if parent and hasattr(parent, 'detail_windows'):
            parent.detail_windows.pop(self.item_name, None)
        
        # 找到主应用窗口并显示
        for widget in QApplication.topLevelWidgets():
            if isinstance(widget, QMainWindow) and widget != self:
                widget.show()
            
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DetailWindow("测试项目")
    window.show()
    sys.exit(app.exec()) 