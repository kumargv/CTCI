import flask 
from methods import getposts, error_request

apiApp = flask.Flask(__name__)

@apiApp.route('/', methods=['GET'])
def home():
    return "<h1>This is an API app<h1>"

@apiApp.route('/api/ping', methods=['GET'])
def apiPing():
    return {"success":"true"}, 200

@apiApp.route('/api/posts', methods=['GET'])
def apiPosts():
    queries = flask.request.args

    validate = error_request(queries)
    if validate is not True:
        return validate[0], validate[1]

    sortBy = 'id'
    direction = 'asc'

    if 'sortBy' in queries:
        sortBy = queries['sortBy']
    if 'direction' in queries:
        direction = queries['direction']

    return getposts(queries['tags'], sortBy, direction)

apiApp.run(port=5000, debug=True)