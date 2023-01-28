import json
from pymongo import MongoClient
from dotenv import dotenv_values

from scraping_utils.scrape import  scrape_nfl_game_lines
from db_operations.creators import Creator

config = dotenv_values(".env")


def scrape_live_store_historical_nfl_game_lines():
    url = 'https://sportsbook.draftkings.com/leagues/football/nfl'
    scrape_results = scrape_nfl_game_lines(url)

    creator = Creator(connection_url=config['DB_CONNECTION_URL'],
                      db_name=config['DB_NAME'],
                      collection_name=config['DB_COLLECTION_GAME_LINES'])
    live_result = creator.create_live_records(scrape_results)
    historical_result = creator.create_historical_records(destination_collection_name=
                                                          config['DB_COLLECTION_GAME_LINES_HISTORY'])


if __name__ == '__main__':
    scrape_live_store_historical_nfl_game_lines()
    pass
