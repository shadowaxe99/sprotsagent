import requests
from bs4 import BeautifulSoup
from pep_talk_generator import generate_pep_talk

# URL of the website with baseball updates
URL = 'https://www.milb.com/scores'

# Function to scrape baseball updates
def scrape_baseball_updates():
    # Send a GET request to the website
    response = requests.get(URL)

    # Parse the website's content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the game results on the webpage
    game_results = soup.find_all('div', class_='game-results')

    # Extract and print the game results
    for game_result in game_results:
        teams = game_result.find_all('span', class_='team-name')
        scores = game_result.find_all('span', class_='team-score')
        if teams and scores:
            print(f'{teams[0].text} {scores[0].text}, {teams[1].text} {scores[1].text}')
            # Generate a pep talk based on the game result
            is_positive = scores[0].text > scores[1].text
            pep_talk = generate_pep_talk(is_positive)
            print('Pep Talk:', pep_talk)

# Example usage
scrape_baseball_updates()