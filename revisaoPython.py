# 1)B
#################################
# 2)
# def main() : 
#     carros = (
#         (
#             'Jetta Variant',
#             'Motor 4.0 Turbo',
#             2003,
#             False,
#             ('Rodas de liga', 'Travas elétricas', 'Piloto automático')
#         ),
#         (
#             'Passat',
#             'Motor Diesel',
#             1991,
#             True,
#             ('Central multimídia', 'Teto panorâmico', 'Freios ABS')
#         )
# )
# A)
# print(f'{carros[1][4][2]}')
# B)
# saida = (carros[0][4][0], carros[0][4][1]) 
# print(saida)
##################################
# 3)
# def main() : 
#     carros = (
#         (
#             'Jetta Variant',
#             'Motor 4.0 Turbo',
#             2003,
#             False,
#             ('Rodas de liga', 'Travas elétricas', 'Piloto automático')
#         ),
#         (
#             'Passat',
#             'Motor Diesel',
#             1991,
#             True,
#             ('Central multimídia', 'Teto panorâmico', 'Freios ABS')
#         )
# )
# for carro in carros:
#    for acessorio in carro[4]:
#        print(acessorio)
##################################
# 4)
# def main():
#     nomes = ['Passat', 'Crossfox', 'DS5', 'C4', 'Jetta']
#     kms = [15000, 12000, 32000, 8000, 50000]

#     zipado = list(zip(nomes, kms))

#     for carro in zipado:
#       if carro[1] < 20000:
#           print(carro[0])
# if __name__ == "__main__":
#     main()

##################################
# 5)
# def main():
#   nomes = ['Passat', 'Crossfox', 'DS5', 'C4', 'Jetta']
#   kms = [15000, 12000, 32000, 8000, 50000]

#   tuplas = dict(zip(nomes, kms))
#   print(tuplas)
#if __name__ == "__main__":
#   main()
##################################
# 6)
# def main(): 
    
#     dados = {
#         'Passat': {
#             'ano': 2012,
#             'km': 50000,
#             'valor': 75000,
#             'acessorios': ['Airbag', 'ABS']
#         },
#         'Crossfox': {
#             'ano': 2015,
#             'km': 35000,
#             'valor': 25000
#         }
#     }
#     print(isIn("acessorios", dados["Crossfox"]))
#     print(isIn("acessorios", dados["Passat"]))
#     print(dados['Crossfox']['valor'])
#     print(dados['Passat']['acessorios'][-1])




# def isIn(chave, dicionario):
#     if chave in dicionario:
#         return True
#     return False



# if __name__ == "__main__":
#     main()
#################################
# 7)
# def main(): 
#     dados = {'Jetta': 88000, 'Crossfox': 72000, 'DS5': 124000}
#     novosDados = {'Passat': 85000, 'Fusca': 150000}
#     dados.update(novosDados)
#     print(dados)


# if __name__ == "__main__":
#     main()
###################################
# 8)
# def main():
#     dados = {
#         'Crossfox': {'valor': 72000, 'ano': 2005},
#         'DS5': {'valor': 125000, 'ano': 2015},
#         'Fusca': {'valor': 150000, 'ano': 1976},
#         'Jetta': {'valor': 88000, 'ano': 2010},
#         'Passat': {'valor': 106000, 'ano': 1998}
#     }

#     for elemento in dados:
#         if dados[elemento]['ano'] >= 2000:
#             print(elemento)

# if __name__ == "__main__":
#     main()

##########################################
# 9) c
##########################################
# 10)
# def main():
#     dados = {
#         'Crossfox': {'km': 35000, 'ano': 2005},
#         'DS5': {'km': 17000, 'ano': 2015},
#         'Fusca': {'km': 130000, 'ano': 1979},
#         'Jetta': {'km': 56000, 'ano': 2011},
#         'Passat': {'km': 62000, 'ano': 1999}
#     }
    
#     km_media(dados, 2019)

# def km_media(dataset,ano_atual):
#     for elemento in dataset:
#        kilometragem = dataset[elemento]['km']
#        anoFabricacao = dataset[elemento]['ano']
#        media = kilometragem / (ano_atual - anoFabricacao)

#        print(media)



# if __name__ == "__main__":
#     main()





