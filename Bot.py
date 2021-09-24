from os import system, name
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
import math
import pyfiglet
from time import sleep
import random, socket, struct , json, urllib.request
import undetected_chromedriver.v2 as uc
from io import BytesIO
from io import StringIO
from PIL import Image
import pytesseract
import base64


# from pyvirtualdisplay import Display

# Boost
boost = False

# Proxy
isProxy = False

# Web driver
driver = None

# Chrome or Anonymous
chromeAnonymous = False 

# Tabs
useTabs = False
tabs = 1

def loop1():
    global i
    exec()
    sleep(10)
    try:
        driver.find_element_by_xpath("//*[@id=\"main\"]/div/div[4]/div/button").click()
    except:
        print("You didn't solve the captcha yet. Need to refresh to avoid endless loop.")
        loop1()
    try:
        sleep(2)
        driver.find_element_by_xpath("//*[@id=\"sid4\"]/div/form/div/input").send_keys(vidUrl)
        sleep(1)
        driver.find_element_by_xpath("//*[@id=\"sid4\"]/div/form/div/div/button").click()
        sleep(2)
        driver.find_element_by_xpath("//*[@id=\"c2VuZC9mb2xsb3dlcnNfdGlrdG9V\"]/div[1]/div/form/button").click()
        sleep(10)
        driver.refresh()
        i += 1
        total = i * 500
        print("Views successfull delivered! Total", total,"views. Send again soon...")
        if not boost : sleep(320)
        loop1()
    except:
        print("A generic error occurred. Now will retry again")
        if not boost : driver.refresh()
        if not boost : sleep(10)
        loop1()

def loop2():
    exec()
    sleep(10)
    try:
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[2]/div/button").click()
    except:
        print("You didn't solve the captcha yet. Need to refresh to avoid endless loop.")
        driver.refresh()
        loop2()
    try:
        sleep(2)
        driver.find_element_by_xpath("/html/body/div[4]/div[3]/div/form/div/input").send_keys(vidUrl)
        sleep(1)
        driver.find_element_by_xpath("/html/body/div[4]/div[3]/div/form/div/div/button").click()
        sleep(10)
        driver.find_element_by_xpath("/html/body/div[4]/div[3]/div/div/div[1]/div/form/button").click()
        sleep(10)
        hearts = driver.find_element_by_xpath('//*[@id="c2VuZE9nb2xsb3dlcnNfdGlrdG9r"]/span').text
        sleep(55)
        print(hearts," Success delivered!")
        sleep(100)
        driver.refresh()
        sleep(200)
        loop2()
    except:
        print("A generic error occurred. Now will retry again")
        driver.refresh()
        sleep(355)
        loop2()

def loop3():
    exec()
    sleep(10)
    try:
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[3]/div/button").click()
    except:
        print("You didn't solve the captcha yet. Need to refresh to avoid endless loop.")
        driver.refresh()
        loop2()
    try:
        sleep(2)
        driver.find_element_by_xpath("/html/body/div[4]/div[4]/div/form/div/input").send_keys(vidUrl)
        sleep(1)
        driver.find_element_by_xpath("/html/body/div[4]/div[4]/div/form/div/div/button").click()
        sleep(5)
        driver.find_element_by_xpath("/html/body/div[4]/div[4]/div/div/div/div/div[1]/div/form/button").click()
        sleep(5)
        driver.find_element_by_xpath("/html/body/div[4]/div[4]/div/div/div/div/form/ul/li/div/button").click()
        sleep(47)
        driver.refresh()
        print("Success delivered!")
        loop3()
    except:
        print("A generic error occurred. Now will retry again")
        driver.refresh()
        sleep(50)
        loop3()

def loop4():
    exec()
    sleep(10)
    wait_time = 660 #11 minutes
    try:
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[1]/div/button").click() #Followers
    except:
        print("You didn't solve the captcha yet. Need to refresh to avoid endless loop.")
        driver.refresh()
        loop4()
    try:
        sleep(1)
        driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/form/div/input").send_keys(vidUrl) #Write
        sleep(2)
        driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/form/div/div/button").click() #Search
        sleep(5)
        driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div/div/div/form/button").click() #AddFollowers
        # driver.execute_script("comfollowers();")
        sleep(20)
        print("Success delivered!")
        driver.refresh()
        sleep(wait_time)
        loop4()
    except:
        print("A generic error occurred. Now will retry again")
        if not boost : driver.refresh()
        if not boost : sleep(10)
        loop4()

