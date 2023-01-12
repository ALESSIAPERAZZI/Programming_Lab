#creare un oggetto CSVFile che rappresenti un file CSV e che:
#venga inizializzato sul nome del file csv
#abbia un attributo "name" che contenga il nome
#abbia un metodo "get_data()" che torni i dati del file csv come lista di liste
#fare la prova con "shampoo_sales.csv"
            
class CSVFile():
    def __init__(self, name):
        self.name = name
    
    def get_data(self):
        my_file = open('shampoo_sales .csv','r') 
        my_list = []
        for line in my_file:
           elements = line.split(',')
           if elements[0] != 'Date':
               my_list.append(elements)
        my_file.close()
        
        return my_list

vendite = CSVFile('shampoo_sales .csv')
print(vendite.name)
print(vendite.get_data())