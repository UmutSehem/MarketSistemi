import sqlite3
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer


class LoginWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.connect_db()
        self.init_ui()

    def connect_db(self):
        self.database_connect = sqlite3.connect("ürünler.db")
        self.cursor = self.database_connect.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS ürünler (URUNLER TEXT, FIYATLAR TEXT)")
        self.database_connect.commit()
    def init_ui(self):



        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(750, 10, 41, 41))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:7px\n"
"")
        self.pushButton.setText("🔎")

        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(10, 60, 871, 591))
        self.frame.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10px")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)

        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 430, 421, 71))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton_2.setStyleSheet("background-color: rgb(85, 170, 127);\n"
"border-radius:7px\n"
"")
        self.pushButton_2.setText("Ürün Ekle")

        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(440, 430, 421, 71))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton_3.setStyleSheet("\n"
"background-color: rgb(170, 0, 0);\n"
"border-radius:7px\n"
"")
        self.pushButton_3.setText("Ürün Kaldır")

        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 510, 851, 71))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"border-radius:7px\n"
"")
        self.pushButton_4.setText("Barkod Okuyucu Bağla")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(550, 380, 31, 21))
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setPlaceholderText("   ₺")

        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(240, 370, 301, 41))
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 170, 0);")
        
        self.lineEdit_4.setText("")
        self.lineEdit_4.setPlaceholderText(" Ürünün İsmi..")


        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(320, 40, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))

        self.label.setText("TUTAR =")

        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(420, 50, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.OpenHandCursor))

        self.textEdit.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>")
        
        self.textBrowser = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser.setGeometry(QtCore.QRect(20, 101, 631, 261))
        self.textBrowser.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.textBrowser.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>")

        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(290, 6, 151, 41))
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton_6.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"border-radius:7px\n"
"")
        
        
        self.pushButton_6.setText("Hesapla")

        self.textBrowser_2 = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser_2.setGeometry(QtCore.QRect(660, 100, 181, 261))
        self.textBrowser_2.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.textBrowser_2.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>")

        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(30, 10, 731, 41))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius:7px\n"
"\n"
"")
        
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(" Ürün Ara..")



        self.pushButton_5 = QtWidgets.QPushButton(self)
        self.pushButton_5.setGeometry(QtCore.QRect(800, 10, 81, 41))
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton_5.setStyleSheet("\n"
"background-color: rgb(170, 0, 0);\n"
"border-radius:7px\n"
"")
        self.pushButton_5.setText("Çıkış")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("market-icon-png-15.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setWindowTitle("(_SHM_)Market Sistemi")

        self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.resize(891,676)
        self.setMaximumSize(891,676)
        
        self.pushButton_2.clicked.connect(self.urunekle)
        self.pushButton_3.clicked.connect(self.urunkaldir)
        self.pushButton_4.clicked.connect(self.barkodokuyucu)
        self.pushButton_5.clicked.connect(self.cikis)



        self.pushButton_6.clicked.connect(self.hesapla)
        self.pushButton.clicked.connect(self.urunara)


        self.urun_listesi = []

        self.show()


    def urunekle(self):
        urun_adi = self.lineEdit_4.text()
        urun_fiyati = self.lineEdit_3.text()
        
        self.cursor.execute("SELECT * FROM ürünler WHERE URUNLER = ?", (urun_adi,))
        existing_product = self.cursor.fetchone()
        
        if existing_product:
            print("Bu ürün zaten ekli!")
        else:
            self.cursor.execute("INSERT INTO ürünler (URUNLER, FIYATLAR) VALUES (?, ?)", (urun_adi, urun_fiyati))
            self.database_connect.commit()
            print("Ürün başarıyla eklendi:", urun_adi, urun_fiyati)

    def urunkaldir(self):
        urun_adi = self.lineEdit_4.text()
    
        self.cursor.execute("SELECT * FROM ürünler WHERE URUNLER = ?", (urun_adi,))
        existing_product = self.cursor.fetchone()
        
        if existing_product:
            self.cursor.execute("DELETE FROM ürünler WHERE URUNLER = ?", (urun_adi,))
            self.database_connect.commit()
            print("Ürün başarıyla silindi:", urun_adi)
        else:
            print("Bu ürün bulunamadı!")

    def barkodokuyucu(self):
        self.barkod_timer = QTimer(self)
        self.barkod_timer.timeout.connect(self.read_barkod)
        self.barkod_timer_interval = 200 
        self.barkod_timer.start(self.barkod_timer_interval)

    def read_barkod(self):
        # Bu fonksiyon barkod okuma işlemlerini yapar.
        # Üzerinden veriyi yakalayabilir ve işleyebilirsiniz.
        # Burada barkod bilgisini alıp ürün adını arayabilirsiniz.
        # self.urunara(barkod_data)
        pass

    def cikis(self):
        exit()




    
    
    
    
    
    
    def hesapla(self):
        toplam_tutar = sum([float(fiyat) for _, fiyat in self.urun_listesi])
        self.textEdit.setText(f"{toplam_tutar:.2f} ₺")


    def urunara(self):
        urun_adi = self.lineEdit.text()
        
        self.cursor.execute("SELECT * FROM ürünler WHERE URUNLER = ?", (urun_adi,))
        product_info = self.cursor.fetchone()
        
        if product_info:
            urun_fiyati = product_info[1]  # İkinci sütun FIYATLAR
            
            self.urun_listesi.append((urun_adi, urun_fiyati))  # Yeni ürünü listeye ekle
            
            urunler_str = "\n".join([ad for ad, _ in self.urun_listesi])
            fiyatlar_str = "\n".join([f"{fiyat} ₺" for _, fiyat in self.urun_listesi])
            
            self.textBrowser.setText(urunler_str)
            self.textBrowser_2.setText(fiyatlar_str)
        else:
            self.textBrowser.setText("Ürün bulunamadı.")
            self.textBrowser_2.setText("")





if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    login_window = LoginWindow()
    sys.exit(app.exec())