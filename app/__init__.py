import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

work_experiences = [
    {"title": "Job Title 1", "company": "Company Name 1", "duration": "Start Date - End Date", "description": "Description of the job and your responsibilities."},
    {"title": "Job Title 2", "company": "Company Name 2", "duration": "Start Date - End Date", "description": "Description of the job and your responsibilities."}
]
hobbies = [
    {"image": "img/hobby1.jpg", "description": "Hobby 1 description."},
    {"image": "img/hobby2.jpg", "description": "Hobby 2 description."}
]
education = [
    {"degree": "Degree Name 1", "institution": "Institution Name 1", "duration": "Start Date - End Date", "description": "Description of the program and any notable achievements."},
    {"degree": "Degree Name 2", "institution": "Wiconsin Name 2", "duration": "Start Date - End Date", "description": "Description of the program and any notable achievements."}
]



@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"), work_experiences=work_experiences, hobbies=hobbies, education=education)


@app.route('/hobbies')
def hobbies_page():
    return render_template('hobbies.html', title="Hobbies", hobbies=hobbies)

def get_menu_items():
    return [
        {"name": "Home", "url": "/"},
        {"name": "Hobbies", "url": "/hobbies"}
    ]

@app.context_processor
def inject_menu():
    return dict(menu_items=get_menu_items())
