# Made by: John Clement J. Ibrahim
##### Cybersecurity - Group 1
# Started on: 12/09/2025, 9:04 PM
# Finished on: 

import tkinter as tk
from tkinter import messagebox, simpledialog

class VendingMachineGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("VendorIT - Vending Machine")
        self.root.geometry("900x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")
        
        self.products = { #note to self: implement stock
            'P01': {'name': 'Galactic Chocolate', 'price': 1.50},
            'P02': {'name': 'KitterKatter', 'price': 1.25},
            'P03': {'name': 'Stand Chips', 'price': 1.75},
            'P04': {'name': 'CodaSoda', 'price': 2.00},
            'P05': {'name': 'Aquafin', 'price': 1.00},
            'P06': {'name': 'Blue Bull', 'price': 2.50},
            'P07': {'name': 'Bazooka Energy Drink', 'price': 2.25},
            'P08': {'name': 'Caribo Gummy Bears', 'price': 1.30},
            'P09': {'name': 'Trail Hax', 'price': 1.80},
            'P10': {'name': 'Chips Sinking', 'price': 1.60},
            'P11': {'name': 'Pretzels', 'price': 1.40},
            'P12': {'name': 'El Jugo Apple Juice', 'price': 2.20},
            'P13': {'name': 'Popcorn', 'price': 1.50},
            'P14': {'name': 'Landflakes', 'price': 1.35},
            'P15': {'name': 'D1 Iced Tea', 'price': 1.90},
            'P16': {'name': 'Bickers Chocolate', 'price': 1.45},
            'P17': {'name': 'ToeTac', 'price': 0.75},
            'P18': {'name': 'NutterButter', 'price': 2.10},
            'P19': {'name': 'Latorade', 'price': 2.30},
            'P20': {'name': 'Sour Patch Adults', 'price': 1.95}
        }
        
        self.cart = []
        
        self.create_widgets()
    
    def create_widgets(self):
        title_frame = tk.Frame(self.root, bg="#2c3e50", height=60)
        title_frame.pack(fill=tk.X)
        title_frame.pack_propagate(False)
        
        title_label = tk.Label(title_frame, text="Welcome to VendorIT!", 
                              font=("Arial", 20, "bold"), fg="white", bg="#2c3e50")
        title_label.pack(pady=15)
        
        main_container = tk.Frame(self.root, bg="#f0f0f0")
        main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        left_frame = tk.Frame(main_container, bg="#f0f0f0")
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 15))
        
        products_label = tk.Label(left_frame, text="Available Products", 
                                 font=("Arial", 14, "bold"), bg="#f0f0f0")
        products_label.pack(pady=(0, 15))
        
        products_canvas_frame = tk.Frame(left_frame, bg="white", relief=tk.RIDGE, bd=2)
        products_canvas_frame.pack(fill=tk.BOTH, expand=True)
        
        canvas = tk.Canvas(products_canvas_frame, bg="white", highlightthickness=0)
        scrollbar = tk.Scrollbar(products_canvas_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="white")
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        for product_id, item in self.products.items():
            product_frame = tk.Frame(scrollable_frame, bg="white", pady=5)
            product_frame.pack(fill=tk.X, padx=10, pady=5)
            
            info_label = tk.Label(product_frame, 
                                 text=f"{product_id}: {item['name']} - ${item['price']:.2f}",
                                 font=("Arial", 11), bg="white", anchor="w")
            info_label.pack(side=tk.LEFT, fill=tk.X, expand=True)
            
            add_btn = tk.Button(product_frame, text="Add to Cart", 
                              command=lambda pid=product_id: self.add_to_cart(pid),
                              bg="#27ae60", fg="white", font=("Arial", 9, "bold"),
                              width=12, cursor="hand2")
            add_btn.pack(side=tk.RIGHT, padx=5)
        
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        right_frame = tk.Frame(main_container, bg="#f0f0f0", width=300)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH)
        right_frame.pack_propagate(False)
        
        cart_label = tk.Label(right_frame, text="Your Cart", 
                            font=("Arial", 14, "bold"), bg="#f0f0f0")
        cart_label.pack(pady=(0, 15))
        
        cart_frame = tk.Frame(right_frame, bg="white", relief=tk.RIDGE, bd=2)
        cart_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 15))
        
        self.cart_listbox = tk.Listbox(cart_frame, font=("Arial", 10), bg="white", 
                                       selectmode=tk.SINGLE)
        self.cart_listbox.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.total_label = tk.Label(right_frame, text="Total: $0.00", 
                                   font=("Arial", 12, "bold"), bg="#f0f0f0")
        self.total_label.pack(pady=(0, 15))
        
        button_frame = tk.Frame(right_frame, bg="#f0f0f0")
        button_frame.pack(fill=tk.X, pady=(0, 10))
        
        clear_btn = tk.Button(button_frame, text="Clear Cart", 
                            command=self.clear_cart,
                            bg="#e74c3c", fg="white", font=("Arial", 10, "bold"),
                            height=2, cursor="hand2")
        clear_btn.pack(fill=tk.X, pady=(0, 10))
        
        checkout_btn = tk.Button(button_frame, text="Proceed to Checkout", 
                               command=self.checkout,
                               bg="#3498db", fg="white", font=("Arial", 11, "bold"),
                               height=2, cursor="hand2")
        checkout_btn.pack(fill=tk.X)
    
    def add_to_cart(self, product_id):
        self.cart.append(product_id)
        item = self.products[product_id]
        messagebox.showinfo("Item Added", f"{item['name']} added to cart!")
        self.update_cart_display()
    
    def update_cart_display(self):
        self.cart_listbox.delete(0, tk.END)
        total = 0
        
        for product_id in self.cart:
            item = self.products[product_id]
            self.cart_listbox.insert(tk.END, f"{item['name']} - ${item['price']:.2f}")
            total += item['price']
        
        self.total_label.config(text=f"Total: ${total:.2f}")
    
    def clear_cart(self):
        if not self.cart:
            messagebox.showinfo("Cart Empty", "Your cart is already empty!")
            return
        
        if messagebox.askyesno("Clear Cart", "Are you sure you want to clear your cart?"):
            self.cart = []
            self.update_cart_display()
            messagebox.showinfo("Cart Cleared", "Your cart has been cleared!")
    
    def checkout(self):
        if not self.cart:
            messagebox.showwarning("Empty Cart", "Your cart is empty! Please add items before checking out.")
            return
        
        total_amount = sum(self.products[pid]['price'] for pid in self.cart)
        
        payment = simpledialog.askfloat("Payment", 
                                       f"Total amount due: ${total_amount:.2f}\n\nEnter payment amount:",
                                       minvalue=0.0)
        
        if payment is None:
            return
        
        if payment < total_amount:
            messagebox.showerror("Insufficient Payment", 
                               f"Insufficient payment!\nYou need ${total_amount - payment:.2f} more.")
            return
        
        change = payment - total_amount
        
        items_list = "\n".join([f"- {self.products[pid]['name']}" for pid in self.cart])
        
        message = "=== TRANSACTION COMPLETE ===\n\n"
        message += "Dispensing items:\n"
        message += items_list
        
        if change > 0:
            message += f"\n\nYour change: ${change:.2f}"
        
        message += "\n\nThank you for your purchase!"
        
        messagebox.showinfo("Transaction Complete", message)
        
        self.cart = []
        self.update_cart_display()

if __name__ == "__main__":
    root = tk.Tk()
    app = VendingMachineGUI(root)
    root.mainloop()