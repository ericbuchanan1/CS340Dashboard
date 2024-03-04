from pymongo import MongoClient
from bson.objectid import ObjectId


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, USER, PASS):
        # Connection Variable
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31720
        DB = 'AAC'
        COL = 'animals'

        # Initialize Connection
        self.client = MongoClient('mongodb://%s:%s@%s:%d' %
                                  (USER, PASS, HOST, PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

    def create(self, data):
        """Insert a new document into the collection."""
        if data is not None:
            self.database.animals.insert_one(data)
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    def read(self, query):
        """Query for documents matching the specified criteria."""
        try:
            documents_cursor = self.collection.find(
                query)  # Use find to retrieve documents
            documents = list(documents_cursor)  # Convert cursor to list
            # Return the documents list or empty list if no documents found
            return documents if documents else []
        except Exception as e:
            print(f"Query failed: {e}")
            return []  # Return an empty list in case of error

    def update(self, query, data):
        """ Update documents matching specified criteria. """
        try:
            result = self.collection.update_many(query, {'$set': data})
            return result.modified_count
        except Exception as e:
            print(f"Update failed: {e}")
            return[]

    def delete(self, query):
        """Delete documents matching specified criteria."""
        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except Exception as e:
            print(f"Delete failed: {e}")
            return[]
