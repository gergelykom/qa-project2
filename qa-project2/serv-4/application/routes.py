from application import app
from flask import render_template
from flask import request, Response
import json

@app.route("/whatudone", methods=["POST", "GET"])
def whatudone():
    get_meal = request.json['meal']
    get_qran = int(request.json['qran'])
    

    if get_qran < 2000 and get_meal == 'paella':
        whatudone = "You will make siesta mandatory!"
    elif 2000 <= get_qran and get_meal == 'paella':
        whatudone = "You will cause the moon to leave Earth's orbit!"

    elif get_qran < 2000 and get_meal == 'stir-fry':
        whatudone = "You just started a chain of events where a goose will be elected as president of the United States!"
    elif 2000 <= get_qran and get_meal == 'stir-fry':
        whatudone = "You will make world-peace happen!"

    elif get_qran < 2000 and get_meal == 'lasagne':
        whatudone = "You will cause a massive (literal) headache for someone!"
    elif 2000 <= get_qran and get_meal == 'lasagne':
        whatudone = "Your meal will cause turnips to rise and enslave humanity!"

    elif get_qran < 2000 and get_meal == 'korean style mapo tofu':
        whatudone = "You will cause number 11 to be removed!"
    elif 2000 <= get_qran and get_meal == 'korean style mapo tofu':
        whatudone = "Your actions will cut infinity into half!"
    
    return Response(str(whatudone), mimetype = 'text/plain')