from Movies import movie_getter
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import selenium.common.exceptions
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
movies = movie_getter()[:20]
ratings = {}
url = "https://www.imdb.com/?ref_=nv_home"
Path = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(options=chrome_options, executable_path=Path)
driver.get(url)
for movie in movies:

    elem = driver.find_element_by_name("q")
    elem.send_keys(movie)
    elem.send_keys(Keys.RETURN)
    time.sleep(10)
    try:
        elex = driver.find_element_by_class_name(
            "result_text").find_element_by_tag_name("a")
        elex.click()
        time.sleep(10)
        elet = driver.find_element_by_class_name("ratingValue").find_element_by_tag_name(
            "strong").find_element_by_tag_name("span").text
    except selenium.common.exceptions.NoSuchElementException:
        pass

    time.sleep(10)
    ratings[movie] = elet
driver.close()
with open("ratings_imdb.txt", 'w') as f:
    for key, value in ratings.items():
        f.write('%s:%s\n' % (key, value))
