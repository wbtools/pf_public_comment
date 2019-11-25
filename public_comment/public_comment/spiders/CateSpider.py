# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'pfinal'
__mtime__ = '2019/11/25'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
import scrapy
import sys
import json
from scrapy.http import Request


class CateSpider(scrapy.Spider):
    name = "cate"
    start_urls = (
        'http://www.dianping.com/shanghai/',
    )
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
    }

    def parse(self, response):
        # print(response)
        for item_url in self.start_urls:
            yield Request(item_url, self.get_cat)

    def get_cat(self, response):
        cat_list = response.xpath('//*[@id="nav"]/div/ul/li/div[2]/div')
        cat_all = []
        for cat in cat_list:
            cat_content = []
            cat_title = cat.xpath('div/div[1]/span/text()').get()
            # //*[@id="nav"]/div/ul/li[1]/div[2]/div/div[1]/div[2]/a[1]
            cat_hrefs = cat.xpath('div/div[2]/a')
            for cat_item in cat_hrefs:
                # print(cat_item)
                cat_content.append({cat_item.xpath('text()').get(): cat_item.attrib['href']})
            cat_all.append({cat_title: cat_content})
        jsonData = json.dumps(cat_all, ensure_ascii=False)
        fileObject = open('cat.json', 'w')
        fileObject.write(jsonData)
        fileObject.close()
