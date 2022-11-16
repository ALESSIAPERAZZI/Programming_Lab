#scrivere una funzione sum_list che sommi tutti gli elementi di una lista
#ricordarsi di coprire il caso della lista vuota

def sum_list(the_list):
    if (len(the_list) == 0):
        return None
    risultato = 0
    for item in the_list:
        risultato = risultato + item
        
    return risultato
   

my_list = []
l = sum_list(my_list)
print(l)