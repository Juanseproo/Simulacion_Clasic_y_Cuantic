import math
def canicas(estado_inicial, matriz_transicion, clicks):
    for k in range(clicks):
        if k >= 1: 
            for i in range(len(result)):
                estado_inicial[i] = result[i] 
            result = [sum(matriz_transicion[i][j] * estado_inicial[j] for j in range(len(estado_inicial))) for i in range(len(matriz_transicion))]
        else:
            result = [sum(matriz_transicion[i][j] * estado_inicial[j] for j in range(len(estado_inicial))) for i in range(len(matriz_transicion))]
    return str(result)

def rendijas_clasic_y_cuantica(vector_estado, matriz_dinamina, clicks):
    for k in range(clicks):
        if k >= 1: 
            for i in range(len(result)):
                vector_estado[i] = result[i] 
            result = [sum(matriz_dinamina[i][j] * vector_estado[j] for j in range(len(vector_estado))) for i in range(len(matriz_dinamina))]
        else:
            result = [sum(matriz_dinamina[i][j] * vector_estado[j] for j in range(len(vector_estado))) for i in range(len(matriz_dinamina))]
    return str(result)
