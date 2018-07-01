import asyncio
import uvloop
import sys
import os
import pydf
import pystache

from sanic import Sanic
from sanic import response
from sanic_cors import CORS, cross_origin
from .nn import recognize

def get_root():
  if getattr(sys, 'frozen', False):
    return os.path.dirname(sys.executable)
  elif __file__:
    return os.path.abspath(os.path.dirname(__file__))


root = get_root()

db = Db(config)

asyncio.set_event_loop(uvloop.new_event_loop())

app = Sanic()
CORS(app, automatic_options=True)


@app.route('/rec', methods=['POST'])
async def recognize_image(request):
    image_file = request.files.get('image')

    # recognize

    file_parameters = {
        'body': image_file.body,
        'name': image_file.name,
        'type': image_file.type,
    }

    return json({ "received": True, "file_names": request.files.keys(), "test_file_parameters": file_parameters })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)