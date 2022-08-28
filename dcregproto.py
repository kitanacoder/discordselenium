import sys
import os
import random
import requests
import time


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#default: Example: nameProg EMAIL NIKNAME
#Input password option -> Example: nameProg EMAIL NIKNAME -p PASSWORD

#for 2Captcha Solver
from selenium.webdriver.firefox.firefox_profile import AddonFormatError
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
Addon = FirefoxProfile("/home/kitana/selenium/sprofil")
###########################################################


SITEKEYS = '4c672d35-0701-42b2-88c3-78380b0db560&theme=dark'
APIKEYS = '6d2047f498b2f9d6dd6d823a876411dd'
REGURLS = 'https://discord.com/register'

CAPINS = 'https://2captcha.com/in.php'
CAPRESS = 'https://2captcha.com/res.php'

def timerloop(sec):
    i = 0
    print ("timer start")
    while sec > i:
        time.sleep(1)
        print ("sec:", sec)
        sec = sec - 1
    print ("timer stop")


def passgen(length):
        chars = list('abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')
        random.shuffle(chars)
        pasw = ''.join([random.choice(chars) for x in range(length)])
        print('Your Password:', pasw)
        return pasw

def capresh(SITEKEY, APIKEY, REGURL, CAPIN, CAPRES):
        stringin = CAPIN + '?key=' + APIKEY + '&method=hcaptcha&sitekey=' + SITEKEY + '&pageurl=' + REGURL
        print (stringin)
        r = requests.get(stringin)
        idcap = r.text
        print (idcap)
        id = idcap[3:]
        print (id)
        ID = id
        print ("wayting ...")
        time.sleep(1)
        #https://2captcha.com/res.php?key=YOUR_API_KEY&action=get&id=2122988149
        stringres = CAPRES + '?key=' + APIKEY + '&action=get&id=' + ID
        print (stringres)
        r = requests.get(stringres)
        resultall = r.text
        #print (resultall)
        #result = resultall[3:]
        #print (result)
##########################################
        while True:
                time.sleep(10)
                if resultall[0:2] == 'OK':
                        print ('loop OK')
                        break
                r = requests.get(stringres)
                resultall = r.text
                print ('waiting ...requests loop')
#########################################
        result = resultall[3:]
        print ("--------------- OK --------------")
        return result



def main():

    try:
        input_email = sys.argv[1]
    except IndexError:
        print ('ERROR: NO EMAIL - Example: nameProg EMAIL NIKNAME')

    try:
        input_nikname = sys.argv[2]
    except IndexError:
        print ('ERROR: NO NIKNAME - Example: nameProg EMAIL NIKNAME')

    try:
        if sys.argv[3] == '-p' :
                inputp_password = sys.argv[4]
                print ('Your Password:', inputp_password)
        else:
                print ('ERROR: NOT valid argument')
    except  IndexError:
        print('Genereshion password....')
        pass_save = passgen(8)


    print ("input_email:", input_email)
    print ("input_nikname:", input_nikname)


    #for 2Captcha Solver
    driver = webdriver.Firefox(Addon)
    #for debug no 2Captha Solver
    #driver = webdriver.Firefox()
    driver.get('https://discord.com/register')

    time.sleep(2)
    email_input = driver.find_element(By.NAME, "email")
    email_input.clear()
    email_input.send_keys(input_email)
    time.sleep(1)
    user_input = driver.find_element(By.NAME, "username")
    user_input.clear()
    user_input.send_keys(input_nikname)

    input_passwd = driver.find_element(By.NAME, "password")
    input_passwd.clear()
    input_passwd.send_keys("pass_save")
    time.sleep(1) 
    dayinput = driver.find_element(By.CLASS_NAME, "day-1uOKpp")
    #dayinput = driver.find_element(By.CLASS_NAME, "month-1Z2bRu")
    
    actions = ActionChains(driver)
    actions.move_to_element(dayinput)
    actions.click(dayinput)
    actions.key_down(Keys.TAB)
    actions.key_up(Keys.TAB)
    
    #add new
    #actions.key_down(Keys.DOWN)
    #actions.key_up(Keys.DOWN)


    actions.key_down(Keys.DOWN)
    actions.key_up(Keys.DOWN)

    actions.key_down(Keys.TAB)
    actions.key_up(Keys.TAB)
    
    actions.perform()
    i = 0
    while i<30:
        actions.key_down(Keys.DOWN)
        actions.key_up(Keys.DOWN)
        #time.sleep(0.5)
        i = i + 1 
    actions.perform()

    actions.key_down(Keys.TAB)
    actions.key_up(Keys.TAB)
    time.sleep(0.5)
    actions.key_down(Keys.TAB)
    actions.key_up(Keys.TAB)

    #raskomentit client
    actions.key_down(Keys.TAB)
    actions.key_up(Keys.TAB)
###########################################
    #actions.key_down(Keys.TAB)
    #actions.key_up(Keys.TAB)

    time.sleep(0.5)
    #raskomentit client
    actions.key_down(Keys.ENTER)
    actions.key_up(Keys.ENTER)
     
    actions.perform()    
############################################
    print("OK-register")
    time.sleep(3)
