import sys
import urllib
import urllib2
from workmgr import WorkMgr, Worker
import time
sys.path.append('./')
from main import *
import string, random
'''
def completed():
	print 'ok'
	wm.stop()
	exit()
'''

def get_rand_str_no_repeat(n):
    allw = string.letters+string.digits
    r = random.sample(allw, n)
    return ''.join(r)

class ImageDownloader(Worker):
	def do(self, item):
		times = 0
		while True:
			if times>3:
				break
			try:
				response = urllib2.urlopen(item, timeout=10).read()
				img_list = findall('<img src="','"\s',response)
				break
			except:
				times+=1
				print 'times:' + str(times)
		#path = "./htm/" + item[-11:] + ".txt"
		#open(path,"w").write(conn.getresponse().read())
		#print path
		if 'img_list' in dir():
			for i in img_list:
				times = 0
				while True:
					if times >3:
						print 'break'
						break
					try:
						data = urllib2.urlopen(i, timeout=10).read()
						break
					except IOError:
						times += 1
						print 'Download file IOError, times:' + str(times)
					except:
						times += 1
						print 'Download file other err, times:' + str(times)
				path = "./img/" + str(get_rand_str_no_repeat(2)) + i[-30:]
				try:
					f = file(path,"wb")
					f.write(data)
				except IOError:
					print 'Write file IOError: ', path
				except:
					print 'Write file other err'
				print path + "|" + str(self.index)
			
		
'''
queue = Queue.Queue(0)
queue.put("/post/2013-07-24/40050886740")
queue.put("/post/2013-07-23/40050061681")
queue.put("/post/2013-07-22/40051402935")
queue.put("/post/2013-07-21/40051077752")
queue.put("/post/2013-07-20/40051252967")
queue.put("/post/2013-07-19/40050535335")
wm = WorkMgr(queue, ImageDownloader)
wm.completed(completed)
wm.setThread(10)
wm.start()
'''
