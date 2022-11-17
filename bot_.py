from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time,os
from dotenv import load_dotenv

load_dotenv()
main_path = os.getenv('drive_link')
log_c = 0
try:
    driver  = webdriver.Chrome(executable_path=main_path)
except:
     driver  = webdriver.Chrome(executable_path=main_path)

def SetGoogle():
        user = os.getenv('email')
        pin = os.getenv('password')
        
        driver.implicitly_wait(15)
        driver.switch_to.new_window()

        driver.get('https://accounts.google.com/signin')

        driver.find_element(By.CSS_SELECTOR, "input#identifierId").send_keys(user)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Next']"))).click()
        driver.find_element(By.NAME,'Passwd').send_keys(pin)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Next']"))).click()
        
        time.sleep(5)
        return 1


    
def MerakiMeeting(link,log_c):
    if not log_c:
        log_c = SetGoogle()
   
    driver.switch_to.new_window()
    driver.get('https://meet.google.com/'+link)
    movies = driver.find_element(By.TAG_NAME, 'body')
    cond = driver.find_element(By.TAG_NAME, 'body').text
    if movies.text == 'Return to home screen':
         print('log in first')
    elif  "You'll be able to join in just a moment" in cond:
         print('your link is not working')
    else:
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Dismiss']"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Join now']"))).click()
        time.sleep(3)
    return log_c

meetings_li = ['ksx-dxcx-ttf','ksx-dxcx-fgh','ksx-dxcx-mit','ksx-dxcx-tif']


for i in meetings_li:
    log_c = MerakiMeeting(i,log_c)
