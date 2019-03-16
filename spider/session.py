# encoding: utf-8

import requests


user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'


class SessionHelper(object):
    
    def __init__(self):
        self.__session = requests.Session()
        self.__init_session()

    def __init_session(self):
        self.__session.headers.update({
            'User-Agent': user_agent
        })

    def get_session(self):
        return self.__session

    def print_cookies(self):
        for cookie in self.__session.cookies:
            print(cookie)

if __name__ == "__main__":
    session_helper = SessionHelper()
    session_helper.get_session()
    session_helper.print_cookies()
