from api_connection import get_crypto_quote_data, get_crypto_listings_data
from data_tranformation import parse_crypt_quote_data, parse_listing_data,parse_crypt_quote_tags_data, parse_quote_tags_listing_data
from database_connect import insert_crypto_data
import time
def main():
    # Requisições
    time.sleep(2)
    crypto_listing_data = get_crypto_listings_data()
    time.sleep(2)
    critpo_quotes_data = get_crypto_quote_data()
    time.sleep(2)
    print(crypto_listing_data)
    print(critpo_quotes_data)

    # Transformação de dados
    time.sleep(2)
    cleaned_quote_data = parse_crypt_quote_data(critpo_quotes_data)
    time.sleep(2)
    cleaned_quote_tags_data = parse_crypt_quote_tags_data(critpo_quotes_data)
    time.sleep(2)
    cleaned_listing_data = parse_listing_data(crypto_listing_data)
    time.sleep(2)
    cleaned_listing_tags_data = parse_quote_tags_listing_data(crypto_listing_data)
    time.sleep(2)


    # inserindo dados da rota /listings/latest
    insert_crypto_data(cleaned_listing_data, 'cryptocurrency_latest_listing')
    insert_crypto_data(cleaned_listing_tags_data, 'cryptocurrency_latest_listing_tags_data')

    # inserindo dados da rota /quotes/latest
    insert_crypto_data(cleaned_quote_tags_data, 'cryptocurrency_quotes_tags_data')
    insert_crypto_data(cleaned_quote_data, 'cryptocurrency_quotes')

    print('Dados extraídos e inseridos com sucesso!')

if __name__ == "__main__":
    main()