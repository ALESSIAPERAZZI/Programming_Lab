class CSVFile():
    def __init__(self, name):
        self.name = name

        
    def get_data(self):

        try:
            my_file = open('shampoo_sales .csv','r') 
        except:
            print('stai cercando di aprire un file inesistente, Errore')
     
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