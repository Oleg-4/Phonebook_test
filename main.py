import sys
import datetime
from main_window import *
from database_script import Models
from PyQt5 import QtCore, QtGui, QtWidgets

### Инициализация всех окон сразу ###

app = QtWidgets.QApplication(sys.argv)

MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

MainWindow_2 = QtWidgets.QMainWindow()
ui2 = Ui_MainWindow_main()
ui2.setupUi(MainWindow_2)

MainWindow_3 = QtWidgets.QMainWindow()
ui3 = Ui_MainWindow_password()
ui3.setupUi(MainWindow_3)

MainWindow_4 = QtWidgets.QMainWindow()
ui4 = Ui_MainWindow_signup()
ui4.setupUi(MainWindow_4)

MainWindow_5 = QtWidgets.QMainWindow()
ui5 = Ui_MainWindow_restructure()
ui5.setupUi(MainWindow_5)

MainWindow_6 = QtWidgets.QMainWindow()
ui6 = Ui_MainWindow_change()
ui6.setupUi(MainWindow_6)

MainWindow_7 = QtWidgets.QMainWindow()
ui7 = Ui_MainWindow_append()
ui7.setupUi(MainWindow_7)

######################################

### Сигналы всех кнопок ###

def main():
	
	MainWindow.show()
	ui.commandLinkButton.clicked.connect(mail_window)
	ui.pushButton_2.clicked.connect(login)
	ui.pushButton_3.clicked.connect(signup)
	ui.pushButton_4.clicked.connect(sys.exit)
	ui2.pushButton_14.clicked.connect(close_with_exit)
	ui2.pushButton_15.clicked.connect(restructure)
	ui3.pushButton_2.clicked.connect(close)
	ui5.pushButton_3.clicked.connect(appender)
	ui5.pushButton_4.clicked.connect(main_show)
	ui5.pushButton.clicked.connect(edit_show)
	ui5.pushButton_2.clicked.connect(deleter)
	ui6.pushButton.clicked.connect(edit_del)
	ui6.pushButton_2.clicked.connect(restructure)
	ui7.pushButton_2.clicked.connect(restructure)
	ui7.pushButton.clicked.connect(add_subs)
	ui4.pushButton_2.clicked.connect(close)
	ui4.pushButton.clicked.connect(newuser)
	ui.lineEdit_2.setEchoMode(2)
	ui.checkBox_2.stateChanged.connect(pass_modify)
	
	
### Параметр для автовхода ###

	if Models.autoin() == '1':
		autointec() 

### Кнопки переключения справочника ###

	ui2.pushButton.clicked.connect(ab)
	ui2.pushButton_2.clicked.connect(vg)
	ui2.pushButton_3.clicked.connect(de)
	ui2.pushButton_4.clicked.connect(jzii)
	ui2.pushButton_5.clicked.connect(kl)
	ui2.pushButton_6.clicked.connect(mn)
	ui2.pushButton_7.clicked.connect(op)
	ui2.pushButton_8.clicked.connect(rs)
	ui2.pushButton_9.clicked.connect(tu)
	ui2.pushButton_10.clicked.connect(fh)
	ui2.pushButton_11.clicked.connect(ccsh)
	ui2.pushButton_12.clicked.connect(pert)
	ui2.pushButton_13.clicked.connect(ua)
	
	sys.exit(app.exec_())

### Открытие различных окон ###
def restructure():

	finder()
	MainWindow_3.close()
	MainWindow_4.close()
	MainWindow_7.close()
	MainWindow_6.close()
	MainWindow.close()
	MainWindow_5.show()
	
def mail_window():
	
	MainWindow.close()
	MainWindow_3.show()

def signup():
	
	MainWindow.close()
	MainWindow_4.show()

def close():

	MainWindow_2.close()
	MainWindow_3.close()
	MainWindow_4.close()
	MainWindow.show()

def appender():
	
	MainWindow_5.close()
	MainWindow_7.show()

def main_show():
	
	MainWindow.close()
	MainWindow_3.close()
	MainWindow_4.close()
	MainWindow_5.close()
	MainWindow_6.close()
	MainWindow_7.close()
	MainWindow_2.show()

