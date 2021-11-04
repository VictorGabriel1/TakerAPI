from flask import Flask

from flask_restful import Resource, Api, reqparse
import werkzeug
from taker import taker
import datetime

app = Flask(__name__, static_folder="images")
api = Api(app)


class UploadImage(Resource):
    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')
        args = parse.parse_args()

        print(args)
        image_file = args['file']
        print('image_file')
        print(image_file)
        image_file.save(f"images/inputs/nova.jpg")
        response = taker("images/inputs/nova.jpg", True)
        print(response)
       
        return response
    #  response = roda_o_codigo()
    #  return response
    #  return {'image_url': 'kajdfhkajhfkshf.jpg', "total": 15}




api.add_resource(UploadImage, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
