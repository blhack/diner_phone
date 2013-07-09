#!/usr/bin/python

import sys
sys.path.append("/var/www/blhack.me/python/")

import phones
import cgi

form = cgi.FieldStorage()

phone_number = form.getvalue("number",0)
password = form.getvalue("password","")

try:
	phone_number = int(phone_number)

except:
	phone_number = 0

if (len(str(phone_number)) == 10) and password == "change_this_to_something":
	phones.send_sms(str(phone_number),"Your food is ready.")

print "content-type:text/html"
print
