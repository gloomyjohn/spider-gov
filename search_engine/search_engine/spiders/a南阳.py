from typing import Any, Generator, Iterable, List, Optional, Union

from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector


class A南阳Spider(ZhengFuBaseSpider):
    name: str = '南阳'
    api = 'http://www.nanyang.gov.cn/search/searchResultGJ.jsp?t_id=41&categoryId=&q={keyword}&site_id=CMSnany&p={page}'
    method = 'GET'

    def edit_page(self, response: Response) -> int:
        """
        返回解析页数.
        """
        pages = response.css('div.pages > span::text').extract()[0].split('共')[2].split('页')[0]
        return int(pages)



    def edit_items_box(self, response: Response) -> Selector:
        """
        返回目录索引.
        返回 Selector
        """
        return response.css('ul.tpxw > li')

    def edit_items(self, items_box: Selector) -> Selector:
        """
        将目录索引整理为标准迭代器.
        """
        return items_box

    def edit_item(self, item: Selector) -> dict:
        """
        从迭代器中提取item.
        """
        data = {
            'url': item.css('::attr(href)').get(),
            'title': item.css('a::text').get(),
            'date': 'unknow',
            'type': item.css('span::text').get(),
            'source': 'unknow'
        }
        return data

