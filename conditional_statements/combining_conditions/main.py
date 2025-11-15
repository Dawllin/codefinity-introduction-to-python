# The item's discount and stock status have been defined
discounted = False
lowStock = True
#Create a boolean variable promotion that is True 
#if the item is not discounted and sufficiently stocked.
movingProduct = discounted or lowStock
promotion = not lowStock
print ("Is the item eligible for promotion?", promotion)