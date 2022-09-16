import random
import time
import os

#-----------Colores-----------
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
preguntas = {
    RED + "¿Que es lo siempre lleva el capitan Jack Sparrow en su bolsillo?\n" + RESET:
    "Una brujula",
    RED + "¿Cual es el barco que desea el capitan Jack Sparrow?\n" + RESET:
    "Perla Negra",
    RED + "Anteriormente el capitan Jack Sparrow fue abandonado en una isla por Barbossa. ¿Que es lo que le dio Barbossa?\n" + RESET:
    "Una pistola con una bala",
    RED + "¿Cuándo accede Jack a ayudar a Will?\n" + RESET:
    "Cuando sabe quien es el padre de Will",
    RED + "¿Donde va escondido Jack para poder escapar de la prisión al principio de la película?" + RESET:
    "En un ataud",
    RED + "¿Cómo se llama el barco fantasma de Piratas del Caribe?" + RESET:
    "El holandes errante",
    RED + "¿A qué destino llegan Barbossa, Turner y Swann en la película 'En el fin del mundo?'" + RESET:
    "Singapur",
    RED + "¿Qué personaje interpreta el actor Bill Nighy?" + RESET:
    "Davy Jones",
    RED + "La joven aristócrata Elizabeth Swann vive enamorada en secreto de su amigo de la infancia:" + RESET:
    "Will Turner",
    RED + "Hechicera con poderes de práctica vudú, astuta, mística, cautivadora y de belleza exotica del cual se encruentra enamorado Davy Jones." + RESET:
    "Calypso",
    RED + "Quien apuñale el corazón de Davy Jones se hará inmortal ¿Recuerda quién terminó apuñalandolo?" + RESET:
    "Will Turner",
    RED + "Nombre de mono del capitan Barbossa." + RESET:
    "Jack",
    RED + "Por cada 10 años en el mar, solo podía estar 1 dia en tierra firme ¿quién debe cumplir con esta regla?" + RESET:
    "El capitan del Holandes Errante",
    RED + "¿Que personaje interpretó Johnny Depp en Piratas del Caribe?" + RESET:
    "Jack Sparrow",
    RED + "¿Qué ocupación tiene James Norrington en Piratas del Caribe 1?" + RESET:
    "Comodoro"
}

opciones = {
    0: ["Una pistola", "Una cantiplora", "Un reloj", "Una brujula"],
    1: ["Holandez Errante", "Perla Negra", "Poseidon", "Sol naciente"],
    2: [
        "Comida", "Una pistola con una bala", "2 barriles de vino",
        "Una bala de cañon"
    ],
    3: [
        "Cuando sabe que es un herrero", "Cuando sabe que puede ser pirata",
        "Cuando sabe quien es el padre de Will",
        "Cuando sabe que Will es seguidor del comodoro Norrington"
    ],
    4: ["En un ataud", "En un barco", "En un barril", "En un submarino"],
    5: [
        "El holandes fantastico", "El holandes temido", "El holandes errante",
        "Ninguno de los anteriores"
    ],
    6: ["China", "Tailandia", "Singapur", "Hong Kong"],
    7: ["Davy Jones", "Davy Smith", "Davy Williams", "Davy Johanssen"],
    8: ["Jack Sparrow", "Joshamee Gibbs", "Will Turner", "James Norrington"],
    9: ["Tia Dalma", "Calypso", "Elizabeth", "Angelica"],
    10: ["Will Turner", "Jack Sparrow", "Diosa Calypso", "Barba Negra"],
    11: ["Jack", "Jango", "Sol", "Lucas"],
    12: [
        "El capitan del Holandes Errante", "El capitan del Perla Negra",
        "El capitan del Venganza de la Reina Ana", "El capitan del Interceptor"
    ],
    13: ["Edward Teach", "Hector Barbossa", "Jack Sparrow", "Joshamee Gibbs"],
    14: ["Tripulante", "Comodoro", "Maestre", "Oficial"]
}

