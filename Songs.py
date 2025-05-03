import pandas as pd

# Sample dataset (you can load this from a CSV file)
data = {
    'user_id': [1, 1, 1, 2, 2, 3, 3, 3],
    'song_id': [101, 102, 103, 101, 104, 105, 102, 106],
    'song_name': ['Shape of You', 'Blinding Lights', 'Levitating', 'Shape of You', 'Take On Me', 'Imagine', 'Blinding Lights', 'Bohemian Rhapsody'],
    'genre': ['Pop', 'Pop', 'Pop', 'Pop', 'Rock', 'Rock', 'Pop', 'Rock'],
    'play_count': [30, 20, 15, 50, 25, 35, 10, 40]
}

df = pd.DataFrame(data)

# Function to generate a personalized playlist for a given user
def generate_playlist(user_id, df):
    # Filter the songs listened by the user
    user_data = df[df['user_id'] == user_id]
    
    # Get the genres the user listens to
    preferred_genres = user_data['genre'].value_counts().index.tolist()
    
    # Recommend songs from those genres that the user hasn't listened to yet
    recommended_songs = df[~df['song_id'].isin(user_data['song_id']) & df['genre'].isin(preferred_genres)]
    
    # Sort recommended songs by play_count (most popular songs first)
    recommended_songs = recommended_songs.sort_values(by='play_count', ascending=False)
    
    return recommended_songs[['song_name', 'genre', 'play_count']]

# Generate a playlist for user 1
playlist_user_1 = generate_playlist(user_id=1, df=df)
print("Recommended Playlist for User 1:")
print(playlist_user_1)
