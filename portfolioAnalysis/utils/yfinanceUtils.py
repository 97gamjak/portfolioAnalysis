import requests

url = 'https://query2.finance.yahoo.com/v1/finance/search'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36',
}


def params_init(text: str):
    params = {}
    params["q"] = text
    params["quotesCount"] = 10
    params["newsCount"] = 0
    params["enableFuzzyQuery"] = False
    params["quotesQueryId"] = "tss_match_phrase_query"

    return params


def get_yf_response_quotes(params):
    response = requests.get(url, headers=headers, params=params).json()

    if not response["quotes"]:
        return None
    else:
        return response["quotes"]
