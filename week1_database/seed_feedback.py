import os
import json
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

def seed_mongo_feedback():
    client = MongoClient(os.getenv("MONGO_URI", "mongodb://localhost:27017/"))
    db = client["online_course_db"]
    collection = db["feedback"]
    
    collection.delete_many({})
    
    with open(os.path.join("data", "feedback.json"), "r", encoding="utf-8") as file:
        feedback_data = json.load(file)
        
    if feedback_data:
        collection.insert_many(feedback_data)
        print(f"Successfully inserted {len(feedback_data)} feedback docs into MongoDB!")

    collection.create_index([("course_id", 1)])
    collection.create_index([("student_id", 1)])
    print("MongoDB indexes created successfully.")

if __name__ == "__main__":
    seed_mongo_feedback()