### Функция представления изменения данных записи ###
def edit_show():
	
	MainWindow_6.show()
	current_person = ui5.comboBox.currentText()
	get_account = Models.get_account(current_person)
	get_low = get_account[0]
	get_1 = str(get_low[0])
	get_2 = str(get_low[1])
	get_3 = get_low[2]

	ui6.lineEdit.setText(get_1)
	ui6.lineEdit_2.setText(get_2)
	ui6.dateEdit.setDate(get_3)
	global static_value
	static_value = ui6.lineEdit.text()

### Функция изменения данных записи ###
def edit_del():

	per_1 = ui6.lineEdit.text()
	per_2 = ui6.lineEdit_2.text()
	per_3 = ui6.dateEdit.dateTime().toString('yyyy-MM-dd')
	Models.delete_account(static_value)
	Models.subscriber_append(per_1,per_2,per_3)
	restructure()
	ui2.listWidget_4.clear()
	hb_pres()

### Функция удаления данных записи ###
def deleter():
	
	now_person = ui5.comboBox.currentText()
	Models.delete_account(now_person)
	restructure()

### Функция автовхода под последним юзером, который вошел с флагом "автовход" и не вышел ###
def autointec():
	
	last_user = list(Models.return_log_pass())
	last_user_form = last_user[0]
	log = last_user_form[1]
	passw = last_user_form[2]
	true_value = Models.login_check(log,passw)
	
	if true_value == True:
		
		MainWindow.close()
		MainWindow_2.show()
		ui2.label.setText('зашли как  ' + log)
		ui2.listWidget_4.clear()
		hb_pres()
	
	else: pass

### Добавление нового пользователя ###
def newuser():
	
	log = ui4.lineEdit.text()
	passw = ui4.lineEdit_2.text()
	pass_chk = ui4.lineEdit_3.text()
	if pass_chk == passw:
		birth = ui4.dateEdit.dateTime().toString('yyyy-MM-dd')
		Models.newuser(log,passw,birth)
		close()
		ui.label.setText('Пользователь успешно создан!')
	else: ui4.label.setText('Повтор пароля неверен!')

### Авторизация ###
def login():

	log = str(ui.lineEdit.text())
	passw = str(ui.lineEdit_2.text())
	check = ui.checkBox.checkState()
	if check == 2:
		Models.autoin_add(True, log, passw)
	else: Models.autoin_add(False, log, passw)
	
	true_value = Models.login_check(log,passw)
	
	if true_value == True:
		
		MainWindow.close()
		MainWindow_2.show()
		ui2.label.setText('зашли как:  ' + log)
		ui2.listWidget_4.clear()
		hb_pres()
	
	else: ui.label.setText('Пользователь не найден!!!')

### Функция закрытия без запоминания автовхода ###
def close_with_exit():
	
	Models.autoin_add(False,'NULL','NULL')
	MainWindow_2.close()
	MainWindow_3.close()
	MainWindow_4.close()
	MainWindow.show()

### Вставка всех абонентов в список выбора ###
def finder():

	ui5.comboBox.clear()
	sub_list = list(Models.subscribers_get())
	sub_list.sort()
	for i in sub_list:
		ui5.comboBox.addItem(i[0])
	
### Очистка виджетов ###
def cleaner():
	
	ui2.listWidget.clear()
	ui2.listWidget_2.clear()
	ui2.listWidget_3.clear()
	

### Добавление нового абонента ###
def add_subs():
	
	name = ui7.lineEdit.text()
	number = ui7.lineEdit_2.text()
	birthdate = ui7.dateEdit.dateTime().toString('yyyy-MM-dd')
	if unique() == True:
		Models.subscriber_append(str(name),str(number),birthdate)
		ui7.lineEdit.clear()
		ui7.lineEdit_2.clear()
		ui7.dateEdit.clear()
		restructure()
		ui2.listWidget_4.clear()
		hb_pres()
	else: ui7.label_4.setText('Запись не уникальна!')

