# Importing all the modules
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime
from colors import bcolors
import getpass
from selenium.webdriver.common.by import By

desc = """This is a Free Version It will Crossopost in 30 community For paid version contact on 
our gmail. As we all know crossposting on reddit takes 2 hours. This is the solution.\nThank You"""
print(bcolors.OKCYAN + desc.center(len(desc)))

# Creating option from over to make it hide from detection
option = Options()
option.add_argument("--headless")
option.add_argument('--no-sandbox')
option.add_argument('--start-maximized')
option.add_argument('--single-process')
option.add_argument('--disable-dev-shm-usage')
option.add_argument("--incognito")
option.add_argument('--disable-blink-features=AutomationControlled')
option.add_argument("--log-level=3")
option.add_argument("--disable-infobars")
option.add_argument("--disable-notifications")
option.add_argument("--disable-extensions")
option.add_experimental_option('useAutomationExtension', False)
option.add_experimental_option("prefs",
                               {"profile.default_content_setting_values.notifications": 2})
option.add_experimental_option(
    "excludeSwitches", ["enable-logging", "disable-popup-blocking", 'enable-automation'])

def logg(driver, username, password):
    # Getting the site for login in Reddit
    driver.get("https://www.reddit.com/login/?dest=https%3A%2F%2Fwww.reddit.com%2F")


    # Maximize the Window for better view
    driver.maximize_window()
    time.sleep(2)

    # Entering Credentials
    driver.find_element(By.ID, "loginUsername").send_keys(username)
    driver.find_element(By.ID, "loginPassword").send_keys(password)

    # Pressing login button
    driver.find_element(By.XPATH,
        "/html/body/div/main/div[1]/div/div[2]/form/fieldset[5]/button").click()
    time.sleep(5)

    driver.get("https://www.reddit.com/")

    time.sleep(10)

    # Pressing login button
    driver.find_element(By.XPATH,
        "/html/body/div/main/div[1]/div/div[2]/form/fieldset[5]/button").click()
    time.sleep(10)
    try:
        driver.find_element(By.XPATH, """//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[4]/div/div/div/header/div[1]/div[2]/button""").click()
    except:
        pass
    driver.find_element(By.XPATH, """//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[1]/header/div/div[1]/div[2]""").click()
    time.sleep(10)
    comm_link = []
    elems = driver.find_elements(By.XPATH, "//a[@href]")
    for elem in elems:
        comm_link.append(elem.get_attribute("href"))

    for i in range(len(comm_link)):
        if comm_link[i]=='https://www.reddit.com/r/popular/':
            index = i
            break
    filtered_comm = comm_link[1:index-1]
    comm = []
    for i in range(len(filtered_comm)):
        splited_link = str(filtered_comm[i]).split("https://www.reddit.com/")
        comm.append(splited_link[1])
    
    return comm

# Function for automation
def cross(username, post, password, t):
    # Path of the driver
    driver = webdriver.Chrome(options=option)
    logg(driver, username, password)

    subred = comm

    url = "https://www.reddit.com/"

    # Communities in which you want to crosspost
    comm = subred

    # Running for loop for Crossposting in every community    
    for j in range(len(comm)):
        time.sleep(t*1)
        link = f'{url}{comm[j]}/{post}'
        try:
            driver.get(link)

        except:
            time.sleep(2)
            driver.quit()
            driver = webdriver.Chrome(options=option)
            logg(driver, username, password)

            # Getting the Post link
            driver.get(f'{url}{comm[j+1]}/{post}')

        try:
            # Press Post Button
            button = driver.find_element(By.XPATH,
                """//*[@id="AppRouter-main-content"]/div/div/div[2]/div[3]/div[1]/div[2]/div[3]/div[2]/div[2]/div/div/div[1]/button""")
            button.click()
            time.sleep(2)
            print(f'Crossposting Completed! in {j+1}', end="\r", flush=True)


        except:
            # If error Occur
            print("MayBe the community doesn't Exist")
        
    # Quit the driver after Crossposting
    driver.quit()

print(bcolors.OKGREEN + """
88""88  888888  88 88    88 88    88  888888
88__88  88__    88   88  88   88  88    88  
88"88   88""    88   88  88   88  88    88  
88  88  888888  88 88    88 88    88    88                                                                                                         
""" + bcolors.ENDC)
# Entering all Important Details---------->
u1 = str(input(bcolors.OKBLUE + "\nPlease Enter your Reddit Username: " + bcolors.BOLD))

pas = str(input(bcolors.WARNING + "\nPlease Enter your Reddit Password:: " + bcolors.BOLD))

p1= (str(input(bcolors.OKBLUE + "\nEnter Your postlink: " + bcolors.BOLD))).split("https://www.reddit.com/")

ti = int(input(bcolors.OKBLUE + "\nEnter how many seconds you want to wait after each crosspost: " + bcolors.BOLD))



#Fuctions for Crossposting and subreddit listing
cross(username = u1, post = p1[1], password = pas, t = ti)

print("We are quitting because we have completed the tasks within 20 seconds software will quit")
time.sleep(20)