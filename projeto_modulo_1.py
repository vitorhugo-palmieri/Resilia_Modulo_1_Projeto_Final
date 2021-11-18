import time  

 
def abertura():
    print("\n\n                       Bem vindo ao PROGRAMA APOLLO 23_\n\n")
    time.sleep(2)
    print("  Nessa aventura estamos a bordo da UVB-76, uma nave com destino á Marte")
    print("  A UBV-76 leva três tripulantes: ")
    print("  Valentina Tereshkova, Iuri Gagarin e Robert Oppenheimer\n")
    print("  Eles tem a chance de serem os primeiros seres humanos a pisar em Marte")
    print("  Vamos ajudá-los a fazer parte da História?\n")
    print("  carregando....")
    time.sleep(5)
    decisao=input("\n Digite (1) para embarcar  -  Digite (0) para desistir: ")    
    while decisao!="1" and decisao!="0":
        print("\n Opção não disponivel astronauta!") 
        decisao=input("\n Digite (1) para embarcar  -  Digite (0) para desistir: ")
    if(decisao=="1"):
        continua=True
    else:
        continua=False
        print(" Você digitou 0, e desistiu do jogo!!")    
    return continua
#FUNÇÃO DE ESCOLHA DE PERSONAGEM PELO USUARIO
def escolha_personagem():
    print("_________________________________________________________________________________")
    print("\n                     Escolha um dos nossos três tripulantes   \n")
    print("                    (1) Valentina (2) Iuri (3) Robert     \n")
    opcao=input(" Quem você quer ser nessa missão? ")
    print("_________________________________________________________________________________")
    while opcao !="1" and opcao !="2" and opcao !="3":
        print("\n               Essa opção não é valida astronauta, escolha  1,2 ou 3                    ")
        opcao=input("     Escolha o seu personagem : ")
        print("_________________________________________________________________________________")
    if(opcao=="1"):
        nome_personagem="Valentina"
    elif(opcao== "2"):
        nome_personagem="Iuri"
    else:
        nome_personagem="Robert"         
    print(" \n                 Voce escolheu  {}, prepare-se \n".format(nome_personagem))
    time.sleep(2)
    return nome_personagem  
#DEFINE QUAL FUNÇÃO PERSONAGEM VAI SER RODADA DE ACORDO COM A ESCOLHA DO USUARIO
def jogar(nome_personagem):
    if(nome_personagem=="Valentina"):
        jogando_com_personagem_1(nome_personagem)
    elif(nome_personagem=="Iuri"):
        jogando_com_personagem_2(nome_personagem)
    elif(nome_personagem=="Robert"):
        jogando_com_personagem_3(nome_personagem)      
#FUNÇÃO ILUSTRATIVA DO LANCAÇENTO
def lancamento():
    print(" Contagem regressiva...")
    time.sleep(1)
    print(" 3")
    time.sleep(1)
    print(" 2")
    time.sleep(1)
    print(" 1")
    time.sleep(1)
    print(" 0...\n")
    time.sleep(2)
    print(" O lançamento é iniciado, a fumaça toma conta da plataforma")
    print(" a UVB-76 está cada vez mais distante da terra\n")
    time.sleep(4)
    print(" Alguns minutos depois, nossos astronautas estão no espaço")
    print(" a terra é linda vista de lá")
    time.sleep(4)
    print("\n\n\n")  
#DEFINE CENARIO 1
def cenario_1(nome_personagem):
    print(" Mas, subtamente\n")
    time.sleep(1)
    print(" ACONTECE UMA EXPLOSÃO!\n")
    time.sleep(2)
    print("\n 'Okay Houston, we've had a problem here'\n\n")
    time.sleep(3)
    print(" É necessario ativar o oxigenio reserva da nave, ")
    print(" e no mostrador aparece as seguintes opçoes:\n")
    time.sleep(3)
    print(" (1) O\u2082 - (2) CO\u2082 - (3) H\u2082O\n")
    decisao=input("\n Qual numero {} deve apertar?:  (1) (2) (3): ".format(nome_personagem))     
    while decisao!="1" and decisao!="2" and decisao!="3" :
        print(" Opção não disponivel astronauta, concentração, estamos sufocando!!\n")
        time.sleep(2)
        decisao=input(" Rápido escolha entre: (1) O\u2082 - (2) CO\u2082 - (3) H\u2082O")
    if(decisao=="3"):
        print("\n\n\n\n  VOCE INJETOU ÁGUA NOS DUTOS, NOSSOS TRIPULANTES ESTÃO MORTOS")
        valida_cenario=False
    elif(decisao=="2"):
        print("\n\n\n\n  VOCE INJETOU DIOXIDO DE CARBONO NOS DUTOS, NOSSOS TRIPULANTES ESTAO TODOS MORTOS")
        valida_cenario=False
    elif(decisao=="1"):
        print("\n\n")
        print(" MUITO BEM, puxe o ar e respire, você ativou o oxigenio reserva\n")
        print(" ESSA FOI POR POUCO!!\n\n")
        time.sleep(5)
        print("\n\n")
        valida_cenario=True
    return valida_cenario
