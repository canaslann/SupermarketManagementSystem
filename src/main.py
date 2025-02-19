import sys
from abc import ABC, abstractmethod
import pymysql
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
from src.loginDb import loginDb
from src.UserInterfaces.loginGUI import Ui_Main, LoginPage
from src.UserInterfaces.productGUI import Ui_Product
from src.UserInterfaces.employeeGUI import Ui_Employee


# MainWindow (Login Page) class
class MainWindow(QMainWindow, Ui_Main):  # login page
    def __init__(self):
        super().__init__()
        self.loginDb = loginDb()
        self.setupUi(self)  # Arayüzü başlat
        self.initUI()  # Ek ayarlar ve işlevler eklemek için

    def initUI(self):
        # Butona tıklama olayını burada bağlıyoruz
        self.pushButton.clicked.connect(self.on_button_click)

    def on_button_click(self):
        username = self.lineEdit.text()  # Kullanıcı adı al
        password = self.lineEdit_2.text()  # Şifreyi al

        # Kullanıcı adı ve şifreyi kontrol et
        if self.loginDb.check_login(username, password):
            print("Giriş başarılı!")
            self.product_window = ProductWindow()  # Ürün penceresini oluştur
            self.product_window.show()  # Ürün penceresini göster
            self.close()  # Login penceresini kapat
            QMessageBox.warning(self, "Successfull", "Kullacini girisi basarili")
        else:
            # Giriş hatalıysa uyarı ver
            QMessageBox.warning(self, "Hata", "Kullanıcı adı veya şifre yanlış!")

class DbOperations(ABC):
    @abstractmethod
    def addDatabase(self):
        pass

    @abstractmethod
    def deleteDatabase(self):
        pass

    @abstractmethod
    def updateDatabase(self):
        pass

    @abstractmethod
    def loadData(self):
        pass

