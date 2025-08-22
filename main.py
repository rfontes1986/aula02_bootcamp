# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

try:
    data_usuario = input ("Digite uma data no formato dd/mm/aaaa: ")

    lista_dia_mes_ano = data_usuario.split("/")

    print (f"O elemento 1 é o {lista_dia_mes_ano[0]}")
    print (f"O elemento 2 é o {lista_dia_mes_ano[1]}")
    print (f"O elemento 3 é o {lista_dia_mes_ano[2]}")
except:
    print ("You didn type a correct date format.")