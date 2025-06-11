from dataclasses import dataclass

@dataclass
class CoinMarket:
    id: str
    name: str
    symbol: str
    current_price: float
    image_url: str

@dataclass
class DerivativeExchange:
    id: str
    name: str
    year_established: int
    country: str
