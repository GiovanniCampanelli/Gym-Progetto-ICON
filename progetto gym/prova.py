import csv
import scrapy
from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.signalmanager import dispatcher

class BooksSpider(scrapy.Spider):
    name = 'books'
    #gioco = input("inserisci il nome del gioco")
    #print(gioco)

    def start_requests(self):
        URL = "https://www.everyeye.it/articoli/recensioni/?pagina=1"
        f=0
        d=str(f)
        print(d)
        #pif = URL.replace("1", "2")
        yield scrapy.Request(url=URL, callback=self.response_parser)

    def response_parser(self, response):

        URL = "https://www.everyeye.it/articoli/recensioni/?pagina=1"
        URL2 = "https://www.eurogamer.it/"
        gioco = input("inserisci il nome del gioco")
        print('inserisci il nome del gioco')
        gioco=gioco.replace(' ', '-')
        URL2+= gioco + '-recensione'
        print(URL2)
        yield scrapy.Request(url=URL2, callback=self.response_parser)
        for selector in response.css('article'):
            yield {
                'descrizione': selector.css('img::attr(title)').extract_first(),
                'price': selector.css('p::text').extract_first()
            }
        pif = URL
        s=1
        i=0
        while i<4:
            f=s-1
            d=str(f)
            dd=str(s)
            URL = URL.replace(d, dd)
            i=i+1
            prov="https://musicbrainz.org/tag/rock/artist?page=1"
            s=s+1
            print(dd)
            yield scrapy.Request(url=URL, callback=self.response_parser)
            for selector in response.css('article'):
                  yield {
                  'descrizione': selector.css('img::attr(title)').extract_first(),
                   'price': selector.css('article > div > a ::text').extract_first()
                        }

        next_page_link = response.css('li.next a::attr(href)').extract_first()
        if next_page_link:
            yield response.follow(next_page_link, callback=self.response_parser)
            i=i+1
            s=s+1


def book_spider_result():
    books_results = []

    def crawler_results(item):
        books_results.append(item)

    dispatcher.connect(crawler_results, signal=signals.item_scraped)
    crawler_process = CrawlerProcess()
    crawler_process.crawl(BooksSpider)
    crawler_process.start()
    return books_results


if __name__ == '__main__':
    books_data=book_spider_result()

    keys = books_data[0].keys()
    with open('books_data.csv', 'w', newline='') as output_file_name:
        writer = csv.DictWriter(output_file_name, keys)
        writer.writeheader()
        writer.writerows(books_data)