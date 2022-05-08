class hotel: #Classe hotel
  def __init__(self,name,stars,normal,weekend):
    #Nome do hotel
    self.nome = name
    #Estrelas que o hotel possui
    self.estrelas = int(stars) 
    #Dicionario que possui os valores de estadia dos dias de semana para sóscios e não-socios
    self.dias_normais = normal
    #Dicionario que possui os valores de estadia dos finais de semana para sóscios e não-socios
    self.fim_semana = weekend
    #Total a ser gasto pelo hospede nesse hotel
    self.total = float(0)
  
  #Função que coloca no total do objeto a quantidade de dinheiro gasto na hospedagem do mesmo
  def precoEstadia(self, tipo,qtd_normais, qtd_finais):
    total = float(self.dias_normais[tipo] * qtd_normais)
    total += float(self.fim_semana[tipo] * qtd_finais)
    self.total = total
