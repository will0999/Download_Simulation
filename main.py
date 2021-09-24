from seed import *
from model import *
from classes import *
from jobs import *
from time import sleep

#CARREGANDO COMPUTADORES E RECURSOS NA LISTA DUPLAMENTE ENCADEADA#
computadores = loadComputers()
recursos = loadResources()
comps = ListaDuplamenteEncadeada()
rec = ListaDuplamenteEncadeada()
  
for i in range (len(computadores)):
    comps.inserir_no_final(computadores[i])

for i in range (len(recursos)):
    rec.inserir_no_final(recursos[i])

#Divisão da banda
def divisaoBanda(jobs, banda):
  adicional_banda = 1.1                 #Banda adicional de 10% para os Computadores prioritários
  banda_convertida = banda * 125        #Convertendo banda de Mbps para KBps
  
  normal = 0                            # Contador de pcs normais
  prioritario = 0                       #Contador de pcs prioritarios
  for i in range(len(jobs)):            #Percorrendo a lista de jobs
    if jobs[i].increaseBand == "N":     #Se o PC não for prioritario adiciona +1 para o contador de pcs normais
      normal += 1
    else:
      prioritario += 1                  #else adiciona +1 para o contador de pcs prioritarios

  divisão_normal = banda_convertida/len(jobs)         #A divisão de banda normal dos computadores

  divisão_prioritaria = divisão_normal * adicional_banda    #Divisão de banda para os computadores prioritários

  if prioritario > 0:                     #Se existirem computadores prioritarios
    resto = banda_convertida - (prioritario * divisão_prioritaria)      #Calcula o resto de banda
    if normal > 0:
      banda_prioritaria = resto/normal        #Calcula a banda dos computadores normais caso existam computadores prioritarios
 
    for i in range(len(jobs)):
      if jobs[i].increaseBand == "N":
        jobs[i].banda= float("{:.2f}".format(banda_prioritaria))      #Armazenando o valor da banda dos pcs normais caso existam computadores prioritarios, em KBps com apenas 2 casas decimais.
      elif normal == 0:                                               
        jobs[i].banda= float("{:.2f}".format(divisão_normal))         #Armazenando o valor da banda para os pcs prioritarios caso não exista nenhum pc normal
      else:
        jobs[i].banda= float("{:.2f}".format(divisão_prioritaria))    #Armazenando o valor da banda dos pcs prioritarios
      

  else:       #Se não existirem computadores prioritarios
    for i in range(len(jobs)):
      jobs[i].banda = float("{:.2f}".format(divisão_normal))          #Armazenando o valor da banda dos pcs caso não existam pcs prioritarios


# contador de ciclos
def contadorCiclos(jobs, finalizado,computadores, recursos, cont_ciclos:int = 1, ranges:int = 1):
  
  if(len(jobs) != 0):                                       #Se o tamanho do jobs for diferente de 0 ele inicia a execução
    for i in range(len(jobs)):                              #Pegamos o tamanho da lista para conseguir percorrer por todos os jobs dentro dela
      print(f"\nCiclo {cont_ciclos}")
      jobs[i].baixado += jobs[i].banda
      if float(jobs[i].baixado) > float(jobs[i].tamanho):   #Caso o tamanho já baixado ultrapasse o tamanho do arquivo
        jobs[i].baixado = jobs[i].tamanho                   #O tamanho baixado passa a ser igual ao tamanho total do arquivo
      print(f"\n{jobs[i]} | {jobs[i].baixado} de {jobs[i].tamanho} {(float(jobs[i].baixado) * 100) // float(jobs[i].tamanho)}%") #Printa todas as informações referentes ao job, quanto ja foi baixado, e a porcentagem de download
      sleep(0.5)
      if(float(jobs[i].baixado) >= float(jobs[i].tamanho)):        #Se o tamanho de "baixado" em determinado job for maior ou igual ao tamanho do seu arquiv oa ser baixado
        print(f"\n\033[1;34mO PC {jobs[i].id} DE IP {jobs[i].ip} FINALIZOU O DOWNLOAD DE {jobs[i].arquivo} em {cont_ciclos} ciclos\033[1;37m")
        finalizado.inserir_no_final(jobs[i])                #colocamos o job na lista de finalizados
        jobs[i].ciclo = cont_ciclos                         #contabilizamos quantos ciclos foram precisos para terminar de baixar
        jobs.remove(i)
        #if (len(jobs) != 0):
        #divisaoBanda(jobs, banda)                                  
        if(ranges == cont_ciclos):                                               #saimos do ciclo
          contadorCiclos(jobs, finalizado,computadores, recursos, cont_ciclos,ranges)
    #print(f"ciclo {cont_ciclos}")
    
  else:
    print("finalizado")
    print(cont_ciclos)
    finalizado.imprimir_lista()                            #ao finalizar imprimimos  a lista de jobs
    menu_principal(jobs, finalizado,computadores, recursos)
  cont_ciclos += 1
  ranges +=1
  contadorCiclos(jobs, finalizado,computadores, recursos, cont_ciclos,ranges)

def menu_principal():
    if True:
        finalizado = ListaDuplamenteEncadeada()
        print('-'*50)
        menu= int(input('\n[1]Inserir novo job\n[2]Iniciar simulação\n[3]Listar Jobs existentes\n[4]Remover job\n[5]Fazer a distribuição de banda\n[6]Listar Jobs Finalizados\n[7]Sair\nEscolha uma das opções:'))
        print('\n','-'*50)
        if menu == 7:
            print('Programa encerrado.')
            exit()
        elif menu ==1:
            print('\n \n \n \n ')
            for i in range(len(computadores)):
                print(f'PC [{i+1}]',computadores[i])
                print()
            menu2= int(input('Digite o número correspondente do pc para escolhe-lo para o download de um dos arquivos:'))
            print('\n \n \n \n ')
            for i in range(len(recursos)):
                print(f'RECURSO [{i+1}]',recursos[i])
                print()
            menu3= int(input(f'Agora digite o número correspondente do recurso que o PC [{menu2}] irá fazer o download: '))
            create_job(computadores, recursos, menu2-1, menu3-1, jobs)
            menu_principal()
            return jobs 
            
        elif menu ==2:
            try:
                len(jobs)
                divisaoBanda(jobs, largura_banda)
                contadorCiclos(jobs, finalizado, computadores, recursos)    #começando simulação
            except SuperExceptionsClass as me:
                print(me)
                sleep(1)
                menu_principal()

        elif menu ==3:
            try:
                print(jobs)
                sleep(3)
                menu_principal()
            except SuperExceptionsClass as me:
                print(me)
                sleep(1)
                menu_principal()
        elif menu ==4:
          try:
            print(jobs)
            opçao = int(input('Digite o Job que queira remover:'))
            opçao -= 1
            jobs.remove(opçao)
            menu_principal()
          except SuperExceptionsClass as me:
            print(me)
            sleep(1)
            menu_principal()
        
        elif menu ==5:
          try:
            divisaoBanda(jobs, largura_banda)
            print(jobs)
            sleep(1)
            menu_principal()
          except SuperExceptionsClass as me:
            print(me)
            sleep(1)
            menu_principal()

        elif menu ==6:
          #finalizado.imprimir_lista()
          #sleep(2)
          menu_principal()
        
if __name__ == "__main__":
  print('-'*50)
  largura_banda= int(input('Informe APENAS O NÚMERO da sua largura de banda entre 1Mbps até 50Mbps:'))
  finalizado = ListaDuplamenteEncadeada()
  jobs = ListaCircular()
  menu_principal()

  