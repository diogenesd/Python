seconds = input("Por favor, entre com o número de segundos que deseja converter: ")

tSeconds = int(seconds)
days = tSeconds // 86400
rSeconds = tSeconds % 86400
hours = rSeconds // 3600
rrSeconds = rSeconds % 3600
minutes = rrSeconds // 60
rrSecondsFinal = rrSeconds % 60

print(days," dias,",hours, "horas,", minutes, "minutos e", rrSecondsFinal, "segundos.")