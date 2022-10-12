#class FuncionesDict(): 
def getValues_Dict_in_List_SingleKey(dict):
    #Este sive para cuando tenemos solo una clave y esta clave contiene una lista

    #clave = dict[0] # esto me devuelve la primera clave
    #print(str(dict))
        for item in dict:     #DICT ES UNA LISTA QUE INTERNAMENTE TIENE UN DICCIONARIO (PARA LOS DOS CASOS)
             msg = str(item["L"])
    # for item in dict:
    #    msg = str(item["L"])   # solo funciona para esta clave que le defini en el parametro de la funcion 
    #    # es decir , genera un dict = [{'L': ['Electronica Digital', 'Programacion Orientada a Objetos', 'Programacion Exploratoria']}]
        return str(msg)    #[msg]  Si le devuelvo con corchetes se los agrega

def getValues_Dict_in_List(dict):
    #Este sive para cuando tenemos muchas una claves y esta clave contiene una lista
    # genera un dict = [{'X': 'Introduccion a la Programacion I', 
    # 'Y': ['Analisis Matematico I', 'Algebra I', 'Ciencias de la Computacion I',
    #  'Algebra Lineal', 'Fisica General', 'Matematica Discreta']}]
        for item in dict:
            msg = str(item["X"]) 
            lista_x = item["Y"]
            for item_x in lista_x:
                msg = str(msg) +", "+ str(item_x)         
        return str(msg) 