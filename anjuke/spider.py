# encoding: utf-8

import csv
import math
import time

import requests
from lxml import etree

from session import SessionHelper


def crawl_loupan(area_code):
	'''
	爬取安居客某城市的楼盘信息
	'''
	session = SessionHelper().get_session()

	base_url = 'https://'+area_code+'.fang.anjuke.com/loupan/'
	r = session.get(base_url)
	html = etree.HTML(r.text)

	result_count = html.xpath('//span[@class="result"]/em/text()')[0]
	page = math.ceil(int(result_count)/30)
	print('>>>>> total count:', result_count, 'page:', page)

	with open('anjuke/.'+area_code+'.csv', 'w', encoding='utf-8-sig', newline='') as csvfile:
		writer = csv.writer(csvfile)
		headers = ['详情链接', '缩略图', '楼盘名称', '楼盘地址', '户型', '楼盘状态', '楼盘标签', '楼盘价格']
		writer.writerow(headers)

		for i in range(1, page+1):
			loupan_url = base_url+'all/p'+str(i)+'/'
			print(loupan_url)
			resp = session.get(loupan_url)
			loupan_html = etree.HTML(resp.text)

			loupan_list = loupan_html.xpath('//div[@class="key-list"]/div[@class="item-mod "]')
			for loupan in loupan_list:
				href = loupan.xpath('./a[@class="pic"]/@href')[0]   # 详情链接
				thum_img = loupan.xpath('./a[@class="pic"]/img/@src')[0]    # 缩略图
				name = loupan.xpath('./div[@class="infos"]/a[@class="lp-name"]/h3/span/text()')[0]  # 楼盘名称
				address = loupan.xpath('./div[@class="infos"]/a[@class="address"]/span/text()')[0]  # 楼盘地址
				huxing = loupan.xpath('./div[@class="infos"]/a[@class="huxing"]/span/text()')	# 户型
				status = loupan.xpath('./div[@class="infos"]/a[@class="tags-wrap"]/div/i/text()')	# 楼盘状态
				tags = loupan.xpath('./div[@class="infos"]/a[@class="tags-wrap"]/div/span/text()')	# 楼盘标签
				price_ele = loupan.xpath('./a[@class="favor-pos"]')[0]
				price_info = price_ele.xpath('string(.)').strip().replace(' ', '').replace('\n', '').replace('\r', '')	# 楼盘价格

				print(href, thum_img)
				print(name, address, huxing)
				print(status, tags, price_info)
				writer.writerow([href, thum_img, name, address, huxing, status, tags, price_info])
			time.sleep(1)

	# with open('anjuke/result.html', 'w', encoding='utf-8') as f:
	#     f.write(r.text)


if __name__ == "__main__":
	# crawl_loupan('wx')	# 无锡楼盘
	# crawl_loupan('hf')	# 合肥楼盘
	# crawl_loupan('nj')	# 南京楼盘
	crawl_loupan('hz')	# 杭州楼盘
