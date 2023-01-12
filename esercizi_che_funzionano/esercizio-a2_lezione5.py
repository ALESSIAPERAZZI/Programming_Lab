class CSVFile():
    def __init__(self, name):
        self.name = name
        
        try:
            self.my_file = open('shampoo_sales .csv','r') 
        except Exception as e:
            print('stai cercando di aprire un file inesistente, Errore, il mio errore è {}'.format(e))
    
    def get_data(self):
        
        my_list = []
        for line in self.my_file:
           elements = line.split(',')
           if elements[0] != 'Date':
               my_list.append(elements)
        self.my_file.close()
        
        return my_list

vendite = CSVFile('shampoo_sales .csv')
print(vendite.name)
print(vendite.get_data())