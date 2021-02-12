from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from replit import db
from goodreadsScrape import get_books

app = Flask('app')

# Support for special characters like accents
app.config['JSON_AS_ASCII'] = False

# CORS Support
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@cross_origin()
def index():
  if 'year' in request.args:
    year = request.args['year']
    
    return jsonify(db[year])
	
  else: 
    return 'This is my personal books API. Written by Alex Reyes for use in www.alexreyes.xyz. Please request a specific year. For example: /?year=2021'

@app.route('/', methods=["POST"])
def update_list(): 
  if 'year' in request.args:
    year = request.args['year']

    bookList = get_books(year)

    bookResult = []

    for book in bookList: 
      title = book[0]
      link = book[1]

      individualBook = [title, link]

      bookResult.append(individualBook)
    
    db[year] = bookResult

    return jsonify(bookList)
  else: 
    return 'SPECIFY YEAR'

app.run(host='0.0.0.0', port=8080)