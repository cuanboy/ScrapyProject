# -*- coding: utf-8 -*-

"""
项目描述：《Scrapy采花大盗小爬虫》：本scrapy爬虫，教大家爬取整个妹纸网站，妹纸4000多，图片10W多，合计10G多数据量……
运行环境：win7 64 + python3.6 + scrapy1.4
运行方式：进入AoiSolas目录（scrapy.cfg所在目录)输入：

scrapy crawl AoiSola

代码详解：http://www.scrapyd.cn/example/176.html;
创建时间：2018年4月20日22:23:19
创建者：scrapy中文网（http://www.scrapyd.cn）；
"""


from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.http import Request
import re


class MyImagesPipeline(ImagesPipeline):

    #
    # def file_path(self, request, response=None, info=None):
    #     """
    #     :param request: 每一个图片下载管道请求
    #     :param response:
    #     :param info:
    #     :param strip :清洗Windows系统的文件夹非法字符，避免无法创建目录
    #     :return: 每套图的分类目录
    #     """
    #     item = request.meta['item']
    #     folder = item['name']
    #
    #     folder_strip = re.sub(r'[？\\*|“<>:/]', '', str(folder))
    #     image_guid = request.url.split('/')[-1]
    #     filename = u'full/{0}/{1}'.format(folder_strip, image_guid)
    #     return filename

    def get_media_requests(self, item, info):
        for image_url in item['ImgUrl']:
            yield Request(image_url,meta={'item':item['name']})

    def file_path(self, request, response=None, info=None):
        name = request.meta['item']
        # name = filter(lambda x: x not in '()0123456789', name)
        name = re.sub(r'[？\\*|“<>:/()0123456789]', '', name)
        image_guid = request.url.split('/')[-1]
        # name2 = request.url.split('/')[-2]
        filename = u'full/{0}/{1}'.format(name, image_guid)
        return filename
        # return 'full/%s' % (image_guid)

    def item_completed(self, results, item, info):
        image_path = [x['path'] for ok, x in results if ok]
        if not image_path:
            raise DropItem('Item contains no images')
        item['image_paths'] = image_path
        return item

