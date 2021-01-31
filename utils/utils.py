import base64
from io import BytesIO
from PIL import Image
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QImage, QPixmap

# convert seconds to human time string
def timeStringFromSeconds(duration):
    # ms = int(secs) * 1000
    secs = int(duration)
    seconds = secs % 60
    seconds = int(seconds)
    minutes =(secs / 60) % 60
    minutes = int(minutes)
    hours = (secs / (60 * 60)) % 24
    if int(hours) > 0:
        return "{0}:{:02}:{:02}".format(hours, minutes, seconds)
    else:
        return "{:02}:{:02}".format(minutes, seconds)

# convert image to base64 string
def imageToB64(image):
    if image is None: return ''
    buff = BytesIO()
    image.convert('RGB').save(buff, format='JPEG')
    byteString = base64.b64encode(buff.getvalue())
    return byteString.decode('utf-8')

# convert base64 string to image
def b64ToImage(b64String):
    if b64String is None: return False
    byteString = b64String.encode('utf-8')
    buff = BytesIO(base64.b64decode(b64String))
    return Image.open(buff)

# convert PIL image to QImage
def pilTopixmap(image):
    bytes_img = BytesIO()
    image.save(bytes_img, format='JPEG')
    qimg = QImage()
    qimg.loadFromData(bytes_img.getvalue())
    return QPixmap.fromImage(qimg)

# show custom dialog
def showDialog(self, icon=QMessageBox.Information, title='Python Music Player', text='', infoText=None, detailText=None):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle(title)
        msg.setText(text)
        if (infoText != None): msg.setInformativeText(infoText)
        if (detailText != None): msg.setDetailedText(detailText)
        msg.setStandardButtons(QMessageBox.Ok)
        return msg.exec_()