comentarios_opciones = {
    "Una pistola":
    "\nIncorrecto, aunque si se puede llevar en un bolsillo",
    "Una cantiplora":
    "\nIncorrecto, no es algo que Jack Sparrow cargaria",
    "Un reloj":
    "\nIncorrecto, Jack Sparrow no tiene nocion del tiempo",
    "Una brujula":
    "El siempre lleva su brujula ya que le indica el camino a lo que mas desea"
    + RESET,
    "V":
    "Jack Sparrow obtuvo su brujula de Tia Dalma",
    "Holandez Errante":
    "\nIncorrecto, aunque si le tiene un cierto gusto por este barco",
    "Perla Negra":
    "Jack siempre quiso el perla negra porque simboliza la libertad " + RESET,
    "Poseidon":
    "\nIncorrecto. El poseidon nunca existio, poseidon es el dios del mar",
    "Sol naciente":
    "\nIncorrecto. Este es un nombre inventado",
    "W":
    "Jack Sparrow odia a Barbosa, porque tiene el Perla Negra",
    "Comida":
    "\nIncorrecto. Aunque puede llegar a sobrevivir un tiempo",
    "Una pistola con una bala":
    "Barbossa  le dio una pistola con una bala para que acabe con su sufrimiento en caso de que no soportase la soledad"
    + RESET,
    "2 barriles de vino":
    "\nIncorrecto. El vino solo le serviria para embriagarse o pasar el rato",
    "Una bala de cañon":
    "\nIncorrecto. No podria hacer nada con una bala de cañon",
    "X":
    "Jack Sparrow paso tiempo en una isla y se salvo gracias a unos traficantes de licor",
    "Cuando sabe que es un herrero":
    "\nIncorrecto. Jack lo conoce mientras estaba escapando ",
    "Cuando sabe que puede ser pirata":
    "\nIncorrecto. Jack no sabia nada del pasado ni quien era Will",
    "Cuando sabe quien es el padre de Will":
    "Jack se entera que el padre de will es Bill Turner" + RESET,
    "Cuando sabe que Will es seguidor del comodoro Norrington":
    "\nIncorrecto. Will no es seguidor de nadie, el solo estaba ayudando a atrapar a un pirata",
    "Y":
    "Jack se da cuenta del padre del Will por un medallon",
    "En un ataud":
    "Jack escapa de la ciudad en un ataúd tirado al mar usando la pata del muerto como remo",
    "En un barco":
    "\nIncorrecto. Jack no tenia un barco con que escapar, ni tripulacion",
    "En un barril":
    "\nIncorrecto. Jack no escapa usando un barril, aunque pudo escapar en eso",
    "En un submarino":
    "\nIncorrectoLos submarinos no existian en esa epoca",
    "Z":
    "Jack escapa de una isla desertica usando tortugas",
    "El holandes fantastico":
    "\nIncorrecto. Es un nombre inventado",
    "El holandes temido":
    "\nIncorrecto. El holandes era temido, pero no es su nombre",
    "El holandes errante":
    "Este es su verdadero nombre",
    "China":
    "\nIncorrecto. No llegan a China",
    "Tailandia":
    "\nIncorrecto. No llegan a Tailandia",
    "Singapur":
    "Los 3 llegan a Singapur",
    "Hong Kong":
    "\nIncorrecto. No llegan a Hong Kong",
    "Davy Jones":
    "Es un demonio marino conocido como el 'Señor de los Siete Mares'",
    "Davy Smith":
    "\nIncorrecto. Es un luchador profesional británico.",
    "Davy Williams":
    "\nIncorrecto. Es el personaje ficticio de la serie Desperate Housewives de la ABC",
    "Davy Johanssen":
    "\nIncorrecto. Es un cantante, compositor y actor estadounidense",
    "Jack Sparrow":
    "\nIncorrecto. Elizabeth le da un beso a Jack, pero no esta enamorada.",
    "Joshamee Gibbs":
    "\nIncorrecto. Es la mano derecha de Jack Sparro y no tiene nada que ver con Elizabeth",
    "Will Turner":
    "Es el único hijo de Bootstrap Bill Turner, amigo de la infancia de Elizabeth y quien apuñala el corazon de Davy Jones",
    "James Norrington":
    "\nIncorrecto. Es el comodoro de Port Royal quien pidio su mano en matrinomio",
    "Tia Dalma":
    "\nIncorrecto. Es el nombre de calypso cuando esta en su forma humana",
    "Calypso":
    " Es una diosa del mar en la mitología griega que vivió en la isla de Ogigia",
    "Diosa Calypso":
    " \nIncorrecto. Es una diosa del mar en la mitología griega que vivió en la isla de Ogigia",
    "Elizabeth":
    "\nIncorrecto. Es la joven hija del gobernador Weatherby Swann de Port Royal",
    "Angelica":
    "\nIncorrecto. Es la hija de Barba Negra",
    "Barba Negra":
    "\nIncorrecto. Es el pirata mas temido en el Caribe",
    "Jack":
    "Es el nombre del mono que siempre acompaña a Barbosa",
    "Jango":
    "\nIncorrecto. Es un nombre comun, que se le colocan a ciertos primates en el zoologico",
    "Sol":
    "\nIncorrecto. Nombre para un simio que parece iluminar algo",
    "Lucas":
    "\nIncorrecto. Nombre de un pato en Looney Toons",
    "El capitan del Holandes Errante":
    "Este sufre dicha maldición, por lo que solo puede estar con sus seres queridos 1 dia cada 10 años",
    "El capitan del Perla Negra":
    "\nIncorrecto. Sufria otra maldición, en la que los hace inmortal",
    "El capitan del Venganza de la Reina Ana":
    "\nIncorrecto. Barab negra podia controlar su barco a voluntad",
    "El capitan del Interceptor":
    "\nIncorrecto. No sufre de ninguna maldicion es solo un navio rapido",
    "Edward Teach":
    "\nIncorrecto. Es mas conocido como Barba Negra",
    "Hector Barbossa":
    "\nIncorrecto. Es un pirata activo en el Mar Caribe y el Señor Pirata del Mar Caspio",
    "Tripulante":
    "\nIncorrecto. El no era un tripulante",
    "Comodoro":
    " El era comandante de un buque",
    "Maestre":
    "\nIncorrecto. Es aquel que ocupa la cúspide del poder en un buque",
    "Oficial":
    "\nIncorrecto. Es el encargado general de la embarcación ",
    "Ninguno de los anteriores":
    ""
}


