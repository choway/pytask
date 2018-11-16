# coding: utf-8

import requests
from lxml import etree


suffix_url = ''

def crawl_loupan():
    '''
    爬取安居客某城市的楼盘信息
    '''

    r = requests.get('https://wx.fang.anjuke.com/loupan/all/p1/')
    html = etree.HTML(r.text)

    result_count = html.xpath('//span[@class="result"]/em/text()')[0]
    print(result_count)

    loupan_list = html.xpath('//div[@class="key-list"]/div[@class="item-mod "]')
    for loupan in loupan_list:
        href = loupan.xpath('./a[@class="pic"]/@href')[0]   # 详情链接
        thum_img = loupan.xpath('./a[@class="pic"]/img/@src')[0]    # 缩略图
        name = loupan.xpath('./div[@class="infos"]/a[@class="lp-name"]/h3/span/text()')[0]  # 楼盘名称
        address = loupan.xpath('./div[@class="infos"]/a[@class="address"]/span/text()')[0]  # 楼盘地址
        huxing = loupan.xpath('./div[@class="infos"]/a[@class="huxing"]/span/text()')

        # print(href, thum_img)
        print(name, address, huxing)

    # with open('anjuke/result.html', 'w', encoding='utf-8') as f:
    #     f.write(r.text)


if __name__ == "__main__":
    crawl_loupan()
