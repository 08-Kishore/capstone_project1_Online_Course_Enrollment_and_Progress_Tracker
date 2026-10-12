import os
import json
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables (optional if you use a .env file for your URI)
load_dotenv()

def seed_mongo_feedback():
    # 1. Connect to MongoDB (local instance by default)
    mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
    client = MongoClient(mongo_uri)
    
    # Select database and collection
    db = client["online_course_db"]
    collection = db["feedback"]
    
    # 2. Clear existing feedback collection to prevent duplication on re-runs (optional)
    collection.delete_many({})
    print("Cleared existing feedback collection.")

    # 3. Load feedback data from the data folder JSON file
    json_file_path = os.path.join("data", "feedback.json")
    
    if not os.path.exists(json_file_path):
        print(f"Error: Could not find {json_file_path}. Make sure your data folder is set up correctly.")
        return

    with open(json_file_path, "r", encoding="utf-8") as file:
        feedback_data = json.load(file)

    # 4. Insert documents into MongoDB
    if feedback_data:
        # Optional: Convert string dates to ISODate format if needed
        for doc in feedback_data:
            if "review_date" in doc and isinstance(doc["review_date"], str):
                from datetime import datetime
                doc["review_date"] = datetime.fromisoformat(doc["review_date"].replace("Z", "+00:00"))

        result = collection.insert_many(feedback_data)
        print(f"Successfully inserted {len(result.inserted_ids)} feedback documents into MongoDB!")

    # 5. Create indexes for fast searching by student or course
    print("Creating MongoDB indexes...")
    collection.create_index([("course_id", 1)])
    collection.create_index([("student_id", 1)])
    collection.create_index([("course_id", 1), ("rating", -1)])
    
    print("MongoDB indexing complete!")

if __name__ == "__main__":
    seed_mongo_feedback()