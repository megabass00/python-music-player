# Dark Style
STYLE_DARK = {
    'MAIN_WINDOW': '''
        QMainWindow {
            background-color: black;
        }
    ''',
    'MENU': '''
        QMenuBar {  
            color: white; 
            background-color: black; 
        }
        QMenuBar::item:selected {  
            background: red;
            color: black;
        }
        QMenuBar::item:pressed {  
            background: #cacaca;
            color: black;
        }
        QMenu {  
            color: red; 
            background-color: black; 
        }
        QMenu::item:selected {  
            background: red;
            color: black;
        }
        QMenu::item:pressed {  
            background: #cacaca;
            color: white;
        }
    ''',
    'VOLUME_SLIDER': '''
        QSlider::groove:horizontal {
            border: 1px solid #860000;
            height: 12px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #FF8383, stop:1 #FDB1B1);
            margin: 2px 0;
            border-radius: 5px;
        }

        QSlider::handle:horizontal {
            background: red;
            border: 1px solid #920000;
            width: 18px;
            margin: -2px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */
            border-radius: 3px;
        }
    ''',
    'SEEK_SLIDER': '''
        QSlider::groove:horizontal {
            border: 1px solid #860000;
            height: 12px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #FF8383, stop:1 #FDB1B1);
            margin: 2px 0;
            border-radius: 5px;
        }

        QSlider::handle:horizontal {
            background: red;
            border: 1px solid #920000;
            width: 18px;
            margin: -2px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */
            border-radius: 3px;
        }
    ''',
    'LIST': '''
        QListView {
            background-color: black; 
            show-decoration-selected: 1;
        }
        QListView::item:selected {
            border: 1px solid #8B0000;
        }
        QListView::item:selected:!active {
            background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                        stop: 0 #C90000, stop: 1 #8E0202);
        }
        QListView::item:selected:active {
            background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                        stop: 0 #C90000, stop: 1 #8E0202);
        }
        QListView::item:hover {
            background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                        stop: 0 #FF8E8E, stop: 1 #FD5858);
        }
    ''',
    'LISTITEM_TITLE': '''
        color: #cacaca;
    ''',
    'LISTITEM_DURATION': '''
        color: #cacaca;
    ''',
    'CONTROL_BUTTON': '''
        QPushButton {
            background-color: red;
            border-width: 0;
            border-radius: 15px;
            padding: 20px;
        }
        QPushButton:hover {
            background-color: rgb(220, 0, 0);
        }
        QPushButton:pressed {
            background-color: rgb(200, 0, 0);
            border-style: inset;
        }
    ''',
    'INFO_LABEL': '''
        QLabel {
            color: white;
        }
    '''
}

# Light Style
STYLE_LIGHT = {
    'MAIN_WINDOW': '''
        QMainWindow {
            background-color: white;
        }
    ''',
    'MENU': '''
        QMenuBar {  
            color: black; 
            background-color: white; 
        }
        QMenuBar::item:selected {  
            color: black;
            background: #d8daf3;
        }
        QMenuBar::item:pressed {  
            color: white;
            background: #b1b5e7;
        }
        QMenu {  
            color: #31389b; 
            background-color: white; 
        }
        QMenu::item:selected {  
            color: black;
            background: #b1b5e7;
        }
        QMenu::item:pressed {  
            color: white;
            background: #888dd9;
        }
    ''',
    'VOLUME_SLIDER': '''
        QSlider {
            min-height: 20px;
            max-height: 20px;
            background: white;
        }
        QSlider::groove:horizontal {
            border: none;
            height: 2px;
            background: #d8daf3;
            margin: 0 12px;
        }
        QSlider::handle:horizontal {
            background: #888dd9;
            border: none;
            width: 23px;
            height: 50px;
            margin: -24px -12px;
        }
    ''',
    'SEEK_SLIDER': '''
        QSlider {
            min-height: 20px;
            max-height: 20px;
            background: white;
        }
        QSlider::groove:horizontal {
            border: none;
            height: 2px;
            background: #d8daf3;
            margin: 0 12px;
        }
        QSlider::handle:horizontal {
            background: #888dd9;
            border: none;
            width: 23px;
            height: 50px;
            margin: -24px -12px;
        }
    ''',
    'LIST': '''
        QListView {
            background-color: white; 
            show-decoration-selected: 1;
        }
        QListView::item:selected {
            border: 1px solid #6a6ea9;
        }
        QListView::item:selected:!active {
            background: #ABAFE5;
        }
        QListView::item:selected:active {
            background: #888dd9;
        }
        QListView::item:hover {
            background: #DCDEF1;
        }
    ''',
    'LISTITEM_TITLE': '''
        color: #616161;
    ''',
    'LISTITEM_DURATION': '''
        color: #616161;
    ''',
    'CONTROL_BUTTON': '''
        QPushButton {
            background-color: #d8daf3;
            border-width: 0;
            border-radius: 15px;
            padding: 20px;
        }
        QPushButton:hover {
            background-color: #ecedf9;
        }
        QPushButton:pressed {
            background-color: #c5c8ed;
            border-style: inset;
        }
    ''',
    'INFO_LABEL': '''
        QLabel {
            color: #616161;
        }
    '''
}

