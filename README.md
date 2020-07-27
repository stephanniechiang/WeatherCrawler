# WeatherCrawler

## Source Analysis

This bot scrapes weather data from the Climatempo website using Scrapy. For more information about the Climatempo website, visit [this website](https://www.climatempo.com.br/). The bot scrapes data from every capital of the country Brazil, from the current day and the following day. 

### Outputs


This bot will produce 54 outputs that will be written in a JSON file.


##### Example (1 output):

```json
[
    {
        "por_do_sol": "17:43h",
        "temperatura-max": "21°",
        "vento": "WSW - 27km/h",
        "quando": "AMANHA",
        "nascer_do_sol": "06:57h",
        "umidade-max": "93%",
        "umidade-min": "74%",
        "descricao": "Amanhã será parecido com hoje. Sol com muitas nuvens durante o dia. Períodos de nublado, com chuva a qualquer hora.",
        "temperatura-min": "14°",
        "cidade": "florianopolis-sc",
        "precipitacao": "20mm - 90%"
    }
]
```


## Bot Usage

To run the bot you must be in the main folder and run the following command:
```
scrapy crawl WeatherSpider -o weather.json  
```
Warning: you must delete the weather.json file before crawling again, you can use the following command for that:
```
rm weather.json
```
## Data Visualization

To better data visualization it was added to the project a python program to convert the output file (weather.json) in a csv file (weather_output.csv). To run the program just run the following command:
```
python json_to_csv.py weather.json weather_output.csv
```
