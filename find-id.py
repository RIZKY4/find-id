# Coding by fb.com/Rizky.Rasata
# Python2
import requests,os,re

baner = """ _____ _           _   ___ ____    _____ ____
|  ___(_)_ __   __| | |_ _|  _ \  |  ___| __ )
| |_  | | '_ \ / _` |  | || | | | | |_  |  _ \

|  _| | | | | | (_| |  | || |_| | |  _| | |_) |
|_|   |_|_| |_|\__,_| |___|____/  |_|   |____/\n"""

try:
 os.system('clear')
 print baner
 u = raw_input('Masukkan username > ')
 url = 'https://www.facebook.com/'+u
 r = requests.get(url).text
 name = re.search('Title">(.*?)</', r).group(1).strip('| Facebook')
 id = re.search('profile/(.*?)" ', r).group(1)

 print '\nNAMA > '+name
 print 'ID   > '+id+'\n'
 
except requests.exceptions.ConnectionError:
 	print 'Koneksi tidak ada'
except AttributeError:
	print 'Username tidak di temukan'
