from models import CoinMarket, DerivativeExchange
from network_service import NetworkService

class CryptoViewModel:
    def __init__(self):
        self.coins = []
        self.exchanges = []

    def fetch_coins(self) -> bool:
        try:
            params = {
                "vs_currency": "usd",
                "order": "market_cap_desc",
                "per_page": 20,
                "page": 1,
                "sparkline": "false"
            }
            data = NetworkService.get("coins/markets", params)
            self.coins = [
                CoinMarket(
                    id=item["id"],
                    name=item["name"],
                    symbol=item["symbol"],
                    current_price=item["current_price"],
                    image_url=item["image"]
                ) for item in data
            ]
            return True
        except Exception:
            return False

    def fetch_exchanges(self) -> bool:
        try:
            data = NetworkService.get("derivatives/exchanges")
            self.exchanges = [
                DerivativeExchange(
                    id=item["id"],
                    name=item["name"],
                    year_established=item.get("year_established") or 0,
                    country=item.get("country") or "Unknown"
                ) for item in data
            ]
            return True
        except Exception:
            return False
