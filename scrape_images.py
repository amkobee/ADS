from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import urllib.request

# start chrome
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36")
driver = webdriver.Chrome(options=chrome_options)
#wait = WebDriverWait(driver, 10)

driver.get('https://reddit.com/r/earthporn/')

# download the first 5 images
i = 1
while i <= 5:

    # get image
    img = driver.find_element_by_xpath(f"(//img[@alt='Post image'])[{i}]")
    src = img.get_attribute('src')

    # download the image
    urllib.request.urlretrieve(src, f"test_{i}.png")

    i += 1

driver.close()
