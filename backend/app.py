from flask import Flask, request, jsonify
from recommendation.api import get_recommendations, get_user_profile, update_user_profile

app = Flask(__name__)

@app.route('/recommendations', methods=['POST'])
def recommendations():
    user_data = request.json
    recommendations = get_recommendations(user_data)
    return jsonify(recommendations)

@app.route('/user-profile/<user_id>', methods=['GET'])
def user_profile(user_id):
    profile = get_user_profile(user_id)
    return jsonify(profile)

@app.route('/user-profile/<user_id>', methods=['PUT'])
def update_profile(user_id):
    profile_data = request.json
    update_user_profile(user_id, profile_data)
    return jsonify({'status': 'Profile updated'})

if __name__ == '__main__':
    app.run(debug=True)
