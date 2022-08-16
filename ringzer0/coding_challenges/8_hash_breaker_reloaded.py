import itertools
import requests
import re
import hashlib

def get_data_from_url(url):
    text = requests.get(url).text
    hash = get_hash_from_text(text)
    salt = get_salt_from_text(text)
    return hash, salt

def get_hash_from_text(text):
    text = re.split('BEGIN HASH -----<br />\s+', text)[1]
    return re.split('<br />', text)[0]

def get_salt_from_text(text):
    text = re.split('BEGIN SALT -----<br />\s+', text)[1]
    return re.split('<br />', text)[0]

def get_flag_from_url(url):
    text = requests.get(url).text
    text = text.split('<div class="alert alert-info">')[1]
    return text.split('</div>')[0]

def hash_breaker():
    url = 'http://challenges.ringzer0team.com:10057/'
    hash, salt = get_data_from_url(url)

    # len(hash) == 40, so most likely a sha-1 hash
    for i in itertools.count(0):
        if hash == hashlib.sha1(str(i).encode('utf-8')+salt.encode('utf-8')).hexdigest():
            break
    message = str(i)
    url_send = 'http://challenges.ringzer0team.com:10057/?r=' + message
    flag = get_flag_from_url(url_send)
    return flag



if __name__ == '__main__':
    print(hash_breaker())