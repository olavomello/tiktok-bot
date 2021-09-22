
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import pyfiglet
from time import sleep
# Random IP
import random, socket, struct , json, urllib.request

# Web driver
driver = None
# IP 
ip = 0
arrIPs = []

def loop1():
    global i
    sleep(10)
    try:
        driver.find_element_by_xpath("//*[@id=\"main\"]/div/div[4]/div/button").click()
    except:
        print("You didn't solve the captcha yet. Need to refresh to avoid endless loop.")
        driver.refresh()
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
        total = i * totalViews
        print("Views successfull delivered! Total", total,"views. Send again soon...")
        sleep(320)
        loop1()
    except:
        print("A generic error occurred. Now will retry again")
        driver.refresh()
        sleep(30)
        loop1()

def loop2():
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
    sleep(20)
    wait_time = 660 #11 minutes
    try:
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[1]/div/button").click() #Followers
    except:
        print("You didn't solve the captcha yet. Need to refresh to avoid endless loop.")
        driver.refresh()
        loop4()
    try:
        sleep(20)
        driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div/div/form/div/input").send_keys(vidUrl) #Write
        sleep(2)
        driver.find_element_by_xpath("//*[@id=\"sid\"]/div/div/div/form/div/div/button").click() #Search
        sleep(20)
        driver.find_element_by_xpath("//*[@id=\"c2VuZF9mb2xsb3dlcnNfdGlrdG9r\"]/div[1]/div/form/button").click() #AddFollowers
        sleep(wait_time/3)
        print("Success delivered!")
        sleep(wait_time/3)
        driver.refresh()
        sleep(wait_time/3)
        loop4()
    except:
        print("A generic error occurred. Now will retry again")
        driver.refresh()
        sleep(wait_time)
        loop4()

def loop5():
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
        sleep(10)
        # driver.find_element_by_xpath("/html/body/div[4]/div[6]/div/div/div/div/div[1]/div/form/button").click() # AddShares
        driver.find_element_by_xpath("//*[@id=\"c2VuZC9mb2xsb3dlcnNfdGlrdG9s\"]/div[1]/div/form/button").click() #AddFollowers
        sleep(10)
        print("Shares sent!")
        sleep(150)
    except Exception as e:
        print("A generic error occurred. Now will retry again. Error : " + str(e))
        driver.refresh()
        sleep(150)
        loop5()

def loop6():
    sleep(1000)
    driver.refresh()
    print("Reload")
    loop5()

# print("Author: https://github.com/NoNameoN-A")

chromiumDriver = 'chromedriver'
totalViews = 500
#vidUrl = "https://www.tiktok.com/@isacaram/video/6910652595497340166" #Change it

vidUrl = str(input("Link do vídeo no Tiktok : "))
if vidUrl == "" : vidUrl = "https://www.tiktok.com/@isacaram/video/6827907779047492869"
print("Boosting vídeo : " + vidUrl)

bot = int(input("What do you want to do?\n1 - Auto views("+str(totalViews)+")\n2 - Auto hearts\n3 - Auto (FIRST) comments heart\n4 - Auto followers\n5 - Auto Share\n6 - Simple reload\n"))
i = 0


# Random IP
def setIP():
    if len(arrIPs) <= 0 :
        # Opening JSON file
        # strJson = 'https://proxylist.geonode.com/api/proxy-list?limit=50&page=1&sort_by=lastChecked&sort_type=desc&country=BR' # BR only
        strJson = 'https://proxylist.geonode.com/api/proxy-list?limit=50&page=1&sort_by=lastChecked&sort_type=desc&filterUpTime=100&google=true&protocols=http%2Chttps'
        user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
        headers={'User-Agent':user_agent,} 
        request=urllib.request.Request(strJson,None,headers) #The assembled request
        response = urllib.request.urlopen(request)
        data = response.read() # The data u need
        dataParse = json.loads(data)
        
        # Generate IP list
        for d in dataParse['data']:
            # print(d['ip'])
            if d['ip'] : 
                arrIPs.append([d['protocols'][0], d['ip'], d['port']])
                # arrIPs.append(["https", "103.58.75.82","80"]) # Fixed to test
    
    # Random IP choice
    return random.choice(arrIPs)

# Main function 
def exec():
    try:

        # IP RANDOMIZER
        # ip = setIP()
        # print("IP : " + str(ip))

        urlMain = "https://vipto.de/"

        # Start Chromium
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--headless')
        chrome_options.add_argument("window-size=200,500")
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        # chrome_options.add_argument("--app=="+urlMain)
        # if ip :
        #     chrome_options.add_argument('--proxy-server=%s' % ip[0]+'://'+ip[1]+':'+ip[2])

        # Add options
        global driver
        driver = webdriver.Chrome(executable_path=r'chromedriver', options=chrome_options)
            
        # Exec
        driver.get(urlMain)

    except Exception as e:
        print("IP randomizer error [", e,"] Trying another...")
        driver.close()
        sleep(1)
        exec()

exec()

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
else:
    print("You can insert just 1, 2, 3, 4, 5 or 6")
