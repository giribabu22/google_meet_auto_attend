from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time,datetime,os
from dotenv import load_dotenv

load_dotenv()

main_path = os.getenv('drive_link')

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = '/snap/bin/brave'
chrome_options.add_argument('--remote-debugging-port=9224')

class Bot():
    def __init__(self,log_c):
         self.driver = webdriver.Chrome(main_path,chrome_options= chrome_options)
         self.log_c = log_c
         self.Error_count = 0

    def NikkiCloseTab(self,tabName):
        li = self.driver.window_handles
        self.driver.switch_to.window(tabName)
        self.driver.close()
        self.driver.window_handles[len(li)-1]

    def SetGoogle(self):
            user = os.getenv('email')
            pin = os.getenv('password')

            self.driver.implicitly_wait(15)
            self.driver.switch_to.new_window()

            self.driver.get('https://accounts.google.com/signin')

            self.driver.find_element(By.CSS_SELECTOR, "input#identifierId").send_keys(user)
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Next']"))).click()
            self.driver.find_element(By.NAME,'Passwd').send_keys(pin)
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Next']"))).click()
            
            time.sleep(5)
            return 1
    def cal_(self):
        print('running')
        self.driver.implicitly_wait(15)
        self.driver.switch_to.new_window()
        self.driver.get(f'https://meet.google.com/{link}')

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Dismiss']"))).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Join now']"))).click()

        studentsDcodeData = self.driver.find_elements(By.CLASS_NAME,'XEazBc')
        students = []
        for s in studentsDcodeData:
                students.append(s.text)
    def joiningMeeting(self,link,end_time):
        try:
            dic = {}
            self.driver.implicitly_wait(15)
            self.driver.switch_to.new_window()
            self.driver.get(f'https://meet.google.com/{link}')
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Dismiss']"))).click()
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Join now']"))).click()
            # if self.Error_count == 2:
            # else:
            #     WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Ask to join']"))).click()
            while True:
                students = []
                time.sleep(2)
                studentsDcodeData = self.driver.find_elements(By.CLASS_NAME,'XEazBc')
                i =0
                while i < len(studentsDcodeData):
                    c = 0
                    if studentsDcodeData.count(studentsDcodeData[i]) > 1:
                        studentsDcodeData.pop(i)
                    else:
                        i+=1

                for s in studentsDcodeData:
                        if s.text not in dic:
                            dic[s.text] = 0
                        else:
                            dic[s.text] += 2  
                cur = str(datetime.datetime.now()).split(' ')
                res = cur[1].split(':')
                if end_time[0] ==  res[0] and end_time[1] == res[1]:
                    break  
            return dic 
        except Exception as e:
            print(e)
            if self.Error_count > 3:
                    return 'error'
            else:
                tab_name = 'Meet - '+ link
                self.NikkiCloseTab(tab_name)
                self.joiningMeeting(link,end_time)

            

cur = str(datetime.datetime.now()).split(' ')
res = cur[1].split(':')
end = int(res[1]) + 1
t = res[0]+":"+str(end)
m = {'gxn-uxpk-jdm':{"starting_time":res[0]+":"+res[1],'ending_time':t},'ksx-dxcx-fgh':{"starting_time":'11:30','ending_time':"12:10"}} 

log_c =0

if "__main__" == __name__:
    botFunction = Bot(log_c)
    # botFunction.SetGoogle()
    def none_stop():
        students = []
        dic = {}
        while len(m):
            for i in m:
                cur = str(datetime.datetime.now()).split(' ')
                res = cur[1].split(':')
                start_time = m[i]["starting_time"].split(':')
                end_time = m[i]["ending_time"].split(':')
                print(start_time,cur)
                if start_time[0] == res[0] and start_time[1] == res[1]:
                    students.append((botFunction.joiningMeeting(i,end_time)))
                    dic[i] = 1
                    print(students) 
                # if com_time[0] == res[0] and com_time[1] == res[1]:
                #     tab_name = 'Meet - '+ i
                #     botFunction.NikkiCloseTab(tab_name)
            time.sleep(1)

    none_stop()
