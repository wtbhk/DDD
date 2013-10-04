#!/usr/bin/python
#encoding=utf-8
import sys
sys.path.append('./')
import Queue, socket
from main import Main
from PyQt4 import QtWebKit, QtGui, QtCore
from workmgr import WorkMgr
from imagedownloader import ImageDownloader
from archivedownloader import ArchiveDownloader
import threading



'''
class Watcher():
	def __init__(self, wm):
		self.wm = wm
	def time(self):
		threading.Timer(20.0, self.time).start()
		print 'Queue:qsize():' + str(self.wm.queue.qsize())
'''

socket.setdefaulttimeout(5)
app = QtGui.QApplication(sys.argv)
archdown = ArchiveDownloader()
queue = Queue.Queue(maxsize=0)
imgdown = WorkMgr(queue, ImageDownloader)
#watcher = Watcher(imgdown)
main = Main(archdown, imgdown, queue, watcher='NULL')
#archdown.start()
sys.exit(app.exec_())
