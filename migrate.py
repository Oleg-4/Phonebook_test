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
		

### различные миграции для базы данных ###
def three():
		query = "CREATE TABLE login (id INT PRIMARY KEY AUTO_INCREMENT,login VARCHAR(30),password VARCHAR(30),birthdate DATE)"
		Database.add_data(query)
		print('.')

def four():
		query = "CREATE TABLE inbool(id INT PRIMARY KEY AUTO_INCREMENT,autoin BOOL,USER VARCHAR(30),PASSWORD VARCHAR(30))"
		Database.add_data(query)
		print('...')

def five():
		query = "CREATE TABLE phonebook(id INT PRIMARY KEY AUTO_INCREMENT, NAME VARCHAR(30),NUMBER VARCHAR(30),birthdate DATE)"
		Database.add_data(query)
		print('.....')

def six():
		query = "INSERT INTO inbool (autoin,USER,PASSWORD) VALUES(FALSE,'Oleg','555')"
		Database.add_data(query)
		print('.......')

def zero():
		query = "CREATE DATABASE IF NOT EXISTS test"
		Database.add_data(query)
		print('')

def one():
		query = "ALTER DATABASE test CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;"
		Database.add_data(query)
		print('.........')

def two():
		query = "ALTER TABLE phonebook CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
		Database.add_data(query)
		print('...........')

def two_1():
		query = "ALTER TABLE inbool CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
		Database.add_data(query)
		print('................................')

def inserter():
		query = "INSERT INTO phonebook(name,number,birthdate) VALUES ('Андрей Петров','89765465456','1992-11-12')"
		Database.add_data(query)
		print('...........')

def two_2():
		query = "ALTER TABLE login CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
		Database.add_data(query)
		print('................................')
		print('--Migrations are successful!!!--')


def main():
	zero()
	three()
	four()
	five()
	six()
	one()
	two()
	two_2()
	inserter()
	two_1()

if __name__=='__main__':
	main()
