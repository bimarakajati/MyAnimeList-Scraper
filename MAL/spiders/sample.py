import scrapy

class AnimeSpider(scrapy.Spider):
    name = "scrapy_mal"
    start_urls = [
        'https://myanimelist.net/topanime.php',
    ]

    def __init__(self):
        self.iterations = 0

    def parse(self, response):
        animes = response.css('tr.ranking-list')

        for anime in animes:
            title = anime.css('h3.anime_ranking_h3 a::text').get()
            score = anime.css('.score-label::text').get()
            episode = anime.css('.information::text')[0].get().strip()
            aired = anime.css('.information::text')[1].get().strip()
            user = anime.css('.information::text')[2].get().strip()

            yield {
                'title': title,
                'score': score,
                'episode': episode,
                'aired': aired,
                'user': user,
            }

        next_page = response.css('a.next::attr(href)').get()
        if next_page and self.iterations < 19:
            self.iterations += 1
            yield response.follow(next_page, callback=self.parse)