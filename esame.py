class CSVTimeSeriesFile(): # creo la classe

    def __init__(self, name):
        
        # Setto la variabile nome del file sulla quale viene istanziata la classe
        self.name = name

        # Provo ad aprire il file e leggere una riga per verificarne l'esistenza e che sia leggibile
        self.can_read = True
        try:
            my_file = open(self.name, 'r')
            my_file.readline()
        except Exception: # se non si può leggere
            self.can_read = False
    

    def get_data(self):
        
        if not self.can_read:
            
            # Se ho settato can_read a False vuol dire che il file non poteva essere aperto o era illeggibile
            # allora alzo una ExamException
            raise ExamException('errore, file non aperto o illeggibile')
            
            # Esco dalla funzione tornando "niente".
            return None

        else:
            
            # Inizializzo una lista vuota per salvare tutti i dati
            data = []
    
            # riapro il file
            my_file = open(self.name, 'r')

            # Leggo il file linea per linea
            for line in my_file:

                listine = [] # lista che si azzera a ogni riga per salvare le coppie di date - numero passeggeri
                
                # Faccio lo split di ogni linea sulla virgola
                elements = line.split(',')
                
                # Posso anche pulire il carattere di newline dall'ultimo elemento con la funzione strip():
                elements[-1] = elements[-1].strip()
                # in realta' strip() toglie anche gli spazi bianchi all'inizio e alla fine di una stringa.
    
                # Se NON sto processando l'intestazione...
                if elements[0] != 'date':

                    # variabile ausiliara per fare un check su anni e mesi
                    tempo = elements[0].split('-') 
                    
                    if type(tempo[0]) is int: # controllo che gli anni siano interi

                        if type(tempo[1]) is int: # controllo che i mesi siano interi
                            
                            if type(elements[1]) is int: # controllo che il numero di passeggeri sia intero 

                                if elements[1] > 0: # controllo che il numero di passeggeri sia positivo
                                
                                    # Aggiungo alla lista gli elementi di questa linea 
                                    # con la data sotto forma di stringa e il numero di passeggeri
                                    listine.append(elements)

                                    # aggiungo la lista piccola alla lista grande prima che si "azzeri"
                                    data.append(listine)

         # se arrivo al comando append vuol dire che la riga del file è "sana", sennò viene saltata senza alzare eccezioni
            
            # Chiudo il file
            my_file.close()

            # controllo che non ci siano date fuori ordine o duplicate prima di ritornare la lista
            for i in range(0, len(data)):
                
                if elements[0] in data[i] >= elements[0] in data[i+1]:
                    
                    raise ExamException('errore, le date a parità di anno non sono ordinate o sono duplicate')
                    # se ci sono timestamp fuori ordine o duplicati alzo un'eccezione, sennò posso ritornare la lista "data"

            if data == []:
                raise ExamException('errore, nessun valore aveva i requisiti per esser aggiunto alla lista data')
                
            # Quando ho processato tutte le righe, ritorno i dati
            return data

# chiusura classe CSVTimeSeriesFile che ritorna la lista di liste



