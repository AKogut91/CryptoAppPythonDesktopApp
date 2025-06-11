import requests

class NetworkService:
    BASE_URL = "https://api.coingecko.com/api/v3/"

    @staticmethod
    def get(path: str, params: dict = None):
        try:
            response = requests.get(NetworkService.BASE_URL + path, params=params)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            raise RuntimeError("Request failed") from e