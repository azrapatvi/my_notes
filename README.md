# Notes App - FastAPI & MongoDB

This is a simple Notes application built with **FastAPI**, **MongoDB**, and **Jinja2 templates**.  
It allows users to **add**, **view**, and **delete** notes using a web interface.

# Features
- Add new notes with a title and description.
- View all notes in a structured table.
- Delete notes individually.
- User-friendly messages for success and errors.

# Environment Variables
Create a `.env` file in the project root with the following variables:

```bash
MONGO_URI=<your-mongodb-connection-string>
SECRET_KEY=<your-secret-key>
```
note:Make sure not to push the .env file to GitHub.

# Usage
# Start the FastAPI server
uvicorn main:app --reload

# Open your browser at
```
http://127.0.0.1:8000/
```

Add notes on the home page.
View and delete notes on the /notes page.

# Technologies Used
```
FastAPI          # Python web framework
MongoDB          # NoSQL database
Jinja2           # HTML templating engine
python-dotenv    # Load environment variables
bson             # ObjectId handling for MongoDB
```
# Project Structure
```
.
├── main.py             # FastAPI application
├── templates/          # HTML templates
│   ├── index.html      # Home page (add notes)
│   └── show.html       # Notes listing page
├── static/             # Static files (CSS/JS if any)
├── .env                # Environment variables (MONGO_URI, SECRET_KEY)
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```


