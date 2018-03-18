import requests


def get_free_game_names():
    url = 'https://www.humblebundle.com/store/api/search?sort=discount&filter=onsale&request=3&page_size=20'
    data = requests.get(url).json()
    return [sale['human_name'] for sale in data["results"] if sale["current_price"][0] == 0]
