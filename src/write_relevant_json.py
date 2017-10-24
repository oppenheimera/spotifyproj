import json
from utils import get_top_n, get_profile_picture

def write(username, top_n, span, filename):
    topsongs = get_top_n(username, top_n, span)
    photo = get_profile_picture(username)
    results = {"top_songs": topsongs, "profile_photo": photo}
    with open(filename, 'w') as f:
        json.dump(results, f)
        f.close()

if __name__ == '__main__':
    write('ariopp', 5, 'short_term', 'ari.json')