# Python Music Player
Basic music player written in *python 3.8* using [PyQt5](https://pypi.org/project/PyQt5/). Interface is designed with tool from [PyQt5-tools](https://pypi.org/project/pyqt5-tools/) (Qt Designer) and after converted to python file. Songs management is controlled by [Pygame](https://www.pygame.org/docs/ref/music.html) library and mp3 metadata processing by [Mutagen](https://mutagen.readthedocs.io/en/latest/index.html). I have also used [Pillow](https://pillow.readthedocs.io/en/stable/index.html) library to manage image data.

Play music files and read mp3 metadata:\
![Python Music Player](https://github.com/megabass00/python-music-player/blob/master/snapshots/player1.gif?raw=true)  
  
Color themes to coustomize view:\
![Python Music Player](https://github.com/megabass00/python-music-player/blob/master/snapshots/player2.gif?raw=true)  
  
## Features
- Customized UI from stylesheet
- Read mp3 metadata (title, album, cover image...)
- Menu bar with actions
- Background thread to update song position
- Volume & play control
- Managed playlist items
- Save playlist to external file
- Load playlist from external file
- Several color themes to choose

## Requeriments
- python 3.5 >=
- PyQt5 5.15.2 >=
- pygame 2.0.1 >=
- mutagen 1.45.1 >=
- pillow 8.1.0 >= 
- PyQt5-tools 5.15.2 >= (optionally) 

If you want you can install packages needed executing __pip install -r requirements.txt__.

## To use
To clone and run this repository you'll need to be installed [Git](https://git-scm.com/) on your computer. I recomend install [Anaconda](https://www.anaconda.com/) to manage Python virtual environments wich helps to arrange python packages. 
````
# Clone this repository
git clone https://github.com/megabass00/python-music-player

# Optionally create virtual environment
conda create --name music-player python=3.8
conda activate music-player

# Install required packages
pip install -r requirements.txt

# Run project
python init.py
````

## Config files
It has some configuration files where you can change several settings:
- utils/config.py: it contains project constants
- utils/styles.py: this file has project stylesheets 

[Here](https://doc.qt.io/qt-5/stylesheet-examples.html) you can encounter a lot of Qt stylesheet examples.

## Commands useful
Bellow you have some userful commands to compile resources, convert ui to python file... In this manner you can contribute to expand project becouse there are some features waiting to be developed :smirk:.

For convert Qt Designer interface to python file
````
pyuic5 -o gui/interface.py interface.ui
```` 

For convert .qrc resources file to python file
````
pyrcc5 assets/resources.qrc -o resources_rc.py
````