#coding=utf-8
#coding by fb.com/Rizky.Rasata
#python2
import requests,os,re

baner = """ _____ _           _   ___ ____    _____ ____
|  ___(_)_ __   __| | |_ _|  _ \  |  ___| __ )
| |_  | | '_ \ / _` |  | || | | | | |_  |  _ \

|  _| | | | | | (_| |  | || |_| | |  _| | |_) |
|_|   |_|_| |_|\__,_| |___|____/  |_|   |____/\n"""

def id():
	try:
		u = raw_input('\nMasukkan username > ')
		url = 'https://www.facebook.com/'+u
		r = requests.get(url).text
		name = re.search('Title">(.*?)</', r).group(1).strip('| Facebook')
		id = re.search('profile/(.*?)" ', r).group(1)
		
		print '\nNama > '+name
		print 'Id   > '+id+'\n'
		exit()
		 
	except requests.exceptions.ConnectionError:
		print '× Koneksi bermasalah'
		exit()
	except AttributeError:
		print '× Username tidak di temukan'
		exit()
		
def user():
	try:
		u = raw_input('\nMasukkan id > ')
		url = 'https://www.facebook.com/'+u
		r = requests.get(url).text
		name = re.search('Title">(.*?)</', r).group(1).strip('| Facebook')
		user = re.search('https://www.facebook.com/(.*?)" />', r).group(1)
		
		print '\nNama     > '+name
		print 'Username > '+user+'\n'
		exit()
		 
	except requests.exceptions.ConnectionError:
		print '× Koneksi bermasalah'
		exit()
	except AttributeError:
		print '× Id tidak di temukan'
		exit()
		
os.system('clear')
print baner
print '1. Cari id menggunakan username'
print '2. Cari username menggunakan id\n'

while True:
	p = raw_input('>> ')
	if p=="":
		print '× Masukkan yg benar'
	elif p=="1":
		id()
	elif p=="2":
		user()
	else:
		print '× Masukkan yg benar'
