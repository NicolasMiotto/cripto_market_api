import pandas as pd
import numpy as np
import json
# metodos da rota /v1/cryptocurrency/quotes/latest'
def parse_crypt_quote_data(response_quote):
    """
    Método que desaninha o campo 'quote' da resposta da api
    e as adiciona em um dataframe para disponilizá-los para análise
    """
    try:
        print('Transformando dados..')
        response = response_quote.json()
        data = response['data']
        flattened_data = []
        for item in data.values():
            base = {key: value for key, value in item.items() if key != 'quote'}
            quote = item.get('quote', {})
            for currency, metrics in quote.items():
                extended = {**base, **{f'{currency}_{y}': x for y, x in metrics.items()}}
                flattened_data.append(extended)
                flattened_df = pd.DataFrame(flattened_data)
                flattened_df= flattened_df.drop(columns='tags')
        flattened_df.columns = [col.lower() for col in flattened_df.columns]
        return flattened_df
    except Exception as e:
        print(f'Erro ao transformar dados: {e}')
        

    


def parse_crypt_quote_tags_data(response_quote):
    """
    Método que retira as tags aninhadas da resposta da api no campo 'tags'
    e as adiciona em um dataframe para disponilizá-los para análise
    """
    try:
        json_quote = response_quote.json()

        df = pd.DataFrame.from_dict(json_quote['data'], orient='index')
    
        tags_df = df[['tags']].explode('tags').reset_index()
        tags_df.rename(columns={'index': 'quote_id'}, inplace=True)
        return tags_df[['quote_id', 'tags']]
    except Exception as e:
        print(f"Erro ao extrair as tags da respota da API: {e}")
    
    


# metodos da rota /v1/cryptocurrency/listings/latest
def parse_quote_listing_data(response_listing):
    """
    Método que desaninha o campo 'quote' da resposta da api
    e as adiciona em um dataframe para disponilizá-los para análise.
    OBS: semelhante ao anterior porém este está preparado para lidar 
    com os dados em formato de lista, retornado da rota /listings/latest
    """
    try:
        response = response_listing.json()
        data = response['data']
        flattened_data = []
        for item in data:
            base = {key: value for key, value in item.items() if key != 'quote'}
            quote = item.get('quote', {})
            for currency, metrics in quote.items():
                extended = {**base, **{f'{currency}_{y}': x for y, x in metrics.items()}}
                flattened_data.append(extended)

        flattened_df = pd.DataFrame(flattened_data)
        if 'tags' in flattened_df.columns:
            flattened_df = flattened_df.drop(columns='tags')

        return flattened_df
    except Exception as e:
        print(f'Erro ao transformar dados: {e}')
    

def parse_quote_tags_listing_data(response_listing):
    """
    Método que retira as tags aninhadas da resposta da api no campo 'tags'
    e as adiciona em um dataframe para disponilizá-los para análise.
    OBS: também semelhante ao anterior porém este está preparado para lidar 
    com os dados em formato de lista, retornado da rota /listings/latest
    """
    try:
        json_listing = response_listing.json()

        df = pd.DataFrame(json_listing['data'])
        if 'tags' in df.columns:
            # Explodir a coluna 'tags' para criar uma linha para cada tag
            tags_df = df[['tags']].explode('tags').reset_index()
            tags_df.rename(columns={'index': 'listing_id'}, inplace=True)
        else:
            tags_df = pd.DataFrame(columns=['listing_id', 'tags'])

        return tags_df[['listing_id', 'tags']].replace(np.nan, '')
    except Exception as e:
        print(f"Erro ao extrair as tags da resposta da API: {e}")
        tags_df = pd.DataFrame(columns=['listing_id', 'tags'])

    

def parse_listing_data(response_listing):
    """
    Metodo que entrega o dataframe totalmente desaninhado, para armazená-lo
    no banco de dados
    """
    try:
        data = parse_quote_listing_data(response_listing)
        df_desaninhado = data.copy()
        # Substituindo valores None por dicionário vazio para lidar com erros
        df_desaninhado['platform'] = df_desaninhado['platform'].apply(lambda x: x if isinstance(x, dict) else {})
        df_desaninhado['name2'] = df_desaninhado['platform'].apply(lambda x: x.get('name', ''))
        df_desaninhado['symbol'] = df_desaninhado['platform'].apply(lambda x: x.get('symbol', ''))
        df_desaninhado['slug'] = df_desaninhado['platform'].apply(lambda x: x.get('slug', ''))
            
        df_desaninhado = df_desaninhado.drop(columns='platform')
        column_mapping = {
            'BRL_price': 'brl_price',
            'BRL_volume_24h': 'brl_volume_24h',
            'BRL_volume_change_24h': 'brl_volume_change_24h',
            'BRL_percent_change_1h': 'brl_percent_change_1h',
            'BRL_percent_change_24h': 'brl_percent_change_24h',
            'BRL_percent_change_7d': 'brl_percent_change_7d',
            'BRL_percent_change_30d': 'brl_percent_change_30d',
            'BRL_percent_change_60d': 'brl_percent_change_60d',
            'BRL_percent_change_90d': 'brl_percent_change_90d',
            'BRL_market_cap': 'brl_market_cap',
            'BRL_market_cap_dominance': 'brl_market_cap_dominance',
            'BRL_fully_diluted_market_cap': 'brl_fully_diluted_market_cap',
            'BRL_tvl': 'brl_tvl',
            'BRL_last_updated': 'brl_last_updated'
        }
        df_desaninhado = df_desaninhado.rename(columns=column_mapping)
        return df_desaninhado
    except Exception as e:
        print(f"Erro ao extrair as tags da resposta da API: {e}")
    
    
    
