from view_model import CryptoViewModel
from view import CryptoApp

if __name__ == "__main__":
    vm = CryptoViewModel()
    app = CryptoApp(vm)
    app.mainloop()