import sqlite3
import datetime
from config import DATABASES
from datetime import datetime, date, time


conn = sqlite3.connect(DATABASES['default']['NAME'])
cursor = conn.cursor()


def crypto_create(chat_id, title):
	cursor.execute("""INSERT INTO Account(chat_id, title) SELECT ?, ? 
		WHERE NOT EXISTS (SELECT 1 FROM Account WHERE title = ? AND chat_id = ?)""", (chat_id, title, title, chat_id))
	conn.commit()


def get_cryptos(chat_id):
	data = {}
	for i in cursor.execute("SELECT id, title FROM Account WHERE chat_id = ?", (chat_id,)):
		data[i[1]] = i[0] # Формат: title == id
	return data


def crypto_del(title):
	cursor.execute('DELETE FROM Account WHERE title = ?', (title,))
	conn.commit()


def get_transaction(account_id):
	data = {}
	for i in cursor.execute('SELECT id, amount, comment, datetime FROM Transactions WHERE account_id = ?', (account_id,)):
		data[i[0]] = {"amount": str(i[1]), 
		"comment": i[2], "datetime": datetime.strptime(i[3], "%Y-%m-%d %H:%M:%S")}
	return data

def transaction_create(account_id, amount, comment=''):
	cursor.execute("INSERT INTO Transactions(account_id, amount, comment) VALUES (?, ?, ?)", (account_id, str(amount), comment))
	conn.commit()

def transaction_del(account_id):
	cursor.execute('DELETE FROM Transactions WHERE account_id = ?', (account_id,))
	conn.commit()

def del_last_transaction(account_id):
	amount, comment = None, None
	for i in cursor.execute('SELECT amount, comment FROM Transactions WHERE account_id = ? ORDER BY -id LIMIT 1', (account_id,)):
		amount, comment = str(i[0]), i[1]
	cursor.execute('DELETE FROM Transactions WHERE id=(SELECT id from Transactions WHERE  account_id = ? ORDER BY -id LIMIT 1)', (account_id,))
	conn.commit()
	return amount, comment


def get_user(user_id):
	tpl = cursor.execute("SELECT user_id, username, datetime, balance FROM User").fetchone()
	return {'user_id': tpl[0], "username": tpl[1], "datetime": tpl[2], 'balance': tpl[3]}

def get_categories():
	data = {}
	for i in cursor.execute("SELECT id, title FROM Category"):
		data[i[1]] = i[0] # Формат: title == id
	return data

def get_goods():
	data = {}
	for i in cursor.execute("SELECT title, id, price, category_id FROM Goods"):
		data[i[0]] = {"id": i[1], "price": i[2], "category_id": i[3]} # i[0] == title
	return data
