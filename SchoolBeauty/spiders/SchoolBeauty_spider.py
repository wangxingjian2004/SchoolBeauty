# -*- coding: utf-8 -*-

import scrapy
import logging
from scrapy.selector import HtmlXPathSelector
import re
import os
import urllib
from SchoolBeauty.items import SchoolbeautyItem
from SchoolBeauty.settings import *

logger = logging.getLogger('main.spiders')

class SchoolBeautySpider(scrapy.Spider):
    name = 'SchoolBeauty'
    allowed_domains = ['xiaohua.com']
    start_urls = [
        'http://www.xiaohuar.com/hua'
    ]

    def parse(self, response):
        '''
        current_url = response.url
        body = response.body
        unicode_body = response.body_as_unicode()
        logger.info('current URL:' + current_url)
        logger.info('body:' + unicode_body)
        '''
        '''
        hxs = HtmlXPathSelector(response)

        if re.match('http://www.xiaohuar.com/list-1-\d+.html', response.url):
            items = hxs.select('//div[@class="item_list infinite_scroll"]/div')
            for i in range(len(items)):
                src = hxs.select('//div[@class="item_list infinite_scroll"]/div[%d]//div[@class="img"]/a/img/@src' % i).extract()
                name = hxs.select('//div[@class="item_list infinite_scroll"]/dir[%d]//div[@class="img"]/span/text()' % i).extract()
                school = hxs.select('//div[@class="item_list infinite_scroll"/div[%d]//div[@class="img"]/div[@class="btns"]/a/text()' % i).extract()
                if src:
                    ab_src = "http://www.xiaohuar.com" + src[0]
                    file_name = "%s_%s.jpg" % (school[0].encode('utf-8'), name[0].encode('utf-8'))
                    file_path = os.path.join('E:\\python\\SchoolBeauty\\picDir', file_name)
                    urllib.urlretrieve(ab_src, file_path)
                    logger.log('ab_src:%s', ab_src)
                    logger.log('file_name:%s', file_name)
                    logger.log('file_path:%s', file_path)
        '''
        file_name = response.url.split("/")[-2]
        for str in response.url.split('/'):
            print("str:" + str)
        root_url = 'http://' + response.url.split('/')[2]
        print('root_url: ' + root_url)


        meta_datas = response.xpath('//div[@class="item masonry_brick"]//div[@class="item_t"]')

        for meta_data in meta_datas:
            try:
                item = SchoolbeautyItem()
                item['pic_url'] = root_url + meta_data.xpath('div[@class="img"]//a//img//@src').extract()[0]
                item['name'] = meta_data.xpath('div[@class="img"]//span[@class="price"]//text()').extract()[0]
                item['school'] = meta_data.xpath('div[@class="img"]//div[@class="btns"]//a//text()').extract()[0]
                print(item['school'])
                print(item['name'])
                print(item['pic_url'])
                file_path = os.path.join(FILE_PATH, item['school'] + '_' + item['name'] + '.jpg')
                urllib.urlretrieve(item['pic_url'], file_path)
            except BaseException, b:
                print(b)


        img_src_links = response.xpath('//div[@class="item masonry_brick"]//div[@class="item_t"]//div[@class="img"]//a//img//@src').extract()
        for src in img_src_links:
            print("src:" + root_url + src)
        with open(file_name, 'wb') as f:
            f.write(response.body)




