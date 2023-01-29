import json
import time

import scrapy
from scrapy.downloadermiddlewares.retry import get_retry_request


class IMDBSpider(scrapy.Spider):
    name = "imdb"

    def start_requests(self):
        urls = [
            'https://www.imdb.com/title/tt0112401/plotsummary',
            'https://www.imdb.com/title/tt0116731/plotsummary',
            'https://www.imdb.com/title/tt0112427/plotsummary'

        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # all the properties we are interested in are stored in a script tag 😠
        # so we need to extract the script tag and then parse the json
        # we need to sleep because sometimes that script tag is not loaded yet 🤷‍♂️
        self.logger.info("taking a break ...")
        time.sleep(10)
        movie_data = response.xpath(
            "//html/body/script[@id='__NEXT_DATA__']//text()").get()

        if not movie_data:
            yield get_retry_request(response.request, spider=self, reason='no movie_data')

        else:
            movie_data = json.loads(movie_data)
            movie_data = movie_data['props']['pageProps']['contentData']

            poster_url = movie_data['posterData']['image']['url']
            title = movie_data["entityMetadata"]["titleText"]["text"]
            id = movie_data["entityMetadata"]["id"]
            plot = movie_data["entityMetadata"]["plot"]["plotText"]["plainText"]

            # if the movie has more than 1 summary, then the first summary is the plot
            # and the second (and subsequent) summary is the actual summary which apparently
            # are written by imdb users
            summaries = movie_data["categories"][0]['section']['items']
            summary = summaries[1] if len(summaries) > 1 else summaries[0]
            summary = scrapy.http.HtmlResponse(
                url='', body=summary['htmlContent'], encoding='UTF-8')
            summary = summary.xpath(
                "//div[@class='ipc-html-content-inner-div']//text()").get()

            yield {
                'title': title,
                'id': id,
                'plot': plot,
                'summary': summary,
                'poster_url': poster_url,
                'source_url': response.url
            }
