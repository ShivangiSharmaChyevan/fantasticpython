from selenium import webdriver
from selenium.webdriver.support import ui
import urllib2
import cookielib
from getpass import getpass
import sys
import os
from stat import *

#path='/media/shivangi/OS/Python27/geckodriver.exe'
driver=webdriver.Firefox()
driver.get("http://www.wow4u.com/page12.html")

message=driver.find_element_by_css_selector(".ez_wrap_table > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2) > div:nth-child(10) > span:nth-child(1)").text
number="8007679554"

if __name__=="__main__":
    username="9938147181"
    password="G3586B"
    #message = "+".join(message.split(' '))
    url ='http://site24.way2sms.com/Login1.action?'
    data = 'username='+username+'&password='+password+'&Submit=Sign+in'
    cj= cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    opener.addheaders=[('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120')]
    try:
        usock =opener.open(url, data)
    except IOError:
        print "error"
    jession_id =str(cj).split('~')[1].split(' ')[0]
    send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
    send_sms_data = 'ssaction=ss&Token='+jession_id+'&mobile='+number+'&message='+message+'&msgLen=136'
    opener.addheaders=[('Referer', 'http://site25.way2sms.com/sendSMS?Token='+jession_id)]
    try:
        sms_sent_page = opener.open(send_sms_url,send_sms_data)
    except IOError:
        print "error"
    print "success" 
            
	    
