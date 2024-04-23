# Recordatorios iniciales

recordatorios = [
    ['2021-01-01', "11:00", "Levantarse y ejercitar"],
    ['2021-05-01', "15:00", "No trabajar"],
    ['2021-07-15', "13:00", "No hacer nada es feriado"],
    ['2021-09-18', "16:00", "Ramadas"],
    ['2021-12-25', "00:00", "Navidad"]
]

# se agrega nuevo evento
recordatorios.append(['2021-02-02', "06:00", "Empezar el Año"])

# Se corrige fecha de evento del día 15 por día 16
for evento in recordatorios:
    if evento[0] == '2021-07-15':
        evento[0] = '2021-07-16'

# se elimina evento del día del trabajo
for evento in recordatorios:
    if 'trabajar' in evento[2].lower():
        recordatorios.remove(evento)

# Se agregan 2 nuevos eventos, cena de navidad y cena de año nuevo
recordatorios.append(['2021-12-24', "22:00", "Cena de Navidad"])
recordatorios.append(['2021-12-31', "22:00", "Cena de Año Nuevo"])

# se ordena la lista
recordatorios.sort()

# Se imprime la lista de eventos con las correcciones solicitadas
for evento in recordatorios:
    print(evento)
