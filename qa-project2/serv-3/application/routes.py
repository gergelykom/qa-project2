from application import app
from flask import request, Response
import random


@app.route("/meal", methods=["GET"])
def get_meal():
    meals = [ 'paella', 'stir-fry', 'lasagne', 'korean style mapo tofu' ]
    meal = request.data.decode("utf-8")
    return Response(str(random.choice(meals)), mimetype = 'text/plain')
    


