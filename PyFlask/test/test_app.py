import unittest
import app
import methods

class Test(unittest.TestCase):
    def testPing():
        response = app.apiApp.get('/api/ping')
        assert response.status_code == 200
        assert {"success": "true"} == response.get_json()

    def testPosts():
        response = app.apiApp.get('/api/posts?tags=history,tech')
        assert response.status_code == 200
        for item in response.get_getjson()['posts']:
            assert 'history' or 'tech' in item['tags']

    def testSortID():
        response = app.apiApp.get('/api/posts?tags=history,tech&sortBy=id')
        assert response.status_code == 200
        query = response.get_json()['posts']
        for i in range(len(query)-1):
            assert query[i]['id'] < query[i+1]['id']

    def testSortDirection():
        response = app.apiApp.get('/api/posts?tags=history,tech&sortBy=id&direction=desc')
        assert response.status_code == 200
        query = response.get_json()['posts']
        for i in range(len(query)-1):
            assert query[i]['id'] > query[i+1]['id']
