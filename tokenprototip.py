from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


from seleniumwire import webdriver
from selenium.webdriver.support.ui import WebDriverWait

def timerloop(sec):
    i = 0
    print ("timer start")
    while sec > i:
        time.sleep(1)
        print ("sec:", sec)
        sec = sec - 1
    print ("timer stop")


def main():
    driver = webdriver.Firefox()
    driver.get('https://discord.com/login')
    time.sleep(5)
    email_input = driver.find_element(By.NAME, "email")
    email_input.clear()

    email_input.send_keys("coderekaterina@gmail.com")
    time.sleep(5)
    pass_input = driver.find_element(By.NAME, "password")
    pass_input.clear()
    pass_input.send_keys("3e4r5tQ6")

    buttons = driver.find_element(By.CSS_SELECTOR, "button[type=submit]")
    buttons.send_keys(Keys.ENTER)
    print("waithing........")
    timerloop(60)    
    print("START 10 sec")
    timerloop(10)
    print("GRAB")
    driver.get('https://discord.com/channels/@me')
    #driver.refresh()
    for request in driver.requests:
        if request.url == 'https://discord.com/api/v9/science':
            print (request.headers['authorization'])
            
    print ("GRAB -- END --")
    print("waiting...")
    timerloop(30)
    print("OK")
    #driver.refresh()
    #driver.close()


if __name__ == '__main__':
	main()

#geckodriver
#C:\install\firefox_sdriver\geckodriver
 
