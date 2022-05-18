import flask  # Flask maps HTTP requests to Python functions.

app = flask.Flask(__name__)  # creates object
app.config['DEBUG'] = True  # starts debugger. If something goes wrong, error shows on browser

# Create some test data for our catalog in the form of a list of dictionaries.
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]


# here we are mapping URL path ('/') to home()
# only GET method is allowed to be used
@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of " \
           "science fiction novels.</p>"


@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return flask.jsonify(books)


@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in flask.request.args:
        id = int(flask.request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    for book in books:
        if id == book['id']:
            return flask.jsonify(book)  # since IDs are unique, only need to return one book.

    return "No such book found"


@app.route('/api/v1/resources/authors', methods=['GET'])
def app_author():
    if 'author' in flask.request.args:
        author = flask.request.args['author']
    else:
        return "Error: No author field provided. Please specify an author."

    results = []

    for book in books:
        if author == book['author']:
            results.append(book)

    if len(results) == 0:
        return "No such author found!"
    else:
        return flask.jsonify(results)


app.run()  # runs the application server
