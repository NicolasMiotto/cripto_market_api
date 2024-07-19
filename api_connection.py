import os, requests
from env import API_KEY



def get_crypto_listings_data():
    """
    Returns a paginated list of all active cryptocurrencies with latest market data.
    The default "market_cap" sort returns cryptocurrency in order of CoinMarketCap's
    market cap rank (as outlined in our methodology) but you may configure this call
    to order by another market ranking field
    """
 
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

    # parâmetros para enviar na requisição para retornar dados por preço e convertidos para real
    parameters = { 
        'sort': 'price',
        'convert': 'BRL' 
        }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': API_KEY
    } 
    try:
        print(f"Solicitando dados da API na rota {url}...")
        response = requests.get(url, params=parameters, headers=headers)
        return response
    except Exception as e:
        print(f"Erro ao solicitar dados da API: {e}")

    


def get_crypto_quote_data():
    """
    Returns the latest market quote for 1 or more cryptocurrencies.
    Use the "convert" option to return market values in multiple fiat 
    and cryptocurrency conversions in the same call.
    """

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

    # parâmetros para enviar na requisição para retornar dados de bitcoin e convertidos para real
    parameters = { 
        'slug':'bitcoin',
        'convert': 'BRL' 
        }

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': API_KEY
    } 
    try:
        print(f"Solicitando dados da API na rota {url}...")
        response = requests.get(url, params=parameters, headers=headers)
    except Exception as e:
        print(f"Erro ao solicitar dados da API: {e}")

    return response
