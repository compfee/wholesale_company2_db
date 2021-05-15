from cryptography.fernet import Fernet
import filler
import connect_sql
import user_info

db = connect_sql.Sql()
login = "newuser"
password = "hellonewuser"
role_id = "1"
cipher = Fernet(user_info.cipher_key)
encrypted_password = password.encode('utf8')
encrypted_password = cipher.encrypt(encrypted_password)

db.cursor.execute("insert into users_wholesale (password, login,role_id) "
                       "values ('" + encrypted_password.decode('utf8') + "', '" + login + "','" + role_id + "')")
db.cnxn.commit()