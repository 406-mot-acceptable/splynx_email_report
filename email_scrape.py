from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

def write_append(fn, ttype, texts):
    for i, ttype in enumerate(texts, 1):
            with open(fn, "a", encoding='utf-8') as file:
               file.write(f"{i}: {ttype}" + "\n")

def scrape_email(url): 
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        driver.get(url)
        time.sleep(5)  
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        driver.quit()
        return soup
    except Exception as e:
        print(f"Error in scrape_email: {e}")
        return None 

def scrape_body():
    soup = raw_email
    body_ele = soup.find_all("div", class_="ticket-message-body message-with-blockquote")
    body_texts = [email_body.get_text(separator=' ', strip=True) for email_body in body_ele]
    write_append("body_scrape", "body", body_texts)

def scrape_auth():
    soup = raw_email
    auth_ele = soup.find_all("strong", class_="comment-title")
    auth_texts = [email_auth.get_text(separator=' ', strip=True) for email_auth in auth_ele]
    write_append("auth_scrape", "auth", auth_texts)

def scrape_time():
    soup = raw_email
    time_ele = soup.find_all("time", class_="text-muted timeago")
    time_texts = [email_time.get_text(separator=' ', strip=True) for email_time in time_ele]
    write_append("time_scrape", "time", time_texts)

## Test URL (Replace with actual email page URL)
if __name__ == "__main__":
    raw_email = scrape_email("https://portal.datonet.co.za/public/tickets?ticket=T0RFMU5qWmxPRGhrWXpCak1XTXpaZGlOYjV3Z3l1Nm5nMnB1cXZvbjhOQT0")
    scrape_body()
    scrape_auth()
    scrape_time()
