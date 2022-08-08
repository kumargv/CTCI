import flask
import requests

#Method to request the specific post
def request(tag):
    URL = 'https://api.hatchways.io/assessment/blog/posts'
    URL += '?tag=' + tag
    response = requests.get(url=URL)
    return response.json()

#Method to request multiple tags and add them to the responses
def multiplerequests(cache, tag1, tag2):
    if not tag1:
        for item in tag2:
            if item['id'] not in cache:
                cache[item['id']] = item['id']
                tag1.append(item)
                return cache, tag1
    if not tag2:
        return cache, tag1

    for item in tag2:
        if item['id'] not in cache:
            cache[item['id']] = item['id']
            tag1.append(item)
    return cache, tag1

#Method to sort the responses
def sortrequest(results, sortBy, direction):
    if direction == "desc":
        results.sort(key=lambda x: x[sortBy], reverse=True)
    else:
        results.sort(key=lambda x: x[sortBy])
    return results

#Method to get the posts as per the API 
def getposts(cls, tags, sortBy='id', direction='asc'):
    responses = []
    cache = dict()
    splitTags = tags.split(',')

    for tag in splitTags:
        cache, responses = cls.multiplerequests(cache,responses,cls.request(tag)['posts'])

    responses = cls.sortrequest(responses, sortBy, direction)

    response = {}
    response["posts"] = responses
    return response

#Method to get check the validity of the request
def error_request (query):
    acceptSortFields = ['id', 'reads', 'likes', 'popularity']
    acceptDirectField = ['asc', 'desc']

    if 'tags' not in query:
        return {"error": "tags parameter is required"}, 400

    if 'sortBy' in query and query['sortBy'] not in acceptSortFields:
        return {"error": "sortBy parameter is invalid"}, 400

    if 'direction' in query and query['direction'] not in acceptDirectField:
        return {"error": "direction parameter is invalid"}, 400

    return True