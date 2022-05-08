from enum import Enum #importa o módulo enum

#Enumeração dos dias da semana abreviados e seus números no calendário
class days_week(Enum):
  #Abreviações dos dias que foram usadas nos exemplos do documento .PDF
  #Os valores correspondem aos mesmos valores da função .weekday() retorna
  MON = 0
  TUES = 1
  WED = 2
  THUR = 3
  FRI = 4
  SAT = 5
  SUN = 6

#Enumeração dos meses abreviados e seus números no calendário
class months(Enum):
  #Abreviações comuns de meses em inglês
  JAN = 1
  FEB = 2
  MAR = 3
  APR = 4
  MAY = 5
  JUN = 6
  JUNE = 6
  JUL = 7
  JULY = 7
  AUG = 8
  SEP = 9
  SEPT = 9
  OCT = 10
  NOV = 11
  DEC = 12