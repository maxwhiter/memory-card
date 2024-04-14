from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QFileDialog, # Диалог открытия файлов (и папок)
    QLabel, QPushButton, QListWidget,
    QHBoxLayout, QVBoxLayout
)
import os

from PIL import Image, ImageFilter

from PyQt5.QtGui import QPixmap


from PyQt5.QtCore import Qt

app = QApplication([])
window = QWidget()
window.resize(700, 500)
window.setWindowTitle('Редактор')
# Виджеты для редактора
label = QLabel('Картинка')
btn_folder = QPushButton('Папка')
btn_bw = QPushButton('Ч/Б') # Кнопка черно-белого режима
btn_left = QPushButton('Лево')
btn_right = QPushButton('Право')
btn_mirror = QPushButton('Зеркало')
btn_sharpness = QPushButton('Резкость (-)')
btn_blur = QPushButton('Размытость')
list_pic = QListWidget()
# Создаём лэйауты
main_h_layout = QHBoxLayout()
v1 = QVBoxLayout()
v2 = QVBoxLayout()
h_btns_layout = QHBoxLayout()
# Размещение кнопок на лэйаут
h_btns_layout.addWidget(btn_left)
h_btns_layout.addWidget(btn_blur)
h_btns_layout.addWidget(btn_right)
h_btns_layout.addWidget(btn_mirror)
h_btns_layout.addWidget(btn_sharpness)
h_btns_layout.addWidget(btn_bw)
# Размещение списка фоток и кнопки "Папка"
v1.addWidget(btn_folder)
v1.addWidget(list_pic)
# Добавляем ко второму вертикальному лэйауту v2 надпись "Картинка" и 
# список кнопок 
v2.addWidget(label, 95)
v2.addLayout(h_btns_layout)
# Добавляем к основному лэйауту побочные вертикальные v1, v2
main_h_layout.addLayout(v1, 20)
main_h_layout.addLayout(v2, 80)
# Добавляем к окну window наш главный лэйаут
window.setLayout(main_h_layout)
window.show()

directory = ''

class ImageProcessor():
    def __init__(self):
        self.filename = None
        self.image = None
        self.dir = None
        self.save_dir = 'changed/'
    def loadImage(self, filename):
        self.filename = filename
        image_path = os.path.join(directory, filename)
        self.image = Image.open(image_path)

    def showImage(self, path):
        label.hide()
        pixmapimage = QPixmap(path)
        w, h = label.width(), label.height()
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        label.setPixmap(pixmapimage)
        label.show()

    def saveImage(self):
        path = os.path.join(directory,self.save_dir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self.filename)
        self.image.save(image_path)
    
    def do_bw(self):
        self.image = self.image.convert('L')
        self.saveImage()
        image_path = os.path.join(directory, self.save_dir, self.filename)
        self.showImage(image_path)
        print('Сделана картинка чб')

    def miror(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveImage()
        image_path = os.path.join(directory, self.save_dir, self.filename)
        self.showImage(image_path)

    def blur(self):
        self.image = self.image.filter(ImageFilter.BLUR)
        self.saveImage()
        image_path = os.path.join(directory, self.save_dir, self.filename)
        self.showImage(image_path)

    def sharpen(self):
        self.image = self.image.filter(ImageFilter.SHARPEN)
        self.saveImage()
        image_path = os.path.join(directory, self.save_dir, self.filename)
        self.showImage(image_path)

    def left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.saveImage()
        image_path = os.path.join(directory, self.save_dir, self.filename)
        self.showImage(image_path)


    def right(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.saveImage()
        image_path = os.path.join(directory, self.save_dir, self.filename)
        self.showImage(image_path)


workdir = ImageProcessor()

def showChosenImage():
    if list_pic.currentRow() >= 0:
        filename = list_pic.currentItem().text()
        workdir.loadImage(filename)
        image_path = os.path.join(directory, workdir.filename)
        workdir.showImage(image_path)

def filter(files, extensions):
    result = []
    for filename in files:
        for ext in extensions:
            if filename.endswith(ext):
                result.append(filename)
    return result

def chooseWorkDir():
    global directory
    directory = QFileDialog.getExistingDirectory()

def showFilenamesList():
    extensions = ['.jpg','.jpeg', '.png', '.gif', '.bmp']
    chooseWorkDir()

    filenames = filter(os.listdir(directory), extensions)

    
    list_pic.clear()
    for file in filenames:
        list_pic.addItem(file)
    
btn_folder.clicked.connect(showFilenamesList)
list_pic.currentRowChanged.connect(showChosenImage)
btn_bw.clicked.connect(workdir.do_bw)
btn_mirror.clicked.connect(workdir.miror)
btn_blur.clicked.connect(workdir.blur)
btn_left.clicked.connect(workdir.left)
btn_right.clicked.connect(workdir.right)
btn_sharpness.clicked.connect(workdir.sharpen)
app.exec_()
