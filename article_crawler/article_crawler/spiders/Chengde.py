from article_crawler.baseSpider import baseSpider


class ChengdeSpider(baseSpider):
    name = '承德'

    @baseSpider.parser('Chengde', 'www.chengde.gov.cn')
    def parser_1(self, response, **kwargs):
        result = {
            'content': response.css("div.cont  ::text").getall(),
        }
        return result