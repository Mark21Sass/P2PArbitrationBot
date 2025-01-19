import requests
from random_user_agent.user_agent import UserAgent


def find_seller(amount):
    params = {'userId': 113234374, 'tokenId': "USDT", 'currencyId': "RUB", 'payment': ["75", "377", "382"], 'side': "1", 'size': "15", 'page': "1", 'sortType': "TRADE_PRICE"}
    headers = {'User-Agent': UserAgent().get_random_user_agent()}
    response = requests.post(url="https://api2.bybit.com/fiat/otc/item/online", data=params, headers=headers)
    offers = dict(response.json())['result']['items']
    minPrice = 1000000000
    seller = None
    sellerURL = None
    for offer in offers:
        if float(offer['minAmount']) <= amount and float(offer['price']) < minPrice:
            minPrice = float(offer['price'])
            seller = offer['nickName']
            sellerURL = 'https://www.bybit.com/ru-RU/fiat/trade/otc/profile/' + offer['userMaskId'] + '/USDT/RUB/item'
    try:
        print('Минимальная сумма в рублях за которую можно купить USDT: ' + str(minPrice))
        print('Никнейм продавца: ' + seller)
        print('Ссылка на его профиль: ' + sellerURL)
    except Exception as ex:
        print('На данный момент нет выгодных предложений')
    return sellerURL, minPrice

