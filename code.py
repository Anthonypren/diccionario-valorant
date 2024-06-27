bienvenida=print("hola bienvenido a el diccionario de palabras que no conozcas")

meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "LS":"se refiere a una persona que hizo un tiro de suerte",
            "NS":"se refiere a una persona que hizo un buen tiro",
            "NT":"se refiere a que el equipo o la persona hizo un buen intento en la ronda",
            "XD":"significa que una persona se esta riendo descontroladamente "
            }
            
for i in range(5): 
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("Esta palabra no lo conozco")
