import sys
import re
from PyQt4 import QtGui, QtCore

def findall(a, b, string):	#find out all strings from string started with a ended with b 
	x = a + ".*?" + b 
	list1 = re.findall(x, string)
	list2 = []
	for i in list1:
		j = re.sub(a,"",i)
		list2.append(re.sub(b,"",j))
	return list2
#def listToQueue(list, queue):

class Main(QtGui.QWidget):
	def __init__(self, archdown, imgdown, queue ,watcher):
		super(Main, self).__init__()
		self.watcher = watcher
		self.archdown = archdown
		self.queue = queue
		imgdown.setThread(10)
		self.imgdown = imgdown
		QtCore.QObject.connect(self.imgdown,QtCore.SIGNAL("completed()"),self.showMessagebox)
		QtCore.QObject.connect(self.imgdown,QtCore.SIGNAL("stoped()"),self.showMessagebox_stoped)
		self.init()
	def showMessagebox(self):
		QtGui.QMessageBox.about(self, "Yoooooooooooo", "Done!")
	def showMessagebox_stoped(self):	#!!!!
		QtGui.QMessageBox.about(self, "Yoooooooooooo", "Stoped!")
	def button1Clicked(self):	#Start down archive
		self.archdown.setUrl(self.lineEdit1.text())
		self.archdown.start()
	def button2Clicked(self):	#Add to queue
		self.archive_html = self.archdown.getHtml()
		self.archdown.stop()
		self.archdown.close()
		self.posts_url_list = findall('<a class="post-meta" target="\_blank" href="','">',self.archive_html)
		for i in self.posts_url_list:
			self.queue.put(i)
	def button3Clicked(self):	#Start down img
		self.imgdown.start()
		if self.watcher != "NULL":
			self.watcher.time()
	def button4Clicked(self):
		self.imgdown.stop()
	def init(self):
		self.resize(600,400)
		
		self.button1 = QtGui.QPushButton('Start Download Archive', self)
		QtCore.QObject.connect(self.button1,QtCore.SIGNAL("clicked()"),self.button1Clicked)
		self.button1.resize(self.button1.sizeHint())
		
		self.button2 = QtGui.QPushButton('Archive Loaded AND Add To Queue', self)
		QtCore.QObject.connect(self.button2,QtCore.SIGNAL("clicked()"),self.button2Clicked)
		self.button2.resize(self.button2.sizeHint())
		
		self.button3 = QtGui.QPushButton('Start Download', self)
		QtCore.QObject.connect(self.button3,QtCore.SIGNAL("clicked()"),self.button3Clicked)
		self.button3.resize(self.button3.sizeHint())

		self.button4 = QtGui.QPushButton('Stop Download', self)
		QtCore.QObject.connect(self.button4, QtCore.SIGNAL("clicked()"), self.button4Clicked)
		self.button4.resize(self.button4.sizeHint())

		self.lineEdit1 = QtGui.QLineEdit()
		
		self.list1 = QtGui.QListView()
		
		self.label1 = QtGui.QLabel('Archive URL')
		self.label2 = QtGui.QLabel('Queue')
		
		grid = QtGui.QGridLayout()
		grid.setSpacing(10)
		
		grid.addWidget(self.label1, 0, 0, 1, 1)
		grid.addWidget(self.lineEdit1, 0, 1, 1, 3)
		grid.addWidget(self.button1, 1, 2, 1, 1)
		grid.addWidget(self.button2, 1, 3, 1, 1)
		grid.addWidget(QtGui.QSplitter(), 2, 0, 1, 4)
		grid.addWidget(self.label2, 3, 0, 1, 1)
		grid.addWidget(self.list1, 3, 1, 10, 3)
		grid.addWidget(self.button3, 14, 2, 1, 1)
		grid.addWidget(self.button4, 14, 3, 1, 1)	
		self.setLayout(grid)
		
		self.show()
