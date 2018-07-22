#coding=utf-8

import pandas as pd


url = 'https://music.163.com/#/discover/playlist/?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset=0'

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)


rst = []
while url != 'javascript:void(0)':
	
	driver.get(url)

	driver.switch_to.frame('contentFrame')
	data = driver.find_element_by_id('m-pl-container').\
	find_elements_by_tag_name('li')
	print data

	for i in range(len(data)):
		nb = data[i].find_element_by_class_name('nb').text
		if u'万' in nb and int(nb.split(u'万')[0]) > 500:
			msk = data[i].find_element_by_css_selector('a.msk')
			tmp = [msk.get_attribute('title'), nb, msk.get_attribute('href')]
			print tmp
			rst.append(tmp)


	url = driver.find_element_by_css_selector('a.zbtn.znxt').\
	get_attribute('href')
	
rst.sort(reverse=True, key=lambda x: int(x[1].split(u'万')[0]))
print rst
df = pd.DataFrame(rst, columns=['标题', '播放数', '链接'])
df.to_excel('../../Downloads/web_test.xlsx')
# html = requests.get('https://www.baidu.com')
# bs_obj = BeautifulSoup(html.text, 'html.parser')
# print html.text
# text_list = bs_obj.find_all('.s-news-special')
# print len(text_list)
# for text1 in text_list:
# 	print text1.text