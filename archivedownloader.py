#!/usr/bin/python
#encoding=utf-8
import sys
from PyQt4 import QtWebKit, QtGui, QtCore
	
class ArchiveDownloader(QtWebKit.QWebView):
	def __init__(self, url=""):
		self.url = url
		QtWebKit.QWebView.__init__(self)
		st = self.settings()
		st.setAttribute(st.AutoLoadImages,False)
		codec = QtCore.QTextCodec.codecForHtml("utf-8")
		QtCore.QTextCodec.setCodecForCStrings(codec)
		QtCore.QTextCodec.setCodecForLocale(codec)
		QtCore.QTextCodec.setCodecForTr(codec)
		#QtCore.QObject.connect(self,QtCore.SIGNAL("contentsChanged()"),self.webkitChanged)
		#QtCore.QObject.connect(self.page().networkAccessManager(),QtCore.SIGNAL("finished (QNetworkReply *)"),self.webkitNetworkFinished)
	def setUrl(self, url):
		self.url = url
	def start(self):
		print 'start'
		self.load(QtCore.QUrl(self.url))
		self.show()
	def getHtml(self):
		return str(self.page().currentFrame().documentElement().toInnerXml().toAscii())
	#def save(self, path):
		#open(path,"w").write(self.page().currentFrame().documentElement().toInnerXml())
	def webkitNetworkFinished(self):
		print "finished"
		





'''
app = QtGui.QApplication(sys.argv)
webView = QtWebKit.QWebView()
st = webView.settings()
st.setAttribute(st.AutoLoadImages,False)
QtCore.QObject.connect(webView,QtCore.SIGNAL("contentsChanged()"),finished)
QtCore.QObject.connect(webView.page().networkAccessManager(),QtCore.SIGNAL("finished (QNetworkReply *)"),test)
webView.load(QtCore.QUrl("http://www.i3u4.com/archive"))
webView.show()

def printit():
	Timer(5.0, printit).start()
	open("./htm2.txt","w").write(webView.page().currentFrame().documentElement().toInnerXml())
printit()
sys.exit(app.exec_())
'''

