import sys

# Nesse arquivos temos a classe que irá imprimir as batalhas no arquivo battle_log.txt

#Log de batalha
class log:
    def __init__(self,arquivo="battle_log.txt" ) :
        self.terminal = sys.stdout 
        #Para não "perder" a saída do terminal pois ela será modificada, originalmente a saída é configurada para o terminal
        self.log_file = open(arquivo,"w",encoding="utf-8") 
        #Abertura do arquivo para que possa ser escrito
        #utf-8 é a biblioteca geral e moderna que abrange vários caracteres 
        
    def write (self,message ) :
    #"Duplica" o texto para aparecer tanto no terminal quanto no arquivo
        self.terminal.write(message) 
        #Sem isso não apareceria os print no terminal
        self.log_file.write(message) 
        #Escreve no arquivo de texto
        
    def flush (self ) :
    #Envio imediato das informações
        self.terminal.flush() 
        #Para o terminal
        self.log_file.flush() 
        #Para o arquivo
    
    def entrada (self,texto) :
    #Função para "substituir" o input para poder armazenar no arquivo de texto
        texto_usuario = input(texto)
        self.log_file.write(texto_usuario +"\n")
        self.log_file.flush()
        return texto_usuario

    def fechar (self):
    #Para fechar o arquivo prevenindo arquivos corrompidos e informações incompletas
        self.log_file.close()
        sys.stdout = self.terminal
        #Restaurando a saído do programa para o terminal novamente

log_obj = log("battle_log.txt")

sys.stdout = log_obj
#stdout é a saída do código, originalmente é o terminal mas aqui eu transformo em um obj da classe Log
