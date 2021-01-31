from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QSizePolicy
from utils.utils import timeStringFromSeconds
from utils.config import *

class PlaylistItem(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(PlaylistItem, self).__init__(parent)
        self.mainLayout = QtWidgets.QGridLayout()
        self.mainLayout.setContentsMargins(5, 5, 5, 5)

        self.cover = QtWidgets.QLabel()
        
        self.titleLabel = QtWidgets.QLabel()
        self.titleLabel.setFont(LISTITEM_LABELS_FONT)
        self.titleLabel.setWordWrap(True)
        self.titleLabel.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.titleLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        self.durationLabel = QtWidgets.QLabel()
        self.durationLabel.setFont(LISTITEM_LABELS_FONT)
        self.durationLabel.setFixedWidth(LISTITEM_DURATION_WIDTH)
        self.durationLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        
        self.mainLayout.addWidget(self.cover, 0, 0)
        self.mainLayout.addWidget(self.titleLabel, 0, 1)
        self.mainLayout.addWidget(self.durationLabel, 0, 2)
        self.setLayout(self.mainLayout)
        
        # apply styles
        self.titleLabel.setStyleSheet('''
            color: #cacaca;
        ''')
        self.durationLabel.setStyleSheet('''
            color: #cacaca;
        ''')

    def setCover(self, coverPixmap):
        resized = coverPixmap.scaled(50, 50, QtCore.Qt.KeepAspectRatio)
        self.cover.setPixmap(resized)

    def setTitle(self, title):
        self.titleLabel.setText(title)

    def setDuration(self, duration):
        self.durationLabel.setText(timeStringFromSeconds(duration))