user_profiles = {}

def get_user_profile(user_id):
    return user_profiles.get(user_id, {'favorite_genres': []})

def update_user_profile(user_id, profile_data):
    user_profiles[user_id] = profile_data
