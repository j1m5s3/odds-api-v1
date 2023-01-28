import json
from pymongo import MongoClient
from dotenv import dotenv_values

from scraping_utils.scrape import  scrape_nfl_game_lines
from db_operations.creators import Creator

config = dotenv_values(".env")


if __name__ == '__main__':
    url = 'https://sportsbook.draftkings.com/leagues/football/nfl'
    scrape_results = scrape_nfl_game_lines(url)

    creator = Creator(connection_url=config['DB_CONNECTION_URL'],
                      db_name=config['DB_NAME'],
                      collection_name=config['DB_COLLECTION_GAME_LINES'])
    result = creator.create_live_records(scrape_results)
    print(result)
    pass
