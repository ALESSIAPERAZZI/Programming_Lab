#scrivere un programma che sommi tutti i valori del file CSV shampoo_sales
#sum_csv(file_name)

values = []
my_file = open('shampoo_sales .csv', 'r')
for line in my_file:
    elements = line.split(',')

    if elements[0] != 'Date':
        date = elements[0]
        value = elements[1]

        values.append(float(value))

def sum_csv(shampoo_sales):
    risultato = 0
    if (len(shampoo_sales) == 0):
        return None
    for item in shampoo_sales:
        risultato = risultato + item
    return risultato


totale = sum_csv(values)
print(totale)