def loop5():
    exec()
    sleep(20)
    try:
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[5]/div/button").click()
    except:
        print("You didn't solve the captcha yet. Need to refresh to avoid endless loop.")
        driver.refresh()
        loop5()
    try:
        sleep(5)
        driver.find_element_by_xpath("/html/body/div[4]/div[6]/div/form/div/input").send_keys(vidUrl) # Write
        sleep(2)
        driver.find_element_by_xpath("/html/body/div[4]/div[6]/div/form/div/div/button").click() # Search
        sleep(5)
        # driver.find_element_by_xpath("/html/body/div[4]/div[6]/div/div/div/div/div[1]/div/form/button").click() # AddShares
        driver.find_element_by_xpath("//*[@id=\"c2VuZC9mb2xsb3dlcnNfdGlrdG9s\"]/div[1]/div/form/button").click() #AddFollowers
        sleep(5)
        print("Shares sent! Sending more in 3 minutes ...")
        sleep(180)
        loop5()
    except Exception as e:
        print("A generic error occurred. Now will retry again. Error : " + str(e))
        driver.refresh()
        sleep(5)
        loop5()

def loop6():
    exec()
    sleep(1000)
    driver.refresh()
    print("Reload")
    loop5()
    
def loop7():
    # Captcha Broker
    clear()
    print(">>>>> Captcha Broker") 
    
    exec()
    sleep(10)

    ## Step 1
    # Get SRC from Captcha IMG
    img_data          =     driver.find_element_by_xpath('/html/body/div[4]/div[2]/form/div/div/img')
    print("Captcha Image : ", img_data)

    # Save file
    imgBlob           =     getImageScreenshot(img_data)
    # Open local file
    img               =   Image.open(imgBlob)  

    ## Step 2
    gray              =   img.convert('L')
    gray.save('img/captcha_gray.png')
    bw                =   gray.point(lambda x: 0 if x < 1 else 255, '1')
    bw.save('img/captcha_thresholded.png')
    
    # Step 3
    strCaptcha        =   pytesseract.image_to_string(bw)
    print("Captcha solved : ", strCaptcha);

    # try:
    #     driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[5]/div/button").click()
    # except:
    #     print("Captcha not found. Need to refresh to avoid endless loop.")
    #     driver.refresh()
    #     loop7()    

# --------------------------------------------------------------------------------------------

## UTILS

# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# Random IP
def setProxy():
    
    global webdriver
    arrIPs = []

    if isProxy == True :
        if len(arrIPs) <= 0 :
            # Opening JSON file
            # strJson   =   'https://proxylist.geonode.com/api/proxy-list?limit=1000&page=1&sort_by=lastChecked&sort_type=desc&country=BR' # BR only
            # strJson   =   'https://proxylist.geonode.com/api/proxy-list?limit=1000&page=1&sort_by=lastChecked&sort_type=desc&filterUpTime=100&country=BR'
            strJson     =   'https://proxylist.geonode.com/api/proxy-list?limit=1000&page=1&sort_by=lastChecked&sort_type=desc&filterUpTime=100&country=BR&protocols=http%2Chttps&anonymityLevel=transparent'
            
            # user agent
            user_agent  =   'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
            headers     =   {'User-Agent':user_agent,} 
            request     =   urllib.request.Request(strJson,None,headers) #The assembled request
            response    =   urllib.request.urlopen(request)
            data        =   response.read() # The data u need
            dataParse   =   json.loads(data)
            
            # Generate IP list
            for d in dataParse['data']:
                # print(d['ip'])
                if d['ip'] : 
                    arrIPs.append([d['protocols'][0], d['ip'], d['port']])
                    # arrIPs.append(["https", "103.58.75.82","80"]) # Fixed to test
        
        # Random IP choice
        ip = random.choice(arrIPs)
    else :
        # Localhost
        ip = ["http", "localhost", "80"]

    # IP
    PROXY   =   ip[1]+":"+ip[2]

    print("Proxy : ", PROXY)

    return [PROXY, ip]

# Element Screenshoot
def getImageScreenshot(element: WebElement) -> bytes:
    global driver
    
    strCaptcha      =   "img/captcha.png" 
    # driver          =   element._parent
    ActionChains(driver).move_to_element(element).perform()  # focus
    driver.save_screenshot(strCaptcha)

    # Base64 to Image
    scr_img     =   Image.open(strCaptcha)
    
    # Element position
    x           =   math.floor(element.location["x"])
    y           =   math.floor(element.location["y"])
    w           =   math.ceil(element.size["width"])
    h           =   math.ceil(element.size["height"])

    # Crop
    scr_img.crop(( x, y, w, h ))
    return scr_img.save(strCaptcha)

