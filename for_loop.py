## for loop ##
# El búcle for se utiliza para repetir una iteración en una colección de datos

scent_oil = ["Bergamot", "Lemon", "Lavender", "Neroli"]

for each in scent_oil:
    print(f"Oil: {each}")
    
    if each == 'Lavender':
        break  # Una condicional más palabra clave (break) rompe el búcle.             
    
else:
    print("\nEnd of loop.")    
    
    
# Ejemplo 2 for loop

numbers = (5, 10)    

for number in numbers:
    print(number)
    
else:
    print("End of loop.")    
    
    
# Ejemplo 3 
# También se puede hacer un búcle a dos colecciones
# utilizando la función zip()

set_of_brands = {"Viktor and Rolf", "Tom Ford", "Burberry"}    
set_of_brands_two = {"Issey Myake", "Jean Paul Gaultier"}

for brand_one, brand_two in zip(set_of_brands, set_of_brands_two):
    print(brand_one)
    print(brand_two)
    
    
else:
    print("End of loop.") 
    

# Ejemplo 4
# Una mejor forma de iterar de manera mas completa
# es utilizando la función enumerate()

names = ["Mark Zuckerberg", "Bill Gates", "Joma Tech"]

for name in enumerate(names):
    print(name)    
    
else:
    print("End.")    
