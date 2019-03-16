# encoding: utf-8

from lxml import etree

from session import SessionHelper


url_1 = 'https://www.champssports.com'


def crawl():
    session_helper = SessionHelper()
    session = session_helper.get_session()
    session.get(url_1)
    session_helper.print_cookies()



if __name__ == "__main__":
    crawl()
