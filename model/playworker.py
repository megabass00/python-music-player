import time
from PyQt5.QtCore import QThread, pyqtSignal
from utils.config import UPDATE_FREQUENCY

class PlayWorker(QThread):
    update = pyqtSignal()

    def __init__(self, parent=None):
        QThread.__init__(self, parent)
        self.running = False

    def run(self):
        self.running = True
        while self.running:
            self.update.emit()
            time.sleep(UPDATE_FREQUENCY)
        # print('** End thread', self.currentThread())