#DEFINE CENARIO 2
def cenario_2(nome_personagem):   
    print(" LOGO DEPOIS, {} percebe que a nave está levemente danificada\n".format(nome_personagem))
    time.sleep(3)
    print(" É preciso fazer um reparo, e para isso, precisa fazer um calculo\n ")
    time.sleep(4)
    print(" E no calculo {} precisa saber quanto é o valor de 5\N{SUPERSCRIPT THREE}(cinco ao cubo)\n".format(nome_personagem))
    time.sleep(5)
    print(" Qual o valor que {} esta procurando? \n".format(nome_personagem))
    decisao=input("(1) 15 - (2) 1150 - (3) 125 ")     
    while decisao!="1" and decisao!="2" and decisao!="3" :
        print(" Opção não disponivel, concentração astronauta!!\n")
        time.sleep(2)
        print(" Qual o valor que {} esta procurando?\n".format(nome_personagem))
        decisao=input("(1) 15 - (2) 1150 - (3) 125  ")
    if(decisao=="1"):
        print("\n\n\n\nVOCÊ ERROU, A NAVE DANIFICADA EXPLODE NO ESPAÇO E TODOS MORREM")
        valida_cenario=False
    elif(decisao=="2"):
        print("\n\n\n\nVOCÊ ERROU, A NAVE DANIFICADE EXPLODE NO ESPAÇO E TODOS MORREM")
        valida_cenario=False
    elif(decisao=="3"):
        print("\n\n")
        print(" MUITO BEM, cálculo correto, tudo em ordem!\n")
        time.sleep(5)
        print("\n\n")
        valida_cenario=True
    return valida_cenario
#DEFINE CENARIO 3
def cenario_3(nome_personagem):
    print(" TUDO PARECE BEM\n")
    time.sleep(2)
    print(' A UVB-76 está na órbita de Marte, todos embarcam na capsula de pouso\n')
    time.sleep(3)
    print(" Mas, {} percebe que a velocidade está muito alta".format(nome_personagem))
    print(" eles estão indo em direção ao solo depressa demais\n")
    time.sleep(5)
    print(" Eles estão á uma velocidade de 190 km/h, mas a velocidade para pouso é 50 km/h\n")
    time.sleep(3)
    print(" Quanto {} deve reduzir para atingir os 50 km\h?: \n".format(nome_personagem))
    time.sleep(3)   
    decisao=input(" (1) 40 Km\h (2) 1,40 m/s (3) 140 km/h ")
    while decisao!="1" and decisao!="2" and decisao!="3" :
        print(" Opção nao disponivel astronauta, vamos bater em marte, decida logo!\n")
        time.sleep(2)
        decisao=input(" Escolha entre: (1) 40 Km\h (2) 1,4 m/s (3) 140 km/h ")
    if(decisao=="1"):
        print("\n\n\n\n  ERRADO! A NAVE ESTA MUITO RÁPIDA, SE CHOCA NO SOLO DE MARTE E TODOS MORREM! ")
        valida_cenario=False
    elif(decisao=="2"):
        print("\n\n\n\n  ERRADO! A VELOCIDADE AINDA É ALTA, A NAVE SE CHOCA NO SOLO DE MARTE E TODOS ESTAO MORTOS")
        valida_cenario=False
    elif(decisao=="3"):
        print("\n\n")
        print("                 O SER HUMANO ESTÁ EM MARTE!!")
        print(" MUITO BEM, VELOCIDADE CONTROLADA, POUSO TRANQUILO E SUAVE\n")
        time.sleep(5)
        print("\n\n")
        valida_cenario=True
    return valida_cenario
