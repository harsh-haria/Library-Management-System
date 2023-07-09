from pymongo import MongoClient
import motor.motor_asyncio
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

conn = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
try:
    conn.admin.command("ping")
    print("You have successfully connected to MongoDB!")
except Exception as e:
    print(e)
