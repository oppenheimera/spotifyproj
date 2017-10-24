from utils import get_auth_token
import spotipy

def get_profile_picture(username):
    token = get_auth_token(username, 'user-read-private')
    sp = spotipy.Spotify(auth=token)
    user_info = sp.user(username)
    profile_address = user_info['images'][0]['url']
    return profile_address

if __name__ == '__main__':
    print(get_profile_picture('ariopp'))