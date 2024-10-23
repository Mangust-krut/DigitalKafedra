# TODO Найдите количество книг, которое можно разместить на дискете

disketa = 1.44*1024*1024
stranici = 100
stroki = 50
simvoli = 25

vsego_simvolov = 100*50*25
ves_knigi = vsego_simvolov*4
kolvo_knig = int(disketa//ves_knigi)
print("Количество книг, помещающихся на дискету:", kolvo_knig)
