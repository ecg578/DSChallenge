def recorrer_laberinto(laberinto, inicio, fin):
    # Dimensiones del laberinto
    filas = len(laberinto)
    columnas = len(laberinto[0])
    orientacion = True

    # Lista de direcciones para moverse en el laberinto (arriba, abajo, izquierda, derecha)
    direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Función auxiliar para calcular la distancia heurística (distancia Manhattan)
    def distancia_heuristica(pos_actual):
        return abs(pos_actual[0] - fin[0]) + abs(pos_actual[1] - fin[1])

    def puede_rotar(fila, columna):
        if (fila - 1 >= 0 and fila + 1 < filas and columna - 1 >= 0 and columna + 1 < columnas):
            return (laberinto[fila][columna] == '.' and laberinto[fila - 1][columna] == '.' and laberinto[fila + 1][columna] == '.' and
                    laberinto[fila][columna - 1] == '.' and laberinto[fila][columna + 1] == '.' and
                    laberinto[fila - 1][columna - 1] == '.' and laberinto[fila - 1][columna + 1] == '.' and
                    laberinto[fila + 1][columna - 1] == '.' and laberinto[fila + 1][columna + 1] == '.')

        return False 

    def es_valida(fila, columna):
        return fila >= 0 and fila < filas and columna >= 0 and columna < columnas and laberinto[fila][columna] == '.'

    def hay_camino_transitable(fila, columna, orientacion):
        if orientacion:
            return es_valida(fila, columna - 1) and es_valida(fila, columna + 1) and columna - 1 >= 0

        return es_valida(fila - 1, columna) and es_valida(fila + 1, columna) and fila - 1 >= 0

    def reconstruir_camino(padres, actual):
        camino = []
        while actual in padres:
            camino.append(actual)
            actual = padres[actual]
        return list(reversed(camino))

    # Inicialización
    g_scores = {inicio: 0}
    f_scores = {inicio: distancia_heuristica(inicio)}
    padres = {}
    open_set = [(f_scores[inicio], inicio)]

    while open_set:
        _, actual = min(open_set)

        if actual == fin:
            # Se ha encontrado el camino
            camino = reconstruir_camino(padres, actual)
            pasos_totales = g_scores[actual]
            print(camino)
            return camino, pasos_totales

        try:
            open_set.remove((f_scores[actual], actual))
        except KeyError:
             return [], -1

        for direccion in direcciones:
            nueva_fila = actual[0] + direccion[0]
            nueva_columna = actual[1] + direccion[1]
            nueva_pos = (nueva_fila, nueva_columna)

            if es_valida(nueva_fila, nueva_columna) and hay_camino_transitable(nueva_fila, nueva_columna, orientacion):
                g_score_nueva_pos = g_scores[actual] + 1

                if nueva_pos not in g_scores or g_score_nueva_pos < g_scores[nueva_pos]:
                    padres[nueva_pos] = actual
                    g_scores[nueva_pos] = g_score_nueva_pos
                    f_scores[nueva_pos] = g_score_nueva_pos + distancia_heuristica(nueva_pos)

                    if (f_scores[nueva_pos], nueva_pos) not in open_set:
                        open_set.append((f_scores[nueva_pos], nueva_pos))

        if orientacion and puede_rotar(actual[0], actual[1]):
            orientacion = False
            if puede_rotar(actual[0], actual[1]):
                g_score_rotar = g_scores[actual] + 1
                rotar_pos = (actual[0], actual[1])
                padres[rotar_pos] = actual
                g_scores[rotar_pos] = g_score_rotar
                f_scores[rotar_pos] = g_score_rotar + distancia_heuristica(rotar_pos)
                if (f_scores[rotar_pos], rotar_pos) not in open_set:
                    open_set.append((f_scores[rotar_pos], rotar_pos))

    # No se ha encontrado un camino
    return [], -1

# Ejemplo de uso
laberinto = [
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['#', '.', '.', '.', '#', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '#', '.', '.', '.', '.'],
    ['.', '#', '.', '.', '.', '.', '.', '#', '.'],
    ['.', '#', '.', '.', '.', '.', '.', '#', '.']
]

inicio = (0, 1)
fin = (3, 8)

camino, pasos_totales = recorrer_laberinto(laberinto, inicio, fin)

if camino:
    print("Se encontró un camino:")
    for fila, columna in camino:
        laberinto[fila][columna] = 'O'
    for fila in laberinto:
        print(' '.join(fila))
    print(pasos_totales)
else:
    print(-1)





# Tercer laberinto
laberinto3 = [
    ['.', '.', '.'],
    ['.', '.', '.'],
    ['.', '.', '.'],
]

inicio3 = (0, 1)
fin3 = (3, 2)

camino3, pasos_totales3 = recorrer_laberinto(laberinto3, inicio3, fin3)

if camino3:
    print("Laberinto 3 - Se encontró un camino:")
    for fila, columna in camino2:
        laberinto3[fila][columna] = 'O'
    for fila in laberinto3:
        print(' '.join(fila))
    print(pasos_totales3)
else:
    print(-1)


# Cuarto laberinto
laberinto4 = [
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '#', '.', '.', '.', '.', '#', '.', '.', '.'],
    ['.', '#', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '#', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '#', '.', '.', '.', '#', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
]

inicio4 = (0, 1)
fin4 = (8, 9)

camino4, pasos_totales4 = recorrer_laberinto(laberinto4, inicio4, fin4)

if camino4:
    print("Laberinto 4 - Se encontró un camino:")
    for fila in laberinto4:
        print(' '.join(fila))
    print(pasos_totales4)
else:
    print(-1)
    