class ProductWindow(QMainWindow, Ui_Product):  # Ürün sayfası
    def __init__(self):
        super().__init__()
        self.db = DbOperations
        self.setupUi(self)  # Arayüzü başlat
        self.loadData()
        self.label_16.mousePressEvent = self.go_to_employee_gui
        self.label_15.mousePressEvent = self.go_to_employee_gui
        self.label_6.mousePressEvent = self.openLoginGUI
        self.label_5.mousePressEvent = self.openLoginGUI
        self.tableWidget.itemSelectionChanged.connect(self.load_selected_row)
        self.pushButton.clicked.connect(self.addDatabase)
        self.pushButton_3.clicked.connect(self.deleteDatabase)
        self.pushButton_2.clicked.connect(self.updateDatabase)

    def go_to_employee_gui(self, event):
        if event.button() == Qt.LeftButton:  # Sol tıklama kontrolü
            self.close()  # Mevcut pencereyi kapat
            self.employee_gui = EmployeeWindow()  # EmployeeGUI başlat
            self.employee_gui.show()  # EmployeeGUI'yi göster

    def openLoginGUI(self, event):
        if event.button() == Qt.LeftButton:  # Sol tıklama kontrolü
            self.close()  # Mevcut pencereyi kapat
            self.employee_gui = MainWindow()  # EmployeeGUI başlat
            self.employee_gui.show()  # EmployeeGUI'yi göster

    def loadData(self):
        try:
            connection = LoginPage.get_database_connection()

            cursor = connection.cursor()
            # `employees` tablosundaki verileri al
            query = "SELECT * FROM products"
            cursor.execute(query)
            rows = cursor.fetchall()

            # Sütun isimlerini al
            column_names = [desc[0] for desc in cursor.description]

            # TableWidget için sütun ve satır boyutlarını ayarla
            self.tableWidget.setRowCount(len(rows))
            self.tableWidget.setColumnCount(len(column_names))
            self.tableWidget.setHorizontalHeaderLabels(column_names)

            # Verileri TableWidget'e ekle
            for row_idx, row in enumerate(rows):
                for col_idx, cell in enumerate(row):
                    self.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(str(cell)))

            # Bağlantıyı kapat
            cursor.close()
            connection.close()

        except pymysql.MySQLError as e:
            print(f"Database connection failed: {e}")

    def addDatabase(self):
        id = self.lineEdit_5.text()
        productName = self.lineEdit_6.text()
        stock = self.lineEdit_7.text()
        productPrice = self.lineEdit_8.text()

        if not id or not productName or not stock or not productPrice:
            print("All fields must be filled.")
            return

        try:
            connection = LoginPage.get_database_connection()
            cursor = connection.cursor()

            # Yeni çalışan ekleme sorgusu
            query = "INSERT INTO products (id, productName, stock, productPrice) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (id, productName, stock, productPrice))
            connection.commit()

            print("Product added successfully.")

            # Veritabanından güncel verileri yeniden yükle
            self.loadData()

            # Formu temizle
            self.lineEdit_5.clear()
            self.lineEdit_6.clear()
            self.lineEdit_7.clear()
            self.lineEdit_8.clear()


            cursor.close()
            connection.close()

        except pymysql.MySQLError as e:
            print(f"Failed to add product: {e}")

    def deleteDatabase(self):
        """Seçili ürünü sil."""
        selected_row = self.tableWidget.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Error", "Please select a row to delete.")
            return

        # ID'yi almak için ilk sütunu (genellikle ID sütunu) seçiyoruz
        selectedItem = self.tableWidget.item(selected_row, 0).text()

        try:
            connection = LoginPage.get_database_connection()
            cursor = connection.cursor()

            # Silme sorgusu
            query = "DELETE FROM products WHERE id = %s"
            cursor.execute(query, (selectedItem))
            connection.commit()

            print("Product deleted successfully.")

            # Tabloyu güncelle
            self.loadData()

            cursor.close()
            connection.close()

        except pymysql.MySQLError as e:
            print(f"Failed to delete product: {e}")

    def updateDatabase(self):
        id = self.lineEdit_5.text()
        productName = self.lineEdit_6.text()
        stock = self.lineEdit_7.text()
        productPrice = self.lineEdit_8.text()

        if not id:
            QMessageBox.warning(self, "Error", "Please select a row to update.")
            return

        try:
            connection = LoginPage.get_database_connection()
            cursor = connection.cursor()

            # Güncelleme sorgusu
            query = """
                UPDATE products
                SET productName = %s, stock = %s, productPrice = %s
                WHERE id = %s
            """
            cursor.execute(query, (productName, stock, productPrice, id))
            connection.commit()

            print("Product updated successfully.")

            # Tabloyu güncelle
            self.loadData()
            cursor.close()
            connection.close()

        except pymysql.MySQLError as e:
            print(f"Failed to update product: {e}")

    def load_selected_row(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row == -1:
            return

        self.lineEdit_5.setText(self.tableWidget.item(selected_row, 0).text())
        self.lineEdit_6.setText(self.tableWidget.item(selected_row, 1).text())
        self.lineEdit_7.setText(self.tableWidget.item(selected_row, 2).text())
        self.lineEdit_8.setText(self.tableWidget.item(selected_row, 3).text())

class EmployeeWindow(QMainWindow, Ui_Employee):  # Ürün sayfası
    def __init__(self):
        super().__init__()
        self.db = DbOperations
        self.setupUi(self)  # Arayüzü başlat
        self.label_7.mousePressEvent = self.openProductGUI
        self.label_14.mousePressEvent = self.openProductGUI
        self.label_6.mousePressEvent = self.openLoginGUI
        self.label_5.mousePressEvent = self.openLoginGUI
        self.tableWidget.itemSelectionChanged.connect(self.load_selected_row)
        self.loadData()
        self.pushButton.clicked.connect(self.addDatabase)
        self.pushButton_3.clicked.connect(self.deleteDatabase)
        self.pushButton_2.clicked.connect(self.updateDatabase)

    def openProductGUI(self, event):
        if event.button() == Qt.LeftButton:
            self.close()
            self.productgui = ProductWindow()  # EmployeeGUI başlat
            self.productgui.show()

    def openLoginGUI(self, event):
        if event.button() == Qt.LeftButton:
            self.close()
            self.productgui = MainWindow()  # EmployeeGUI başlat
            self.productgui.show()

    def addDatabase(self):
        id = self.lineEdit_5.text()
        employeeName = self.lineEdit_6.text()
        employeeAge = self.lineEdit_7.text()
        phoneNum = self.lineEdit_9.text()
        section = self.lineEdit_10.text()

        if not id or not employeeName or not employeeAge or not phoneNum or not section:
            print("All fields must be filled.")
            return

        try:
            connection = LoginPage.get_database_connection()
            cursor = connection.cursor()

            # Yeni çalışan ekleme sorgusu
            query = "INSERT INTO employees (id, employeeName, employeeAge, phoneNum, section) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (id, employeeName, employeeAge, phoneNum, section))
            connection.commit()

            print("Employee added successfully.")

            # Veritabanından güncel verileri yeniden yükle
            self.loadData()

            # Formu temizle
            self.lineEdit_5.clear()
            self.lineEdit_6.clear()
            self.lineEdit_7.clear()
            self.lineEdit_9.clear()
            self.lineEdit_10.clear()

            cursor.close()
            connection.close()

        except pymysql.MySQLError as e:
            print(f"Failed to add employee: {e}")

    def deleteDatabase(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Error", "Please select a row to delete.")
            return

        # ID'yi almak için ilk sütunu (genellikle ID sütunu) seçiyoruz
        selectedItem = self.tableWidget.item(selected_row, 0).text()

        try:
            connection = LoginPage.get_database_connection()
            cursor = connection.cursor()

            # Silme sorgusu
            query = "DELETE FROM employees WHERE id = %s"
            cursor.execute(query, (selectedItem,))
            connection.commit()

            print("Employee deleted successfully.")

            # Tabloyu güncelle
            self.loadData()

            cursor.close()
            connection.close()

        except pymysql.MySQLError as e:
            print(f"Failed to delete employee: {e}")

    def updateDatabase(self):
        id = self.lineEdit_5.text()
        employeeName = self.lineEdit_6.text()
        employeeAge = self.lineEdit_7.text()
        phoneNum = self.lineEdit_9.text()
        section = self.lineEdit_10.text()

        if not id:
            QMessageBox.warning(self, "Error", "Please select a row to update.")
            return

        try:
            connection = LoginPage.get_database_connection()
            cursor = connection.cursor()

            # Güncelleme sorgusu
            query = """
                UPDATE employees
                SET employeeName = %s, employeeAge = %s, phoneNum = %s, section = %s
                WHERE id = %s
            """
            cursor.execute(query, (employeeName, employeeAge, phoneNum, section, id))
            connection.commit()

            print("Employee updated successfully.")

            # Tabloyu güncelle
            self.loadData()

            cursor.close()
            connection.close()

        except pymysql.MySQLError as e:
            print(f"Failed to update employee: {e}")

    def load_selected_row(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row == -1:
            return

        self.lineEdit_5.setText(self.tableWidget.item(selected_row, 0).text())
        self.lineEdit_6.setText(self.tableWidget.item(selected_row, 1).text())
        self.lineEdit_7.setText(self.tableWidget.item(selected_row, 2).text())
        self.lineEdit_9.setText(self.tableWidget.item(selected_row, 3).text())
        self.lineEdit_10.setText(self.tableWidget.item(selected_row, 4).text())

    def loadData(self):
        try:
            connection = LoginPage.get_database_connection()
            cursor = connection.cursor()

            query = "SELECT * FROM employees"
            cursor.execute(query)
            rows = cursor.fetchall()

            # Sütun isimlerini al
            column_names = [desc[0] for desc in cursor.description]

            # TableWidget için sütun ve satır boyutlarını ayarla
            self.tableWidget.setRowCount(len(rows))
            self.tableWidget.setColumnCount(len(column_names))
            self.tableWidget.setHorizontalHeaderLabels(column_names)

            # Verileri TableWidget'e ekle
            for row_idx, row in enumerate(rows):
                for col_idx, cell in enumerate(row):
                    self.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(str(cell)))

            # Bağlantıyı kapat
            cursor.close()
            connection.close()

        except pymysql.MySQLError as e:
            print(f"Database connection failed: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()  # Login sayfası başlatılıyor
    window.show()
    sys.exit(app.exec_())

