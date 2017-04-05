from mastodon import Mastodon
from generate import generate

import sys

def load_lemmas():
    verbs = dict()
    verbs['say'] = [x.strip() for x in open("say_lemmas.txt").readlines()]
    verbs['eat'] = [x.strip() for x in open("eat_lemmas.txt").readlines()]
    verbs['save'] = [x.strip() for x in open("save_lemmas.txt").readlines()]
    verbs['forgive'] = [x.strip() for x in
            open("forgive_lemmas.txt").readlines()]
    return verbs

def main():
    import sys
    client_id, client_secret, access_token = sys.argv[1:]
    api = Mastodon(client_id, client_secret, access_token,
            api_base_url="https://botsin.space")
    status = api.toot(generate(load_lemmas()))
    print "posted status", status['url']

if __name__ == '__main__':
    main()

