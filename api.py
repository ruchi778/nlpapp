import paralleldots
paralleldots.set_api_key('usrYigdA9Ak7Ar89TaUrD5iX9S9cOjtL01RXprNUNSA')


def ner(text):

    ner = paralleldots.ner(text)
    return ner