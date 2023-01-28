from pymongo import MongoClient


class Creator:
    def __init__(self, connection_url, db_name, collection_name):
        self.client = MongoClient(connection_url)
        self.db_name = db_name
        self.collection_name = collection_name

        self.db_handler = self.client[self.db_name][self.collection_name]

    def create_live_records(self, records):
        # TEMPORARY ############
        self.db_handler.drop()
        ########################

        if type(records) is list:
            result = self.db_handler.insert_many(records)
            return result
        if type(records) is dict:
            result = self.db_handler.insert_one(records)
            return result

    def create_historical_records(self, destination_collection_name):
        pass