### Вывод именинников ###
def hb_pres():
	
	pres_list = Models.hb_list()
	for i in pres_list:
		count = 0
		while count < 8:
			now = str(datetime.datetime.now() + datetime.timedelta(days=count))
			now_cut = now[5:10]
			date_birth = str(i[1])
			db = date_birth[-5:]
			if db == now_cut:
				ui2.listWidget_4.addItem(str(i[0]))
			count += 1

### Уникальность записи в базу ###
def unique():
	
	per_1 = ui7.lineEdit.text()
	per_2 = ui7.lineEdit_2.text()
	per_3 = ui7.dateEdit.dateTime().toString('yyyy-MM-dd')
	unique_list = Models.subscribers_get()
	for i in unique_list:
		if str(i[0]) == str(per_1):
			if str(i[1]) == str(per_2):
				if str(i[2]) == str(per_3):
					return False
	return True

### Проявление пароля ###
def pass_modify():
	
	if ui.checkBox_2.checkState() == 2:
		ui.lineEdit_2.setEchoMode(0)
	else: ui.lineEdit_2.setEchoMode(2)


################################################################################################
###  Дальше идет позор. Он тут появился оттого, что я не нашел как вместе с сигналом кнопки  ###
###              передавать в функцию её параметры. Заранее извиняюсь                        ###
################################################################################################	


def ab():
	cleaner()
	ret_list = []
	sub_list = Models.subscribers_get()
	for i in sub_list:
		header = i[0]
		if header[0].upper() == 'А':
			ret_list.append(i)
	for i in sub_list:
		header = i[0]
		if header[0].upper() == 'Б':
			ret_list.append(i)
	for i in ret_list:
		ui2.listWidget.addItem(i[0])
		ui2.listWidget_2.addItem(i[1])
		ui2.listWidget_3.addItem(str(i[2]))



def vg():
	cleaner()
	ret_list = []
	sub_list = Models.subscribers_get()
	for i in sub_list:
		header = i[0]
		if header[0].upper() == 'В':
			ret_list.append(i)
	for i in sub_list:
		header = i[0]
		if header[0].upper() == 'Г':
			ret_list.append(i)
	for i in ret_list:
		ui2.listWidget.addItem(i[0])
		ui2.listWidget_2.addItem(i[1])
		ui2.listWidget_3.addItem(str(i[2]))

def de():
	cleaner()
	ret_list = []
	sub_list = Models.subscribers_get()
	for i in sub_list:
		header = i[0]
		if header[0].upper() == 'Д':
			ret_list.append(i)
	for i in sub_list:
		header = i[0]
		if header[0].upper() == 'Е':
			ret_list.append(i)
	for i in ret_list:
		ui2.listWidget.addItem(i[0])
		ui2.listWidget_2.addItem(i[1])
		ui2.listWidget_3.addItem(str(i[2]))

def jzii():
	cleaner()
	ret_list = []
	sub_list = Models.subscribers_get()
	for i in sub_list:
		header = i[0]
		if header[0].upper() == 'Ж':
			ret_list.append(i)
	for i in sub_list:
		header = i[0]
		if header[0].upper() == 'З':
			ret_list.append(i)
	for i in sub_list:
		header = i[0]
		if header[0].upper() == 'И':
			ret_list.append(i)
	for i in sub_list:
		header = i[0]
		if header[0].upper() == 'Й':
			ret_list.append(i)
	for i in ret_list:
		ui2.listWidget.addItem(i[0])
		ui2.listWidget_2.addItem(i[1])
		ui2.listWidget_3.addItem(str(i[2]))

def kl():
	cleaner()
	ret_list = []
	sub_list = Models.subscribers_get()
	for i in sub_list:
		header = i[0]
		if header[0].upper() == 'К':
			ret_list.append(i)
	for i in sub_list:
		header = i[0]
		if header[0].upper() == 'Л':
			ret_list.append(i)
	for i in ret_list:
		ui2.listWidget.addItem(i[0])
		ui2.listWidget_2.addItem(i[1])
		ui2.listWidget_3.addItem(str(i[2]))

