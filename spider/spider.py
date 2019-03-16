# encoding: utf-8

from lxml import etree

from session import SessionHelper


url = 'https://www.footaction.com/category/mens/shoes/new.html'


def crawl():
    session_helper = SessionHelper()
    session = session_helper.get_session()
    r = session.get(url)

    session_helper.print_cookies()
#   print(r.text)

    html = etree.HTML(r.text)
    product_list = html.xpath('//div[@class="SearchResults"]/ul[@class="row row-2cols--xs row-3cols--sm gutter"]/li[@class="product-container col"]')
    for product in product_list:
        href = product.xpath('./div[@class="c-product-card"]/a/@href')[0]
        name = product.xpath('./div[@class="c-product-card"]/a/span[@class="product-name"]/span/span[@class="primary"]/text()')[0]
        price = product.xpath('./div[@class="c-product-card"]/div[@class="c-product-price"]//span[@aria-hidden="true"]/text()')[0]
        print(href, name, price)


if __name__ == "__main__":
    crawl()