# creo la funzione per calcolare la lista richiesta dall'esercizio
def detect_similar_monthly_variations(time_series, years):

    # controllo che la lista years sia "sana"
    if years == []:
        raise ExamException('errore, lista anni vuota')

    if len(years) != 2:
        raise ExamException('errore, lista anni con troppi o troppo pochi elementi')

    # controllo che la lista time_series sia sana
    if time_series == []:
        raise ExamException('errore, lista date e passeggeri vuota')

    # controllo che gli anni siano validi
    if type(years[0]) is not int:
        raise ExamException('errore, anno 1 non valido')

    if type(years[1]) is not int:
        raise ExamException('errore, anno 2 non valido')

    if years[0] < 0:
        raise ExamException('errore, anno 1 non valido, negativo')

    if years[1] < 0:
        raise ExamException('errore, anno 1 non valido, negativo')

    if (years[0] - years[1]) != 1:
        raise ExamException('errore, anni non consecutivi')

    if (years[0] - years[1]) != -1:
        raise ExamException('errore, anni non consecutivi')

    # creo una lista per salvare i due anni che ci interessano
    anni1 = []
    anni2 = []

    # creo una lista per salvare il numero dei passeggeri nei due anni che ci interessano
    num_pas1 = []
    num_pas2 = []

    # creo un booleano per valutare se gli anni forniti da years vanno bene
    esiste1 = False

    for i in range(0, len(time_series)): # guardo le listine una ad una

        for elements in time_series[i]:
            
            tempo = elements.split('-')  # diviso l'anno dal mese
            
            if tempo[0] == years[0]:

                esiste1 = True # se va bene, cambio il booleano

                try:
                    anni1.append(time_series[i]) # aggiungo alla lista anni solo quelli che mi interessano
                except:
                    raise ExamException('impossibile aggiungere alla lista anni1 questo elemento')

    # se l'esistenza è ancora falsa, sollevo un'eccezione
    if esiste1 is False:
        raise ExamException('anno 1 non presente nella time series')

    # creo un altro booleano per valutare se gli anni forniti da years vanno bene
    esiste2 = False

    for i in range(0, len(time_series)): # guardo le listine una ad una

        for elements in time_series[i]:
            
            tempo = elements.split('-')  # diviso l'anno dal mese
            
            if tempo[0] == years[1]:

                esiste2 = True # se va bene, cambio il booleano

                try:
                    anni2.append(time_series[i]) # aggiungo alla lista anni solo quelli che mi interessano
                except:
                    raise ExamException('impossibile aggiungere alla lista anni2 questo elemento')

    # se l'esistenza è ancora falsa, sollevo un'eccezione
    if esiste2 is False:
        raise ExamException('anno 2 non presente nella time series')
            
    
    # ora ho due liste con tutti i dati degli anni che vanno bene   
    
    # ora separo il numero di passeggeri in base ai due anni
    
    for elements in anni1:

            tempo = elements[0].split('-')  # diviso l'anno dal mese

            num_pas1[tempo[1] - 1] = elements[1]

    for elements in anni2:

            tempo = elements[0].split('-')  # diviso l'anno dal mese

            num_pas2[tempo[1] - 1] = elements[1]
    

        # in questo modo ho creato le due liste con il numero dei passeggeri collocate in ordine di mesi
        # nella posizione mese-1 (es. gennaio = 0)

    # controllo che le due liste abbiano entrambe 12 elementi
    if num_pas1 == []:
        raise ExamException('errore, la lista dei passeggeri del primo anno è vuota')

    if num_pas2 == []:
        raise ExamException('errore, la lista dei passeggeri del secondo anno è vuota')

    if num_pas1 is not list:
        raise ExamException('errore, la lista dei passeggeri del primo anno non è una lista')

    if num_pas2 is not list:
        raise ExamException('errore, la lista dei passeggeri del secondo anno non è una lista')

    # aggiungo nelle posizioni mancanti i valori non se non sono già occupate dal numero di passeggeri
    if len(num_pas1) != 12:
        for i in range(0, 11):
            if num_pas1[i] is not None:
                pass
            else:
                num_pas1[i] = None

    if len(num_pas2) != 12:
        for i in range(0, 11):
            if num_pas2[i] is not None:
                pass
            else:
                num_pas2[i] = None
    
    # creo due liste per salvare le variazioni del numero di passeggeri nelle coppie di mesi vicine
    variations_1 = []
    variations_2 = []

    for i in range(0, len(num_pas1) - 1): # vengono fuori 11 sottrazioni da 12 mesi, e l'ultima sottrazione è 11-10 (dic - nov)

        if num_pas1[i] is None:
            
            risultato = None

        elif num_pas1[i + 1] is None:
            
            risultato = None
            
        else:
            
            risultato = num_pas1[i+1] - num_pas1[i]

        variations_1.append(risultato) 
        # ho creato la prima lista di sottrazioni gia riordinate in base al mese

    for i in range(0, len(num_pas2) - 1): # vengono fuori 11 sottrazioni da 12 mesi, e l'ultima sottrazione è 11-10 (dic - nov)

        if num_pas2[i] is None:
            
            risultato = None

        elif num_pas2[i + 1] is None:
            
            risultato = None
            
        else:
            
            risultato = num_pas2[i+1] - num_pas2[i]

        variations_2.append(risultato) 
        # ho creato la seconda lista di sottrazioni anche queste ordinate in base al mese

    # controllo che le liste delle variazioni siano "sane"
    if variations_1 == []:
        raise ExamException('errore, la lista delle variazioni del primo anno è vuota')

    if variations_2 == []:
        raise ExamException('errore, la lista delle variazioni del secondo anno è vuota')

    if len(variations_1) != 11:
        raise ExamException('errore, la lista delle variazioni del primo anno non ha 11 elementi')

    if len(variations_2) != 11:
        raise ExamException('errore, la lista delle variazioni del secondo anno non ha 11 elementi')

    if variations_1 is None:
        raise ExamException('errore, la lista delle variazioni del primo anno non ha valori')

    if variations_2 is None:
        raise ExamException('errore, la lista delle variazioni del secondo anno non ha valori')
    
    # creo una lista per salvare i true o false che concludono l'esercizio
    finish = []

    for j in range(0, len(variations_1)): # le due liste hanno la stessa lunghezza quindi è indifferente

        if variations_1[j] is None:

            finish.append(False) # se un solo valore dei due è None, si mette False

        if variations_2[j] is None:

            finish.append(False) # se un solo valore dei due è None, si mette False
            
        if (-2 <= (variations_1[j] - variations_2[j]) <= 2):

            finish.append(True) # se sono simili, si mette True

        else:

            finish.append(False) # in ogni altro caso, si mette False

    return finish
    # ritorno la lista di true e false

    
# creo la classe apposita per alzare le eccezioni
class ExamException(Exception):
    pass


    
# per testare il programma
# time_series_file = CSVTimeSeriesFile(name = 'data.csv')
# time_series = time_series_file.get_data()
# years = [1949, 1950]
# risultato = detect_similar_monthly_variations(time_series, years)
#print(risultato)
