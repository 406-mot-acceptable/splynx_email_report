from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

def scrape_email(url):
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        driver.get(url)
        
        time.sleep(5)  # Allow time for JavaScript to render
        
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        driver.quit()
        
        email_content = soup.get_text(separator='\n', strip=True)
        
        print("Extracted Email Content:")
        print(email_content)  # Test output to console
        
        return email_content
    except Exception as e:
        print(f"Error in scrape_email: {e}")
        return None

# Test URL (Replace with actual email page URL)
if __name__ == "__main__":
    test_url = "https://portal.datonet.co.za/public/tickets?ticket=T0RFMU5qWmxPRGhrWXpCak1XTXpaZGlOYjV3Z3l1Nm5nMnB1cXZvbjhOQT0"
    scrape_email(test_url)
