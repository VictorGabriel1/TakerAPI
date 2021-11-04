from flask import Flask
from flask_restful import Resource, Api, reqparse
import werkzeug
from taker import taker
import datetime

app = Flask(__name__,static_folder="output")
api = Api(app)

class UploadImage(Resource):
   def post(self):
     parse = reqparse.RequestParser()
     parse.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')
     args = parse.parse_args()

     print(args)
    # image_file = args['file']
    # image_file.save(f"images/{datetime()}.jpg")

    #  response = roda_o_codigo()
    #  return response
    #  return {'image_url': 'kajdfhkajhfkshf.jpg', "total": 15}

taker("images/Bob2.png", True)

api.add_resource(UploadImage, '/images/saida.png')

if __name__ == '__main__':
    app.run(debug=True)
    
