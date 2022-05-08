from .hotel import hotel #Importa a classe hotel para criar os objetos
from .dates_manag import * #Importação das funções para manipulação das datas

#Criação de um dicionário que possui todos os objetos dos hoteis
hotels = {
    "Lakewood": hotel(
      "Lakewood",
      int(3),
      {"Regular":float(110),"Rewards":float(80)},
      {"Regular":float(90),"Rewards":float(80)}
    ),
    "Bridgewood": hotel(
      "Bridgewood",
      int(4),
      {"Regular":float(160),"Rewards":float(110)},
      {"Regular":float(60),"Rewards":float(50)}
    ),
    "Ridgewood": hotel(
      "Ridgewood",
      int(5),
      {"Regular":float(220),"Rewards":float(100)},
      {"Regular":float(150),"Rewards":float(40)}
    )
}

def get_cheapest_hotel(booking):   #DO NOT change the function's name
    #Tira da string o tipo de hospedagem
    tipo = booking[0:7].title()
    #Caso o tipo de hospedagem tenha sido escrito errado
    if (tipo != "Rewards" and tipo != "Regular"):
      return "Error!"
    #Pega todas as datas colocadas pelo usuário e coloca numa lista
    reservas = booking[9:].replace(" ","").split(",")
    #Qtd de dias da semana e finais de semana que o hospede ficará
    qtd_normais = 0
    qtd_finais = 0
    #For para validação de todas as datas
    for x in reservas:
      value = get_dates(x)
      #Caso alguma data não seja válida um erro ocorre
      if(value == -1):
        return "Error!"
      #A data sendo valida, ve se o dia é da semana ou no final dela, adicionando na variavel respectiva
      else:
        if(value == 5 or value == 6):
          qtd_finais += 1
        else:
          qtd_normais += 1
    #Faz as contas de qual hotel é mais vantajoso
    for x,y in enumerate(hotels):
      hotels[y].precoEstadia(tipo, qtd_normais, qtd_finais)
      #Caso seja o primeiro hotel, ele será o escolhido inicialmente
      if(x == 0):
        cheapest_hotel = hotels[y].nome
      else:
        #Não sendo o primeiro hotel, ve se o preço do hotel atual é menor ou ...
        # se a qualidade é melhor pelo mesmo preço 
        if(hotels[y].total < hotels[cheapest_hotel].total) or (hotels[y].total == hotels[cheapest_hotel].total and hotels[y].estrelas > hotels[cheapest_hotel].estrelas):
          cheapest_hotel = hotels[y].nome
    return cheapest_hotel