# Main function 
def exec():
    try:

        # Open virtual display
        # display = Display(visible=0, size=(800, 800))
        # display.start()

        # Main base tool site
        urlMain =   "https://vipto.de/" #"https://agenciadix.com.br/"

        # Start Chromium Options
        if chromeAnonymous == False :
            # chrome_options = webdriver.ChromeOptions()
            chrome_options = Options()
        else :
            chrome_options = uc.ChromeOptions()
            

        # chrome_options.add_argument('--headless')
        chrome_options.add_argument('window-size=200,700')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--ignore-ssl-errors')  
        chrome_options.add_argument('--hide-scrollbars')    
        chrome_options.add_argument("--log-level=3")  # fatal 
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")  
        if chromeAnonymous == False :    
            chrome_options.add_experimental_option('useAutomationExtension', False)
            chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
            chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # chrome_options.add_argument("--app=="+urlMain)
        # User agent
        user_agent = 'Mozilla/5.0 CK={} (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'
        chrome_options.add_argument("user-agent="+user_agent)
        
        if isProxy == True:
            # Set Proxy
            PROXY = setProxy()
            
            # Capabilities
            desired_capabilities = webdriver.DesiredCapabilities.CHROME.copy()
            # Change the proxy properties of that copy.
            desired_capabilities['proxy'] = {
                "httpProxy" : PROXY[0],
                "ftpProxy"  : PROXY[0],
                "sslProxy"  : PROXY[0] if PROXY[1][0] == "https" else '',
                "proxyType" : "MANUAL",
                'noProxy'   : None,
                "class"     : 'org.openqa.selenium.Proxy',
                'autodetect': False
            }  

            # Add Proxy support SSL 
            desired_capabilities['acceptSslCerts'] = True if PROXY[1][0] == "https" else False

            # Proxy      
            chrome_options.add_argument('--proxy-server='+PROXY[1][0]+'://'+PROXY[0])

        # Start server
        global driver
        if chromeAnonymous == False :
            if not driver :
                driver = webdriver.Chrome(executable_path=r'chromedriver', options=chrome_options)
        else :
            uc.TARGET_VERSION = 78        
            driver = uc.Chrome(options=chrome_options)

        # you have to use remote, otherwise you'll have to code it yourself in python to 
        # dynamically changing the system proxy preferences
        # driver = webdriver.Remote (urlMain, desired_capabilities)            

        # Tabs
        global useTabs
        if useTabs == True :
            # Open a new window
            driver.execute_script("window.open('');")
            # Switch to the new window and open new URL
            global tabs
            driver.switch_to.window(driver.window_handles[tabs])
            # Total tabs
            tabs = len(driver.window_handles)
            print("tabs : ", tabs)

        # you have to use remote, otherwise you'll have to code it yourself in python to 
        # dynamically changing the system proxy preferences
        # driver = webdriver.Remote(urlMain)

        # Exec
        driver.get(urlMain)

    except Exception as e:
        print("Engine error. Trying another...")
        if chromeAnonymous == False : 
            driver.close()
        sleep(1)
        exec()


# -------------------------------------------------------------------------------------------

print("############################################################")
print("######################## TIKTOK BOT ########################")
print("############################################################")

# 
vidUrl = str(input("Link do vídeo no Tiktok : "))
if vidUrl == "" : vidUrl = "https://www.tiktok.com/@isacaram/video/6827907779047492869"
print("Boosting vídeo : " + vidUrl)

bot = int(input("\n\n########## What do you want to do ? ##########\n\n1 - Auto views(500)\n2 - Auto hearts\n3 - Auto (FIRST) comments heart\n4 - Auto followers\n5 - Auto Share\n6 - Simple reload\n7 - Captcha Broker\n\n##############################################\n\n"))
i = 0

if bot == 1:
    loop1()
elif bot == 2:
    loop2()
elif bot == 3:
    loop3()
elif bot == 4:
    loop4()
elif bot == 5:
    loop5()
elif bot == 6:
    loop5()
elif bot == 7:
    loop7()    
else:
    print("You can insert just 1, 2, 3, 4, 5, 6 or 7")