#DEFINE CENARIO FINAL
def cenario_Final(nome_personagem):
    print(" A UVB-76 ESTA VOLTANDO PARA A TERRA\n")
    time.sleep(3)
    print(" Mas, \n")
    time.sleep(1)
    print(" Na reentrada algo da errado")
    print(" a nave está quase queimando em contato com a atmosfera da terra\n")
    time.sleep(4)
    print(" {} precisa calcular a força resultante da sua nave\n".format(nome_personagem))
    print(" e precisa saber o valor da gravidade da terra\n")
    time.sleep(4)
    print(" E então, qual é o valor aproxiamado da gravidade na terra?\n")
    time.sleep(3)
    decisao=input(" (1) 50 kg  (2) 9,8 m/s\N{SUPERSCRIPT TWO}  (3) 8 anos-luz : ")   
    while decisao!="1" and decisao!="2" and decisao!="3" :
        print(" Opção não disponivel a nave vai derreter!!\n")
        time.sleep(2)
        decisao=input(" Escolha rápido entre (1) 50 kg  (2) 9,8 m/s\N{SUPERSCRIPT TWO}  (3) 8 anos-luz : ")
    if(decisao=="1"):
        print("\n\n\n\n  ESTÁ ERRADO, A NAVE SE DESINTEGRA NA ATMOSFERA, NOSSOS HEROIS ESTÃO MORTOS")
        valida_cenario=False
    elif(decisao=="2"):
        print("\n\n")
        print("  MUITO BEM, NOSSOS HEROIS CHEGAM SÃO E SALVOS Á TERRA!")
        time.sleep(3)
        print("\n\n")
        valida_cenario=True
    elif(decisao=="3"):    
        print("\n\n\n\n  ESTÁ ERRADO, A NAVE SE DESINTEGRA NA ATMOSFERA, NOSSOS HEROIS ESTÃO MORTOS")
        valida_cenario=False
    return valida_cenario
#DEFINE CENARIOS PARA O JOGADOR 1
def jogando_com_personagem_1(nome_personagem):
    fase_1=cenario_1(nome_personagem)
    if fase_1==True:
        fase_2=cenario_2(nome_personagem)
        if(fase_2==True):
            fase_3=cenario_3(nome_personagem)
            if (fase_3==True):
                fase_final=cenario_Final(nome_personagem)
                if(fase_final==True):
                    mensagem_vencedor()
                else:
                    mensagem_perdedor()                        
            else:    
                mensagem_perdedor()
        else:
            mensagem_perdedor()
    else:
        mensagem_perdedor()
#DEFINE CENARIOS PARA PERSONAGEM 2
def jogando_com_personagem_2(nome_personagem):
    fase_1=cenario_2(nome_personagem)
    if fase_1==True:
        fase_2=cenario_1(nome_personagem)
        if(fase_2==True):
            fase_3=cenario_3(nome_personagem)
            if (fase_3==True):
                fase_final=cenario_Final(nome_personagem)
                if(fase_final==True):
                    mensagem_vencedor()
                else:
                    mensagem_perdedor()         
            else: 
                mensagem_perdedor()
        else:
            mensagem_perdedor()
    else:
        mensagem_perdedor()
#DEFINE CENARIOS PARA O JOGADOR 3
def jogando_com_personagem_3(nome_personagem):
    fase_1=cenario_1(nome_personagem)
    if fase_1==True:
        fase_2=cenario_3(nome_personagem)
        if(fase_2==True):
            fase_3=cenario_2(nome_personagem)
            if (fase_3==True):
                fase_final=cenario_Final(nome_personagem)
                if(fase_final==True):
                    mensagem_vencedor()
                else:
                    mensagem_perdedor()          
            else:  
                mensagem_perdedor()
        else:
            mensagem_perdedor()
    else: 
        mensagem_perdedor()
def mensagem_perdedor():
    print("\n//////////////// VOCÊ PERDEU !! ")
    time.sleep(3)
    reinicio=input("Deseja jogar novamente? (1) Sim (2) Não: ")
    if(reinicio=="1"):        
        andamento_do_jogo()
    elif(reinicio=="2"):
        print("FIM DO JOGO")
    else:
        mensagem_perdedor()

def mensagem_vencedor():
    print("***********************************************************************")
    print("******* VOCÊ FEZ HISTÓRIA, LEVOU O SER HUMANO Á MARTE, PARÁBENS *******")
    print("***********************************************************************\n")
    time.sleep(5)
    print("***********************************************************************")
    print("******* DESEMBARQUE, ACENE PARA SEUS FÂS E ABRACE SEUS FAMILIARES *****")
    print("***********************************************************************\n")
    time.sleep(5)
    print(" FIM DO JO...um momento!")
    time.sleep(2)
    print("QUE SER ESTRANHO É AQUELE SAINDO DA SUA NAVE??????\n")
    time.sleep(3)
    print("continua...\n")
    time.sleep(1)
    print("FIM DO JOGO")

###################################### ANDAMENTO DO JOGO ###########################################

def andamento_do_jogo():
    continua=abertura() 

    if continua==True:
        opcao=escolha_personagem()
        lancamento()
        jogar(opcao) 
    else:
        print("FIM DO JOGO")    

andamento_do_jogo()         