class CSVTimesSeriesFile: #creo la classe per creare la lista di liste

    def __init__(self, name):
        
        # Setto il nome del file
        self.name = name
        

    def get_data(self):

        # Verifico l'esistenza del file e il fatto che non sia vuoto nel get_data
        self.can_read = True
        
        try:
            my_file = open(self.name, 'r')
            my_file.readline()
        except:
            self.can_read = False
        
        if not self.can_read: #se è illeggibile alzo un'eccezione
            raise ExamException ('il file è illeggibile o vuoto')
        
        else:
            
            # Inizializzo una lista vuota per salvare la lista di liste
            data = []
    
            # Apro il file
            my_file = open(self.name, 'r')

            # Leggo il file linea per linea
            for line in my_file:

                coppie = [] #lista che si azzera a ogni ciclo per salvare le coppie
                
                # Faccio lo split di ogni linea sulla virgola
                elements = line.split(',')
    
                # Se NON sto processando l'intestazione...
                if elements[0] != 'epoch':

                   # trasformo in intero nel caso epoch sia un float
                    if type(elements[0]) is float:
                        elements[0] = int(elements[0])
                    
                    # controllo sia un intero
                    if type(elements[0]) is int:

                        #controllo che la temperature sia un valore numerico
                        if type(elements[1]) is int or float:
                            
                            # Aggiungo alla lista gli elementi di questa linea
                            coppie.append(elements)
                            # Aggiungo alla lista principale la mini-lista appena creata prima che venga riazzerata
                            data.append(coppie)

                # se non si verificano tutti gli if costruiti uno dentro l'altro si passa alla linea successiva finchè il ciclo for non termina 
                            
            # Chiudo il file a ciclo terminato
            my_file.close()
            
            # Quando ho processato tutte le righe, ritorno i dati
            return data


# creo la funzione nel corpo principale del programma
def compute_daily_max_difference(time_series):

    #creo la lista per salvare i risultati
    result = []

    # non so come confrontare due epoch e soprattutto come vedere se sono in ordine, soprattutto perche avendo creato una lista di lista sono tutti degli elements[0] in ogni lista  

            
# classe per gli errori
class ExamException(Exception):
    pass


