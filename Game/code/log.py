import sys

# Nesse arquivos temos a classe que irá imprimir as batalhas no arquivo battle_log.txt

#Log de batalha
class Log:
    def __init__(self,arquivo="battle_log.txt" ) :
        self.terminal = sys.stdout 
        #Para não "perder" a saída do terminal pois ela será modificada, originalmente a saída é configurada para o terminal
        self.log_file = None 
        self.arquivo = arquivo
    
    def __enter__ (self ) :
        try:
            self.log_file = open("battle_log.txt", "w", encoding="utf-8")
        except (PermissionError, FileNotFoundError) as e:
            print(f"Erro ao abrir o arquivo , ERRO: {e}")
            self.log_file = None
        sys.stdout = self
        return self
        
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
    
    def __exit__ (self, exc_type, exc_value, exc_tb):
        #Parâmetros essenciais para o Python poder fechar caso ocorra algum erro
        sys.stdout = self.terminal
        #Caso ocorra algum erro, o arquivo será fechado
        if self.log_file:
            self.log_file.close()