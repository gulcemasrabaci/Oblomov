import sys
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        
        super().__init__()
        self.form_widget = Oblomov()
        self.setCentralWidget(self.form_widget)
        
        self.setGeometry(100, 100, 1500, 1000)
        self.setWindowTitle('Welcome, Oblomov!')
        self.setWindowIcon(QIcon('kitap3.png'))
        
        saveAction = QAction("Save my progress!", self)
        saveAction.setShortcut("Ctrl+S")
        saveAction.setStatusTip("Save!")
        #action.triggered.connect()
        
        mainMenu = self.menuBar()
        saveMenu = mainMenu.addMenu('&Save')
        quitMenu = mainMenu.addMenu('&Quit')
        
        saveMenu.addAction(saveAction)
        
        extractAction = QAction(QIcon("cardigan.jpg"), 'Cardiganize and leave', self)
        extractAction2 = QAction(QIcon("planet.jpg"), 'Planetize', self)
        #extractAction.triggered.connect(self.close_application)
        
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractAction)
        self.toolBar.addAction(extractAction2)
        
        checkBox = QCheckBox("I am reading this book now", self)
        checkBox.move(300, 50)
        checkBox.resize(checkBox.minimumSizeHint())
        #checkBox.toggle() #automatically checked!
        checkBox.stateChanged.connect(self.make_current_book)
        
        self.show()

    def make_current_book(self, state):
        
        if state == Qt.Checked:
            pass
        else:
            pass

class Oblomov(QWidget):
    
    def __init__(self):
        
        super().__init__() #super returns parent obj QWidget
        
        self.initUI()
        
    def initUI(self):
        
        self.resize(800, 500)
        #self.setWindowTitle('Welcome, Oblomov!')
        #self.setWindowIcon(QIcon('cutmypic.png'))
        
        self.createTable()
        
        self.layout = QVBoxLayout()
        
        '''
        self.buttonlayout = QHBoxLayout()
        
        self.addRowButton = QPushButton("Add new book")
        self.addRowButton.setFixedWidth(50)
        self.addRowButton.clicked.connect(self.addRow)
        
        self.speedButton = QPushButton("Calculate average speed")       
        self.saveButton = QPushButton("Save")        
        self.statsButton = QPushButton("Oblomovistic stats")
        
        self.clearButton = QPushButton("Clear all books")
        self.clearButton.clicked.connect(self.clearMessage)
        
        self.buttonlayout.addWidget(self.addRowButton)
        self.buttonlayout.addWidget(self.speedButton)
        self.buttonlayout.addWidget(self.saveButton)
        self.buttonlayout.addWidget(self.statsButton)
        self.buttonlayout.addWidget(self.clearButton)
        
        self.layout.addLayout(self.buttonlayout)
        '''
              
        self.layout.addWidget(self.table)
        self.setLayout(self.layout)
        
        #self.show()
        
    def createTable(self):
        
        self.table = QTableWidget()
        self.table.setRowCount(1)
        self.table.setColumnCount(8)
        self.table.resize(self.table.minimumSizeHint())
        
        self.table.setHorizontalHeaderLabels(("Author; Book; Start; Finish; Pages; Current Page; Pages Left; Speed").split(";"))
       
    def addRow(self):
        
        rowPosition = self.table.rowCount()
        self.table.insertRow(rowPosition)
            
        
    def calculateSpeed(self):
        pass
  
    def saveNewInput(self):
        #list
        pass    
    
    def clearMessage(self):
        
        reply = QMessageBox.question(self, 'Wait!', "You really wanna burn them all?",
                                     QMessageBox.Yes | QMessageBox.No, 
                                     QMessageBox.No)
        '''
        if reply == QMessageBox.Yes:
            #do sth
            #event.accept()
        else:
            #do sth else
            #event.ignore()
        '''   
            
if __name__ == '__main__':
        
    app = QApplication(sys.argv)
    obj = MainWindow()
    sys.exit(app.exec_())  