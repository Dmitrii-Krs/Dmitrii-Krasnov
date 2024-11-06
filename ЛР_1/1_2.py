# TODO Найдите количество книг, которое можно разместить на дискете
Size_disk,Pages,Strings, Quantity_Symbols, Symbol  = round(1.44*(1024**2)), 100, 50, 25, 4
Volume_book = Pages * Strings * Quantity_Symbols * Symbol
result = Size_disk//Volume_book
print("Количество книг, помещающихся на дискету:", result)
