import requests
import pprint


def find_buyer(amount):
    params = {"userId": 113234334, "tokenId":"USDT", "currencyId": "RUB", "payment": [], "side": "0", "size": "10", "page": "1", "amount": "", "vaMaker": 'false', "bulkMaker": 'false', "canTrade": 'false', "sortType": "TRADE_PRICE", "paymentPeriod": [], "itemRegion": 1}
    response = requests.post(url='https://api2.bybit.com/fiat/otc/item/online', data=params)
    pprint.pprint(dict(response.json()))

find_buyer(1000000)
