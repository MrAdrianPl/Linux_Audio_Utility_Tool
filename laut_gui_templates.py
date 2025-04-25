from PyQt6.QtGui import QPolygon,QRegion
from PyQt6.QtCore import QPoint,QSize,Qt,QMargins,QRect
from PyQt6.QtWidgets import (QPushButton
                             ,QSizePolicy
                             ,QComboBox
                             ,QLabel
                             ,QHBoxLayout
                             ,QCheckBox
                             ,QLineEdit
                             ,QVBoxLayout
                             ,QLayout
                             ,QBoxLayout
                             ,QFrame)

def sign_mask(x,y):
    points = [QPoint(0, 0), QPoint(int(x/2), 0), QPoint(x, int(y/2)), QPoint(int(x/2), y), QPoint(0, y)]    
    return QRegion(QPolygon(points))
    
def rhombus_mask(x,y):
    points = [QPoint(int(x/2), 0), QPoint(x, int(y/2)), QPoint(int(x/2),y), QPoint(0, int(y/2))]    
    return QRegion(QPolygon(points))   

def circle_mask(x,y):   
    return QRegion(0,0,x,y,QRegion.RegionType.Ellipse) 

def SeparatorVertical():
    Separator = QFrame()
    Separator.setFrameShape(QFrame.Shape.HLine)
    #Separator.setSizePolicy(QSizePolicy.Policy.Minimum,QSizePolicy.Policy.Expanding)
    Separator.setLineWidth(3)
    Separator.setProperty("class","Layout_Style")
    return Separator

def warning_icon(icon_h: int ,icon_w: int,tooltip_text:str):
    button = QPushButton()
    button.setFixedSize(QSize(icon_h, icon_w))
    button.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed))
    button.setMask(rhombus_mask(icon_h,icon_w))
    button.setText('!')
    button.setToolTip(tooltip_text)
    button.setProperty("class","Warning_Icon")

    return button   

def info_icon(icon_h: int ,icon_w: int,tooltip_text:str):
    button = QPushButton()
    button.setFixedSize(QSize(icon_h, icon_w))
    button.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed))
    #button.setMask(circle_mask(icon_h,icon_w))
    button.setText('?')
    button.setToolTip(tooltip_text)
    button.setProperty("class","Info_Icon")

    return button 

def StandardDropdownTemplate(LableName: str,ValuesList:list,CatchFunc,DefaultValues,Tooltipstr=None):
    #Add Sample rates dropdown
    def_lable = QLabel(LableName)
    
    dropdown = QComboBox()
    dropdown.addItems(ValuesList)
    dropdown.currentTextChanged.connect(CatchFunc)
    dropdown.setCurrentText(DefaultValues)

    whole = QVBoxLayout()
    inside = QHBoxLayout()
    inside.addWidget(def_lable)
    inside.addWidget(dropdown)

    if Tooltipstr is not None:
        info = info_icon(24,24,Tooltipstr)
        info.setProperty("class","Info_Icon_Small")
        inside.addWidget(info)
    
    whole.addLayout(inside)
    whole.addWidget(SeparatorVertical())

    return whole 

def StandardCheckboxTemplate(LableName: str,CatchFunc,DefValue,Tooltipstr=None):
    #Add Sample rates dropdown
    def_lable = QLabel(LableName)
    
    checkbox = QCheckBox()
    checkbox.setChecked(DefValue)
    checkbox.checkStateChanged.connect(CatchFunc)

    whole = QVBoxLayout()
    inside = QHBoxLayout()
    inside.addWidget(def_lable)
    inside.addWidget(checkbox)

    if Tooltipstr is not None:
        info = info_icon(24,24,Tooltipstr)
        info.setProperty("class","Info_Icon_Small")
        inside.addWidget(info)
    
    whole.addLayout(inside)
    whole.addWidget(SeparatorVertical())

    return whole     

