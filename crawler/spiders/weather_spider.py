import scrapy
import parser
from scrapy.exporters import JsonItemExporter

class WeatherSpider(scrapy.Spider):
    name = "WeatherSpider"

    def start_requests(self):
        capitals = [
            '343/portovelho-ro',
            '6/riobranco-ac',
            '25/manaus-am',
            '593/palmas-to',
            '347/boavista-rr',
            '232/belem-pa',
            '39/macapa-ap',
            '256/joaopessoa-pb',
            '264/teresina-pi',
            '94/saoluis-ma',
            '60/fortaleza-ce',
            '384/aracaju-se',
            '334/natal-rn',
            '259/recife-pe',
            '56/salvador-ba',
            '8/maceio-al',
            '88/goiania-go',
            '212/campogrande-ms',
            '558/saopaulo-sp',
            '84/vitoria-es',
            '218/cuiaba-mt',
            '61/brasilia-df',
            '107/belohorizonte-mg',
            '321/riodejaneiro-rj',
            '363/portoalegre-rs',
            '271/curitiba-pr',
            '377/florianopolis-sc'
        ]
        urls = [
            'https://www.climatempo.com.br/previsao-do-tempo/cidade/',
            'https://www.climatempo.com.br/previsao-do-tempo/amanha/cidade/'
        ]
        for url in urls:
            for city in capitals:
                link = "{}{}".format(url,city)
                yield scrapy.Request(
                    url=link, 
                    callback=self.on_city_page, 
                    meta={'city': city}
                    )

    def on_city_page(self, response):
        cityname = response.meta['city'].split("/")[1]

        if "amanha" in response.url:
            filename = "original_pages/{}-amanha".format(cityname) 
            data = parser.parse_data(cityname,response.body,"AMANHA")
        else:
            filename = "original_pages/{}-hoje".format(cityname) 
            data = parser.parse_data(cityname,response.body,"HOJE") 
        
        with open("{}.html".format(filename), 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % "{}.html".format(filename))

        # data = parser.parse_data(cityname,response.body)

        return data