# Nature Style
STYLE_NATURE = {
    'MAIN_WINDOW': '''
        QMainWindow {
            background-color: #003300;
        }
    ''',
    'MENU': '''
        QMenuBar {  
            color: white; 
            background-color: #003300; 
        }
        QMenuBar::item:selected {  
            color: white;
            background: #008000;
        }
        QMenuBar::item:pressed {  
            color: black;
            background: #99ff99;
        }
        QMenu {  
            color: white; 
            background-color: #003300; 
        }
        QMenu::item:selected {  
            color: white;
            background: #008000;
        }
        QMenu::item:pressed {  
            color: black;
            background: #99ff99;
        }
    ''',
    'VOLUME_SLIDER': '''
        QSlider {
            min-height: 20px;
            max-height: 20px;
            background: #003300;
        }
        QSlider::groove:horizontal {
            border: none;
            height: 2px;
            background: #006600;
            margin: 0 12px;
        }
        QSlider::handle:horizontal {
            background: #99ff99;
            border: none;
            width: 10px;
            height: 20px;
            margin: -10px -12px;
            border-radius: 5px;
        }
    ''',
    'SEEK_SLIDER': '''
        QSlider::groove:horizontal {
            border: 1px solid #003300;
            height: 7px;
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #009900, stop:1 #006600);
            margin: 2px 0;
            border-radius: 2px;
        }

        QSlider::handle:horizontal {
            background: #4dff4d;
            border: 1px solid #ccffcc;
            width: 18px;
            margin: -2px 0;
            border-radius: 2px;
        }
    ''',
    'LIST': '''
        QListView {
            background-color: black; 
            show-decoration-selected: 1;
        }
        QListView::item:selected {
            border: 1px solid #99ff99;
        }
        QListView::item:selected:!active {
            background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                        stop: 0 #00b300, stop: 1 #008000);
        }
        QListView::item:selected:active {
            background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                        stop: 0 #00b300, stop: 1 #008000);
        }
        QListView::item:hover {
            background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                        stop: 0 #004d00, stop: 1 #001a00);
        }
    ''',
    'LISTITEM_TITLE': '''
        color: #cacaca;
    ''',
    'LISTITEM_DURATION': '''
        color: #cacaca;
    ''',
    'CONTROL_BUTTON': '''
        QPushButton {
            background-color: #99ff99;
            border-width: 0;
            border-radius: 3px;
            padding: 20px;
        }
        QPushButton:hover {
            background-color: #ccffcc;
        }
        QPushButton:pressed {
            background-color: #4dff4d;
            border-style: inset;
        }
    ''',
    'INFO_LABEL': '''
        QLabel {
            color: #ccffcc;
        }
    '''
}