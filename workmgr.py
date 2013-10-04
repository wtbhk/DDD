#!/usr/bin/python
#encoding=utf-8
import threading, Queue
import time
from PyQt4 import QtCore
import pdb
class WorkMgr(QtCore.QObject):
	def __init__(self, queue, worker=0):
		super(WorkMgr, self).__init__()
		if worker != 0:
			self.worker = worker
		self.threadQuantity = 5
		self.queue = queue
		self.threads = [n for n in range(self.threadQuantity)]
	def setWorker(self, worker):
		self.worker = worker
	def setThread(self, quantity):
		if self.isrunning == True: return False
		self.threadQuantity = quantity
		self.threads = [n for n in range(self.threadQuantity)]
		return True
	def start(self):
		for i in range(self.threadQuantity):
			self.threads[i] = self.worker(i, self.queue, self.done)
			self.threads[i].start()
	def stop(self):
		for i in range(self.threadQuantity):
			self.threads[i].stop()
	def restart(self):
		self.stop()
		while(True):
			if self.isrunning() == False:
				break
		self.start()
	def completed(self):
		self.emit(QtCore.SIGNAL('completed()'))
	def stoped(self):
		self.emit(QtCore.SIGNAL("stoped()"))
	def done(self, index, item):
		if self.isrunning() == False:
			if self.queue.empty():
				self.completed()
			self.stoped()
	def isrunning(self):
		for i in range(self.threadQuantity):
			if self.threads[i].done == 0:
				return True
		return False
class Worker(threading.Thread): #工作类
	def __init__(self, index, queue, done_func): #构造函数
		self.sign = 1				#停止标志
		self.done = 1				#完成标志
		threading.Thread.__init__(self)
		self.index = index
		self.queue = queue
		self.done_func = done_func
		self.setDaemon(True)  #随主进程一起结束
	def run(self):
		while True: 
			pdb.set_trace()
			#print "worker",self.index," start"
			if self.sign == 0:
				break
			else:
				if self.queue.qsize() > 0:
					self.done = 0
					self.item = self.queue.get(timeout=5)
					self.do(self.item)
					#self.queue.task_done()
					#print "worker",self.index," done"
					self.complete()

	def do(self, item):
		time.sleep(random.random())
		#print "index:",self.index, "task", item, "finished"
	def stop(self):
		self.sign = 0
	def complete(self):
		self.done = 1
		self.done_func(self.index, self.item)
		
'''	
queue = Queue.Queue(0)
for i in range(100):
	queue.put(i)
workmgr = WorkMgr(queue,Worker)
workmgr.setThread(10)
workmgr.start()
'''
