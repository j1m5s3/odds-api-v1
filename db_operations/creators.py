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
            if result.acknowledged:
                print(f"Created records with ids: {result.inserted_ids}")
                return result.inserted_ids
        if type(records) is dict:
            result = self.db_handler.insert_one(records)
            if result.acknowledged:
                print(f"Created record with id: {result.inserted_id}")
                return result.inserted_id

    def create_historical_records(self, destination_collection_name):
        from_source_collection = self.db_handler
        to_destination_collection = self.client[self.db_name][destination_collection_name]

        # Find all records in the source collection
        from_records = from_source_collection.find()

        # Insert the records into the destination collection
        result = to_destination_collection.insert_many(from_records)
        if result.acknowledged:
            print(f"Created records with ids: {result.inserted_ids}")
            return result.inserted_ids

        return

