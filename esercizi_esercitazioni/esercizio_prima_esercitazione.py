# classe per gli errori

class ExamException(Exception):
    pass

# classe MovingAverage con il metodo compute()

class MovingAverage():

    # definisco il costruttore
    def __init__(self, finestra):
        self.finestra = finestra

        if type(finestra) is not int:
            raise ExamException('non mi hai dato un valore numerico intero per la finestra')

        if finestra <= 0:
            raise ExamException('non mi hai dato un valore numerico positivo per la finestra')

    # creo il metodo compute che riceve in input una lista
    def compute(self, lista):

        if lista is None:
            raise ExamException('la lista non esiste')

        if type(lista) is not list:
            raise ExamException('la lista non è una lista')

        if len(lista) < self.finestra :
            raise ExamException('la finestra è più grande della lista')

        if len(lista) == 0 :
            raise ExamException('la lista è vuota')

        for item in lista:
            if type(item) is not int and type(item) is not float:
                raise ExamException('la lista non è composta interamente da numeri')


        medie = []  # creo una lista vuota dove salvare i risultati

        i = 0 # variabile d'appoggio per ciclare la lista

        while(i <= (len(lista) - self.finestra)):

            k = 0
            sum = 0

            while(k < self.finestra):

                sum += lista[i + k]
                k = k + 1

            media = sum / self.finestra

            medie.append(media)

            i = i + 1

        return medie    

# moving_average = MovingAverage(2)
# result = moving_average.compute([2, 4, 8, 16])
# print(result)
