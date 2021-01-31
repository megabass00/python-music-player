import resources_rc
import os, webbrowser, pygame, json, threading
from io import BytesIO
from PyQt5 import QtWidgets, QtGui, QtCore, QtSvg, uic
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from mutagen.id3 import ID3
from mutagen.mp3 import MP3
from PIL import Image
from utils.utils import *
from utils.config import *
from utils.styles import *
from gui.interface import Ui_MainWindow
from gui.listitem import PlaylistItem
from model.playerstate import PlayerState
from model.playworker import PlayWorker

class MusicPlayer(QtWidgets.QMainWindow, Ui_MainWindow):
    listSongs = []
    currentState = PlayerState.STOP
    currentIndex = 0
    lastSelectedPath = ''
    updateThread = None
    selectedStyle = 'dark'

    def __init__(self, *args, obj=None, **kwargs):
        super(MusicPlayer, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.iconPlay = QtGui.QIcon(':/controls/play')
        self.iconPause = QtGui.QIcon(':/controls/pause')
        self.iconStop = QtGui.QIcon(':/controls/stop')
        
        self.viewer = QtSvg.QSvgWidget()
        self.viewer.load(':info/eq-disable')
        self.viewer.setGeometry(QtCore.QRect(0, 200, 200, 70))
        self.coverLayout.addWidget(self.viewer)

        self.setUiActions()
        self.applyStyle()

        self.mixer = pygame.mixer
        self.mixer.init()
        self.setSongInfo()

        

    def setUiActions(self):
        # configure menu actions
        self.actionOpenFiles.triggered.connect(self.openFiles)
        self.actionOpenPlayList.triggered.connect(self.openPlaylist)
        self.actionSavePlayList.triggered.connect(self.savePlayList)
        self.actionExit.triggered.connect(self.exit)
        self.actionContribute.triggered.connect(self.contribute)
        self.actionAboutMe.triggered.connect(self.aboutMe)
        # self.actionStyleDark.triggered.connect(self.styleSelected)
        # self.actionStyleLight.triggered.connect(self.styleSelected)
        self.menuStyle.triggered.connect(self.styleSelected)

        # configure player actions
        self.playList.itemDoubleClicked.connect(self.listItemDoubleClick)
        self.playList.itemPressed.connect(self.listItemPressed)
        self.addButton.clicked.connect(self.openFiles)
        self.removeButton.clicked.connect(self.removeSelectedSong)

        self.playPauseButton.clicked.connect(self.playPauseSong)
        self.stopButton.clicked.connect(self.stopSong)
        self.previousButton.clicked.connect(self.previousSong)
        self.nextButton.clicked.connect(self.nextSong)
        self.volumeSlider.valueChanged.connect(self.volumeChanged)
        self.seekSlider.valueChanged.connect(self.seekChanged)

    def applyStyle(self):
        currentStyle = self.getStyle()
        self.setStyleSheet(currentStyle['MAIN_WINDOW'])
        self.menubar.setStyleSheet(currentStyle['MENU'])
        self.playList.setStyleSheet(currentStyle['LIST'])

        self.seekSlider.setStyleSheet(currentStyle['SEEK_SLIDER'])
        self.volumeSlider.setStyleSheet(currentStyle['VOLUME_SLIDER'])

        self.addButton.setStyleSheet(currentStyle['CONTROL_BUTTON'])
        self.removeButton.setStyleSheet(currentStyle['CONTROL_BUTTON'])
        self.previousButton.setStyleSheet(currentStyle['CONTROL_BUTTON'])
        self.nextButton.setStyleSheet(currentStyle['CONTROL_BUTTON'])
        self.playPauseButton.setStyleSheet(currentStyle['CONTROL_BUTTON'])
        self.stopButton.setStyleSheet(currentStyle['CONTROL_BUTTON'])

        self.infoArtistLabel.setStyleSheet(currentStyle['INFO_LABEL'])
        self.infoTitleLabel.setStyleSheet(currentStyle['INFO_LABEL'])
        self.infoAlbumLabel.setStyleSheet(currentStyle['INFO_LABEL'])
        self.durationLabel.setStyleSheet(currentStyle['INFO_LABEL'])
        self.volumeLabel.setStyleSheet(currentStyle['INFO_LABEL'])

        if (self.selectedStyle == 'light'):
            self.volumeIcon.setPixmap(QtGui.QPixmap(':controls/volume-black'))
        else:
            self.volumeIcon.setPixmap(QtGui.QPixmap(':controls/volume-white'))

        self.updatePlaylist()


    """ THREAD WORKER """
    def initUpdateWorker(self):
        self.showEQAnimation()
        self.updateThread = PlayWorker(self)
        self.updateThread.update.connect(self.updatePlayInfo)
        self.updateThread.start()

    def endUpdateWorker(self):
        self.hideEQAnimation()
        self.updateThread.running = False
        self.updateThread.quit()

    def updatePlayInfo(self):
        if (len(self.listSongs) == 0): return
        song = self.listSongs[self.currentIndex]
        self.statusLabel.setText("Playing: {0} - {1} ({2})...".format(song['artist'], song['title'], song['album']))
        self.durationLabel.setText("{0} / {1}".format(
            timeStringFromSeconds(self.seekSlider.value()), 
            timeStringFromSeconds(int(song['duration']))
        ))
        self.seekSlider.setValue(int(self.mixer.music.get_pos() / 1000))

    def resetPlayInfo(self):
        self.seekSlider.setValue(0)
        self.durationLabel.setText('0:00 / 0:00')


    """ EVENTS """
    def seekChanged(self, value):
        if self.currentState == PlayerState.PLAYING:
            total = int(self.listSongs[self.currentIndex]['duration'])
            if value >= total: value = total - 1
            # self.mixer.music.pause()
            # self.mixer.music.rewind()
            # self.mixer.music.set_pos(value)
            # self.mixer.music.unpause() 

    def volumeChanged(self, value):
        self.mixer.music.set_volume(value / 100)
        self.volumeLabel.setText(str(value) + '%')


    """ PLAYER ACTIONS """
    def listItemDoubleClick(self, item):
        self.currentIndex = self.playList.currentRow()
        self.currentState = PlayerState.STOP
        self.playPauseSong()

    def listItemPressed(self, item):
        self.listClearSelection()
        self.listSelectIndex(self.currentIndex)

    def removeSelectedSong(self):
        if (len(self.listSongs) == 0):
            showDialog(self, title='No songs!!!', text='Your playlist is empty', infoText='Firstly you must add songs to playlist')
        else:
            self.stopSong()
            self.listSongs.pop(self.currentIndex)
            self.updatePlaylist()


    """ PLAYER ACTIONS """
    def previousSong(self):
        self.currentIndex -= 1
        if self.currentIndex < 0:
            self.currentIndex = len(self.listSongs) - 1
        self.currentState = PlayerState.STOP
        self.playPauseSong()
    
    def nextSong(self):
        self.currentIndex += 1
        if self.currentIndex >= len(self.listSongs):
            self.currentIndex = 0
        self.currentState = PlayerState.STOP
        self.playPauseSong()
             
    def playPauseSong(self):
        if self.currentState == PlayerState.STOP:
            if len(self.listSongs) == 0: return 
            song = self.listSongs[self.currentIndex]
            self.setSongInfo(song)
            self.listSelectIndex(self.currentIndex)
            self.seekSlider.setRange(0, int(song['duration']))
            self.seekSlider.setValue(0)
            self.mixer.music.load(song['path'])
            self.mixer.music.play()
            self.currentState = PlayerState.PLAYING
            self.playPauseButton.setIcon(self.iconPause)
            self.initUpdateWorker()

        elif self.currentState == PlayerState.PLAYING:
            self.mixer.music.pause()
            self.currentState = PlayerState.PAUSE
            self.playPauseButton.setIcon(self.iconPlay)
            self.endUpdateWorker()

        elif self.currentState == PlayerState.PAUSE:
            self.mixer.music.unpause()
            self.currentState = PlayerState.PLAYING
            self.playPauseButton.setIcon(self.iconPause)
            self.initUpdateWorker()

    def stopSong(self):
        if (self.currentState == PlayerState.STOP): return
        self.mixer.music.fadeout(STOP_FADEOUT)
        self.currentState = PlayerState.STOP
        self.playPauseButton.setIcon(self.iconPlay)
        self.endUpdateWorker()
        self.listClearSelection()
        self.setSongInfo()
        self.resetPlayInfo()
        self.updateStatusLabel()
            

    """ MENU ACTIONS """
    def openFiles(self):
        filters = 'MP3 Files (*.mp3)'
        files, _ = QFileDialog.getOpenFileNames(self, 'Select files to add playlist', self.defaultDir(), filters)
        for file in files:
            if file.endswith('.mp3') and not self.pathExistsInPlaylist(file):
                self.addSongToPlaylist(file)

        if len(files) > 0:
            self.lastSelectedPath = os.path.basename(files[0])
            self.updatePlaylist()

    def updatePlaylist(self):
        self.playList.clear()
        self.stopSong()
        self.currentIndex = 0
        self.updateStatusLabel()
        if (len(self.listSongs) == 0): return
        currentStyle = self.getStyle()
        for item in self.listSongs:
            listItem = PlaylistItem()
            listItem.setCover(pilTopixmap(b64ToImage(item['cover'])))
            listItem.setTitle(item['title'])
            listItem.titleLabel.setStyleSheet(currentStyle['LISTITEM_TITLE'])
            listItem.setDuration(str(item['duration']))
            listItem.durationLabel.setStyleSheet(currentStyle['LISTITEM_DURATION'])
            listWidgetItem = QtWidgets.QListWidgetItem()
            listWidgetItem.setSizeHint(listItem.sizeHint())
            self.playList.addItem(listWidgetItem)
            self.playList.setItemWidget(listWidgetItem, listItem)
    
    def openPlaylist(self):
        filePath, _ = QFileDialog.getOpenFileName(self, 'Select a playlist to open', self.defaultDir(), 'Playlist (*.json )')
        if filePath == '': return
        self.lastSelectedPath = os.path.basename(filePath)
        jsonFile = open(filePath)
        jsonArray = json.load(jsonFile)
        self.listSongs.clear()
        for item in jsonArray:
            self.listSongs.append(item)
        
        if len(jsonArray) > 0:
            self.updatePlaylist()

    def savePlayList(self):
        filePath, _ = QFileDialog.getSaveFileName(self, 'Save current playlist', self.defaultDir(), ('Playlist Files (*.json)'))
        if filePath != '':
            self.lastSelectedPath = os.path.basename(filePath)
        with open(filePath, 'w') as outfile:
            json.dump(self.listSongs, outfile)

    def exit(self):
        print('see u soon!!!')
        self.mixer.music.unload()
        if self.updateThread !=  None and self.updateThread.isRunning():
            print('Quiting update thread')
            self.endUpdateWorker()
    
    def contribute(self):
        webbrowser.open('https://github.com/megabass00/python-music-player')
    
    def aboutMe(self):
        webbrowser.open('https://github.com/megabass00')

    def styleSelected(self, action):
        if action.text() == 'Dark':
            self.selectedStyle = 'dark'
        elif action.text() == 'Light':
            self.selectedStyle = 'light'
        elif action.text() == 'Nature':
            self.selectedStyle = 'nature'
        self.applyStyle()

        actions = self.menuStyle.actions()
        for i in range(len(actions)):
            currentAction = actions[i]
            if currentAction.text() != action.text():
                currentAction.setChecked(False)
            else:
                currentAction.setChecked(True)
    

    """ CLASS METHODS """
    def addSongToPlaylist(self, filePath):
        realpath = os.path.realpath(filePath)
        track = MP3(realpath)
        # for key in track.tags.__dict__:
        #     print(key)
        tags = ID3(realpath)
        # print(tags.pprint())
        duration = track.info.length
        bitrate = track.info.bitrate
        channels = track.info.channels
        sampleRate = track.info.sample_rate

        title = track.tags['TIT2'].text[0] if 'TIT2' in track.tags else   \
                track.tags['TOFN'].text[0] if 'TOFN' in track.tags else \
                os.path.basename(os.path.normpath(filePath)).split('.')[0]

        album = track.tags['TALB'].text[0] if 'TALB' in track.tags else   \
                track.tags['TOAL'].text[0] if 'TOAL' in track.tags else   \
                'Unknown Album'
        if album.strip() == '': album = 'Unknown Album'

        artist = track.tags['TOPE'].text[0] if 'TOPE' in track.tags else 'Unknown Artist'
        if artist.strip() == '': artist = 'Unknown Artist'

        if tags.get('APIC:') is not None:
            pict = tags.get('APIC:').data
            cover = Image.open(BytesIO(pict)).convert('RGB')
            print('Cover picture size: ' + str(cover.size)) 
        else:
            cover = self.coverPlaceholderImage()
            print('Opps! no cover was recovered')

        dict = {}
        dict['path'] = str(realpath)
        dict['duration'] = str(int(duration))
        dict['bitrate'] = str(bitrate)
        dict['channels'] = str(channels)
        dict['samplerate'] = str(sampleRate)
        dict['artist'] = str(artist)
        dict['title'] = str(title)
        dict['album'] = str(album)
        dict['cover'] = imageToB64(cover)
        self.listSongs.append(dict.copy())

    def setSongInfo(self, song=None):
        artist = '-'
        title = '-'
        album = '-'
        cover = None
        if song is not None:
            artist = song['artist']
            title = song['title']
            album = song['album']
            cover = song['cover']
        self.infoArtistLabel.setText(artist)
        self.infoTitleLabel.setText(title)
        self.infoAlbumLabel.setText(album)
        if cover is None:
            coverPlaceholder = QtGui.QIcon(':/info/cover')
            pixmap = coverPlaceholder.pixmap(self.coverLabel.width(), self.coverLabel.height())
            self.coverLabel.setPixmap(pixmap)
        else:
            coverPixmap = pilTopixmap(b64ToImage(cover))
            resized = coverPixmap.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
            self.coverLabel.setPixmap(resized)

    def pathExistsInPlaylist(self, path):
        for item in self.listSongs:
            if item['path'] == os.path.realpath(path):
                return True

        return False

    def coverPlaceholderImage(self):
        image = QtGui.QImage(':info/cover')
        buff = QtCore.QBuffer()
        buff.open(QtCore.QBuffer.ReadWrite)
        image.save(buff, 'PNG')
        return Image.open(BytesIO(buff.data()))

    def defaultDir(self):
        if self.lastSelectedPath != '':
            return self.lastSelectedPath
        else:
            return DEFAULT_SOURCE_DIR 

    def listClearSelection(self):
        for i in range(self.playList.count()):
            item = self.playList.item(i)
            item.setSelected(False)

    def listSelectIndex(self, index):
        item = self.playList.item(index)
        item.setSelected(True)
        self.playList.setFocus()
    
    def updateStatusLabel(self):
        if (len(self.listSongs) > 0):
            self.statusLabel.setText('Select a song and play it')
        else:
            self.statusLabel.setText('Load songs and play them...')

    def getStyle(self):
        if self.selectedStyle == 'dark':
            return STYLE_DARK
        elif self.selectedStyle == 'light':
            return STYLE_LIGHT
        elif self.selectedStyle == 'nature':
            return STYLE_NATURE
        return STYLE_DARK # default

    def showEQAnimation(self):
        self.viewer.load(':info/eq-enable')

    def hideEQAnimation(self):
        self.viewer.load(':info/eq-disable')

