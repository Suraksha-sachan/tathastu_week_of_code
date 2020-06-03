cp=float(input("Enter Cost Price"))
sp=float(input("Enter Selling Price"))
profit=sp-cp
print("Profit: ", profit)
newSellingPrice=1.05*profit+sp-profit
print("NewSellingPrice: ",newSellingPrice)
