lista=[
    {'student_id': 1, 'name': 'Jean Castro', 'class': 'V'},
    {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'},
    {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'},
    {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'},
    {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}
]
lista_di_liste=[]
for x in range(len(lista)):
     lista_di_liste.append([])
     for i in lista[x]:
        lista_di_liste[x].append(lista[x][i])
     
print(lista_di_liste)