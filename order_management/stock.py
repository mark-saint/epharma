import json
from typing import List
from .product import Product

class Stock:
    """Represents the catalog of products
    
    Attributes:
        products: the list of products
    """
    def __init__(self, products: List[Product]) -> None:
        self.products = products

    def update(self, id: str, change: int):
        """Update the quantity of a product by adding or removing
        
        Args:
            id: identifier of the product
            change: the value by which the quantity should be update (+1 adds 1, -2 removes 2 for example)
        """
        #TODO: Make sure the product exists, and that by making the change, the value is still >= 0
       
        #TODO: Update the quantity

        product = self.getProductByID(id)
        if product is not None and product.quantity + change >= 0:
            product.quantity += change


    def getProductByID(self, id: str) -> Product:
        """Gets a product by its ID

        Args:
            id: identifier of the product
        
        Returns: the product's object
        """
        #TODO: Implement te function

        for product in self.products:
            if product.id == id:
                return product
        return None


        
    def dump(self, outfile: str):
        """Saves the stock to a JSON file"""
        #TODO: Implement the function
        product_list = [product.__dict__ for product in self.products]
        
        # Create a dictionary to store the list of products
        stock_data = {"products": product_list}
        
        # Save the data to the specified JSON file
        with open(outfile, 'w') as f:
            json.dump(stock_data, f, indent=4)
    
    @staticmethod
    def load(infile: str):
        """Loads the stock from an existing file
        
        Args: 
            infile: input file to the function
        """
        with open(infile, 'r') as f:
            stock_data = json.load(f)
            
            # Create a list to store the loaded products
            
            
            for product_dict in stock_data:
                product = Product(
                    code=product_dict["code"],
                    name=product_dict["name"],
                    brand=product_dict["brand"],
                    quantity=product_dict["quantity"],
                    category=product_dict["category"],
                    description=product_dict["description"],
                    price=product_dict["price"],
                    dosage_instruction=product_dict["dosage_instruction"],
                    requires_prescription=product_dict["requires_prescription"]
                )
                self.products.append(product)
        
    
    def __str__(self) -> str:
        """Returns a string representation of the stock
        """
        #TODO: Return the description of the stock with a nice output showing the ID, Name, Brand, Description, Quantity, Price, and the requires_prescription field

        stock_str = ""
        for product in self.products:
            stock_str += f"ID: {product.id}\nName: {product.name}\nBrand: {product.brand}\nDescription: {product.description}\nQuantity: {product.quantity}\nPrice: {product.price}\nRequires Prescription: {product.requires_prescription}\n\n"
        return stock_str