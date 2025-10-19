from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient
from bson import ObjectId
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()


# Jinja2 templates folder
templates = Jinja2Templates(directory="templates")

MONGO_URI = os.getenv("MONGO_URI")
SECRET_KEY = os.getenv("SECRET_KEY")

# MongoDB connection
client = MongoClient(MONGO_URI)
db = client["mynotes"]
collection = db["notes"]

# Home page - show form
@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": ""})

# Form submission
@app.post("/submit", response_class=HTMLResponse)
async def submit(request: Request, title: str = Form(...), description: str = Form(...)):
    try:
        collection.insert_one({"title": title, "description": description})
        message = "✅ Note has been added successfully!"
        category = "success"
    except Exception as e:
        print("Error:", e)
        message = "❌ Failed to add note. Please try again!"
        category = "danger"

    return templates.TemplateResponse("index.html", {"request": request, "message": message, "category": category})

@app.get("/notes", response_class=HTMLResponse)
def show(request: Request):
    result = list(collection.find())
    for doc in result:
        doc["_id"] = str(doc["_id"])
    return templates.TemplateResponse("show.html", {"request": request, "result": result})

@app.post("/do", response_class=HTMLResponse)
def do(request: Request, id: str = Form(...)):
    result = collection.delete_one({"_id": ObjectId(id)})
    
    if result.deleted_count > 0:
        message = "✅ Note has been deleted successfully!"
        category="success"
    else:
        message = "❌ Failed to delete note. Please try again!"
        category="danger"

    # Fetch updated notes list
    updated = list(collection.find())
    for doc in updated:
        doc["_id"] = str(doc["_id"])

    return templates.TemplateResponse(
        "show.html",
        {"request": request, "result": updated, "message": message,"category":category}
    )
