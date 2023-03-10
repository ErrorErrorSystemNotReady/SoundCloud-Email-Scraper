import requests
import random
import time
import datetime
import json
import hashlib
from bs4 import BeautifulSoup

# Load hashtags from file
with open('hashtags.txt', 'r') as f:
    hashtags = [line.strip() for line in f]

# Load proxies from file
with open('proxies.txt', 'r') as f:
    proxies = [line.strip() for line in f]

# Define headers
headers = {
    'User-Agent': None,
    'Referer': None,
    'Accept-Language': None,
    'Cookie': None
}

# Define function to generate random user agent
def get_random_user_agent():
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    ]
    return random.choice(user_agents)

# Define function to generate random referer
def get_random_referer():
    referers = [
        'https://www.google.com/',
        'https://www.youtube.com/',
        'https://www.facebook.com/'
    ]
    return random.choice(referers)

# Define function to generate random language
def get_random_language():
    languages = [
        'en-US',
        'en-GB',
        'fr-FR',
        'de-DE',
        'es-ES',
        'it-IT'
    ]
    return random.choice(languages)

# Define function to generate random cookie
def get_random_cookie():
    cookies = [
        {'name': 'user_id', 'value': hashlib.sha256(str(random.random()).encode()).hexdigest()},
        {'name': 'session_id', 'value': hashlib.sha256(str(random.random()).encode()).hexdigest()}
    ]
    return json.dumps(random.choice(cookies))

# Define function to generate random delay time
def get_random_delay_time():
    return random.uniform(5, 10)

# Define function to check if proxy is working
def check_proxy(proxy):
    try:
        response = requests.get('https://www.soundcloud.com/', headers=headers, proxies={'https': proxy}, timeout=10)
        if response.status_code == 200:
            return True
        else:
            return False
    except:
        return False

# Define function to get list of working proxies
def get_working_proxies(proxies):
    working_proxies = []
    for proxy in proxies:
        if check_proxy(proxy):
            working_proxies.append(proxy)
    return working_proxies

# Get list of working proxies
working_proxies = get_working_proxies(proxies)

# Loop through hashtags
for hashtag in hashtags:

    # Define URL to search for hashtag
    url = f'https://www.soundcloud.com/search?q=%23{hashtag}&sc_src=auto_search_box&query_urn=soundcloud%3Asearch-autocomplete'

    # Make request to URL with random user agent, referer, language, and cookie
    headers['User-Agent'] = get_random_user_agent()
    headers['Referer'] = get_random_referer()
    headers['Accept-Language'] = get_random_language()
    headers['Cookie'] = get_random_cookie()
    
    # Use a random
    # Make request to URL with random user agent, referer, language, and cookie
    headers['User-Agent'] = get_random_user_agent()
    headers['Referer'] = get_random_referer()
    headers['Accept-Language'] = get_random_language()
    headers['Cookie'] = get_random_cookie()

    # Make request with a random working proxy
    if working_proxies:
        proxy = random.choice(working_proxies)
        response = requests.get(url, headers=headers, proxies={'https': proxy})
    else:
        response = requests.get(url, headers=headers)

    # Parse response with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all track titles and print them
    tracks = soup.find_all('a', {'class': 'trackItem__trackTitle sc-link-dark'})
    for track in tracks:
        print(track.text)

    # Wait for a random amount of time before making next request
    time.sleep(get_random_delay_time())