def StandardInputTemplate(LableName: str,size:QSize,CatchFunc,DefaultValues,Tooltipstr=None):
    #Add Sample rates dropdown
    def_lable = QLabel(LableName)
    
    Input_Temp = QLineEdit()
    
    Input_Temp.setSizePolicy(QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred))
    Input_Temp.setMinimumSize(size)
    Input_Temp.textChanged.connect(CatchFunc)
    
    Input_Temp.setProperty("class","Standard_Input")
    Input_Temp.setText(DefaultValues)
    
    whole = QVBoxLayout()
    inside = QHBoxLayout()
    inside.addWidget(def_lable)
    inside.addWidget(Input_Temp)

    if Tooltipstr is not None:
        info = info_icon(24,24,Tooltipstr)
        info.setProperty("class","Info_Icon_Small")
        inside.addWidget(info)    

    whole.addLayout(inside)
    whole.addWidget(SeparatorVertical())

    return whole

def StandardLableTemplate(LableName: str,size:QSize):
    #Add Sample rates dropdown
    def_lable = QLabel(LableName)
    def_lable.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum))
    def_lable.setMinimumSize(size)

    return def_lable

def StandardButtonTemplate(ButtonText:str,ButtonSize:QSize,ButtonFucntion,Tooltipstr=None) -> QPushButton:
    standard_button = QPushButton(ButtonText)
    standard_button.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed))
    standard_button.setFixedSize(ButtonSize)
    standard_button.clicked.connect(ButtonFucntion)

    if Tooltipstr is not None:
        standard_button.setToolTip(Tooltipstr)
        
    return standard_button


def AbsLableTemplate(LableName: str,size:QSize):
    #Add Sample rates dropdown
    def_lable = QLabel(LableName)
    def_lable.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))
    def_lable.setMinimumSize(size)

    return def_lable




class FlowLayout(QBoxLayout):
    def __init__(self, parent=None):
        super().__init__(parent)

        if parent is not None:
            self.setContentsMargins(QMargins(0, 0, 0, 0))

        self._item_list = []

    def __del__(self):
        item = self.takeAt(0)
        while item:
            item = self.takeAt(0)

    def addItem(self, item):
        self._item_list.append(item)

    def count(self):
        return len(self._item_list)

    def itemAt(self, index):
        if 0 <= index < len(self._item_list):
            return self._item_list[index]

        return None

    def takeAt(self, index):
        if 0 <= index < len(self._item_list):
            return self._item_list.pop(index)

        return None

    def expandingDirections(self):
        return Qt.Orientation(0)

    def hasHeightForWidth(self):
        return True

    def heightForWidth(self, width):
        height = self._do_layout(QRect(0, 0, width, 0), True)
        return height

    def setGeometry(self, rect):
        super(FlowLayout, self).setGeometry(rect)
        self._do_layout(rect, False)

    def sizeHint(self):
        return self.minimumSize()

    def minimumSize(self):
        size = QSize()

        for item in self._item_list:
            size = size.expandedTo(item.minimumSize())

        size += QSize(2 * self.contentsMargins().top(), 2 * self.contentsMargins().top())
        return size

    def _do_layout(self, rect, test_only):
        x = rect.x()
        y = rect.y()
        line_height = 0
        spacing = self.spacing()

        for item in self._item_list:
            style = item.widget().style()
            layout_spacing_x = style.layoutSpacing(
                QSizePolicy.ControlType.PushButton, QSizePolicy.ControlType.PushButton,
                Qt.Orientation.Horizontal
            )
            layout_spacing_y = style.layoutSpacing(
                QSizePolicy.ControlType.PushButton, QSizePolicy.ControlType.PushButton,
                Qt.Orientation.Vertical
            )
            space_x = spacing + layout_spacing_x
            space_y = spacing + layout_spacing_y
            next_x = x + item.sizeHint().width() + space_x
            if next_x - space_x > rect.right() and line_height > 0:
                x = rect.x()
                y = y + line_height + space_y
                next_x = x + item.sizeHint().width() + space_x
                line_height = 0

            if not test_only:
                item.setGeometry(QRect(QPoint(x, y), item.sizeHint()))

            x = next_x
            line_height = max(line_height, item.sizeHint().height())

        return y + line_height - rect.y()