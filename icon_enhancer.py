import ctypes
import sys
from ctypes import wintypes
from PyQt5 import QtWidgets, QtGui, QtCore

class IconEnhancer(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Icon Enhancer')
        self.setGeometry(100, 100, 300, 150)
        self.setFixedSize(300, 150)

        self.label = QtWidgets.QLabel('Icon Size:', self)
        self.label.move(30, 30)

        self.slider = QtWidgets.QSlider(QtCore.Qt.Horizontal, self)
        self.slider.setGeometry(100, 30, 150, 20)
        self.slider.setMinimum(16)
        self.slider.setMaximum(256)
        self.slider.setValue(48)
        self.slider.valueChanged.connect(self.changeIconSize)

        self.applyButton = QtWidgets.QPushButton('Apply', self)
        self.applyButton.setGeometry(100, 80, 100, 30)
        self.applyButton.clicked.connect(self.applyChanges)

        self.show()

    def changeIconSize(self):
        size = self.slider.value()
        self.label.setText(f'Icon Size: {size}')

    def applyChanges(self):
        size = self.slider.value()
        self.setDesktopIconSize(size)
        QtWidgets.QMessageBox.information(self, 'Success', 'Icon size updated!')

    def setDesktopIconSize(self, size):
        SPI_SETICONMETRICS = 0x002E

        class ICONMETRICS(ctypes.Structure):
            _fields_ = [
                ("cbSize", ctypes.c_int),
                ("iHorzSpacing", ctypes.c_int),
                ("iVertSpacing", ctypes.c_int),
                ("iTitleWrap", ctypes.c_int),
                ("lfFont", ctypes.c_byte * 92)
            ]

        icon_metrics = ICONMETRICS()
        icon_metrics.cbSize = ctypes.sizeof(ICONMETRICS)
        icon_metrics.iHorzSpacing = size
        icon_metrics.iVertSpacing = size

        ctypes.windll.user32.SystemParametersInfoW(SPI_SETICONMETRICS, icon_metrics.cbSize, ctypes.byref(icon_metrics), 0)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = IconEnhancer()
    sys.exit(app.exec_())