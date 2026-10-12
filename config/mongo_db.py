import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

def get_mongo_collection(collection_name="feedback"):
    """Establishes and returns a MongoDB collection reference."""
    try:
        mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
        client = MongoClient(mongo_uri)
        db = client[os.getenv("MONGO_DB_NAME", "online_course_db")]
        return db[collection_name]
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        return None