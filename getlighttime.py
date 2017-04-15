
#f = open("1.txt",'r+')
#f1 = open("temp.txt",'wr+')
#uniq = set(open('1.txt').readlines())
from collections import Counter
import sys
import urllib

def download(src, dest):
	urllib.urlretrieve (src, dest)
temp = ' '
time = 0
length = 100
lights = []
with open('RFIDRead.txt') as openfileobject:
    for line in openfileobject:
		if line == temp:
			continue
		temp = line	
		left_text = line.partition(" ")[0]
		right_text = line.partition(" ")[2]
		if int(right_text) == 0:
			fl = open("light.txt",'w+')
			fl.write(str(0))
			fl.write("\n")
			fl.write(str(30))
			fl.close()
			sys.exit()
		#print left_text , right_text,'\n'
		download(,'2.txt')
		with open('2.txt') as file2:
			for line in file2:
				ltext = line.partition(" ")[0]
				rtext = line.partition(" ")[2]
				#print ltext, rtext
				if left_text==ltext:
					time = int(rtext) - int(right_text)
					print left_text,ltext
					print time
					break
		'''if time==0:
			with open('3.txt') as file2:
				for line in file2:
					ltext = line.partition(" ")[0]
					rtext = line.partition(" ")[2]
				#print ltext, rtext
					if left_text==ltext:
						time = int(rtext) - int(right_text)
						print left_text,ltext
						print time
						break
		if time==0:
			with open('4.txt') as file2:
				for line in file2:
					ltext = line.partition(" ")[0]
					rtext = line.partition(" ")[2]
					#print ltext, rtext
					if left_text==ltext:
						time = int(rtext) - int(right_text)
						print left_text,ltext
						print time
						break
		'''
		if time==0:
			lighttime = 20

		else:
			sp = length/time
			if sp<20:
				lighttime = 20
			elif sp<40:
				lighttime = 10
			else:
				lighttime = 5
		lights.append(lighttime)
print lights
data = Counter(lights)
most = data.most_common(1)
green = [int(i[0]) for i in most]
print green[0]
red = 30 - green[0]
fl = open("light.txt",'w+')
fl.write(str(red))
fl.write("\n")
fl.write(str(green[0]))
fl.close()
		#line  = f.readline()
#time = int(left_text)
#f.close()