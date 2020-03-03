#-*- coding:utf-8 -*-
# Author:K
# http://www.allitebooks.org/

import requests
from lxml import etree
import os
import csv

class BooksSpider(object):
    def open_file(self):
        # 创建目录
        if not os.path.exists('D:/allitebooks数据'):
            os.mkdir('D:/allitebooks数据')

        self.fp = open('D:/allitebooks数据/allitebooks.csv','w',encoding = 'utf-8-sig',newline = '')
        self.writer = csv.writer(self.fp)
        headers = ['书名','作者','年份','语言','分类','图片']
        # 写入表头
        self.writer.writerow(headers)

    def run(self):
        # 得到所有详情页面的url
        self.get_urls()

    def get_urls(self):
        # 若要获取多页，则修改range范围即可
        for page in range(1,2):
            page_url = 'http://www.allitebooks.org/page/%s/'%page
            response = requests.get(page_url)
            tree = etree.HTML(response.text)
            detail_urls = tree.xpath('//h2[@class="entry-title"]/a/@href')
            self.parse_page(detail_urls)


    def parse_page(self,urls):
        for url in urls:
            response = requests.get(url = url)
            tree = etree.HTML(response.text)
            header_infos = tree.xpath('//header[@class="entry-header"]')
            # print(header_infos) 测试
            for info in header_infos:
                data = []
                # 获取书名，并添加到列表中
                book_name = info.xpath('./h1/text()')[0]
                data.append(book_name)
                # 获取作者列表
                author_list = info.xpath('.//div[@class="book-detail"]/dl/dd[1]/a/text()')
                # 若作者有多个的话就将多个作者之间用 / 分隔
                if len(author_list) > 1:
                    author = ''
                    for auth in author_list:
                        if auth != author_list[-1]:
                            author = author + auth + ' / '
                        else:
                            author = author + auth
                    data.append(author)
                else:
                    author = author_list[0]
                    data.append(author)
                # 获取年份，并添加到列表中
                year = info.xpath('.//div[@class="book-detail"]/dl/dd[3]/text()')[0].strip()
                data.append(year)
                # 获取书的语言，并添加到列表中
                language = info.xpath('.//div[@class="book-detail"]/dl/dd[5]/text()')[0].strip()
                data.append(language)
                # 获取书的分类，并添加到列表中
                category = info.xpath('.//div[@class="book-detail"]/dl/dd[8]/a/text()')[0].strip()
                data.append(category)
                # 获取图片的url，并添加到列表中
                img_url = info.xpath('.//div[1]/a/img/@src')[0]
                data.append(img_url)
                # print(book_name,year,language,category,img_url) 测试
                self.save_data(data)

    def save_data(self,data):
        self.writer.writerow(data)

    def close_file(self):
        self.fp.close()


if __name__ == '__main__':
    spider = BooksSpider()
    spider.open_file()
    spider.run()
    spider.close_file()