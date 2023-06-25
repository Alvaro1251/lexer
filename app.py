ESTADO_FINAL = "ESTADO FINAL"
ESTADO_NO_FINAL = "NO ACEPTADO"
ESTADO_TRAMPA = "EN ESTADO TRAMPA"

def automata_si(lexema):
    estado_actual = 0
    estados_finales=[2]
    for caracter in lexema:
        if estado_actual == 0 and caracter == 's':
            estado_actual = 1
        elif estado_actual == 1 and caracter == 'i':
            estado_actual = 2
        else:
            estado_actual = -1
            break
        
    if estado_actual == -1:
        return ESTADO_TRAMPA
    if estado_actual in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL

def automata_sino(lexema):
    estado_actual = 0
    estados_finales=[4]
    for caracter in lexema:
        if estado_actual == 0 and caracter == 's':
            estado_actual = 1
        elif estado_actual == 1 and caracter == 'i':
            estado_actual = 2
        elif estado_actual == 2 and caracter == 'n':
            estado_actual = 3
        elif estado_actual == 3 and caracter == 'o':
            estado_actual = 4
        else:
            estado_actual = -1
            break
        
    if estado_actual == -1:
        return ESTADO_TRAMPA
    if estado_actual in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL

def automata_entonces(lexema):
    estado_actual = 0
    estados_finales = [8]
    for caracter in lexema:
        if estado_actual == 0 and caracter == 'e':
            estado_actual = 1
        elif estado_actual == 1 and caracter == 'n':
            estado_actual = 2
        elif estado_actual == 2 and caracter == 't':
            estado_actual = 3
        elif estado_actual == 3 and caracter == 'o':
            estado_actual = 4
        elif estado_actual == 4 and caracter == 'n':
            estado_actual = 5
        elif estado_actual == 5 and caracter == 'c':
            estado_actual = 6
        elif estado_actual == 6 and caracter == 'e':
            estado_actual = 7
        elif estado_actual == 7 and caracter == 's':
            estado_actual = 8
        else:
            estado_actual = -1
            break
        
    if estado_actual == -1:
        return ESTADO_TRAMPA
    if estado_actual in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL

def automata_oprel(lexema):
    estado_actual = 0
    estados_finales = [1, 2]
    for caracter in lexema:
        if estado_actual == 0 and caracter == '<':
            estado_actual = 1
        elif estado_actual == 0 and caracter == '>':
            estado_actual = 1
        elif estado_actual == 1 and caracter == '=':
            estado_actual = 2
        else:
            estado_actual = -1
            break
    
    if estado_actual == -1:
        return ESTADO_TRAMPA
    if estado_actual in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL
    
TOKENS_POSIBLES = [("si", automata_si),("entonces", automata_entonces),("sino", automata_sino)]

def lexer(codigo_fuente):
    tokens = []
    posicion_actual = 0
    while posicion_actual < len(codigo_fuente):
        while codigo_fuente[posicion_actual].isspace():
            posicion_actual = posicion_actual + 1
        
        comienzo_lexema = posicion_actual
        posibles_tokens = []
        posibles_tokens_con_un_carcter_mas = []
        lexema = ""
        var_aux_todos_en_estado_trampa = False

        while not var_aux_todos_en_estado_trampa:
            var_aux_todos_en_estado_trampa = True
            lexema = codigo_fuente[comienzo_lexema:posicion_actual+1]
            posibles_tokens = posibles_tokens_con_un_carcter_mas
            posibles_tokens_con_un_carcter_mas = []

            for (un_tipo_de_token, afd) in TOKENS_POSIBLES:
                simulacion_afd = afd(lexema)
                if simulacion_afd == ESTADO_FINAL:
                    posibles_tokens_con_un_carcter_mas.append(un_tipo_de_token)
                    var_aux_todos_en_estado_trampa = False
                elif simulacion_afd == ESTADO_NO_FINAL:
                    var_aux_todos_en_estado_trampa = False
            
            posicion_actual = posicion_actual + 1
        
        if len(posibles_tokens) == 0:
            print("ERROR: TOKEN DESCONOCIDO" + lexema)
        
        un_tipo_de_token = posibles_tokens[0]

        token = (un_tipo_de_token, lexema)
        tokens.append(token)

    return tokens 




