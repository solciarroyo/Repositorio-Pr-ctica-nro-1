def calcular_estadisticas (names, goals, goals_avoided, assists):

    # Ponemos los nombres en una lista utilizando map() y strip() para eliminar los espacios en blanco 
    nombres = list(map(str.strip, names.split(",")))
    
    # Crear el diccionario de estadísticas
    estadisticas = {}
    for i in range(len(nombres)):
        estadisticas[nombres[i]] = (goals[i], goals_avoided[i], assists[i])
    
    return estadisticas