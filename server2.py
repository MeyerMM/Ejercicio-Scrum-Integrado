from flask import Flask, jsonify, request
import ast
from nltk.corpus import stopwords

"""
Autores = Juan, Desire y Rafael

Nosotros, el equipo2, realizamos una api con 4 endpoints, intentando realizarlos en los tres mini-springs asignados.
Primero leimos lo que se nos pedia realizar y una vez leido nos dimos cuenta que eran endpoints similares con
restricciones parecidas. Aun así vimos que la mejor opción era repartirnos el trabaja haciendo cada uno un endpoint.
Lo que hicimos en cada spring fue:
    - spring 1: Juan empezó con el endpoint 1, Desire con el 3 y yo(Rafa) empezé con el 2.
    - spring 2: Juan tuvo algun problema con el entorno de de desarrollo y una vez solucionado ya pudo empezar con su tarea.
                Desire acabó su tarea.
                Yo vi como funcionaba la librería ast y como la usabamos todos, compartí la información.
    - spring 3: Desire empezó con el endpoint 4. Y nos dimos cuenta que el endpoint 3 miraba en una lista de palabras 
                y no en una lista de listas. Por lo demas, nos acercabamos a la solucion final de los tres primeros endpoints.

En la fase que tendría que haber sido de integración entre equipos, seguimos con el desarrollo de los endpoints.
Desire terminó los endpoints 3 y 4, antes de que se fuera el cliente. Juan terminó el endpoint 1 una vez se marchó el cliente.
Yo tuve muchos problemas con la librería nltk y hasta bastante tarde no conseguí solucionarlo (ntlk.download('stopwords').
Una vez solucionado, el endpoint funcionaba correctamente. Eso si una vez se marchó el cliente.
Y con esto solo faltaba la integración con el otro equipo que se hizo otro día.
"""

app = Flask(__name__)


@app.route('/filterListSigns/', methods=['GET'])
def filterList1():
    frase = request.args.get('phrase')
    forbidden = ("?", "¿", "¡", "!", " ", ",", ".", ";", ":")
    listas = ast.literal_eval(frase)
    result = []
    listagrande = []


    for lista in listas:
        currentList = ast.literal_eval(str(lista))
        for word in currentList:
            if word not in forbidden:
                result.append(word)
        if result!=[]:
            listagrande.append(result)
        result = []

    return jsonify(listagrande)


@app.route("/filterStopWords/", methods=["GET"])
def sacarStopWords():
    """Quita las stop words de una lista de listas de palabras.

    Para que la libreria stopwords funcione, hay que descargarsela.

    :return: devuelve lista de lista de palabras.
    """

    stopWords = set(stopwords.words('english'))
    phrases = request.args.get("phrases")

    resultadoFinal = []
    listPhrases = ast.literal_eval(phrases)

    for words in listPhrases:
        result = []
        for word in words:
            if word not in stopWords:
                result.append(word)
        resultadoFinal.append(result)

    return jsonify(resultadoFinal)


# Gets a list of list of words and returns the list containing only words with more then 4 letters
@app.route('/filterList/', methods=['GET'])
def filterList():
    phrases = request.args.get('phrase')
    lists = ast.literal_eval(phrases)

    result = []

    for list in lists:
        currentList = ast.literal_eval(str(list))

        for word in currentList:
            if len(word) >= 4:
                result.append(word)

    return jsonify(result)


# Gets a list of list of words and returns information about the number of words in all the list
# the number of list passed and the size of the longest word in the list
@app.route('/listInfo/', methods=['GET'])
def filterLIstList():
    phrases = request.args.get('phrase')
    lists = ast.literal_eval(phrases)

    numword = 0
    wordwithMaxLenght = 0
    numlist = len(lists)

    for list in lists:
        currentList = ast.literal_eval(str(list))
        numword += len(currentList)

        for word in currentList:
            if len(word) > wordwithMaxLenght:
                wordwithMaxLenght = len(word)

    return jsonify({'numberOfList': numlist, 'numberOfWords': numword, 'longestWordLength': wordwithMaxLenght})



app.run(host="127.0.0.1", port=5000, debug=True)