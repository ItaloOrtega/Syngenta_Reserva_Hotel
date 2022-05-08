from datetime import datetime #Importação do modulo de data para verificar se a data é valida
from .dates import * #Importação das classes de dias da semana e meses

#Retorna o número do dia da semana escrito pelo usuário
def get_day(day_str):
  value = -1
  for x in days_week:
    if day_str.upper() == x.name:
      value = x.value

  return value

#Retorna o número do mês escrito pelo usuário
def get_month(month_str):
  value = 0
  for x in months:
    if month_str.upper() == x.name:
      value = x.value

  return value

#Função para retirar dia, mês, ano e dia da semana da entrada do usuário
def get_dates(data):
  ini = 0
  fim = 0
  #Encontrar o dia do mês
  for x,y in enumerate(data):
    try:
      int(y)
    except:
      fim = x
      break
  day = int(data[ini:fim])
  ini = fim
  #Encontrar o mês
  for x,y in enumerate(data[fim:]):
    try:
      int(y)
      fim = x-1
    except:
      pass
  #Recebe o número do mês e o ano
  month = get_month(data[ini:fim])
  year = int(data[fim:fim+4])
  #Receber o número do dia da semana. 0 = Segunda | 6 = Domingo
  day_week = get_day(data[fim+5:len(data)-1])
  value = -1
  #A data escolhida pelo usuário sendo valida, retorna o valor do dia da semana que ela cai
  #Não sendo retorna -1, e é retornado ao usuario a mensagem de "Error!"
  try:
    #If que executa a função de verificar o dia da semana dessa data
    #A data não sendo possivel no calendario ou o dia da semana escrito pelo usuário nessa data sendo incorreto
    #Gera um erro
    if(datetime(year, month, day).weekday() == day_week):
      value = day_week
  except:
    pass
  return value