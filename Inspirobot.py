from selenium import webdriver
from time import sleep
import smtplib

user = 'username'
passwd = 'password'
                       
chrome_path = r"C:\PhantomJS\bin\phantomjs.exe"
driver = webdriver.PhantomJS(chrome_path)
driver.get("http://inspirobot.me")

a = driver.find_element_by_class_name('btn-text')
a.click()
sleep(10)

img = driver.find_element_by_class_name('generated-image')
src = img.get_attribute('src')
driver.quit()

server = smtplib.SMTP('74.125.142.108', timeout = 120)
server.starttls()
server.login(user,passwd)

server.sendmail('hlocke23@gmail.com', 'trigger@applet.ifttt.com ', str(src)[7::])
print(str(src))
server.quit()