from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon
import comtypes.client
from pdf2docx import Converter
import os
import sys
import time
from PIL import Image


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1200, 783)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C://Users/abdul/Desktop/python-projectes/FormatMate/fileConverterIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: #F5F5F5;\n"
"\n"
"")
        MainWindow.setIconSize(QtCore.QSize(30, 30))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelTitle = QtWidgets.QLabel(self.centralwidget)
        self.labelTitle.setGeometry(QtCore.QRect(470, 20, 261, 61))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(22)
        self.labelTitle.setFont(font)
        self.labelTitle.setStyleSheet("color: #000;\n"
"")
        self.labelTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitle.setWordWrap(False)
        self.labelTitle.setObjectName("labelTitle")
        self.inputFileLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.inputFileLineEdit.setGeometry(QtCore.QRect(210, 310, 501, 61))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(1)
        self.inputFileLineEdit.setFont(font)
        self.inputFileLineEdit.setStyleSheet("QLineEdit {\n"
"color: #000;\n"
"font-size: 16px;\n"
"font-weight: bold;\n"
"padding: 5px;\n"
"border-radius: 6px;\n"
"border: 2px solid #ced4da;\n"
"}")
        self.inputFileLineEdit.setText("")
        self.inputFileLineEdit.setReadOnly(True)
        self.inputFileLineEdit.setObjectName("inputFileLineEdit")
        self.browseButton = QtWidgets.QPushButton(self.centralwidget)
        self.browseButton.setGeometry(QtCore.QRect(770, 310, 221, 61))
        self.browseButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.browseButton.setMouseTracking(False)
        self.browseButton.setStyleSheet("QPushButton {\n"
"background-color: #3b5bdb;\n"
"border-radius: 6px;\n"
"border-width: 0;\n"
"color: #fff;\n"
"font-family: -apple-system,system-ui,\"Segoe UI\",Roboto,\"Helvetica Neue\",Ubuntu,sans-serif;\n"
"font-size: 20px;\n"
"font-weight: bold;\n"
"text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #fff;\n"
"color: black;\n"
"border: 2px solid  #3b5bdb;\n"
"}\n"
"\n"
"\n"
"")
        self.browseButton.setObjectName("browseButton")
        self.convertButton = QtWidgets.QPushButton(self.centralwidget)
        self.convertButton.setGeometry(QtCore.QRect(770, 490, 221, 61))
        font = QtGui.QFont()
        font.setFamily("-apple-system")
        font.setPointSize(1)
        font.setBold(False)
        font.setWeight(50)
        self.convertButton.setFont(font)
        self.convertButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.convertButton.setStyleSheet("QPushButton {\n"
"background-color: #0ca678;\n"
"border-radius: 6px;\n"
"border-width: 0;\n"
"color: #fff;\n"
"font-family: -apple-system,system-ui,\"Segoe UI\",Roboto,\"Helvetica Neue\",Ubuntu,sans-serif;\n"
"font-size: 20px;\n"
"font-weight: bold;\n"
"text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #fff;\n"
"color: black;\n"
"border: 2px solid #0ca678;\n"
"}\n"
"\n"
"")
        self.convertButton.setObjectName("convertButton")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(210, 490, 501, 61))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.comboBox.setStyleSheet("border: 2px solid  #ced4da;\n"
"border-radius: 6px;\n"
"color:  #000;\n"
"")
        self.comboBox.setIconSize(QtCore.QSize(10, 10))
        self.comboBox.setDuplicatesEnabled(False)
        self.comboBox.setFrame(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(["Select...", "Word to PDF", "PDF to Word", "JPEG to PNG", "PNG to JPEG"])
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(490, 90, 211, 191))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(".\\logo2.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.outputFileLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.outputFileLineEdit.setGeometry(QtCore.QRect(210, 400, 501, 61))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(1)
        self.outputFileLineEdit.setFont(font)
        self.outputFileLineEdit.setStyleSheet("QLineEdit{\n"
"color:  #000;\n"
"font-size: 16px;\n"
"font-weight: bold;\n"
"padding: 5px;\n"
"border-radius: 6px;\n"
"border: 2px solid  #ced4da;\n"
"}")
        self.outputFileLineEdit.setReadOnly(True)
        self.outputFileLineEdit.setObjectName("outputFileLineEdit")
        self.destinationButton = QtWidgets.QPushButton(self.centralwidget)
        self.destinationButton.setGeometry(QtCore.QRect(770, 400, 221, 61))
        self.destinationButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.destinationButton.setStyleSheet("QPushButton {\n"
"background-color: #FFA500;\n"
"border-radius: 6px;\n"
"border-width: 0;\n"
"color: #fff;\n"
"font-family: -apple-system,system-ui,\"Segoe UI\",Roboto,\"Helvetica Neue\",Ubuntu,sans-serif;\n"
"font-size: 20px;\n"
"font-weight: bold;\n"
"text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #fff;\n"
"color: black;\n"
"border: 2px solid #FFA500;\n"
"}\n"
"\n"
"\n"
"")
        self.destinationButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 600, 781, 91))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(1)
        self.label_2.setFont(font)
        self.label_2.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.label_2.setStyleSheet("QLabel {\n"
"color: #fdd835;\n"
"font-size: 20px;\n"
"padding: 5px;\n"
"border-radius: 6px;\n"
"border: 0;\n"
"}")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FormatMate"))
        self.labelTitle.setText(_translate("MainWindow", "FormatMate"))
        self.inputFileLineEdit.setPlaceholderText(_translate("MainWindow", "Input path..."))
        self.browseButton.setText(_translate("MainWindow", "Browse"))
        self.convertButton.setText(_translate("MainWindow", "Convert"))
        self.outputFileLineEdit.setPlaceholderText(_translate("MainWindow", " Output path..."))
        self.destinationButton.setText(_translate("MainWindow", "Output Path"))
        self.label_2.setText(_translate("MainWindow", ""))


        # connect browse button to browse function
        self.browseButton.clicked.connect(self.browse)

        # connect destination button to destination function
        self.destinationButton.clicked.connect(self.destination)

        # connect convert button to convert function
        self.convertButton.clicked.connect(self.convert)


    def browse(self):
        self.label_2.setText("")
        self.filename = QtWidgets.QFileDialog.getOpenFileName()
        self.path = self.filename[0]
        self.inputFileLineEdit.setText(self.path)
    

    def destination(self):
        # get output directory from the user
        self.select_output_path = QtWidgets.QFileDialog.getExistingDirectory()
        self.outputFileLineEdit.setText(self.select_output_path)


    # Word to pdf
    def WORD_TO_PDF(self):

        time.sleep(0.5)

        self.inputFileLineEdit.clear()
        self.outputFileLineEdit.clear()
               
        wdFormatPDF = 17

        input_word_file_path = os.path.normpath(self.path)
        input_word_file = self.path.split(r"/")[-1]


        if " " in input_word_file:
            # Replace the whitespace characters with hyphens
            output_pdf_file_path = self.select_output_path + "/" + input_word_file.replace(" ", "-")
        else:
            # Use the original file name
            output_pdf_file_path = self.select_output_path + "/" + input_word_file

        output_pdf_file_path = output_pdf_file_path.replace(".docx", ".pdf")

        word = comtypes.client.CreateObject('Word.Application')
        doc = word.Documents.Open(input_word_file_path)
        doc.SaveAs(output_pdf_file_path, FileFormat=wdFormatPDF)
        doc.Close()
        word.Quit()

        self.comboBox.setCurrentIndex(0)

    # Pdf to word
    def PDF_TO_WORD(self):

        time.sleep(0.5)

        self.inputFileLineEdit.clear()
        self.outputFileLineEdit.clear()

        input_pdf_file_path = os.path.normpath(self.path)
        input_pdf_file = self.path.split(r"/")[-1]

        if " " in input_pdf_file:
            # Replace the whitespace characters with hyphens
            output_word_file_path = self.select_output_path + "/" + input_pdf_file.replace(" ", "-")
        else:
            # Use the original file name
            output_word_file_path = self.select_output_path + "/" + input_pdf_file

        output_word_file_path = output_word_file_path.replace(".pdf", ".docx")

        cv = Converter(input_pdf_file_path)
        cv.convert(output_word_file_path, start=0, end=None)
        cv.close()

        self.comboBox.setCurrentIndex(0)

    # jpeg to png
    def JPEG_TO_PNG(self):
        time.sleep(0.5)

        self.inputFileLineEdit.clear()
        self.outputFileLineEdit.clear()

        input_jpeg_file_path = os.path.normpath(self.path)
        input_jpeg_file = self.path.split(r"/")[-1]

        if " " in input_jpeg_file:
            # Replace the whitespace characters with hyphens
            output_png_file_path = self.select_output_path + "/" + input_jpeg_file.replace(" ", "-")
        else:
            # Use the original file name
            output_png_file_path = self.select_output_path + "/" + input_jpeg_file

        output_png_file_path = output_png_file_path.replace(".jpeg", ".png")

        # Open the JPEG image
        img = Image.open(input_jpeg_file_path)
        # Convert the image to PNG
        img.save(output_png_file_path, 'PNG')



    # png to jpeg
    def PNG_TO_JPEG(self):
        time.sleep(0.5)

        self.inputFileLineEdit.clear()
        self.outputFileLineEdit.clear()

        input_png_file_path = os.path.normpath(self.path)
        input_png_file = self.path.split(r"/")[-1]

        if " " in input_png_file:
            # Replace the whitespace characters with hyphens
            output_jpeg_file_path = self.select_output_path + "/" + input_png_file.replace(" ", "-")
        else:
            # Use the original file name
            output_jpeg_file_path = self.select_output_path + "/" + input_png_file

        output_jpeg_file_path = output_jpeg_file_path.replace(".png", ".jpeg")

        # Open the PNG image
        img = Image.open(input_png_file_path).convert('RGB')
        # Convert the image to JPEG
        img.save(output_jpeg_file_path, 'JPEG')

    
    def show_conversion_completed_message(self, icon):
        msg = QMessageBox()
        msg.setWindowIcon(icon)
        msg.setWindowTitle("Conversion completed")
        msg.setText("The conversion was completed successfully.")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()    



    def convert(self):

        option = self.comboBox.currentText()

        success_icon = QIcon("success-icon.png")
        failure_icon = QIcon("failure-icon.png")

        try:

            if self.path.endswith(".docx") and option == "Word to PDF":
                self.WORD_TO_PDF()
                self.show_conversion_completed_message(success_icon)

            elif self.path.endswith(".pdf") and option == "PDF to Word":
                self.PDF_TO_WORD()
                self.show_conversion_completed_message(success_icon)

            elif self.path.endswith(".jpeg") and option == "JPEG to PNG":
                self.JPEG_TO_PNG()
                self.show_conversion_completed_message(success_icon)

            elif self.path.endswith(".png") and option == "PNG to JPEG":
                self.PNG_TO_JPEG()
                self.show_conversion_completed_message(success_icon)

            else:
                self.label_2.setText("Please select the right option for the file you want to convert!")

        except Exception as e:
            # Show the error message
            msg = QMessageBox()
            msg.setWindowIcon(failure_icon)
            msg.setWindowTitle("Error")
            msg.setText(str(e))
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
