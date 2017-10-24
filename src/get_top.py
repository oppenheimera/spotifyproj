import spotipy
import spotipy.util as util
from json import loads
from sys import argv

"""
Currently, this is a command line utility that prints my
top n songs, tab indented, for any three "terms" (long-term, medium-term, 
or short-term) to stdout. If no term is specified, it defaults to short-term.

USAGE:
$ python3.x get_top.py long_term 1
range: long_term
    LITE SPOTS, KAYTRANADA
$ python3.x get_top.py 2
range: short_term
    Crew, GoldLink
    Navajo, Masego
"""

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

    if token:
        sp = spotipy.Spotify(auth=token)
        sp.trace =  False
        print("range:", term)
        results = sp.current_user_top_tracks(time_range=term, limit=n)
        for i, item in enumerate(results['items']):
            song = item['name']
            artist = item['artists'][0]['name']
            print("\t{}, {}".format(song, artist))
    else:
        print("Can't get token for " + user)


if __name__ == "__main__":
    print(get_auth_token('ariopp', 'user-top-read'))
    n = int(argv[-1])
    if len(argv) == 3:
        term = argv[-2]
        get_top_n('ariopp', n, term)
    else:
        get_top_n('ariopp', n)
