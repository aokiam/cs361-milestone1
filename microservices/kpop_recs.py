# this will give a user a kpop recommendation based on their jpop likes
from flask import Flask, request, jsonify
import json 

app = Flask(__name__)

def load_data():
    with open('data/artist_info.json') as f:
        return json.load(f)
    
# endpoint to recommend kpop artists
@app.route('/recommend_kpop', methods=['GET'])
def recommend_kpop():
    # get names of kpop artist from the request
    jpop_artist = request.args.get('jpop_artist')
    data = load_data()

    # find kpop artist in the json and get their attributes
    for artist in data['artists']:
        if artist['pop'] == 'j-pop' and artist['name'] == jpop_artist:
            # find kpop artist with at least one matching attribute
            matching_kpop = [
                kpop for kpop in data['artists']
                if kpop['pop'] == 'k-pop' and set(artist['attributes']).intersection(kpop['attributes'])
            ]
            if matching_kpop:
                return jsonify(matching_kpop)
            else:
                return jsonify({"message": "J-pop artist not found."})


if __name__ == '__main__':
    app.run(port=5002)