def mn():
	cleaner()
	ret_list = []
	sub_list = Models.subscribers_get()
	for i in sub_list:
		header = i[0]
		if header[0].upper() == 'М':
			ret_list.append(i)
	for i in sub_list:
		header = i[0]
		if header[0].upper() == 'Н':
			ret_list.append(i)
	for i in ret_list:
		ui2.listWidget.addItem(i[0])
		ui2.listWidget_2.addItem(i[1])
		ui2.listWidget_3.addItem(str(i[2]))

def op():
	cleaner()
	ret_list = []
	sub_list = Models.subscribers_get()
	for i in sub_list:
		header = i[0]
		if header[0].upper() == 'О':
			ret_list.append(i)
	for i in sub_list:
		header = i[0]
		if header[0].upper() == 'П':
			ret_list.append(i)
	for i in ret_list:
		ui2.listWidget.addItem(i[0])
		ui2.listWidget_2.addItem(i[1])
		ui2.listWidget_3.addItem(str(i[2]))

def rs():
	cleaner()
	ret_list = []
	sub_list = Models.subscribers_get()
	for i in sub_list:
		header = i[0]
		if header[0].upper() == 'Р':
			ret_list.append(i)
	for i in sub_list:
		header = i[0]
		if header[0].upper() == 'С':
			ret_list.append(i)
	for i in ret_list:
		ui2.listWidget.addItem(i[0])
		ui2.listWidget_2.addItem(i[1])
		ui2.listWidget_3.addItem(str(i[2]))

def tu():
	cleaner()
	ret_list = []
	sub_list = Models.subscribers_get()
	for i in sub_list:
		header = i[0]
		if header[0].upper() == 'Т':
			ret_list.append(i)
	for i in sub_list:
		header = i[0]
		if header[0].upper() == 'У':
			ret_list.append(i)
	for i in ret_list:
		ui2.listWidget.addItem(i[0])
		ui2.listWidget_2.addItem(i[1])
		ui2.listWidget_3.addItem(str(i[2]))

def fh():
	cleaner()
	ret_list = []
	sub_list = Models.subscribers_get()
	for i in sub_list:
		header = i[0]
		if header[0].upper() == 'Ф':
			ret_list.append(i)
	for i in sub_list:
		header = i[0]
		if header[0].upper() == 'Х':
			ret_list.append(i)
	for i in ret_list:
		ui2.listWidget.addItem(i[0])
		ui2.listWidget_2.addItem(i[1])
		ui2.listWidget_3.addItem(str(i[2]))

def ccsh():
	cleaner()
	ret_list = []
	sub_list = Models.subscribers_get()
	for i in sub_list:
		header = i[0]
		if header[0].upper() == 'Ц':
			ret_list.append(i)
	for i in sub_list:
		header = i[0]
		if header[0].upper() == 'Ч':
			ret_list.append(i)
	for i in sub_list:
		header = i[0]
		if header[0].upper() == 'Ш':
			ret_list.append(i)
	for i in sub_list:
		header = i[0]
		if header[0].upper() == 'Щ':
			ret_list.append(i)
	for i in ret_list:
		ui2.listWidget.addItem(i[0])
		ui2.listWidget_2.addItem(i[1])
		ui2.listWidget_3.addItem(str(i[2]))

def pert():
	cleaner()
	ret_list = []
	sub_list = Models.subscribers_get()
	for i in sub_list:
		header = i[0]
		if header[0].upper() == 'Ы':
			ret_list.append(i)
	for i in sub_list:
		header = i[0]
		if header[0].upper() == 'Э':
			ret_list.append(i)
	for i in ret_list:
		ui2.listWidget.addItem(i[0])
		ui2.listWidget_2.addItem(i[1])
		ui2.listWidget_3.addItem(str(i[2]))

def ua():
	cleaner()
	ret_list = []
	sub_list = Models.subscribers_get()
	for i in sub_list:
		header = i[0]
		if header[0] == 'Ю':
			ret_list.append(i)
	for i in sub_list:
		header = i[0]
		if header[0] == 'Я':
			ret_list.append(i)
	for i in ret_list:
		ui2.listWidget.addItem(i[0])
		ui2.listWidget_2.addItem(i[1])
		ui2.listWidget_3.addItem(str(i[2]))



if __name__=="__main__":
    main()
  
