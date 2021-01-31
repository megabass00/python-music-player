import sys
from PyQt5.QtWidgets import QApplication 
from gui.main import MusicPlayer

# init app
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MusicPlayer()
    window.show()
    app.exec()
