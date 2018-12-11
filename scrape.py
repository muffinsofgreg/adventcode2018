from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup


def simple_get(url, cookie):
    """
    Attempts to get the content at 'url' by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return it,
    otherwise return None.
    """
    try:
        with closing(get(url, cookies=cookie, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None
    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Return True is the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()

    return (resp.status_code == 200
            and content_type is not None
            and (content_type.find('html') > -1
                 or content_type.find('text/plain') > -1)
            )


def log_error(e):
    """
    It is always a good idea to log errors.
    This function just prints them, but you can make it do anything
    """
    print(e)
