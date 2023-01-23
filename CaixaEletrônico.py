from collections import Counter

#-------------- Variaveis -------------------#
Dinheiro = {10: 0, 20: 0, 50: 0, 100: 0}        #Registra a quantidade de cedulas do caixa
Cedulas = (100, 50, 20, 10)                          #Valor fixo das cedulas
escolhaMenu = 0                                      #Variavel de Menu

#------------- Menu do caixa -------------------#
print('Bem-vindo! Selecione a opção desejada:\n')

if sum(notas * count for (notas, count) in Dinheiro.items()) == 0:
    print('Atenção! Sem cédulas na máquina, favor repor\n')
    
while True:
    print('\n1 - Reposição de cédulas')
    print('2 - Saque')
    escolhaMenu = input('Opção: ')
#--------------------------------------------------------------------------------------------------#
#                                #Reposição de Cédulas                                             #
#--------------------------------------------------------------------------------------------------# 
    if escolhaMenu == '1':
        print('Especifique a quantidade de notas a serem adicionadas. Caso não adicione uma certa nota, basta pressionar "enter" para ir à próxima.')
        for Notas, Quantidades in Dinheiro.items(): #Para cada valor de nota, deve escolher-se a quantidade a ser inserida
            print('Insira o valor para notas de R$', Notas)
            new_value = input()
            if new_value:           #Caso o input não seja uma string vazia, ele irá adicionar a nova quantia à quantia antiga de cédulas
                new_value = Quantidades + int(new_value)
                Dinheiro[Notas] = new_value
            else:                   #Caso contrario, ele manterá o valor anterior
                pass
        print('O caixa foi reposto. Novas quantias de notas:')
        for NovaNota, NotaQuantidade in Dinheiro.items():
            print('R$',NovaNota, ' ', NotaQuantidade, 'unidades.')
            print('Balanço total em reais: ', sum(Nota * Conta for (Nota, Conta) in Dinheiro.items()))
            
#--------------------------------------------------------------------------------------------------#
#                                #Saque de Dinheiro                                                #
#--------------------------------------------------------------------------------------------------#            
    if escolhaMenu == '2':
        
#---------------------- Função para Contagem de Notas para Saque ----------------------------------#
        
        def QuantasNotas(ValorSaque, ValorNota):
                    global Cedulas, SaldoRestante, Dinheiro, Saque, somaSaldo
                    NotaDS = Dinheiro.get(ValorNota)                #Pega a quantidade de notas do valor que estao disponiveis
                    NotasC = divmod(ValorSaque, ValorNota)          #Dividir o valor de saque pelo valor da nota

                    #NotasC = (Notas possiveis, Valor restante)
                    if NotaDS == None:
                        NotaDS = 0
                    if NotasC[0] <= NotaDS:                         #Quantidade de notas exigidas <= Quantidade de Notas disponiveis
                        Saque.update({ValorNota:NotasC[0]})         #Recebe o maximo de notas
                        SaldoRestante = NotasC[1]                   #Saldo total quitado
                        return Saque, SaldoRestante

                    elif NotasC[0] >= NotaDS and NotaDS != 0:       #Quantidade de notas exigidas > Quantidade de Notas disponiveis e existem notas
                        Saque.update({ValorNota:NotaDS})            #Recebe o maximo de notas
                        SaldoRestante = (NotasC[0] - NotaDS) * ValorNota + NotasC[1]   #Saldo restante é a diferença entre o que foi sacado e o valor anterior + o que restou de saldo da divisão (divmod)
                        return Saque, SaldoRestante
                    
                    elif NotasC[0] >= NotaDS and NotaDS == 0:       #Quantidade de notas exigidas > Quantidade de Notas disponiveis e não há notas
                        Saque.update({ValorNota:0})
                        SaldoRestante = ValorSaque
                        return Saque, SaldoRestante
                    
             
#--------------------------------------------------------------------------------------------------#                
#------------------------------- Função de atualização do dinheiro --------------------------------# 

        def AtualizaDinheiro(Saque):
            global Dinheiro
            Dinheiro = dict(Counter(Dinheiro) - Counter(Saque))
            return Dinheiro

#--------------------------------------------------------------------------------------------------#
#                                #Realizando o saque                                               #
#--------------------------------------------------------------------------------------------------#            

#---------------------------- Variáveis atualizadas a cada saque ----------------------------------#
        Saldo = 0                                       #Saldo do caixa
        ValorSaque = 0                                  #Valor de saque escolhido pelo cliente
        Saque = {10: 0, 20: 0, 50: 0, 100: 0}   #Registra a quantidade de cedulas a serem sacadas

#--------------------------------------------------------------------------------------------------#
        
        somaSaldo = sum(nota * count for (nota, count) in Dinheiro.items())     #Verifica Saldo do caixa
        
        if somaSaldo == 0:                                                      #Caso não hajam cédulas, imprime um erro
            print('Não foi possível realizar a operação, por favor, tente novamente. \nErro: Sem cédulas')
            break
        ValorSaque = int(input('Qual valor voce deseja sacar? '))               #Informando o valor de retirada
        if ValorSaque % 10 != 5:                                                #Apenas valores não divísiveis por 5

            if ValorSaque > 0 and ValorSaque <= somaSaldo:                      #Sequência para checagem de valores, da nota de maior valor para menor valor
                QuantasNotas(ValorSaque, 100)
                if SaldoRestante > 0:
                    QuantasNotas(SaldoRestante, 50)
                    if SaldoRestante > 0:
                        QuantasNotas(SaldoRestante, 20)
                    if SaldoRestante > 0:
                        QuantasNotas(SaldoRestante, 10)
                AtualizaDinheiro(Saque)
                
                SomaSaque = sum(notas * count for (notas, count) in Saque.items())      #Verificando se a soma total do saque é equivalente ao Valor de Saque pedido
                if SomaSaque != ValorSaque:
                    print('Erro. Não é possível liberar este valor')
                    break
            else:                                                                       #Caso o valor de saque seja maior que o saldo, resulta em erro.
                print('Não foi possível realizar a operação, por favor, tente novamente. \nErro: Sem cédulas')
                break

#---------------------------- Imprimindo as cédulas de saque ----------------------------------#
            for cedulas in Saque:
                    print('Voce irá receber', Saque[cedulas], 'nota(s) de R$', cedulas)


