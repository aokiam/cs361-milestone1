# this will display a given artist's information
from flask import Flask, jsonify, request
import json

app = Flask(__name__)
app.config["DEBUG"] = True

# load artist info when app starts
with open('data/artist_info.json') as f:
    artist_data = json.load(f)

def filter_artist_info(artist_name):
    for artist in artist_data["artists"]:
        if artist["name"] == artist_name:
            return{
                "name": artist["name"],
                "pop": artist["pop"],
                "genres": artist["genres"],
                "years_active": artist["years_active"],
                "members": artist["members"],
                "company": artist["company"],
                "recommendations": artist["recommendations"],
                "top3": artist["top3"],
                "learn_more": artist["learn_more"]
            }
    return None

@app.route('/artist_details', methods=['GET'])
def artist_details():
    artist_name = request.args.get('artist')
    if not artist_name:
        return jsonify({"error": "No artist specified"}), 400
    
    artist_info = filter_artist_info(artist_name)
    if not artist_info:
        return jsonify({"error": "Artist not found"}), 400
    
    return jsonify(artist_info), 200

if __name__ == '__main__':
    app.run(port=5004)
