from PyQt6.QtGui import QPolygon,QRegion
from PyQt6.QtCore import QPoint,QSize
from PyQt6.QtWidgets import (QPushButton
                             ,QSizePolicy
                             ,QComboBox
                             ,QLabel
                             ,QHBoxLayout
                             ,QCheckBox
                             ,QLineEdit
                             ,QVBoxLayout
                             ,QLayout)

def sign_mask(x,y):
    points = [QPoint(0, 0), QPoint(int(x/2), 0), QPoint(x, int(y/2)), QPoint(int(x/2), y), QPoint(0, y)]    
    return QRegion(QPolygon(points))
    
def rhombus_mask(x,y):
    points = [QPoint(int(x/2), 0), QPoint(x, int(y/2)), QPoint(int(x/2),y), QPoint(0, int(y/2))]    
    return QRegion(QPolygon(points))   

def circle_mask(x,y):   
    return QRegion(0,0,x,y,QRegion.RegionType.Ellipse) 

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

    whole = QHBoxLayout()
    whole.addWidget(def_lable)
    whole.addWidget(dropdown)

    if Tooltipstr is not None:
        info = info_icon(24,24,Tooltipstr)
        info.setProperty("class","Info_Icon_Small")
        whole.addWidget(info)

    return whole 

def StandardCheckboxTemplate(LableName: str,CatchFunc,Tooltipstr=None):
    #Add Sample rates dropdown
    def_lable = QLabel(LableName)
    
    checkbox = QCheckBox()
    checkbox.checkStateChanged.connect(CatchFunc)

    whole = QHBoxLayout()
    whole.addWidget(def_lable)
    whole.addWidget(checkbox)

    if Tooltipstr is not None:
        info = info_icon(24,24,Tooltipstr)
        info.setProperty("class","Info_Icon_Small")
        whole.addWidget(info)

    return whole     

def StandardInputTemplate(LableName: str,size:QSize,CatchFunc,DefaultValues,Tooltipstr=None):
    #Add Sample rates dropdown
    def_lable = QLabel(LableName)
    
    Input_Temp = QLineEdit()
    
    Input_Temp.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed))
    Input_Temp.setFixedSize(size)
    Input_Temp.textChanged.connect(CatchFunc)
    
    Input_Temp.setProperty("class","Standard_Input")
    Input_Temp.setText(DefaultValues)
    
    whole = QHBoxLayout()
    whole.addWidget(def_lable)
    whole.addWidget(Input_Temp)

    if Tooltipstr is not None:
        info = info_icon(24,24,Tooltipstr)
        info.setProperty("class","Info_Icon_Small")
        whole.addWidget(info)    

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