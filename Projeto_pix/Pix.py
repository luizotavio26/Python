#%%

class Cliente:
    def __init__(self, nome:str, cpf: str, saldo:float):
        self.nome = nome
        self.__extrato = []
        self.__cpf = cpf
        self.__saldo = saldo

    def get_extrato(self):
        return self.__extrato
    
    def get_cpf(self):
        cpf_exibido = ""
        for i in range(len(self.__cpf)):
            if i > 2 and i < 11 and self.__cpf[i] != '.':
                cpf_exibido += "x"
            else:
                cpf_exibido += self.__cpf[i]
        return cpf_exibido
    
    def get_saldo(self):
        return self.__saldo

    def depositar(self, valor:float):
        self.__saldo+=valor

    def retirar(self, valor:float):
        if valor<= self.__saldo:
            self.__saldo-= valor

        else:
            print(" Saldo insuficiente para realizar a transferência.")

    def realizar_pix(self, valor: float, destinatario: str):
        self.destinatario = destinatario
        if valor<= self.__saldo:
            pix = Pix(self, destinatario, valor)
            pix.executar()
            self.registrar_transacao(pix)
            destinatario.registrar_transacao(pix)

        #se o valor for menor ou igual ao saldo,
        #a variável pix chama a classe Pix,
        #registra a transação pela função registrar_transacao (para o rementente)
        #registra a transacao pro destinatario

        else:
            print("Saldo insuficiente para realizar a transferência.")

    def registrar_transacao(self, transacao):
        self.transacao = transacao
        self.__extrato.append(transacao)

#------------------------------------------------------------------------------#
class Pix:
    def __init__(self, remetente:Cliente, destinatario:Cliente, valor: float):
        self.__remetente = remetente
        self.__destinatario = destinatario
        self.__valor = valor

    def executar(self):
        if self.__remetente. get_saldo() >= self.__valor:
            self.__remetente.retirar(self.__valor)
            self.__destinatario.depositar(self.__valor)

        # se o saldo do remetente for menor ou igual ao valor digitado,
        # retira o valor do remetente  usando a função retirar
        # deposita ao destinatário usando a função depositar

        else:
            print("Saldo insuficiente para realizar a transferência.")



    def exibir_informacoes(self):
        print("Rementente:", self.__remetente.get_cpf())
        print("Destinatário:", self.__destinatario.get_cpf())
        print("Valor: R$", self.__valor)

    # mostra o cpf do remetente, parcialmente
    # mostra o cpf do destinatário, parcialmente
    # mostra o valor da transação

#--------------------------------------------------------------------------#
cliente1 = Cliente("Maria", "123.456.789-00", 1000.0)
cliente2 = Cliente("João", "987.654.321-00", 500.0)

print(f"Saldo do cliente {cliente1.nome}: R${cliente1.get_saldo()}")
print(f"Saldo do cliente {cliente2.nome}: R${cliente2.get_saldo()}")  

cliente1.realizar_pix(200.0, cliente2)

print(f"Saldo do cliente {cliente1.nome}: R${cliente1.get_saldo()}")
print(f"Saldo do cliente {cliente2.nome}: R${cliente2.get_saldo()}")

extrato_c1 = cliente1.get_extrato()
for pix in extrato_c1:
    pix.exibir_informacoes()

extrato_c2 = cliente2.get_extrato()
for pix in extrato_c2:
    pix.exibir_informacoes()

cliente2.realizar_pix(9000.0, cliente1)

# %%
