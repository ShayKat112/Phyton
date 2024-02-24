import requests

def scan_file(file_path):
    url = 'https://www.virustotal.com/vtapi/v2/file/scan'
    params = {'apikey' : API_KEY}

    with open(file_path, 'rb') as file:
        files = {'file': file}
        response = requests.post(url, files= files, params=params)










file_path = ""