############################################
##### for ban ##############################
    ###chekbox = driver.find_element(By.CLASS_NAME, "inputDefault-2F39XG")
    ####chekbox = driver.find_element(By.CSS_SELECTOR, "type=checkbox")
   # chekbox = driver.find_element(By.CLASS_NAME, "checkbox-f1HnKB")
   # actions.move_to_element(chekbox)
   # actions.click(chekbox)  

   # actions.key_down(Keys.TAB)
   # actions.key_up(Keys.TAB)
   # actions.key_down(Keys.TAB)
   # actions.key_up(Keys.TAB)
   # actions.key_down(Keys.TAB)
   # actions.key_up(Keys.TAB)  
   # actions.key_down(Keys.ENTER)
   # actions.key_up(Keys.ENTER)   
   # actions.perform() 
####################################################################
    #otv = capresh(SITEKEYS, APIKEYS, REGURLS, CAPINS, CAPRESS)
    #print (otv)

#    js_script = f"""
#          let captchaElement = document.querySelector('[name="h-captcha-response"]')
#          let inputElement = document.createElement('input');
#          inputElement.setAttribute('type', 'hidden');
#          inputElement.setAttribute('name', 'response_token');
#          inputElement.setAttribute('value', "{otv}");
#          captchaElement.appendChild(inputElement)
#    """

#    js_script = f"""window[wigetInfo.callback]("{otv}");"""
    # wait for iframe
    #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#root > div > main > div > section > form > div > div > div > iframe')))
    #WebDriverWait(driver, 0).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#checkbox"))).click()
    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))#.click()
    
    #driver.find_element(By.TAG_NAME, "iframe").click()
    
    #time.sleep(10)
    #driver.switch_to.frame(frameswitch)
    otv = capresh(SITEKEYS, APIKEYS, REGURLS, CAPINS, CAPRESS)
    print (otv)
    print("execute_script")
    driver.execute_script("document.querySelector(" + "'" + '[name="h-captcha-response"]' + "'" + ").innerHTML = " + "'" + otv + "'")
    
    
    frameswitch = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "html.keyboard-mode.full-motion.disable-forced-colors.theme-dark.platform-web.font-size-16 body div div iframe")))#.click()
    driver.switch_to.frame(frameswitch)
    print ("frame switch") 
    #otv = capresh(SITEKEYS, APIKEYS, REGURLS, CAPINS, CAPRESS)
    #print (otv)
    ### worked
    #driver.execute_script("document.querySelector(" + "'" + '[name="h-captcha-response"]' + "'" + ").innerHTML = " + "'" + otv + "'")
    
    print("switch default content")
    driver.switch_to.default_content()
    #driver.switch_to.frame(frameswitch)
    #otv = capresh(SITEKEYS, APIKEYS, REGURLS, CAPINS, CAPRESS)
    #print (otv)

    #driver.execute_script("document.querySelector(" + "'" + '[name="h-captcha-response"]' + "'" + ").innerTEXT = " + "'" + otv + "'")
    #driver.find_element(By.XPATCH, "//*[@id="h-captcha-response-068gioz8af6w"]")
    #capklika = driver.find_element(By.NAME, "h-captcha-response")
    #capklika = driver.find_element(By.CSS_SELECTOR, "#h-captcha-response-068gioz8af6w")
    #capklika = driver.find_element(By.CSS_SELECTOR, "div.button-submit")
    #capklika = driver.find_element(By.XPATH, "/html/body/div[2]/div[8]")
    #HELPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
    #capklika = driver.find_element(By.CSS_SELECTOR, ".button-submit")
    timerloop(5)
    #capklika = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "button-submit")))#.click(
    #capklika = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".button-submit")))#.click(
    #frameswitch = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "html body.no-selection div.challenge-container div.challenge div.challenge-view div.challenge-header div.challenge-prompt div.prompt-padding h2.prompt-text"))).click()
    #driver.switch_to.frame(frameswitch)
    print ("frame switch2")
    #try: 
    #capklika = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "html body.no-selection div.challenge-interface div.button-submit.button div.text"))).click()
    #driver.find_element(By.CSS_SELECTOR, "html body.no-selection div.challenge-interface div.button-submit.button").click()
    #html body.no-selection div.challenge-interface div.button-submit.button div.text
    #capklika = driver.find_element(By.CLASS_NAME, "button-submit button")
    #except TimeoutException as e:
    #    print ("timeout exp")
    #    print (e)
    #    return e
    #chekklika = driver.find_element(By.ID, "checkbox")
    #capklika = driver.find_element(By.CLASS_NAME, "button-submit button")
    #capklika = driver.find_element(By.CLASS_NAME, "button-submit button")
    #actions.click(chekklika)
    timerloop (120)
    #time.sleep(5)
    #actions.click(capklika)
    #actions.perform()

    #driver.find_element(By.CSS_SELECTOR, "#root > div > main > div > section > form > button._2iYm2u0v9LWjjsuiyfKsv4._1z3RdCK9ek3YQYwshGZNjf._3zBeuZ3zVV-s2YdppESngy._28oc7jlCOdc1KAtktSUZvQ").click()
    print("Captcha OK")
if __name__ == '__main__':
    main()
