import logging
from motor.motor_asyncio import AsyncIOMotorClient
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

client: AsyncIOMotorClient = None

def startup_db_client():
    global client
    try:
        mongo_uri = os.getenv('MONGO_URL')
        client = AsyncIOMotorClient(mongo_uri)
        logging.info("Connected to MongoDB successfully.")
    except Exception as e:
        logging.error(f"Failed to connect to MongoDB: {e}")
    return client['fast-api']

def shutdown_db_client():
    client.close()
    logging.info("MongoDB connection closed.")

def get_database():
    return startup_db_client()
