import requests
import re
import base64
import hashlib
import subprocess
import os

DIR_PATH = os.path.dirname(os.path.realpath(__file__))

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

def get_flag_from_url(url):
    text = requests.get(url).text
    text = text.split('<div class="alert alert-info">')[1]
    return text.split('</div>')[0]

def i_saw_a_little_elf():
    print(os.path.dirname(os.path.realpath(__file__)))
    url = 'http://challenges.ringzer0team.com:10015/'
    elf, checksum = get_data_from_url(url)
    elf_md5 = None
    # msg is encrypted multiple times

    while checksum != elf_md5:
        try:
            elf = base64.b64decode(elf)
            elf_md5 = hashlib.md5(elf[::-1]).hexdigest()
        except Exception:
            break

    # decoded elf message is reversed
    elf = elf[::-1]

    # with open(f'{DIR_PATH}/file', 'wb') as file:
    #     file.write(elf)
    # assert os.path.isfile(f'{DIR_PATH}/file')
    # secret_message = subprocess.run(f'{DIR_PATH}/file', capture_output=True).decode('utf-8').strip()
    # print(secret_message)
    
    # secret_message = (elf[0x5e6:0x5ea]).decode('utf-8')+(elf[0x5ee:0x5f0]).decode('utf-8')

    # print(secret_message)
    # url_send = url + '?r=' + secret_message
    # flag = get_flag_from_url(url_send)
    # return flag

if __name__ == '__main__':
    print(i_saw_a_little_elf())