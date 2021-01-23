from application import app
from flask import request, Response
import random


@app.route("/qran", methods=["GET"])
def get_qran():
    qrans = [ '80' , '800' , '1600' , '2400' , '3200' , '4000']
    return Response(str(random.choice(qrans)), mimetype = 'text/plain')