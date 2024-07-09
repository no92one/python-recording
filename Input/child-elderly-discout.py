# Skapa ett programm som räknar ut hur mycket en biljett kostar med olika rabatter.
# Programmet ska fråga användaren om deras ålder och sen svara med vilken 
# priskategori dem tillhör och vad deras biljettpris blir.

# Ordinarie biljett pris är 55 kr.
# Det finns 4 olika kategorier:
# Över 64 år    Kategori: "Pensionär"   Pris: 30% rabatt.
# 19-64 år      Kategori: "Vuxen"       Pris: Ordinarie pris.
# 5-18 år       Kategori: "Ungdom"      Pris: 15% rabatt.
# Under 5 år    Kategori: "Barn"        Pris: Grattis.

age = int(input('Ange din ålder: '))
price = 55

if age < 5:
    price = 0
    group = "Barn"


# age = int(input('\nAnge din ålder: '))
# price = 55
# group = 'Vuxen'

# if age < 5:
#     price *= 0
#     group = 'Barn'
# elif age <= 18:
#     price *= 0.85
#     group = 'Ungdom'
# elif age >= 65:
#     price *= 0.70
#     group = 'Pensionär'

# print(f'{age} år = {group}\nDitt pris blir {price} kr.')