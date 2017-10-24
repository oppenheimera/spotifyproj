from json import loads
import spotipy
import spotipy.util as util

def get_auth_token(username, scope):
    """
    :param username: pretty damn obvious what this one is
    :param scope: the scope of the request
    Returns a token.
    Currently, this also depends on having a hidden JSON file with the 
    proper client_id and client_secret stored in it.
    """
    d = loads(open('.client.json').read())
    CLIENT_ID = d['client_id']
    CLIENT_SECRET = d['client_secret']
    REDIRECT_URI = 'http://localhost:8888/callback'
    token = util.prompt_for_user_token(username, scope, client_id=CLIENT_ID,
                                client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI)
    return token
    
def get_top_n(user, n, term='short_term'):
    """
    :param user: the user whose amazing music you want to know about
    :param n: the number of top songs that you want to see
    :param term: the term that you want to access. Appropriate parameters 
    are: 'short_term', 'medium_term', or 'long_term'
    TODO: make this write JSON to a DB associating a user with their top songs.
    """
    token = get_auth_token(user, 'user-top-read')
    ans = dict()
    if token:
        sp = spotipy.Spotify(auth=token)
        sp.trace =  False
        results = sp.current_user_top_tracks(time_range=term, limit=n)
        for i, item in enumerate(results['items']):
            song = item['name']
            artist = item['artists'][0]['name']
            ans[i] = [song, artist]
        return ans
    else:
        return ("Can't get token for " + user)

def get_profile_picture(username):
    """
    Returns a web address pointing to the users spotify
    profile photo.
    """
    token = get_auth_token(username, 'user-read-private')
    sp = spotipy.Spotify(auth=token)
    user_info = sp.user(username)
    profile_address = user_info['images'][0]['url']
    return profile_address
