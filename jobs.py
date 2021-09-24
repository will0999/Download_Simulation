#Implementado a classe dos jobs
class Job:
    def __init__(self, id, ip, arquivo_solicitado, tamanho_arquivo, unidade, increaseBand,larguraBanda = 0 ,tamanhoBaixado = 0, ciclo = 0):
        self.id = id
        self.ip = ip
        self.arquivo = arquivo_solicitado
        self.tamanho = tamanho_arquivo
        self.unidade = unidade
        self.increaseBand = increaseBand
        self.banda = larguraBanda
        self.baixado = tamanhoBaixado
        self.ciclo = ciclo

    def __repr__(self):
        return "id=%s ip=%s arqivoSolicitado=%s tamanhoArquivo=%s%s, increaseBand=%s, largura=%sMbps" % (self.id, self.ip, self.arquivo, self.tamanho, self.unidade, self.increaseBand, float("{:.2f}".format(self.banda/125)))


#Cadastrar Job
#Ao criar um job será passado uma lista duplamente encadeada com comps e outra com recourses, juntamente com o índice dos conts e a lista circular.
def create_job(comps, rec, cont1: int, cont2: int, circular):
  if(rec[cont2].unit == "MB"):
    size_kb = float(rec[cont2].size.replace(",", ".")) * 1024 #Convertendo tamanho do arquivo para Kb
    temp = Job(comps[cont1].id, comps[cont1].ip, rec[cont2].name, size_kb, rec[cont2].unit.replace("MB", "KB"), comps[cont1].increaseBand)
    circular.append(temp)
    return
  temp = Job(comps[cont1].id, comps[cont1].ip, rec[cont2].name, rec[cont2].size, rec[cont2].unit,  comps[cont1].increaseBand)
  circular.append(temp)