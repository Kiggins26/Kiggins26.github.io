from requests import get
from requests.exceptions import RequestException
from contextlib import closing
# from bs4 import BeautifulSoup
import re

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

def search_by_tag(tag, max=50):
    rhtml = str(sget('https://www.instagram.com/explore/tags/{}/'.format(tag)))
    matches = re.compile('"shortcode":"[a-zA-Z1-9]*"').findall(rhtml)
    res = ["https://www.instagram.com/p/" + match[13:-1] for match in matches][:max]
    return res

print(search_by_tag('basketball'))