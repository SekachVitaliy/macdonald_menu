from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
import sys


class Ui_MainWindow(object):
    def __init__(self):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1000, 1000)
        MainWindow.setWindowTitle('Меню')
        MainWindow.setWindowIcon(QIcon('img/icon.png'))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.previous_menu = 'burgeru'
        self.first_menu = True

        # Инициализация главного текста
        self.main_label = QtWidgets.QLabel(self.centralwidget)
        self.main_label.setGeometry(QtCore.QRect(300, 10, 530, 70))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        self.main_label.setFont(font)
        self.main_label.setAlignment(QtCore.Qt.AlignCenter)
        self.main_label.setObjectName("main_label")
        self.main_label.setText("МЕНЮ")

        # Инициализация кнопки Отмена
        self.otmena = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.otmena.setGeometry(QtCore.QRect(100, 920, 250, 60))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(27)
        font.setBold(True)
        self.otmena.setFont(font)
        self.otmena.setObjectName("otmena")
        self.otmena.setText("Отмена")

        # Инициализация кнопки Оплата
        self.oplata = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.oplata.setGeometry(QtCore.QRect(700, 920, 250, 60))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(27)
        font.setBold(True)
        self.oplata.setFont(font)
        self.oplata.setObjectName("oplata")
        self.oplata.setText("Оплатить")

        # Инициализация кнопки навигации Бургери
        self.burgeru = QtWidgets.QPushButton(self.centralwidget)
        self.burgeru.setGeometry(QtCore.QRect(20, 200, 150, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        font.setBold(True)
        self.burgeru.setFont(font)
        self.burgeru.setObjectName("burgeru")
        self.burgeru.setStyleSheet('border-style: solid; border-width: 1px; border-color: black;')
        self.burgeru.setText("Бургери")

        # Инициализация кнопки навигации Гарниры
        self.garniru = QtWidgets.QPushButton(self.centralwidget)
        self.garniru.setGeometry(QtCore.QRect(20, 250, 150, 50))
        self.garniru.setFont(font)
        self.garniru.setObjectName("garniru")
        self.garniru.setStyleSheet('border-style: solid; border-width: 1px; border-color: black;')
        self.garniru.setText("Гарніри")

        # Инициализация кнопки навигации Курица
        self.kyrka = QtWidgets.QPushButton(self.centralwidget)
        self.kyrka.setGeometry(QtCore.QRect(20, 300, 150, 50))
        self.kyrka.setFont(font)
        self.kyrka.setObjectName("kyrka")
        self.kyrka.setStyleSheet('border-style: solid; border-width: 1px; border-color: black;')
        self.kyrka.setText("Курка")

        # Инициализация кнопки навигации Напитки
        self.napoi = QtWidgets.QPushButton(self.centralwidget)
        self.napoi.setGeometry(QtCore.QRect(20, 350, 150, 50))
        self.napoi.setFont(font)
        self.napoi.setObjectName("napoi")
        self.napoi.setStyleSheet('border-style: solid; border-width: 1px; border-color: black;')
        self.napoi.setText("Напої")

        # Инициализация линни для красоты
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 650, 1000, 60))
        self.line.setStyleSheet("color: rgb(69, 139, 103);")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(60)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")

        # Инициализация надписи 'Мой заказ'
        self.static_label_zakaz = QtWidgets.QLabel(self.centralwidget)
        self.static_label_zakaz.setGeometry(QtCore.QRect(20, 660, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        self.static_label_zakaz.setFont(font)
        self.static_label_zakaz.setStyleSheet("background-color: rgb(69, 139, 103);\n"
                                              "color: rgb(255, 255, 255);\n"
                                              "")
        self.static_label_zakaz.setObjectName("static_label_zakaz")
        self.static_label_zakaz.setText("Мой заказ")

        # Инициализация надписи 'Всего:0'
        self.suma = QtWidgets.QLabel(self.centralwidget)
        self.suma.setGeometry(QtCore.QRect(720, 660, 300, 40))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        self.suma.setFont(font)
        self.suma.setStyleSheet("background-color:rgb(69, 139, 103);\n"
                                "color: rgb(255, 255, 255);")
        self.suma.setObjectName("suma")
        self.suma.setText("Всего: 0")
        self.suma.result = 0

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)

        self.zakaz = QtWidgets.QTextEdit(self.centralwidget)
        self.zakaz.setStyleSheet("border: 0px solid black }")
        self.zakaz.setReadOnly(True)
        self.zakaz.setGeometry(QtCore.QRect(20, 720, 600, 200))
        self.zakaz.setObjectName("zakaz")
        self.zakaz.setFont(font)
        # burgeru[0] = big_mak, [1]=big_texas, [2]=big_teysti, [3]=double_chiz, [4]=gamburger, [5]=mak_chicken

        self.zakaz.burgeru = [
            {
                "name": "Біг Техас",
                "price": 0,
                "quantity": 0,
                "gaps": 20

            },
            {
                "name": "Біг Тейсті",
                "price": 0,
                "quantity": 0,
                "gaps": 19

            },
            {
                "name": "Дабл Чізбургер",
                "price": 0,
                "quantity": 0,
                "gaps": 15
            },
            {
                "name": "Біг Мак",
                "price": 0,
                "quantity": 0,
                "gaps": 22
            },
            {
                "name": "Гамбургер",
                "price": 0,
                "quantity": 0,
                "gaps": 20
            },
            {
                "name": "МакЧікен",
                "price": 0,
                "quantity": 0,
                "gaps": 21
            }]
        # chicken[0] = double_kentuki, [1]=chicken_rol, [2]=naggets_6, [3]=naggets_9, [4]=naggets_20
        self.zakaz.chicken = [
            {
                "name": "Дабл Кентукі",
                "price": 0,
                "quantity": 0,
                "gaps": 17

            },
            {
                "name": "Чікен Рол",
                "price": 0,
                "quantity": 0,
                "gaps": 20

            },
            {
                "name": "Чікен Наггетс 6шт",
                "price": 0,
                "quantity": 0,
                "gaps": 12
            },
            {
                "name": "Чікен Наггетс 9шт",
                "price": 0,
                "quantity": 0,
                "gaps": 12
            },
            {
                "name": "Чікен Наггетс 20шт",
                "price": 0,
                "quantity": 0,
                "gaps": 11
            }]
        # garniru[0] = chicken_salat, [1]=salat, [2]=dipu, [3]=small_fri [4]=big_fri, [5]=sous_fri
        self.zakaz.garniru = [
            {
                "name": "Чікен салат",
                "price": 0,
                "quantity": 0,
                "gaps": 18

            },
            {
                "name": "Мікс салат",
                "price": 0,
                "quantity": 0,
                "gaps": 19

            },
            {
                "name": "Діпи",
                "price": 0,
                "quantity": 0,
                "gaps": 25
            },
            {
                "name": "Картопля Фрі маленька",
                "price": 0,
                "quantity": 0,
                "gaps": 8
            },
            {
                "name": "Картопля Фрі велика",
                "price": 0,
                "quantity": 0,
                "gaps": 10
            },
            {
                "name": "Картопля Фрі з сирним соусом",
                "price": 0,
                "quantity": 0,
                "gaps": 1
            }]
        # napoi[0] = amerikano, [1]=late, [2]=black_tea, [3]=coca_cola, [4]=fanta, [5]=sprite
        self.zakaz.napoi = [
            {
                "name": "Американо",
                "price": 0,
                "quantity": 0,
                "gaps": 20

            },
            {
                "name": "Лате",
                "price": 0,
                "quantity": 0,
                "gaps": 25

            },
            {
                "name": "Чорний чай",
                "price": 0,
                "quantity": 0,
                "gaps": 19
            },
            {
                "name": "Кока-кола",
                "price": 0,
                "quantity": 0,
                "gaps": 20
            },
            {
                "name": "Фанта",
                "price": 0,
                "quantity": 0,
                "gaps": 24
            },
            {
                "name": "Спрайт",
                "price": 0,
                "quantity": 0,
                "gaps": 23
            }]

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #  Покдлючение обраточников к кнопке
        self.otmena.clicked.connect(lambda: self.func_otmena())
        self.oplata.clicked.connect(lambda: self.func_oplata())
        self.burgeru.clicked.connect(lambda: self.show_menu_burgeru())
        self.garniru.clicked.connect(lambda: self.show_menu_garniru())
        self.kyrka.clicked.connect(lambda: self.show_menu_kyrka())
        self.napoi.clicked.connect(lambda: self.show_menu_napoi())

    def setupUi(self, MainWindow):
        self.show_menu_burgeru()

    # функция показывает меню бургери-----------------------------------------------------------------------------------
    def show_menu_burgeru(self):
        self.set_menu('burgeru')
        self.main_label.setText('Бургери')

        self.big_texas = QtWidgets.QPushButton(self.centralwidget)
        self.big_texas.name = 'Біг Техас'
        self.big_texas.setGeometry(QtCore.QRect(250, 100, 200, 200))
        self.big_texas.setStyleSheet("background-image: url(img/burgeru/big_texas.png);border-style: none;")
        self.big_texas.price = 52.00
        self.big_texas.clicked.connect(lambda: self.pressed_big_texas())

        self.big_teysti = QtWidgets.QPushButton(self.centralwidget)
        self.big_teysti.name = 'Біг Тейсті'
        self.big_teysti.setGeometry(QtCore.QRect(500, 100, 200, 200))
        self.big_teysti.setStyleSheet("background-image: url(img/burgeru/big_teysti.png);border-style: none;")
        self.big_teysti.price = 55.00
        self.big_teysti.clicked.connect(lambda: self.pressed_big_teysti())

        self.double_chiz = QtWidgets.QPushButton(self.centralwidget)
        self.double_chiz.name = 'Дабл Чізбургер'
        self.double_chiz.setGeometry(QtCore.QRect(750, 100, 200, 200))
        self.double_chiz.setStyleSheet("background-image: url(img/burgeru/double_chiz.png);border-style: none;")
        self.double_chiz.price = 29.00
        self.double_chiz.clicked.connect(lambda: self.pressed_double_chiz())

        self.big_mak = QtWidgets.QPushButton(self.centralwidget)
        self.big_mak.name = 'Біг Мак'
        self.big_mak.setGeometry(QtCore.QRect(250, 350, 200, 200))
        self.big_mak.setStyleSheet("background-image: url(img/burgeru/big_mak.png);border-style: none;")
        self.big_mak.price = 65.00
        self.big_mak.clicked.connect(lambda: self.pressed_big_mak())

        self.gamburger = QtWidgets.QPushButton(self.centralwidget)
        self.gamburger.name = 'Гамбургер'
        self.gamburger.setGeometry(QtCore.QRect(500, 350, 200, 200))
        self.gamburger.setStyleSheet("background-image: url(img/burgeru/gamburger.png);border-style: none;")
        self.gamburger.price = 25.00
        self.gamburger.clicked.connect(lambda: self.pressed_gamburger())

        self.mak_chicken = QtWidgets.QPushButton(self.centralwidget)
        self.mak_chicken.name = 'МакЧікен'
        self.mak_chicken.setGeometry(QtCore.QRect(750, 350, 200, 200))
        self.mak_chicken.setStyleSheet("background-image: url(img/burgeru/mak_chicken.png);border-style: none;")
        self.mak_chicken.price = 40.00
        self.mak_chicken.clicked.connect(lambda: self.pressed_mak_chicken())

        self.big_texas.show()
        self.big_teysti.show()
        self.double_chiz.show()
        self.big_mak.show()
        self.gamburger.show()
        self.mak_chicken.show()

    # функция показывает меню гарниры-----------------------------------------------------------------------------------
    def show_menu_garniru(self):

        self.set_menu('garniru')
        self.main_label.setText('Гарниры')

        self.chicken_salat = QtWidgets.QPushButton(self.centralwidget)
        self.chicken_salat.name = 'Чікен салат'
        self.chicken_salat.setGeometry(QtCore.QRect(250, 100, 200, 200))
        self.chicken_salat.setStyleSheet("background-image: url(img/garniru/chicken_salat.png);border-style: none;")
        self.chicken_salat.price = 63.00
        self.chicken_salat.clicked.connect(lambda: self.pressed_chicken_salat())

        self.salat = QtWidgets.QPushButton(self.centralwidget)
        self.salat.name = 'Мікс салат'
        self.salat.setGeometry(QtCore.QRect(500, 100, 200, 200))
        self.salat.setStyleSheet("background-image: url(img/garniru/salat.png);border-style: none;")
        self.salat.price = 45.00
        self.salat.clicked.connect(lambda: self.pressed_salat())

        self.dipu = QtWidgets.QPushButton(self.centralwidget)
        self.dipu.name = 'Діпи'
        self.dipu.setGeometry(QtCore.QRect(750, 100, 200, 200))
        self.dipu.setStyleSheet("background-image: url(img/garniru/dipu.png);border-style: none;")
        self.dipu.price = 25.00
        self.dipu.clicked.connect(lambda: self.pressed_dipu())

        self.small_fri = QtWidgets.QPushButton(self.centralwidget)
        self.small_fri.name = 'Картопля Фрі маленька'
        self.small_fri.setGeometry(QtCore.QRect(250, 350, 200, 200))
        self.small_fri.setStyleSheet("background-image: url(img/garniru/small_fri.png);border-style: none;")
        self.small_fri.price = 18.00
        self.small_fri.clicked.connect(lambda: self.pressed_small_fri())

        self.big_fri = QtWidgets.QPushButton(self.centralwidget)
        self.big_fri.name = 'Картопля Фрі велика'
        self.big_fri.setGeometry(QtCore.QRect(500, 350, 200, 200))
        self.big_fri.setStyleSheet("background-image: url(img/garniru/big_fri.png);border-style: none;")
        self.big_fri.price = 30.00
        self.big_fri.clicked.connect(lambda: self.pressed_big_fri())

        self.sous_fri = QtWidgets.QPushButton(self.centralwidget)
        self.sous_fri.name = 'Картопля Фрі з сирним соусом'
        self.sous_fri.setGeometry(QtCore.QRect(750, 350, 200, 200))
        self.sous_fri.setStyleSheet("background-image: url(img/garniru/sous_fri.png);border-style: none;")
        self.sous_fri.price = 50.00
        self.sous_fri.clicked.connect(lambda: self.pressed_sous_fri())

        self.chicken_salat.show()
        self.salat.show()
        self.dipu.show()
        self.small_fri.show()
        self.big_fri.show()
        self.sous_fri.show()

    # функция показывает меню курка-------------------------------------------------------------------------------------
    def show_menu_kyrka(self):

        self.set_menu('kyrka')
        self.main_label.setText('Курица')

        self.double_kentuki = QtWidgets.QPushButton(self.centralwidget)
        self.double_kentuki.name = 'Дабл Кентукі'
        self.double_kentuki.setGeometry(QtCore.QRect(250, 100, 200, 200))
        self.double_kentuki.setStyleSheet("background-image: url(img/chicken/double_kentuki.png);border-style: none;")
        self.double_kentuki.price = 60.00
        self.double_kentuki.clicked.connect(lambda: self.pressed_double_kentuki())

        self.chicken_rol = QtWidgets.QPushButton(self.centralwidget)
        self.chicken_rol.name = 'Чікен Рол'
        self.chicken_rol.setGeometry(QtCore.QRect(500, 100, 200, 200))
        self.chicken_rol.setStyleSheet("background-image: url(img/chicken/chicken_rol.png);border-style: none;")
        self.chicken_rol.price = 55.00
        self.chicken_rol.clicked.connect(lambda: self.pressed_chicken_rol())

        self.mak_chicken = QtWidgets.QPushButton(self.centralwidget)
        self.mak_chicken.name = 'МакЧікен'
        self.mak_chicken.setGeometry(QtCore.QRect(750, 100, 200, 200))
        self.mak_chicken.setStyleSheet("background-image: url(img/burgeru/mak_chicken.png);border-style: none;")
        self.mak_chicken.price = 40.00
        self.mak_chicken.clicked.connect(lambda: self.pressed_mak_chicken())

        self.naggets_6 = QtWidgets.QPushButton(self.centralwidget)
        self.naggets_6.name = 'Чікен Наггетс 6шт'
        self.naggets_6.setGeometry(QtCore.QRect(250, 350, 200, 200))
        self.naggets_6.setStyleSheet("background-image: url(img/chicken/naggets_6.png);border-style: none;")
        self.naggets_6.price = 40.00
        self.naggets_6.clicked.connect(lambda: self.pressed_naggets_6())

        self.naggets_9 = QtWidgets.QPushButton(self.centralwidget)
        self.naggets_9.name = 'Чікен Наггетс 9шт'
        self.naggets_9.setGeometry(QtCore.QRect(500, 350, 200, 200))
        self.naggets_9.setStyleSheet("background-image: url(img/chicken/naggets_9.png);border-style: none;")
        self.naggets_9.price = 65.00
        self.naggets_9.clicked.connect(lambda: self.pressed_naggets_9())

        self.naggets_20 = QtWidgets.QPushButton(self.centralwidget)
        self.naggets_20.name = 'Чікен Наггетс 20шт'
        self.naggets_20.setGeometry(QtCore.QRect(750, 350, 200, 200))
        self.naggets_20.setStyleSheet("background-image: url(img/chicken/naggets_20.png);border-style: none;")
        self.naggets_20.price = 100
        self.naggets_20.clicked.connect(lambda: self.pressed_naggets_20())

        self.double_kentuki.show()
        self.chicken_rol.show()
        self.mak_chicken.show()
        self.naggets_6.show()
        self.naggets_9.show()
        self.naggets_20.show()

    # функция показывает меню напитки-----------------------------------------------------------------------------------
    def show_menu_napoi(self):

        self.set_menu('napoi')
        self.main_label.setText('Напитки')

        self.amerikano = QtWidgets.QPushButton(self.centralwidget)
        self.amerikano.name = 'Американо'
        self.amerikano.setGeometry(QtCore.QRect(250, 100, 200, 200))
        self.amerikano.setStyleSheet("background-image: url(img/napoi/amerikano.png);border-style: none;")
        self.amerikano.price = 20.00
        self.amerikano.clicked.connect(lambda: self.pressed_amerikano())

        self.late = QtWidgets.QPushButton(self.centralwidget)
        self.late.name = 'Лате'
        self.late.setGeometry(QtCore.QRect(500, 100, 200, 200))
        self.late.setStyleSheet("background-image: url(img/napoi/late.png);border-style: none;")
        self.late.price = 24.00
        self.late.clicked.connect(lambda: self.pressed_late())

        self.black_tea = QtWidgets.QPushButton(self.centralwidget)
        self.black_tea.name = 'Чорний чай'
        self.black_tea.setGeometry(QtCore.QRect(750, 100, 200, 200))
        self.black_tea.setStyleSheet("background-image: url(img/napoi/black_tea.png);border-style: none;")
        self.black_tea.price = 17.00
        self.black_tea.clicked.connect(lambda: self.pressed_black_tea())

        self.coca_cola = QtWidgets.QPushButton(self.centralwidget)
        self.coca_cola.name = 'Кока-кола'
        self.coca_cola.setGeometry(QtCore.QRect(250, 350, 200, 200))
        self.coca_cola.setStyleSheet("background-image: url(img/napoi/coca_cola.png);border-style: none;")
        self.coca_cola.price = 22.00
        self.coca_cola.clicked.connect(lambda: self.pressed_coca_cola())

        self.fanta = QtWidgets.QPushButton(self.centralwidget)
        self.fanta.name = 'Фанта'
        self.fanta.setGeometry(QtCore.QRect(500, 350, 200, 200))
        self.fanta.setStyleSheet("background-image: url(img/napoi/fanta.png);border-style: none;")
        self.fanta.price = 18.00
        self.fanta.clicked.connect(lambda: self.pressed_fanta())

        self.sprite = QtWidgets.QPushButton(self.centralwidget)
        self.sprite.name = 'Спрайт'
        self.sprite.setGeometry(QtCore.QRect(750, 350, 200, 200))
        self.sprite.setStyleSheet("background-image: url(img/napoi/sprite.png);border-style: none;")
        self.sprite.price = 18.00
        self.sprite.clicked.connect(lambda: self.pressed_sprite())

        self.amerikano.show()
        self.late.show()
        self.black_tea.show()
        self.coca_cola.show()
        self.fanta.show()
        self.sprite.show()

    # Функции которые показывают конкретное меню------------------------------------------------------------------------
    def close_menu_burgeru(self):
        self.big_texas.close()
        self.big_teysti.close()
        self.double_chiz.close()
        self.big_mak.close()
        self.gamburger.close()
        self.mak_chicken.close()

    def close_menu_garniru(self):
        self.chicken_salat.close()
        self.salat.close()
        self.dipu.close()
        self.small_fri.close()
        self.big_fri.close()
        self.sous_fri.close()

    def close_menu_kyrka(self):
        self.double_kentuki.close()
        self.chicken_rol.close()
        self.mak_chicken.close()
        self.naggets_6.close()
        self.naggets_9.close()
        self.naggets_20.close()

    def close_menu_napoi(self):
        self.amerikano.close()
        self.late.close()
        self.black_tea.close()
        self.coca_cola.close()
        self.fanta.close()
        self.sprite.close()

    # закрывает предидущее меню-----------------------------------------------------------------------------------------
    def set_menu(self, set_current_menu):
        if self.first_menu is not True:
            if self.previous_menu == 'burgeru':
                self.close_menu_burgeru()
                self.previous_menu = set_current_menu
            elif self.previous_menu == 'kyrka':
                self.close_menu_kyrka()
                self.previous_menu = set_current_menu
            elif self.previous_menu == 'garniru':
                self.close_menu_garniru()
                self.previous_menu = set_current_menu
            elif self.previous_menu == 'napoi':
                self.close_menu_napoi()
                self.previous_menu = set_current_menu
        else:
            self.first_menu = False

    # обработка кнопок меню burgeru-------------------------------------------------------------------------------------
    def pressed_big_mak(self):
        self.add_burger(dish_name=self.big_mak.name, price=self.big_mak.price)

    def pressed_big_texas(self):
        self.add_burger(dish_name=self.big_texas.name, price=self.big_texas.price)

    def pressed_big_teysti(self):
        self.add_burger(dish_name=self.big_teysti.name, price=self.big_teysti.price)

    def pressed_double_chiz(self):
        self.add_burger(dish_name=self.double_chiz.name, price=self.double_chiz.price)

    def pressed_gamburger(self):
        self.add_burger(dish_name=self.gamburger.name, price=self.gamburger.price)

    def pressed_mak_chicken(self):
        self.add_burger(dish_name=self.mak_chicken.name, price=self.mak_chicken.price)

    # обпработка кнопок меню chicken------------------------------------------------------------------------------------
    def pressed_chicken_rol(self):
        self.add_chicken(dish_name=self.chicken_rol.name, price=self.chicken_rol.price)

    def pressed_double_kentuki(self):
        self.add_chicken(dish_name=self.double_kentuki.name, price=self.double_kentuki.price)

    def pressed_naggets_6(self):
        self.add_chicken(dish_name=self.naggets_6.name, price=self.naggets_6.price)

    def pressed_naggets_9(self):
        self.add_chicken(dish_name=self.naggets_9.name, price=self.naggets_9.price)

    def pressed_naggets_20(self):
        self.add_chicken(dish_name=self.naggets_20.name, price=self.naggets_20.price)

    # обработка кнопок меню garniru ------------------------------------------------------------------------------------
    def pressed_big_fri(self):
        self.add_garnir(dish_name=self.big_fri.name, price=self.big_fri.price)

    def pressed_chicken_salat(self):
        self.add_garnir(dish_name=self.chicken_salat.name, price=self.chicken_salat.price)

    def pressed_dipu(self):
        self.add_garnir(dish_name=self.dipu.name, price=self.dipu.price)

    def pressed_salat(self):
        self.add_garnir(dish_name=self.salat.name, price=self.salat.price)

    def pressed_small_fri(self):
        self.add_garnir(dish_name=self.small_fri.name, price=self.small_fri.price)

    def pressed_sous_fri(self):
        self.add_garnir(dish_name=self.sous_fri.name, price=self.sous_fri.price)

    # обработка кнопок меню napoi---------------------------------------------------------------------------------------
    def pressed_amerikano(self):
        self.add_napitok(dish_name=self.amerikano.name, price=self.amerikano.price)

    def pressed_black_tea(self):
        self.add_napitok(dish_name=self.black_tea.name, price=self.black_tea.price)

    def pressed_coca_cola(self):
        self.add_napitok(dish_name=self.coca_cola.name, price=self.coca_cola.price)

    def pressed_fanta(self):
        self.add_napitok(dish_name=self.fanta.name, price=self.fanta.price)

    def pressed_late(self):
        self.add_napitok(dish_name=self.late.name, price=self.late.price)

    def pressed_sprite(self):
        self.add_napitok(dish_name=self.sprite.name, price=self.sprite.price)

    # Отмена заказа
    def func_otmena(self):
        self.zakaz.burgeru = [
            {
                "name": "Біг Техас",
                "price": 0,
                "quantity": 0,
                "gaps": 20

            },
            {
                "name": "Біг Тейсті",
                "price": 0,
                "quantity": 0,
                "gaps": 19

            },
            {
                "name": "Дабл Чізбургер",
                "price": 0,
                "quantity": 0,
                "gaps": 15
            },
            {
                "name": "Біг Мак",
                "price": 0,
                "quantity": 0,
                "gaps": 22
            },
            {
                "name": "Гамбургер",
                "price": 0,
                "quantity": 0,
                "gaps": 20
            },
            {
                "name": "МакЧікен",
                "price": 0,
                "quantity": 0,
                "gaps": 21
            }]
        # chicken[0] = double_kentuki, [1]=chicken_rol, [2]=naggets_6, [3]=naggets_9, [4]=naggets_20
        self.zakaz.chicken = [
            {
                "name": "Дабл Кентукі",
                "price": 0,
                "quantity": 0,
                "gaps": 17

            },
            {
                "name": "Чікен Рол",
                "price": 0,
                "quantity": 0,
                "gaps": 20

            },
            {
                "name": "Чікен Наггетс 6шт",
                "price": 0,
                "quantity": 0,
                "gaps": 12
            },
            {
                "name": "Чікен Наггетс 9шт",
                "price": 0,
                "quantity": 0,
                "gaps": 12
            },
            {
                "name": "Чікен Наггетс 20шт",
                "price": 0,
                "quantity": 0,
                "gaps": 11
            }]
        # garniru[0] = chicken_salat, [1]=salat, [2]=dipu, [3]=small_fri [4]=big_fri, [5]=sous_fri
        self.zakaz.garniru = [
            {
                "name": "Чікен салат",
                "price": 0,
                "quantity": 0,
                "gaps": 18

            },
            {
                "name": "Мікс салат",
                "price": 0,
                "quantity": 0,
                "gaps": 19

            },
            {
                "name": "Діпи",
                "price": 0,
                "quantity": 0,
                "gaps": 25
            },
            {
                "name": "Картопля Фрі маленька",
                "price": 0,
                "quantity": 0,
                "gaps": 8
            },
            {
                "name": "Картопля Фрі велика",
                "price": 0,
                "quantity": 0,
                "gaps": 10
            },
            {
                "name": "Картопля Фрі з сирним соусом",
                "price": 0,
                "quantity": 0,
                "gaps": 1
            }]
        # napoi[0] = amerikano, [1]=late, [2]=black_tea, [3]=coca_cola, [4]=fanta, [5]=sprite
        self.zakaz.napoi = [
            {
                "name": "Американо",
                "price": 0,
                "quantity": 0,
                "gaps": 20

            },
            {
                "name": "Лате",
                "price": 0,
                "quantity": 0,
                "gaps": 25

            },
            {
                "name": "Чорний чай",
                "price": 0,
                "quantity": 0,
                "gaps": 19
            },
            {
                "name": "Кока-кола",
                "price": 0,
                "quantity": 0,
                "gaps": 20
            },
            {
                "name": "Фанта",
                "price": 0,
                "quantity": 0,
                "gaps": 24
            },
            {
                "name": "Спрайт",
                "price": 0,
                "quantity": 0,
                "gaps": 23
            }]
        self.show_result()

    # Оплата приложения-------------------------------------------------------------------------------------------------
    def func_oplata(self):
        self.main_label.setText('Готово')

    # zakaz.burgeru[0] = big_mak, [1]=big_texas, [2]=big_teysti, [3]=double_chiz, [4]=gamburger, [5]=mak_chicken
    # garniru[0] = chicken_salat, [1]=salat, [2]=dipu, [3]=small_fri [4]=big_fri, [5]=sous_fri
    # zakaz.chicken[0] = double_kentuki, [1]=chicken_rol, [2]=naggets_6, [3]=naggets_9, [4]=naggets_20
    # zakaz.napoi[0] = amerikano, [1]=late, [2]=black_tea, [3]=coca_cola, [4]=fanta, [5]=sprite
    # Добавление блюда
    def add_burger(self, dish_name, price):
        # проходим по бургерам
        for dish in self.zakaz.burgeru:
            if dish['name'] == dish_name:
                if dish['quantity'] == 0:
                    dish['quantity'] = 1
                    dish['price'] = price
                else:
                    dish['quantity'] += 1
                break
        self.show_result()

    # проходим по гарнирам
    def add_garnir(self, dish_name, price):
        for dish in self.zakaz.garniru:
            if dish['name'] == dish_name:
                if dish['quantity'] == 0:
                    dish['quantity'] = 1
                    dish['price'] = price
                else:
                    dish['quantity'] += 1
                break
        self.show_result()

    # добавляем курицу
    def add_chicken(self, dish_name, price):
        for dish in self.zakaz.chicken:
            if dish['name'] == dish_name:
                if dish['quantity'] == 0:
                    dish['quantity'] = 1
                    dish['price'] = price
                else:
                    dish['quantity'] += 1
                break
        self.show_result()

    # добавляем напиток
    def add_napitok(self, dish_name, price):
        for dish in self.zakaz.napoi:
            if dish['name'] == dish_name:
                if dish['quantity'] == 0:
                    dish['quantity'] = 1
                    dish['price'] = price
                else:
                    dish['quantity'] += 1
                break
        self.show_result()

    # Выводим результат выбора пользователя в
    def show_result(self):
        result = ''
        self.suma.result = 0
        # проходим по бургерам и добавляем на вывод
        for dish in self.zakaz.burgeru:
            if dish['quantity'] != 0:

                result += "{}x {}      {} грн\n".format(dish['quantity'], dish['name'].ljust(15, ' '), dish['price'])
                self.suma.result += dish['price']

        # проходим по гарнирам и добавляем на вывод
        for dish in self.zakaz.garniru:
            if dish['quantity'] != 0:

                result += "{}x {}      {} грн\n".format(dish['quantity'], dish['name'].ljust(15, ' '), dish['price'])
                self.suma.result += dish['price']

        # проходим по курице и добавляем на вывод
        for dish in self.zakaz.chicken:
            if dish['quantity'] != 0:

                result += "{}x {}      {} грн\n".format(dish['quantity'], dish['name'].ljust(15, ' '), dish['price'])
                self.suma.result += dish['price']

        # проходим по напиткам и добавляем на вывод
        for dish in self.zakaz.napoi:
            if dish['quantity'] != 0:

                result += "{}x {}      {} грн\n".format(dish['quantity'], dish['name'].ljust(15, ' '), dish['price'])
                self.suma.result += dish['price']

        write_file(result)
        self.zakaz.setText(result)
        self.suma.setText('Всего:' + str(self.suma.result))


def write_file(data):
    file = open('zakaz.txt', 'w', encoding='utf-8')
    print(data)
    file.write(data)
    file.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    menu = Ui_MainWindow()
    menu.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
