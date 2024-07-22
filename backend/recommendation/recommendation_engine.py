from .music_data import load_music_data

def get_recommendations(user_data):
    # Kullanıcı verilerine göre öneriler oluşturma
    music_data = load_music_data()
    recommended_songs = [song for song in music_data if song['genre'] in user_data['favorite_genres']]
    return recommended_songs