def verificar_respuesta(respuesta, respuesta_input, comentarios, nombre):
    val = 0
    if (respuesta == respuesta_input):
        val = random.randint(15, 38)
        print(GREEN + 'Muy bien ' + RESET + nombre + GREEN + ' acertaste.')
        print(comentarios[respuesta])

        print("\n Tu puntaje aumenta en " + BLUE + str(val) + RESET)
        return val

    elif (respuesta != respuesta_input):
        if (respuesta_input == 'X' or respuesta_input == 'Y'
                or respuesta_input == 'Z' or respuesta_input == 'V'
                or respuesta_input == 'W'):
            val = random.randint(40, 48)
            print(comentarios[respuesta_input])

            print("\n Descubriste el secreto, tu puntaje aumenta en " + BLUE +
                  str(val) + RESET)
            return val
        else:
            val = random.randint(7, 20)
            print(comentarios[respuesta_input])

            print("\n Se te resta un puntaje de " + BLUE + str(val) + RESET)
            return -val


def trivia():
    iniciar_trivia = True
    intentos = 0
    puntaje_por_intento = []
    print(BLUE + "-----------Bienvenido a mi trivia-----------")
    print("La tematica sera sobre Piratas del Caribe")
    print("Para empezar me gustaria saber tu nombre" + RESET)
    nombre = input("Ingresa tu nombre: ").upper()
    while (iniciar_trivia == True):
        intentos += 1

        puntaje_por_pregunta = []
        if (len(puntaje_por_intento) == 1):
            print("Tu puntaje anterior es " + str(puntaje_por_intento[0]))
        elif (len(puntaje_por_intento) > 1):
            print("Los puntajes anteriores son: ", end="")
            for i in puntaje_por_intento:
                print(i, end=" ")

        puntaje = random.randint(0, 11)
        puntaje_por_pregunta.append(puntaje)

        time.sleep(2)
        print(
            GREEN + "\n------------------- Hola " + nombre +
            " -------------\n" + RESET +
            "Lo que tienes que hacer es responder las siguientes preguntas escribiendo la letra de la alternativa que creas correcta y presiona 'Enter' para enviar tus respuesta: \n"
        )
        time.sleep(4)

        print("\n" + nombre + " Inicialmente tienes: " + str(puntaje) +
              " puntos")
        print("\n")
        for i in range(10):
            time.sleep(0.5)
            print(RED + "Cargando" + i * '.' + RESET, end="\r")
        gen_preguntas(preguntas, opciones, comentarios_opciones, nombre,
                      puntaje_por_pregunta)
        time.sleep(4)
        print("\nGracias por jugar a mi Trivia. " + nombre +
              " obtuviste un puntaje de " + BLUE +
              str(sum(puntaje_por_pregunta)) + RESET)

        input("Ingrese Enter para continuar.... \n")
        os.system('clear')
        puntaje_por_intento.append(sum(puntaje_por_pregunta))

        print("\n¿Deseas intentar la trivia nuevamente?")
        repetir_trivia = input(
            "Ingresa 'si' para repetir, o cualquier tecla para finalizar: "
        ).lower()
        if (repetir_trivia == "si"):
            print("Muy bien!! Intenta superar tu puntaje")
        if (repetir_trivia != "si"):
            print("\n" + nombre +
                  " espero  que lo hayas pasado bien, hasta pronto!")
            iniciar_trivia = False


def gen_preguntas(preguntas, opciones, comentario, nombre,
                  puntaje_por_pregunta):
    contador_respuesta = 0

    for elem in preguntas:
        new_val = {'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y', 'Z': 'Z'}
        print(GREEN +
              "-------------------------------------------------------" +
              RESET)
        print(RED + str(contador_respuesta + 1) + ".-" + RESET, elem)
        cont_letter = 0
        random.shuffle(opciones[contador_respuesta])
        for i in opciones[contador_respuesta]:
            new_val[chr(65 + cont_letter)] = i
            print(chr(65 + cont_letter) + ")", i)
            cont_letter += 1
        #new_val[chr(86 + contador_respuesta)] = chr(86 + contador_respuesta)
        contador_respuesta += 1
        print()

        respuesta = input("Ingrese A,B,C o D: ").upper()
        while (respuesta not in new_val):
            respuesta = input(
                "Opción no valida, ingrese una respuesta valida (A,B,C,D):"
            ).upper()
        puntos = verificar_respuesta(preguntas[elem], new_val[respuesta],
                                     comentario, nombre)
        puntaje_por_pregunta.append(puntos)
        new_val.clear()
        time.sleep(3)


trivia()
