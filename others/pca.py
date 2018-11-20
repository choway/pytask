# encoding: utf-8

"""

"""

import requests
import json


def get_pca_map():
	""" 获取腾讯地图的省市区数据, 并保存到文件 """

	api_url = 'https://api.weixin.qq.com/wxa/get_district'
	token = '15_YNN9H97Kuo7GPUw1Ti-WrSouYF99Vmmx4wVmPwn63GTQ6dy30zKK80lZU5ru2D6xDnL11bvfNp9MClMcwnT9P72VxNz0qVAuKXp4ViYpiYDv2k6plgV5O-8EqWvJEhxnzTYiXfX2-YkXvQu8MDThAHAHYO'
	params = { 'access_token': token }
	r = requests.get(api_url, params=params)
	
	pca = r.json()['result']
	provinces = pca[0]
	citys = pca[1]
	areas = pca[2]

	pca_list = []

	for p in provinces:	# 省份遍历
		province = {}
		province['name'] = p['fullname']
		print(province['name'])

		city_list = []
		c_area_list = []

		p_cidx_begin = p['cidx'][0]
		p_cidx_end = p['cidx'][1]
		for i in range(p_cidx_begin, p_cidx_end+1):	# 城市遍历
			city = {}
			area_list = []

			if 'cidx' in citys[i]:
				city['name'] = citys[i]['fullname']
				c_cidx_begin = citys[i]['cidx'][0]
				c_cidx_end = citys[i]['cidx'][1]
				for j in range(c_cidx_begin, c_cidx_end+1): # 区县遍历
					area_list.append(areas[j]['fullname'])
				city['area'] = area_list
				city_list.append(city)

			else:
				city['name'] = province['name']
				c_area_list.append(citys[i]['fullname'])
				if (i == p_cidx_begin):
					city['area'] = c_area_list
					city_list.append(city)
	
		province['city'] = city_list
		print(province)
		pca_list.append(province)

	with open('others/pca.js', 'w', encoding='utf-8') as f:
		f.write(str(pca_list))


if __name__ == "__main__":
	get_pca_map()
