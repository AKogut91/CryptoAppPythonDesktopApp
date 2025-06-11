import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO


class CryptoApp(tk.Tk):
    def __init__(self, view_model):
        super().__init__()
        self.title("Crypto Info")
        self.geometry("700x500")

        self.vm = view_model
        self.selected_type = tk.StringVar(value="coins")

        # Toggle (Segmented Picker)
        toggle_frame = ttk.Frame(self)
        toggle_frame.pack(pady=10)

        ttk.Radiobutton(toggle_frame, text="Coin Markets", variable=self.selected_type,
                        value="coins", command=self.refresh).pack(side=tk.LEFT, padx=10)
        ttk.Radiobutton(toggle_frame, text="Derivatives Exchanges", variable=self.selected_type,
                        value="exchanges", command=self.refresh).pack(side=tk.LEFT, padx=10)

        # Treeview for showing data
        self.tree = ttk.Treeview(self, columns=("img", "name", "extra1", "extra2"), show="headings", height=18)
        self.tree.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        self.tree.heading("img", text="Image")
        self.tree.heading("name", text="Name")
        self.tree.heading("extra1", text="Price / Country")
        self.tree.heading("extra2", text="Symbol / Year")

        self.tree.column("img", width=50, anchor=tk.CENTER)
        self.tree.column("name", width=200)
        self.tree.column("extra1", width=150)
        self.tree.column("extra2", width=150)

        # Cache for images so they're not garbage collected
        self.images_cache = {}

        # Initial load
        self.refresh()

    def refresh(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        self.images_cache.clear()

        if self.selected_type.get() == "coins":
            success = self.vm.fetch_coins()
            if not success:
                messagebox.showerror("Request is Failured", "Failed to fetch coin market data.")
                return
            self.show_coins()
        else:
            success = self.vm.fetch_exchanges()
            if not success:
                messagebox.showerror("Request is Failured", "Failed to fetch exchange data.")
                return
            self.show_exchanges()

    def show_coins(self):
        for coin in self.vm.coins:
            try:
                resp = requests.get(coin.image_url)
                img_data = resp.content
                pil_img = Image.open(BytesIO(img_data)).resize((32, 32))
                tk_img = ImageTk.PhotoImage(pil_img)
                self.images_cache[coin.id] = tk_img
            except Exception:
                tk_img = None

            self.tree.insert(
                "",
                "end",
                iid=coin.id,
                values=("", coin.name, f"${coin.current_price:,.2f}", coin.symbol.upper())
            )
            if tk_img:
                self.tree.item(coin.id, image=tk_img)

        self.tree.configure(displaycolumns=("name", "extra1", "extra2"))

    def show_exchanges(self):
        for ex in self.vm.exchanges:
            self.tree.insert(
                "",
                "end",
                iid=ex.id,
                values=("", ex.name, ex.country, f"Since {ex.year_established}" if ex.year_established else "Year N/A")
            )
        self.tree.configure(displaycolumns=("name", "extra1", "extra2"))

