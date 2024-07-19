CREATE TABLE cryptocurrency_quotes (
    id INT,
    name VARCHAR(50),
    symbol VARCHAR(50),
    slug VARCHAR(50),
    num_market_pairs INT,
    date_added TIMESTAMPTZ,
    max_supply VARCHAR(50),
    circulating_supply NUMERIC,
    total_supply NUMERIC,
    is_active INT,
    infinite_supply BOOLEAN,
    platform VARCHAR(255),
    cmc_rank INT,
    is_fiat VARCHAR(255),
    self_reported_circulating_supply NUMERIC,
    self_reported_market_cap NUMERIC,
    tvl_ratio NUMERIC,
    last_updated TIMESTAMPTZ,
    BRL_price NUMERIC,
    BRL_volume_24h NUMERIC,
    BRL_volume_change_24h VARCHAR(255),
    BRL_percent_change_1h VARCHAR(255),
    BRL_percent_change_24h VARCHAR(255),
    BRL_percent_change_7d VARCHAR(255),
    BRL_percent_change_30d VARCHAR(255),
    BRL_percent_change_60d VARCHAR(255),
    BRL_percent_change_90d VARCHAR(255),
    BRL_market_cap VARCHAR(255),
    BRL_market_cap_dominance VARCHAR(255),
    BRL_fully_diluted_market_cap VARCHAR(255),
    BRL_tvl VARCHAR(255),
    BRL_last_updated TIMESTAMPTZ
);

drop table cryptocurrency_quotes
	
CREATE TABLE cryptocurrency_quotes_tags_data(
	quote_id INT,
	tags VARCHAR(100)
)


CREATE TABLE cryptocurrency_latest_listing (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    symbol VARCHAR(50),
    slug VARCHAR(50),
    num_market_pairs INT,
    date_added TIMESTAMPTZ,
    max_supply VARCHAR(50),
    circulating_supply NUMERIC,
    total_supply NUMERIC,
    infinite_supply BOOLEAN,
    cmc_rank INT,
    self_reported_circulating_supply NUMERIC,
    self_reported_market_cap NUMERIC,
    tvl_ratio NUMERIC,
    last_updated TIMESTAMPTZ,
    BRL_price VARCHAR(255),
    BRL_volume_24h NUMERIC,
    BRL_volume_change_24h VARCHAR(255),
    BRL_percent_change_1h VARCHAR(255),
    BRL_percent_change_24h VARCHAR(255),
    BRL_percent_change_7d VARCHAR(255),
    BRL_percent_change_30d VARCHAR(255),
    BRL_percent_change_60d VARCHAR(255),
    BRL_percent_change_90d VARCHAR(255),
    BRL_market_cap VARCHAR(255),
    BRL_market_cap_dominance VARCHAR(255),
    BRL_fully_diluted_market_cap VARCHAR(255),
    BRL_tvl VARCHAR(255),
    BRL_last_updated TIMESTAMPTZ,
    name2 VARCHAR(50)
);

CREATE TABLE cryptocurrency_latest_listing_tags_data(
	listing_id INT,
	tags VARCHAR(100)
)


