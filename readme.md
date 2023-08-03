# MyAnimeList Scraper
This is a Scrapy project that is designed to scrape the top anime from MyAnimeList (https://myanimelist.net/topanime.php). The scraper extracts anime titles, scores, episode count, aired dates, and user counts.

## ✨ Prerequisites
- Python 3.x
- Scrapy

## 💁‍ How to use:
1. Install Scrapy library:
    ```shell
    pip install scrapy
    ```
2. Clone this repository:
    ```shell
    git clone https://github.com/bimarakajati/MyAnimeList-Scraping.git
    ```
3. Navigate to the MyAnimeList-Scraping folder:
    ```shell
    cd MyAnimeList-Scraping
    ```
4. To run the scraper, execute the following command:
    ```shell
    scrapy crawl scrapy_mal -O myanimelist.csv
    ```
    ```shell
    scrapy crawl scrapy_mal -O myanimelist.json
    ```
5. The scraped data will be saved in CSV/JSON format.

## ✨ Result:
|title                                              |score|episode        |aired              |user             |
|---------------------------------------------------|-----|---------------|-------------------|-----------------|
|Fullmetal Alchemist: Brotherhood                   |9.10 |TV (64 eps)    |Apr 2009 - Jul 2010|3,203,554 members|
|Steins;Gate                                        |9.07 |TV (24 eps)    |Apr 2011 - Sep 2011|2,461,811 members|
|Bleach: Sennen Kessen-hen                          |9.06 |TV (13 eps)    |Oct 2022 - Dec 2022|463,851 members  |
|Gintama°                                           |9.06 |TV (51 eps)    |Apr 2015 - Mar 2016|601,875 members  |
|Shingeki no Kyojin Season 3 Part 2                 |9.05 |TV (10 eps)    |Apr 2019 - Jul 2019|2,131,225 members|
|...                                                |...  |...            |...                |...              |
|Akage no Anne                                      |7.77 |TV (50 eps)    |Jan 1979 - Dec 1979|31,363 members   |
|Digimon Adventure                                  |7.77 |TV (54 eps)    |Mar 1999 - Mar 2000|391,438 members  |
|Dragon Ball Z Special 2: Zetsubou e no Hankou!! Nokosareta Chousenshi - Gohan to Trunks|7.77 |Special (1 eps)|Feb 1993 - Feb 1993|106,640 members  |
|Ginga Eiyuu Densetsu: Die Neue These - Kaikou      |7.77 |TV (12 eps)    |Apr 2018 - Jun 2018|82,377 members   |
|Hadashi no Gen                                     |7.77 |Movie (1 eps)  |Jul 1983 - Jul 1983|51,291 members   |

## 📝 Note:
The spider is set to loop through 20 pages of the top anime list (self.iterations < 19). 1 page has 50 titles, so scraping 20 pages will generate 1000 records. You can adjust this value based on your requirements.

Remember to respect the website's terms of service and rate-limit your requests to avoid overloading their server. Happy scraping! 🕷️

## 📙 Reference:
- https://myanimelist.net/
- https://docs.scrapy.org/