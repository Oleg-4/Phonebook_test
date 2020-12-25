import mariadb
import sys


### Класс Database инициирует соединение и взаимодействие с базой данных ###
class Database:

### Этот метод добавляет данные в базу ###
	def add_data(query):
		
		try:
		    conn = mariadb.connect(
 
   ### ПАРАМЕТРЫ ДЛЯ ПОДКЛЮЧЕНИЯ К БАЗЕ ДАННЫХ ###
	        
		        user="root",
		        password="777777",
		        host="127.0.0.1",
		        port=3306,
		        database="test"

   ### ПАРАМЕТРЫ ДЛЯ ПОДКЛЮЧЕНИЯ К БАЗЕ ДАННЫХ ###
		    )
		except mariadb.Error as e:
		    print(f"Error connecting to MariaDB Platform: {e}")
		    sys.exit(1)


		cur = conn.cursor()

		cur.execute(query)
		conn.commit()
		
### Этот метод извлекает данные из базы ###		
	def get_data(query):

		try:
		    conn = mariadb.connect(

   ### ПАРАМЕТРЫ ДЛЯ ПОДКЛЮЧЕНИЯ К БАЗЕ ДАННЫХ ###

		        user="root",
		        password="777777",
		        host="127.0.0.1",
		        port=3306,
		        database="test"

   ### ПАРАМЕТРЫ ДЛЯ ПОДКЛЮЧЕНИЯ К БАЗЕ ДАННЫХ ###

		    )
		except mariadb.Error as e:
		    print(f"Error connecting to MariaDB Platform: {e}")
		    sys.exit(1)


		cur = conn.cursor()
		cur.execute(query)
		return cur

### Класс Models описывает взаимодействие общей логики из main с базой данных ###
class Models:

### Проверка наличия пользователя в базе ###
	def login_check(login_,password_):

		ret_value = False
		query = """SELECT login,password FROM login"""
		query_result = Database.get_data(query)
		temp_list = list(query_result)
		for i in temp_list:
			if login_ == i[0]:
				if password_ == i[1]:
					ret_value = True

		return ret_value 

### Запись нового пользователя в базу ###
	def newuser(*args):
		query = "INSERT INTO login(login,password,birthdate) VALUES (" + str(args)[1:-1] + ")"
		Database.add_data(query)

### Несколько методов для работы автовхода	
	def autoin():
		query = "SELECT autoin FROM inbool ORDER BY id DESC LIMIT 1 "
		ret = list(Database.get_data(query))
		return str(ret[0])[1:-2]

	def return_log_pass():
		query = "SELECT autoin,user,password FROM inbool WHERE autoin = 1 ORDER BY id DESC LIMIT 1 "
		ret_list = list(Database.get_data(query))
		return ret_list

	def autoin_add(*args):
		query = "INSERT INTO inbool(autoin,user,password) VALUES" + str(args)
		Database.add_data(query)

### Метод добавления нового абонента в книгу ###
	def subscriber_append(*args):
		query = "INSERT INTO phonebook (name,number,birthdate) VALUES" + str(args)
		Database.add_data(query)
	
### Извлечение данных абонентов ###
	def subscribers_get():
		query = "SELECT name,number,birthdate FROM phonebook"
		ret = list(Database.get_data(query))
		return ret

###	Извлечения данных абонента по имени ###
	def get_account(person):
		query = "SELECT name,number,birthdate FROM phonebook WHERE name = " + "'" + str(person) + "'"
		ret = list(Database.get_data(query))
		return ret

### Удаление абонента ###
	def delete_account(person):
		query = "DELETE FROM phonebook WHERE name = " + "'" + str(person) + "'"
		Database.add_data(query)

### Список именинников ###
	def hb_list():
		query = "SELECT name,birthdate FROM phonebook" 
		ret = list(Database.get_data(query))
		return ret
