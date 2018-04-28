# -*- coding: utf-8 -*-
#!/usr/bin/env python
import os
import time
import datetime
import pickle
import RPi.GPIO as GPIO
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
temp_sensor = '/sys/bus/w1/devices/28-0215819851ff/w1_slave'
row_no = 0
row_li = 0
temp_zad = 80
t = 0
li=[]

#ODCZYT CZASU
def loc_time():
	localtime = time.strftime("%d.%m.%Y %H:%M:%S")
	czas = time.strftime("%H.%M.%S")
	return localtime, czas

znacznik = loc_time()[1]
sciezkaDoPliku = '/home/pi/python_scripts/log_temperatury_'+znacznik+'.log'
#OBSLUGA PLIKU
def usunPlik():
		if os.path.isfile(sciezkaDoPliku) :
			os.unlink(sciezkaDoPliku)
		else :
			print "Plik z logiem jescze nie istnieje :p"
try:
	temp_zad = input("\nProgram bedzie zapalał diodę w przypadku przekroczenia temperatury maksymalnej \n\nPodaj temperaturę maksymalną: ")

except (ValueError, TypeError, NameError):
	print("To nie była liczba!")

try:
	t = input("Podaj odstęp pomiędzy pomiarami: ")

except (ValueError, TypeError, NameError):
	print "To nie była liczba!"

print "\n"
#ODCZYT PLIKU CZUJNIKA
def temp_raw():
	f = open(temp_sensor, 'r')
	lines = f.readlines()
	f.close()
	return lines

#OBSLUGA CZUJNIKA
def read_temp():
	lines = temp_raw()
	while lines[0].strip()[-3:] != 'YES':
		print "Odczyt temperatury zakonczony niepowiodzeniem :( "+loc_time()
		time.sleep(1)
		lines = temp_raw()
	temp_output = lines[1].find('t=')
	if temp_output != -1:
		temp_string = lines[1].strip()[temp_output+2:]
		temp_c = float(temp_string) / 1000.0
		temp_f = temp_c * 9.0 / 5.0 + 32.0
		czas3 = loc_time()
	return temp_c, temp_f, czas3


#OBSLUGA DIODY
def led(pin, t, temp_zad):
	if read_temp()[0] > temp_zad:
		GPIO.setup(pin, GPIO.OUT)
		GPIO.output(pin, GPIO.HIGH)
		time.sleep(t)
		GPIO.output(pin, GPIO.LOW)
	else:
		time.sleep(t)


#WYDRUK POMIARU

usunPlik() # dodane usuniecie pliku loga przed nowym cyklem pomiaru
while True:
	row_no = row_no+1 #inkrementacja liczby pomiarów
	data3 = str(str(row_no)+". "+str(loc_time()[0])+" %.2f "% read_temp()[0])
	print data3+"°C"
	li.append(data3+'\n')
	if len(li)>=10: # zapis do pliku
		for i in li:
			fws = open(sciezkaDoPliku,'a')
			fws.write(i)
		fws.close()
		li = []
	led(17, t, temp_zad) #ZAPALANIE DIODY lub sleep


GPIO.cleanup()
