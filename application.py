from selenium import webdriver
from selenium.common.exceptions import TimeoutException,NoSuchElementException
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options
import time,sys,os,datetime,csv
from sys import platform
logFile = open("log.txt","a+")
logFile.write("\nStarted at: " + str(datetime.datetime.now()))
cur_path = sys.path[0]
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)


if platform == "linux" or platform == "linux2":
    # linux
    path = resource_path('I:\\clients\\chromedriver')
else:
    path = resource_path('I:\\clients\\chromedriver.exe')
chrome_options = Options()
# chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--headless")
# chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--window-size=1920,1080")
# chrome_options.add_argument("--no-sandbox") # linux only
# chrome_options.headless = True # also works
# driver = webdriver.Chrome()
    # Windows...
print("\n\nProcessing.....")

driver =webdriver.Chrome(path,options=chrome_options)
# driver =webdriver.Chrome(path,)

            
driver.maximize_window()
# open link
# driver.set_page_load_timeout(120)
driver.set_page_load_timeout(30)

try:
    driver.get("https://www.scorptec.com.au/product/cases/all-cases")
    logFile.write("\nsuccess : Loaded...")
    print("success : Loaded...")
except TimeoutException as e:
    logFile.write("\ninfo : website taking too long to load...stopped")
    print("info : website taking too long to load...stopped")
if os.path.isfile('file.csv'):
    print ("info : File already exist")
    logFile.write("info : File already exist")
else:
    with open("file.csv","w+",newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['Name',"Description","Price","Img_url"])
        print ("info : File not exist... will create new file")
        logFile.write("info : File not exist... will create new file")
products_links = []
try:
    for i in range(2):
        links = driver.find_elements_by_xpath("//div[@class='desc']/a")
        for d in links:
            href = d.get_attribute("href")
            # print(href)
            products_links.append(href)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(5)

    print(len(products_links))
    # print(products_links)
except Exception as e:
    print(e)
    logFile.write("\n" + str(e))
# write to csv from website links
try:
    for link in products_links:
        row = []
        driver.get(link)
        try:
            name = driver.find_element_by_id("product_name").text
            row.append(name)
        except Exception as e:
            print(e)
            row.append(None)
        try:
            desc = driver.find_element_by_css_selector("h2.h2desc").text
            row.append(desc)
        except Exception as e:
            print(e)
            row.append(None)
        try:
            price = driver.find_element_by_id("price-price").text
            row.append(price)
        except Exception as e:
            print(e)
            row.append(None)
        try:
            img = driver.find_element_by_id("large_image").get_attribute("src")
            row.append(img)
        except Exception as e:
            print(e)
            row.append(None)
        try:
            with open('file.csv',"a+",newline='', encoding='utf-8') as f:
                writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
                writer.writerow(row)
        except Exception as e:
            print(e)
            logFile.write("\n" + str(e))
except Exception as e:
    print(e)
    logFile.write("\n" + str(e))
    
print("success : complete" )
logFile.write("success : complete" )