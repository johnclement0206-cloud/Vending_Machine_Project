# Made by: John Clement J. Ibrahim
##### Cybersecurity - Group 1
# Started on: 12/09/2025, 9:04 PM
# Finished on: 12/18/2025, 10:14 AM

import tkinter as tk
from tkinter import messagebox, simpledialog
import random

class VendingMachineGUI:
    def __init__(self, root):
        """Initialize the vending machine GUI with window settings and product inventory"""
        self.root = root
        self.root.title("VendorIT - Vending Machine")
        self.root.geometry("900x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")
        
        # Product inventory with name, price, and randomized stock quantity (1-15)
        self.products = {
            'P01': {'name': 'Galactic Chocolate', 'price': 1.50, 'stock': random.randint(1, 15)},
            'P02': {'name': 'KitterKatter', 'price': 1.25, 'stock': random.randint(1, 15)},
            'P03': {'name': 'Stand Chips', 'price': 1.75, 'stock': random.randint(1, 15)},
            'P04': {'name': 'CodaSoda', 'price': 2.00, 'stock': random.randint(1, 15)},
            'P05': {'name': 'Aquafin', 'price': 1.00, 'stock': random.randint(1, 15)},
            'P06': {'name': 'Blue Bull', 'price': 2.50, 'stock': random.randint(1, 15)},
            'P07': {'name': 'Bazooka Energy Drink', 'price': 2.25, 'stock': random.randint(1, 15)},
            'P08': {'name': 'Caribo Gummy Bears', 'price': 1.30, 'stock': random.randint(1, 15)},
            'P09': {'name': 'Trail Hax', 'price': 1.80, 'stock': random.randint(1, 15)},
            'P10': {'name': 'Chips Sinking', 'price': 1.60, 'stock': random.randint(1, 15)},
            'P11': {'name': 'Pretzels', 'price': 1.40, 'stock': random.randint(1, 15)},
            'P12': {'name': 'El Jugo Apple Juice', 'price': 2.20, 'stock': random.randint(1, 15)},
            'P13': {'name': 'Popcorn', 'price': 1.50, 'stock': random.randint(1, 15)},
            'P14': {'name': 'Landflakes', 'price': 1.35, 'stock': random.randint(1, 15)},
            'P15': {'name': 'D1 Iced Tea', 'price': 1.90, 'stock': random.randint(1, 15)},
            'P16': {'name': 'Bickers Chocolate', 'price': 1.45, 'stock': random.randint(1, 15)},
            'P17': {'name': 'ToeTac', 'price': 0.75, 'stock': random.randint(1, 15)},
            'P18': {'name': 'NutterButter', 'price': 2.10, 'stock': random.randint(1, 15)},
            'P19': {'name': 'Latorade', 'price': 2.30, 'stock': random.randint(1, 15)},
            'P20': {'name': 'Sour Patch Adults', 'price': 1.95, 'stock': random.randint(1, 15)}
        }
        
        # Shopping cart to store selected product IDs
        self.cart = []
        
        # Dictionary to store button references for updating their state
        self.product_buttons = {}
        
        # Create the GUI layout
        self.create_widgets()
    
    def create_widgets(self):
        """Build the complete GUI interface with all frames and widgets"""
        
        # Header section with title
        title_frame = tk.Frame(self.root, bg="#2c3e50", height=60)
        title_frame.pack(fill=tk.X)
        title_frame.pack_propagate(False)
        
        title_label = tk.Label(title_frame, text="Welcome to VendorIT!", 
                              font=("Arial", 20, "bold"), fg="white", bg="#2c3e50")
        title_label.pack(pady=15)
        
        # Main container holding left and right sections
        main_container = tk.Frame(self.root, bg="#f0f0f0")
        main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Left section: Product list
        left_frame = tk.Frame(main_container, bg="#f0f0f0")
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 15))
        
        products_label = tk.Label(left_frame, text="Available Products", 
                                 font=("Arial", 14, "bold"), bg="#f0f0f0")
        products_label.pack(pady=(0, 15))
        
        # Scrollable frame for products
        products_canvas_frame = tk.Frame(left_frame, bg="white", relief=tk.RIDGE, bd=2)
        products_canvas_frame.pack(fill=tk.BOTH, expand=True)
        
        canvas = tk.Canvas(products_canvas_frame, bg="white", highlightthickness=0)
        scrollbar = tk.Scrollbar(products_canvas_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="white")
        
        # Configure canvas scroll region when frame size changes
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Create product entries with stock display
        for product_id, item in self.products.items():
            product_frame = tk.Frame(scrollable_frame, bg="white", pady=5)
            product_frame.pack(fill=tk.X, padx=10, pady=5)
            
            # Product information label with stock count
            stock_status = f"(Stock: {item['stock']})"
            info_label = tk.Label(product_frame, 
                                 text=f"{product_id}: {item['name']} - ${item['price']:.2f} {stock_status}",
                                 font=("Arial", 11), bg="white", anchor="w")
            info_label.pack(side=tk.LEFT, fill=tk.X, expand=True)
            
            # Add to cart button (disabled if out of stock)
            add_btn = tk.Button(product_frame, text="Add to Cart", 
                              command=lambda pid=product_id: self.add_to_cart(pid),
                              bg="#27ae60", fg="white", font=("Arial", 9, "bold"),
                              width=12, cursor="hand2")
            add_btn.pack(side=tk.RIGHT, padx=5)
            
            # Store button reference for later updates
            self.product_buttons[product_id] = {
                'button': add_btn,
                'label': info_label
            }
            
            # Disable button if product is out of stock
            if item['stock'] == 0:
                add_btn.config(state=tk.DISABLED, bg="#95a5a6", cursor="arrow")
        
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Right section: Shopping cart
        right_frame = tk.Frame(main_container, bg="#f0f0f0", width=300)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH)
        right_frame.pack_propagate(False)
        
        cart_label = tk.Label(right_frame, text="Your Cart", 
                            font=("Arial", 14, "bold"), bg="#f0f0f0")
        cart_label.pack(pady=(0, 15))
        
        # Cart items display frame
        cart_frame = tk.Frame(right_frame, bg="white", relief=tk.RIDGE, bd=2)
        cart_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 15))
        
        self.cart_listbox = tk.Listbox(cart_frame, font=("Arial", 10), bg="white", 
                                       selectmode=tk.SINGLE)
        self.cart_listbox.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Total price label
        self.total_label = tk.Label(right_frame, text="Total: $0.00", 
                                   font=("Arial", 12, "bold"), bg="#f0f0f0")
        self.total_label.pack(pady=(0, 15))
        
        # Action buttons frame
        button_frame = tk.Frame(right_frame, bg="#f0f0f0")
        button_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Clear cart button
        clear_btn = tk.Button(button_frame, text="Clear Cart", 
                            command=self.clear_cart,
                            bg="#e74c3c", fg="white", font=("Arial", 10, "bold"),
                            height=2, cursor="hand2")
        clear_btn.pack(fill=tk.X, pady=(0, 10))
        
        # Checkout button
        checkout_btn = tk.Button(button_frame, text="Proceed to Checkout", 
                               command=self.checkout,
                               bg="#3498db", fg="white", font=("Arial", 11, "bold"),
                               height=2, cursor="hand2")
        checkout_btn.pack(fill=tk.X)
    
    def add_to_cart(self, product_id):
        """Add selected product to cart and immediately reduce stock"""
        item = self.products[product_id]
        
        # Check if product is in stock
        if item['stock'] <= 0:
            messagebox.showwarning("Out of Stock", 
                                 f"{item['name']} is currently out of stock!")
            return
        
        # Add product to cart
        self.cart.append(product_id)
        
        # Immediately reduce stock when item is added to cart
        self.products[product_id]['stock'] -= 1
        
        # Update the GUI to reflect new stock level
        self.update_product_display()
        
        messagebox.showinfo("Item Added", f"{item['name']} added to cart!")
        self.update_cart_display()
    
    def update_cart_display(self):
        """Refresh the cart listbox and total price display"""
        self.cart_listbox.delete(0, tk.END)
        total = 0
        
        # Display each item in cart with its price
        for product_id in self.cart:
            item = self.products[product_id]
            self.cart_listbox.insert(tk.END, f"{item['name']} - ${item['price']:.2f}")
            total += item['price']
        
        # Update total price label
        self.total_label.config(text=f"Total: ${total:.2f}")
    
    def update_product_display(self):
        """Update product labels and buttons to reflect current stock levels"""
        for product_id, refs in self.product_buttons.items():
            item = self.products[product_id]
            
            # Update label to show current stock
            stock_status = f"(Stock: {item['stock']})"
            refs['label'].config(
                text=f"{product_id}: {item['name']} - ${item['price']:.2f} {stock_status}"
            )
            
            # Enable or disable button based on stock availability
            if item['stock'] == 0:
                refs['button'].config(state=tk.DISABLED, bg="#95a5a6", cursor="arrow")
            else:
                refs['button'].config(state=tk.NORMAL, bg="#27ae60", cursor="hand2")
    
    def clear_cart(self):
        """Empty the shopping cart and restore stock for all items"""
        if not self.cart:
            messagebox.showinfo("Cart Empty", "Your cart is already empty!")
            return
        
        # Confirm before clearing
        if messagebox.askyesno("Clear Cart", "Are you sure you want to clear your cart?"):
            # Restore stock for each item in the cart
            for product_id in self.cart:
                self.products[product_id]['stock'] += 1
            
            # Clear the cart
            self.cart = []
            
            # Update both displays
            self.update_cart_display()
            self.update_product_display()
            
            messagebox.showinfo("Cart Cleared", "Your cart has been cleared and stock has been restored!")
    
    def checkout(self):
        """Process payment and complete the transaction"""
        if not self.cart:
            messagebox.showwarning("Empty Cart", 
                                 "Your cart is empty! Please add items before checking out.")
            return
        
        # Calculate total amount
        total_amount = sum(self.products[pid]['price'] for pid in self.cart)
        
        # Prompt for payment
        payment = simpledialog.askfloat("Payment", 
                                       f"Total amount due: ${total_amount:.2f}\n\nEnter payment amount:",
                                       minvalue=0.0)
        
        # User cancelled payment dialog - restore stock
        if payment is None:
            # Restore stock for items in cart since payment was cancelled
            for product_id in self.cart:
                self.products[product_id]['stock'] += 1
            
            self.cart = []
            self.update_cart_display()
            self.update_product_display()
            messagebox.showinfo("Checkout Cancelled", "Items have been returned to stock.")
            return
        
        # Validate sufficient payment
        if payment < total_amount:
            # Restore stock for items in cart since payment failed
            for product_id in self.cart:
                self.products[product_id]['stock'] += 1
            
            messagebox.showerror("Insufficient Payment", 
                               f"Insufficient payment!\nYou needed ${total_amount - payment:.2f} more.\n\nItems have been returned to stock.")
            
            self.cart = []
            self.update_cart_display()
            self.update_product_display()
            return
        
        # Calculate change
        change = payment - total_amount
        
        # Note: Stock was already reduced when items were added to cart
        # No need to reduce stock again here
        
        # Create transaction summary
        items_list = "\n".join([f"- {self.products[pid]['name']}" for pid in self.cart])
        
        message = "=== TRANSACTION COMPLETE ===\n\n"
        message += "Dispensing items:\n"
        message += items_list
        
        if change > 0:
            message += f"\n\nYour change: ${change:.2f}"
        
        message += "\n\nThank you for your purchase!"
        
        messagebox.showinfo("Transaction Complete", message)
        
        # Clear cart (stock already reduced)
        self.cart = []
        self.update_cart_display()

if __name__ == "__main__":
    root = tk.Tk()
    app = VendingMachineGUI(root)
    root.mainloop()
