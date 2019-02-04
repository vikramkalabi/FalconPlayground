import json

import falcon


class Sample:

    def on_get(self, request, response):
        response.status = falcon.HTTP_200
        response.body = json.dumps({
            'message': 'Falcon is flying high'
        })


app = falcon.API()
app.add_route('/sample', Sample())
