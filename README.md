## 🧠 Prompt: for Generating a Python desktop app

Create a Python desktop application using the MVVM (Model-View-ViewModel) architecture that fetches cryptocurrency market data and derivatives exchange data from the CoinGecko REST API.

# Requirements:
Use the API base URL: https://api.coingecko.com/api/v3/ with endpoints:
coins/markets (pass vs_currency=usd and other optional parameters)
derivatives/exchanges
Implement a reusable NetworkService to handle generic HTTP GET requests.
Define Model classes for coin market data and derivative exchange data.
Create a ViewModel class responsible for fetching data and exposing lists of models.

#Build a GUI View using Tkinter with:
A segmented toggle (radio buttons) to switch between viewing coin markets and derivative exchanges.

# A Treeview table showing:
For coins: image, name, current price, and symbol.
For exchanges: name, country, and year established.
Display an alert box titled "Request is Failured" on any API request failure.

Set the window title to "Crypto Info".
Properly separate concerns so the Model, ViewModel, NetworkService, and View logic are in distinct components or classes.

- - - - - - - - - - - - - - - - - - - - - 

# 
crypto_app/
─ main.py
─ models.py
─ network_service.py
─ view_model.py
─ view.py
