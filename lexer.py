# Importante:
# -----------
# importar AFD desde otro archivo (mas prolijo) en orden de relevancia
# En cada uno requerimos:
# - 'tipo': clase de token que reconoce dicho autómata
# - 'delta': dict[(estado, simbolo): estado_siguiente]
# - 'estados_aceptados': list[int]
# - 'estado_inicial': int


#importar archivo con codigos de pruebas, donde la prueba tiene que tener el nombre
from afds import lista_afds
from tests import pruebas
from tests import pruebaserror


def lexer_multiples_afds(codigo_fuente):
    tokens = []
    pos_actual = 0
    n = len(codigo_fuente)

    while pos_actual < n: #while para caracter, tipo define cual AFD es el correcto y lexema devuelve la cadena
        longitud_mejor_match = 0
        tipo_mejor_match = None
        lexema_mejor_match = ''

        for afd in lista_afds: # Recorre con la cadena cada AFD
            tipo, estado_inicial, delta, estados_aceptados = afd
            estado_actual = estado_inicial
            pos_lexema_actual = pos_actual
            ultima_pos_aceptada =-1

            while pos_lexema_actual < n:
                clave = (estado_actual, codigo_fuente[pos_lexema_actual])
                if clave not in delta:
                    break # si no esta es porque va al trampa y se corta
                estado_actual = delta[clave]
                pos_lexema_actual += 1
                if estado_actual in estados_aceptados:
                    ultima_pos_aceptada = pos_lexema_actual

            if ultima_pos_aceptada > pos_actual:
                longitud_lexema_actual = ultima_pos_aceptada - pos_actual
                if longitud_lexema_actual > longitud_mejor_match: #cambio de cual es el aceptado maximal munch
                    longitud_mejor_match = longitud_lexema_actual
                    tipo_mejor_match = tipo
                    lexema_mejor_match = codigo_fuente[pos_actual:ultima_pos_aceptada] #pasa el lexema o conjunto de caracteres

        if longitud_mejor_match == 0:
            raise ValueError(f"Carácter Inesperado en posición {pos_actual}")

        tokens.append((tipo_mejor_match, lexema_mejor_match))
        pos_actual += longitud_mejor_match #arranca del ultimo lugar

    tokens.append(("EOF", "EOF")) #se agrega manual el final de los tokens
    return tokens #salida del lexer con el conjunto de tokens

#for para el formato de listas de pruebas, ejemplo
#pruebas = [
#   "int x = 5;",
#    "float y = 3.14;",
#    "if(x>0){x=x-1;}",

#extender mas para un codigo real

for i, prueba in enumerate(pruebas, start=1):

    print(f"\n--- PRUEBA {i} ---")
    print("Código fuente:")
    print(prueba)
#el try en este se agrega momentaneamente para identificar errores en afd, luego se debe quitar porque deben dar correctos
    try:
        tokens = lexer_multiples_afds(prueba)

        print("Tokens encontrados:")

        for token in tokens:
            print(token)

    except ValueError as e:
        print("ERROR:", e)


# pruebas que deben dar error

for i, prueba in enumerate(pruebaserror, start=1):

    print(f"\n--- PRUEBA ERROR {i} ---")
    print("Código fuente:")
    print(prueba)

    print("El lexer debe dar error")
#se agrega el try para que por mas que de error se continue con la lista
    try:
        tokens = lexer_multiples_afds(prueba)

        print("Tokens encontrados:")

        for token in tokens:
            print(token)

    except ValueError as e:
        print("ERROR DETECTADO CORRECTAMENTE:")
        print(e)