import mariadb
import pandas as pd
def connect():
	try:
		conn = mariadb.connect(
				user = 'root',
				password = '1234567890qwerty',
				host = 'localhost',
				port = 3306,
				database = 'test',
				)
	except maridb.Error as e:
		print(f"Error connecting to MariaDB: {e}")
		conn = -1

	return conn

def create_users(df):#, cur):
	#cnx = cur.cursor()
	#print(cur)
	for idx, row in df.iterrows():
		try:#
			usuario = row.usuario.replace(".", "")
			pswd = row.pswd
			str_1 = f"CREATE USER IF NOT EXISTS {usuario}@'localhost' identified by '{pswd}'"
			str_2 = f"CREATE DATABASE {usuario}"
			str_3 = f"GRANT ALL PRIVILEGES ON {usuario}.* TO {usuario}@'localhost'"
			str_4 = f"FLUSH PRIVILEGES"
			str_5 = f"DROP DATABASE IF EXISTS '{usuario}';"
			str_6 = f"DROP USER IF EXISTS {usuario}@localhost;"
			#cnx.execute(str_1)
			#cnx.execute(str_2)
			#cnx.execute(str_3)
			#cnx.execute(str_5)
			#cnx.execute(str_6)
			#cnx.execute(str_4)
			print(f"{str_1}\n{str_2}\n{str_3}\n{str_4}\n{str_5}\n{str_6}")

		except mariadb.Error as e:
			print(f"Error: {e}")
		#print(f"{row.usuario} --> {row.pswd}")
	#cur.close()
	
df = pd.read_csv("usuarios.csv")
#con = connect()
create_users(df)


