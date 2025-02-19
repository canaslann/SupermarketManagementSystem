import mysql

from src.UserInterfaces.loginGUI import LoginPage


class loginDb:
    def check_login(self, username, password):
        try:
            connection = LoginPage.get_database_connection()  # Veritabanına bağlan
            cursor = connection.cursor()

            # admins tablosunda kullanıcı adı ve şifreyi sorgula
            query = "SELECT * FROM admins WHERE username = %s AND password = %s"
            cursor.execute(query, (username, password))

            # Eğer eşleşen kayıt varsa True döndür
            result = cursor.fetchone()
            cursor.close()
            connection.close()

            if result:
                return True
            else:
                return False
        except mysql.connector.Error as err:
            print(f"Veritabanı hatası: {err}")
            return False
        except Exception as e:
            print(f"Beklenmedik hata: {e}")
            return False