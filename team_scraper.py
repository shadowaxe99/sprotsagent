from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from pep_talk_generator import generate_pep_talk

# Setup Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')

# Setup WebDriver
webdriver_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# URL of the website with the team list
URL = 'https://www.milb.com/team'

def scrape_team_list():
    # Navigate to the website
    driver.get(URL)

    # Find the team list on the webpage
    team_list = driver.find_element(By.CLASS_NAME, 'team-list')

    # Extract and print the team names and generate a pep talk for each team
    for team in team_list.find_elements(By.TAG_NAME, 'li'):
        print(team.text)
        pep_talk = generate_pep_talk(True)
        print('Pep Talk:', pep_talk)

    # Close the WebDriver
    driver.quit()

# Example usage
scrape_team_list()