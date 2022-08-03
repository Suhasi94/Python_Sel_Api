from selenium.webdriver import Chrome
from requests import request
from pytest import mark

driver = Chrome("./chromedriver")
driver.get(r"C:\Users\singh\PycharmProjects\project1new\_selenium\sir file\links.html")

# Find all the links 
links = driver.find_elements_by_xpath("//a")

# Iterate through the list and get the value of "href" attribute
urls = [ ]
for link in links:
    urls.append((link.text, link.get_attribute("href")))

@mark.parametrize("link_text, url", urls)
def test_broken_links(link_text, url):
    print(f"Hitting url: {url} Link text {link_text}")
    response = request("GET", url)
    assert response.status_code == 200