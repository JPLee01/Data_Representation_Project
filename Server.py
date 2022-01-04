#Data Representation - Project
#John Paul Lee - G00387906
#Lecturer - Andrew Beatty
#Code is adapted from code generated through lectures through the semester

#Import required modules
from ElectronicDAO import electronicDAO

from flask import Flask, url_for, request, redirect, abort, jsonify

app = Flask(__name__, static_url_path='', static_folder='staticpages')


#@app.route('/')
#def index():
    # Return message to shoe the server is working
    # return  "Welcome. The server is working" 

    

# getAll 
# curl http://127.0.0.1:5000/electronic

@app.route('/electronic') # works
def getAll():
   return jsonify(electronicDAO.getAll())

# findById
# curl http://127.0.0.1:5000/electronic/XX

@app.route('/electronic/<int:electronic_id>') # works
def findById(electronic_id): 
    return jsonify(electronicDAO.findById(electronic_id))

# create
# curl -X POST -d "{\"electronic_make\":\"Apple\", \"electronic_model\": \"iPad\",\"electronic_price\": 350.00}" -H Content-Type:application/json http://127.0.0.1:5000/electronic
# curl http://127.0.0.1:5000/electronic

@app.route('/electronic', methods=['POST']) # works
def create(): 
    if not request.json: 
        #Abort the request if it is not in the correct json format
        print("WRONG!")
        abort(400)
    #If it is correct request do this
    item = { 
        "electronic_make": request.json["electronic_make"],
        "electronic_model": request.json["electronic_model"],
        "electronic_price": request.json["electronic_price"]
    }
    return jsonify(electronicDAO.create(item))


# update
# curl -X PUT -d "{\"electronic_make\":\"Apple\", \"electronic_model\": \"Macbook Pro\",\"electronic_price\": 4000.00}" -H Content-Type:application/json http://127.0.0.1:5000/electronic/XX

@app.route('/electronic/<int:electronic_id>', methods=['PUT'])
def update(electronic_id):
    foundItem = electronicDAO.findById(electronic_id)
    print(foundItem)
    if foundItem == {}:
        return jsonify({}), 404
    currentItem = foundItem
    if 'electronic_make' in request.json:
        currentItem['electronic_make'] = request.json['electronic_make']
    if 'electronic_model' in request.json:
        currentItem['electronic_model'] = request.json['electronic_model']
    if 'electronic_price' in request.json:
        currentItem['electronic_price'] = request.json['electronic_price']
    electronicDAO.update(currentItem)
    return jsonify(currentItem)

# delete
# curl -X DELETE http://127.0.0.1:5000/electronic/XX

@app.route('/electronic/<int:electronic_id>', methods=['DELETE'])
def delete(electronic_id):
    electronicDAO.delete(electronic_id)
    return jsonify({"Done":True})




if __name__ == "__main__":
    app.run(debug=True)

