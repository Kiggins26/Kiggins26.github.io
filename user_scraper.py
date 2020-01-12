from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import re

def output(s):
    with open('test.html', 'w') as f: f.write(s)

def sget(url):
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        print('Error during requests to {0} : {1}'.format(url, str(e)))
        return None

def is_good_response(resp):
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)

def search_by_tag(tag, mx=50):
    rhtml = str(sget('https://www.instagram.com/explore/tags/{}/'.format(tag)))
    matches = re.compile('"shortcode":"[a-zA-Z1-9]*"').findall(rhtml)
    # print('https://www.instagram.com/explore/tags/{}/'.format(tag))
    res = [match[13:-1] for match in matches]
    return res

def get_user_by_post(id):
    # print('id=' + id)
    rhtml = str(sget('https://www.instagram.com/p/{}/'.format(id)))
    # output(BeautifulSoup(rhtml).prettify())
    matches = re.compile(r'\(@[a-zA-Z1-9\.]+\)').search(rhtml)
    if matches:
        return matches[0][2:-1]
    else:
        return None
    # url = 'https://www.instagram.com/' + user

def get_users_by_tag(tag, mx=50):
    return [get_user_by_post(id) for id in search_by_tag(tag, mx)]

print(get_users_by_tag('basketball'))
