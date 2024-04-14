#подключение библиотек
from random import shuffle
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QPushButton, QHBoxLayout, QMessageBox, QRadioButton, QGroupBox, QButtonGroup
#создание приложения и главного окна
class Question():
    def __init__(
    self, queastion, right_answer,
    wrong1, wrong2, wrong3):
        self.queastion = queastion
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

total  = 0
right = 0

queastions = []
queastions.append(Question('В каком году Mr Beast Создал канал', '2012', '2013', '2011', '2009'))

queastions.append(Question('Кто во время ухаживания кусают друг друга?', 
                            'синие акулы', 
                            'лангусты', 
                            'ленивцы', 
                            'кошки'))
queastions.append(Question('О чем речь? \n эта станция метро была построена в столице Украины в Киевеи считается самой глубокой в мире (105,5)', 
                            'Арсенальная', 
                            'бигест', 'морская', 'станция 546'))
queastions.append(Question('в каком году в Польше были выпущены коллекционные монеты с изображением героев советского мультфильма `Ну, погоди`', 
                            '2010', '1458', '2019', '2018'))
queastions.append(Question('где в средневековье подавали пиво на завтрак?', 'Англия', 'Нигер', 'Китай', 'Норвегия'))

app = QApplication([])
main_win = QWidget()
main_win.resize(500,125)
#создание виджетов главного окна
main_win.setWindowTitle('Конкурс от Crazy people')
box = QGroupBox()
box_answer = QGroupBox()
layout_box = QVBoxLayout()
answer_text = QLabel('Прав ты или нет?')
layout_box.addWidget(answer_text, alignment = Qt.AlignCenter)
box_answer.setLayout(layout_box)

queastion = QLabel ('В каком году Mr Beast Создал канал')
groop_btn = QButtonGroup()
btn_answer1 = QRadioButton('2012')
btn_answer2 = QRadioButton('2014')
btn_answer3 = QRadioButton('2015')
btn_answer4 = QRadioButton('2009')
btn_list = [btn_answer1,btn_answer2,btn_answer3,btn_answer4]



groop_btn.addButton(btn_answer1)
groop_btn.addButton(btn_answer2)
groop_btn.addButton(btn_answer3)
groop_btn.addButton(btn_answer4)
Layout_main = QVBoxLayout()

Layout_h1 = QHBoxLayout()
Layout_h2 = QHBoxLayout()





# btn_answer4.clicked.connect(show_win)
# btn_answer1.clicked.connect(show_looser)
# btn_answer2.clicked.connect(show_looser)
# btn_answer3.clicked.connect(show_looser)

Layout_main.addWidget(queastion, alignment = Qt.AlignCenter)
Layout_h1.addWidget(btn_answer1, alignment = Qt.AlignCenter)
Layout_h1.addWidget(btn_answer2, alignment = Qt.AlignCenter)
Layout_h2.addWidget(btn_answer3,alignment = Qt.AlignCenter)
Layout_h2.addWidget(btn_answer4, alignment = Qt.AlignCenter)
LayoutW1 = QVBoxLayout()
# LayoutW1.addLayout(Layout_h1)
LayoutW1.addLayout(Layout_h1)
LayoutW1.addLayout(Layout_h2)
box.setLayout(LayoutW1)
# box.setLayout(Layout_h3)
btn = QPushButton('ОТВЕТИТЬ')

Layout_main.addWidget(box)
Layout_main.addWidget(box_answer)
box_answer.hide()

Layout_main.addWidget(btn, stretch = 2)
main_win.setLayout(Layout_main)

#расположение виджетов по лэйаутам

#обработка нажатий на переключатели
def ask(q: Question):

    shuffle(btn_list)
    btn_list[0].setText(q.right_answer)
    btn_list[1].setText(q.wrong1)
    btn_list[2].setText(q.wrong2)
    btn_list[3].setText(q.wrong3)
    answer_text.setText(q.right_answer)
    queastion.setText(q.queastion)
    show_qestion()

def show_result(result):
    answer_text.setText(result)
    show_answer()

def check_answer():
    if btn_list[0].isChecked():
        global right
        show_result('Правильно!')
        right+=1
    else:
        if btn_list[1].isChecked() or btn_list[2].isChecked() or btn_list[3].isChecked():

            show_result('неправильно!')
current_q = 0
def next_question():
    global current_q, total
    total+=1
    
    print('statistic:')
    print('total qestion:', total)
    print('correct answers:',right)
    print('rating', (right/total)*100,'%')
    current_q += 1
    if current_q > len(queastions):
        current_q = 0
    q = queastions[current_q]
    ask(q)

def show_answer():
    box.hide()
    box_answer.show()
    btn.setText('След. вопрос')

def show_qestion():
    box.show()
    box_answer.hide()
    btn.setText('ОТВЕТИТЬ')
    groop_btn.setExclusive(False)
    btn_answer1.setChecked(False)
    btn_answer2.setChecked(False)
    btn_answer3.setChecked(False)
    btn_answer4.setChecked(False)
    groop_btn.setExclusive(True)

def change():
    if btn.text() == 'ОТВЕТИТЬ':
        check_answer()
    else:
        next_question()
#отображение окна приложения 
btn.clicked.connect(change)
main_win.show()
app.exec_()