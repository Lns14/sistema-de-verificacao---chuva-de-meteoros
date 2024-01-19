# menu em loop 
 
controle = 1 
 
opcao0 = "OPÇÃO INVÁLIDA" 
 
opcao1 = '1. Definir perímetro da propriedade e da edificação de interesse' 
 
opcao2 = '2. Definir localização da UPMCC e unificar sistemas de coordenadas de referência' 
 
opcao3 = '3. Processar registros de chuva de meteoros' 
 
opcao4 = '4. Apresentar estatísticas da última chuva processada' 
 
opcao5 = '5. Sair' 
 
 
print('Sistema para Análise de Chuva de Meteoros') 
 
print(opcao1, opcao2, opcao3, opcao4, opcao5, sep='\n')
 
menu = int(input()) 
 
 
while menu != 5: 
 
    if menu < 1 or menu > 5: 
 
        print(opcao0) 
 
    elif menu == 1: 
 
        print("Opção escolhida: 1") 
 
        # pedindo as coordenadas dos cantos fazenda 
 
        xf = float(input('Insira o x do ponto superior esquerdo da fazenda: ')) 
 
        yf = float(input('Insira o y do ponto superior esquerdo da fazenda: ')) 
 
        xf2 = float(input('Insira o x do ponto inferior direito da fazenda: ')) 
 
        yf2 = float(input('Insira o y do ponto inferior direito da fazenda: ')) 
 
        # pedindo as coordenadas dos cantos da sede 
 
        xs = float(input('Insira o x do ponto superior esquerdo da sede: ')) 
 
        ys = float(input('Insira o y do ponto superior esquerdo da sede: ')) 
 
        xs2 = float(input('Insira o x do ponto inferior direito da sede: ')) 
 
        ys2 = float(input('Insira o y do ponto inferior direito da sede: ')) 
 
        print('Dados da propriedade e sede registradas com sucesso!') 
 
    elif menu == 2: 
 
        print("Opção escolhida: 2") 
 
        # pedindo a localização da UPMCC 
 
        xupmcc = float(input('Insira a coordenada x da UPMCC: ')) 
 
        yupmcc = float(input('Insira a coordenada y da UPMCC: ')) 
 
        print('Localização da UPMCC registrada com sucesso!') 
 
    elif menu == 3: 
 
        print("Opção escolhida: 3") 
 
        if controle < 3: 
 
            print("Impossível processar qualquer registro de queda no momento: localização da propriedade ainda não informada") 
 
        else:
 
            primeiro_quadrante = 0 
 
            segundo_quadrante = 0 
 
            terceiro_quadrante = 0 
 
            quarto_quadrante = 0 
 
            edificacao_principal = 0 
 
            dentro_prop = 0 
 
            # pedindo raio e ângulo 
 
            registro = 1
 
            print(f'\nRegistro #{registro}')
 
            raio = float(input("Distância: "))
 
            while raio >= 0: 
 
                angulo = float(input("Ângulo: ")) 
 
                registro += 1  
 
                # transformando coordenadas polares em cartesianas (meteorito) 
 
                import math 
 
                angulo = math.radians(angulo) 
 
                x = raio * math.cos(angulo) 
 
                y = raio * math.sin(angulo) 
 
                # transladando as coordenadas que começam em um ponto diferente de 0 (origem) 
 
                tx = x + xupmcc 
 
                ty = y + yupmcc 
 
                print(f'[INFO] ponto convertido: ({x:.2f};{y:.2f}) com origem na UPMCC, ou ({tx:.2f};{ty:.2f}) com origem no ponto (0;0)')
 
                # verificando se os meteoros caíram na propriedade e em qual quadrante
 
                if xs <= tx <= xs2 and ys >= ty >= ys2: 
 
                    edificacao_principal += 1
 
                    print(f'[INFO] meteoro atingiu a edificação principal')
 
                if xf <= tx <= xf2 and yf >= ty >= yf2 :  
 
                      dentro_prop += 1
 
                      if tx > 0 and ty > 0:
 
                        primeiro_quadrante += 1
 
                        print(f'[INFO] meteoro caiu dentro da propriedade, no quadrante NE a partir do ponto (0;0)')
 
                      elif tx < 0 and ty > 0:
 
                        segundo_quadrante += 1
 
                        print(f'[INFO] meteoro caiu dentro da propriedade, no quadrante NO a partir do ponto (0;0)')
 
                      elif tx < 0 and ty < 0: 
 
                        terceiro_quadrante += 1
 
                        print(f'[INFO] meteoro caiu dentro da propriedade, no quadrante SO a partir do ponto (0;0)')
 
                      elif tx > 0 and ty < 0: 
  
                        quarto_quadrante += 1
 
                        print(f'[INFO] meteoro caiu dentro da propriedade, no quadrante SE a partir do ponto (0;0)')
                
                print(f'\nRegistro #{registro}')
 
                raio = float(input("Distância: "))
 
            print(f'Fim da coleta de registros: {registro-1} quedas informadas') 
 
    elif menu == 4: 
 
        print("Opção escolhida: 4") 
 
        if controle < 4: 
 
            print("Impossível processar estatísticas da última chuva processada: não foi feito nenhum processamento ainda") 
 
        else:
 
            #calculando a porcentagem de cada queda na propriedade e nos quadrantes
 
            p_dentro_prop = (dentro_prop/registro)*100 
 
            p_primeiro_quadrante = (primeiro_quadrante/dentro_prop)*100 
 
            p_segundo_quadrante = (segundo_quadrante/dentro_prop)*100 
 
            p_terceiro_quadrante = (terceiro_quadrante/dentro_prop)*100 
 
            p_quarto_quadrante = (quarto_quadrante/dentro_prop)*100
 
            #imprimindo os dados da chuva
 
            print(f'Total de quedas registradas: {registro-1}') 
 
            print(f'Quedas dentro da propriedade: {dentro_prop} ({p_dentro_prop:.2f}% do total)') 
 
            print(f'Quadrante NE: {primeiro_quadrante} ({p_primeiro_quadrante:.2f}% das quedas na propriedade)') 
 
            print(f'Quadrante NO: {segundo_quadrante} ({p_segundo_quadrante:.2f}% das quedas na propriedade)') 
 
            print(f'Quadrante SO: {terceiro_quadrante} ({p_terceiro_quadrante:.2f}% das quedas na propriedade)') 
 
            print(f'Quadrante SE: {quarto_quadrante} ({p_quarto_quadrante:.2f}% das quedas na propriedade)') 
 
 
            if edificacao_principal >= 1: 
 
                print('A edificação principal foi atingida? SIM') 
 
            else: 
 
                print('A edificação principal foi atingida? NÃO') 
 
    print('\nSistema para Análise de Chuva de Meteoros') 
 
    print(opcao1, opcao2, opcao3, opcao4, opcao5, sep='\n')
 
    menu = int(input()) 
 
    controle += 1 
 
 
 
print(' Encerrando sistema…')
