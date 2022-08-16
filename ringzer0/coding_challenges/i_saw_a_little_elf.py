from tabnanny import check
import requests
import re
import base64
import hashlib

def get_data_from_url(url):
    text = requests.get(url).text
    elf_message = get_elf_message_from_text(text)
    checksum = get_checksum_from_text(text)
    return elf_message, checksum

def get_elf_message_from_text(text):
    text = re.split('BEGIN Elf Message -----<br />\s+', text)[1]
    return re.split('<br />', text)[0]

def get_checksum_from_text(text):
    text = re.split('----- BEGIN Checksum -----<br />\s+', text)[1]
    return re.split('<br />', text)[0]

def i_saw_a_little_elf():
    url = 'http://challenges.ringzer0team.com:10015/'
    elf_message, checksum = get_data_from_url(url)
    # When you examine the elf message, you can see that its a base64 encoding
    # (mix of uppercase, lowercase and often ends with a '=' bc of padding)
    decoded_elf_message = base64.b64decode(elf_message)
    # reverse the elf message
    hash = hashlib.md5(decoded_elf_message).hexdigest()
    print(hash, checksum)

i_saw_a_little_elf()