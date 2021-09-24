#Implementação da super classe de Excessões#
class SuperExceptionsClass(Exception):
    def __init__(self, message):
        super().__init__(message)

#Classe "No" que engloba os atributos de todas as estruturas de dados escolhidas#
class No:
    def __init__(self, carga: object = None, ant: 'No' = None,prox: 'No' = None):
        self.carga = carga
        self.prox = self#prox
        self.ant = ant

    def __str__(self):
        return str(self.carga)


#Implementação da classe LISTA DUPLAMENTE ENCADEADA pra o carregamento dos computadores e recursos#
       
class ListaDuplamenteEncadeada:
    def __init__(self):
        self.cabeca = None
        self.cauda = None  

    def imprimir_lista(self):
        if self.cabeca is None:
            print("Lista vazia")
            return

        atual: 'No' = self.cabeca
        while atual is not None:
            print(atual)
            atual = atual.prox

    def inserir_no_inicio(self, valor: object):
        novo: 'No' = No(valor)
        if self.cabeca is None:
            self.cabeca = self.cauda = novo
        else:        
            novo.prox = self.cabeca
            self.cabeca = novo
            novo.prox.ant = novo

    def inserir_no_final(self, valor):
        novo: 'No' = No(valor)
        if self.cabeca is None:
            self.cabeca = self.cauda = novo
        else:
          novo.ant = self.cauda # O anterior do nó novo será a cauda atual
          novo.ant.prox = novo # O próximo do elemento anterior será o novo elemento a ser inserido
          self.cauda = novo # a cauda passa a ser o elemento novo a ser inserido

    def remover_do_inicio(self):
        if self.cabeca is None:
            print("Lista vazia")
            return
        
        if self.cabeca == self.cauda:
            self.cabeca = self.cauda = None
        else:
            self.cabeca = self.cabeca.prox 
            self.cabeca.ant = None # O anterior da nova cabeça agora passa a apontar para None

    def remover_do_final(self):
        if self.cabeca is None:
            print("Lista vazia")
            return
        
        if self.cabeca == self.cauda:
            self.cabeca = self.cauda = None
        else:
            # Note que agora não é mais necessário percorrer a lista até o final, basta começar navegando pela cauda
            self.cauda = self.cauda.ant # Faz a cauda apontar agora para o penúltimo elemento da lista
            self.cauda.prox = None # o próximo da nova cauda agora passa a pontar para None

    def imprimir_invertido(self):
        atual: 'No' = self.cauda
        while atual is not None:
            print(atual.carga)
            atual = atual.ant

    def remover_de_posicao(self, pos):
      if pos == 0:
        self.remover_do_inicio()
        return

      atual: 'No' = self.cabeca
      contador: int = 0
      while atual is not None:
        if pos == contador:
          atual.ant.prox = atual.prox
          if atual.prox is not None:
            atual.prox.ant = atual.ant
          else:
            self.cauda = atual
        atual = atual.prox
        contador += 1

    def __getitem__(self, indice):
            if isinstance(indice, slice):
                fatia = ListaDuplamenteEncadeada()
                atual: 'No' = self.cabeca
                
                inicio = indice.start if indice.start else 0
                final = indice.stop if indice.stop else self.total

                for i in range(final):
                    if i >= inicio:
                        fatia.append(atual.carga)
                    atual = atual.prox
                return fatia
            else:
                atual: 'No' = self.cabeca
                for i in range(indice): 
                    atual = atual.prox
                return atual.carga


class ListaCircular:
    def __init__(self):
        self.cabeca = None
        self.count = 0
     
    def __repr__(self):
        string = ""
        cont = 0
        if(self.cabeca == None):
            #Lançando exeção caso o usúario tente listar os jobs existentes e não existir jobs
            raise SuperExceptionsClass("Não há jobs.")
          
        string += f"JOB {cont+1}: {self.cabeca.carga}\n"
        cont += 1      
        temp = self.cabeca.prox
        while(temp != self.cabeca):
            string += f"JOB {cont+1}: {temp.carga}\n"
            temp = temp.prox
            cont += 1
        return string
     
    def append(self, carga):
        self.insert(carga, self.count)
        return
     
    def insert(self, carga, index):
        if (index > self.count) | (index < 0):
            #retornando exceção caso o usuário tente adicionar uma carga em um indíce que não tenha na lista.
            raise SuperExceptionsClass(f"Não foi possível inserir o indíce, pois o indice '{index}',não existe na lista ou é menor que 0\nTamanho da lista: {self.count}")   
             
        if self.cabeca == None:
            self.cabeca = No(carga)
            self.count += 1
            return
         
        temp = self.cabeca
        for _ in range(self.count - 1 if index - 1 == -1 else index - 1):
            temp = temp.prox
             
        aftertemp = temp.prox 
        temp.prox = No(carga)
        temp.prox.prox = aftertemp
        if(index == 0):
            self.cabeca = temp.prox
        self.count += 1
        return
     
    def remove(self, index):
        if (index >= self.count) | (index < 0):
            #retornando exceção caso o usuário tente remover um indíce que não tenha na lista.
            raise SuperExceptionsClass(f"Não foi possível remover o indíce, pois o indice '{index}',não existe na lista ou é menor que 0\nTamanho da lista: {self.count}")
         
        if self.count == 1:
            self.cabeca = None
            self.count = 0
            return
         
        before = self.cabeca
        for _ in range(self.count - 1 if index - 1 == -1 else index - 1):
            before = before.prox
        after = before.prox.prox
         
        before.prox = after
        if(index == 0):
            self.cabeca = after
        self.count -= 1
        return
     
    def index(self, carga):
        temp = self.cabeca
        for i in range(self.count):
            if(temp.carga == carga):
                return i
            temp = temp.prox
        return None

    def __len__(self):
        if self.cabeca == None:
            raise SuperExceptionsClass('Lista vazia')

        atual = self.cabeca.prox
        c = 1
        while atual is not self.cabeca:
            c+=1
            atual = atual.prox
        return c

    #Método para conseguir dar print na lista por índice, ex: print(lista[0])
    def __getitem__(self, indice):
            if isinstance(indice, slice):
                fatia = ListaCircular()
                atual: 'No' = self.cabeca
                
                inicio = indice.start if indice.start else 0
                final = indice.stop if indice.stop else self.total

                for i in range(final):
                    if i >= inicio:
                        fatia.append(atual.carga)
                    atual = atual.prox
                return fatia
            else:
                atual: 'No' = self.cabeca
                for i in range(indice): 
                    atual = atual.prox
                #return f"id: {atual.carga.id}\nip: {atual.carga.ip}\narquivo solicitado: {atual.carga.arquivo}\ntamanho do arquivo: {atual.carga.tamanho}{atual.carga.unidade}"
                return atual.carga


    def mostrar(self, indice):
            if isinstance(indice, slice):
                fatia = ListaCircular()
                atual: 'No' = self.cabeca
                
                inicio = indice.start if indice.start else 0
                final = indice.stop if indice.stop else self.total

                for i in range(final):
                    if i >= inicio:
                        fatia.append(atual.carga)
                    atual = atual.prox
                return fatia
            else:
                atual: 'No' = self.cabeca
                for i in range(indice): 
                    atual = atual.prox
                return f"id: {atual.carga.id}\nip: {atual.carga.ip}\narquivo solicitado: {atual.carga.arquivo}\ntamanho do arquivo: {atual.carga.tamanho}{atual.carga.unidade}"


