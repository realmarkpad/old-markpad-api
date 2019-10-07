import motor.motor_asyncio
from app.config import MONGO_URI, MONGO_DATABASE_NAME

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db = client[MONGO_DATABASE_NAME]
