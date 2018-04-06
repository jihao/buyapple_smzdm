# -*- coding: utf-8 -*-
import scrapy
import codecs


class RecentDiscountSpider(scrapy.Spider):
    name = "recent_discount"
    allowed_domains = ["smzdm.com"]
    start_urls_dict = {'http://wiki.smzdm.com/p/0qqdedj/jiage/':'AirPods'}
    save_folder = "./dist"

    def start_requests(self):
        for url in self.start_urls_dict.keys():
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # print(response.encoding)
        filename = self.start_urls_dict.get(response.url)
        content = " ".join(response.css('ul.youhui_list').extract())
        save_path = self.save_folder+'/'+filename+'.html'
        fd = codecs.open(save_path, 'w', 'utf-8')
        fd.write(content)
        fd.close()

        print('done write to ' + save_path)
        pass
