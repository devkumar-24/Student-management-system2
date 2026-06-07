from pymongo import MongoClient

MONGO_URI = "mongodb+srv://devkumar:dev89866@cluster0.kgk4tx3.mongodb.net/?appName=Cluster0"

client = MongoClient("mongodb+srv://devkumar:dev89866@cluster0.kgk4tx3.mongodb.net/?appName=Cluster0")

db = client["student_management"]

students = db["students"]
attendance = db["attendance"]
marks = db["marks"]
users = db["users"]
