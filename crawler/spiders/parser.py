from lxml import etree

def _to_etree(body, encoding="utf-8"):
	try:
		return etree.HTML(body.decode(encoding))
	except:
		return None

def parse_data(cityname,body,when):
    tree = _to_etree(body)

    data = {
        'quando': when,
        'cidade': cityname,
        'descricao': get_desc(tree),
        'temperatura-min': get_min_temp(tree),
        'temperatura-max': get_max_temp(tree),
        'precipitacao': get_prec(tree),
        'vento': get_wind(tree),
        'umidade-min': get_min_humid(tree),
        'umidade-max': get_max_humid(tree),
        'nascer_do_sol': get_sun_initial_hour(tree),
        'por_do_sol':get_sun_final_hour(tree)
    }

    return data

def get_desc(tree):
    desc = tree.xpath('string(//div[@id="mainContent"]/div[6]/div[3]/div[1]/div[2]/div[2]/div[1]/div[1]/p)')

    return desc.strip().replace("\n\n\n\n\n",". ").replace("\n\n \n\n\n",". ").replace("\n \n\n\n\n",". ").replace("\n\n\n \n\n",". ")
    
def get_min_temp(tree):
    min_temp = tree.xpath('string(//span[@id="min-temp-1"])')

    return min_temp

def get_max_temp(tree):
    max_temp = tree.xpath('string(//span[@id="max-temp-1"])')

    return max_temp

def get_prec(tree):
    prec = tree.xpath('string(//div[@id="mainContent"]/div[6]/div[3]/div[1]/div[2]/div[2]/div[2]/div[1]/ul/li[2]/span[2])')

    return prec.strip()

def get_wind(tree):
    wind = tree.xpath('string(//div[@id="mainContent"]/div[6]/div[3]/div[1]/div[2]/div[2]/div[2]/div[1]/ul/li[3]/div)')

    return wind.strip()

def get_min_humid(tree):
    min_humid = tree.xpath('string(//div[@id="mainContent"]/div[6]/div[3]/div[1]/div[2]/div[2]/div[2]/div[1]/ul/li[4]/div/span[2])')

    return min_humid

def get_max_humid(tree):
    max_humid = tree.xpath('string(//div[@id="mainContent"]/div[6]/div[3]/div[1]/div[2]/div[2]/div[2]/div[1]/ul/li[4]/div/span[4])')

    return max_humid

def get_sun_initial_hour(tree):
    sun_initial_hour = tree.xpath('string(//div[@id="mainContent"]/div[6]/div[3]/div[1]/div[2]/div[2]/div[2]/div[1]/ul/li[5]/span[2]/text()[1])')

    return sun_initial_hour.strip()

def get_sun_final_hour(tree):
    sun_final_hour = tree.xpath('string(//div[@id="mainContent"]/div[6]/div[3]/div[1]/div[2]/div[2]/div[2]/div[1]/ul/li[5]/span[2]/text()[2])')

    return sun_final_hour.strip()