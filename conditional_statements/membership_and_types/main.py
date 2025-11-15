# Product details
description = "Imported honey, raw and unfiltered"
price = "5.99"
count = 120
#Use membership operators to check if the substrings "raw" and "Imported" are in the description variable.
contains_raw = "raw" in description
contains_Imported= "Imported" in description
#Use the type() function to check if
price_is_float = type(price) == float
count_is_int = type(count) == int
#Output
print("Contains 'raw':", contains_raw)
print("Contains 'Imported':", contains_Imported)
print("Is price a float?:", price_is_float)
print("Is count an integer?:", count_is_int)