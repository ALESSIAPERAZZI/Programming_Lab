# classe per gli errori

class ExamException(Exception):
    pass

# classe Diff con il metodo compute()

class Diff():

    # definisco il costruttore
    def __init__(self, ratio = 1):
        self.ratio = ratio

        if ratio is None:
            raise ExamException('non mi hai dato ratio, uso il valore di default 1')
            ratio = 1

        if type(ratio) is not int and type(ratio) is not float:
            raise ExamException('non mi hai dato un ratio numerico, uso il valore di default 1')
            ratio = 1    

        if ratio <= 0:
            raise ExamException('non mi hai dato un ratio < di 0, uso il valore di default 1')
            ratio = 1



    # creo il metodo compute che riceve in input una lista
    def compute(self, lista):

        if lista is None:
            raise ExamException('la lista non esiste')

        if type(lista) is not list:
            raise ExamException('la lista non è una lista')

        if len(lista) == 1 :
            raise ExamException('la lista ha 1 elemento, non posso fare la differenza')

        if len(lista) == 0 :
            raise ExamException('la lista è vuota')

        for item in lista:
            if type(item) is not int and type(item) is not float:
                raise ExamException('la lista non è composta interamente da numeri')


        sottrazioni = []  # creo una lista vuota dove salvare i risultati

        i = 0 # variabile d'appoggio per ciclare la lista

        while(i < len(lista) - 1):

            sottrazione = 0 # serve per resettarla ad ogni ciclo

            sottrazione = lista[i + 1] - lista[i]

            risultato = sottrazione / self.ratio

            sottrazioni.append(risultato)

            i = i + 1

        return sottrazioni

# diff = Diff()
# result = diff.compute([2,4,8,16])
# print(result)