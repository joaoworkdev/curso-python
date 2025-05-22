cadastro = {"nome": "Pedro", "idade": 21}
print(cadastro["nome"])
print(cadastro["idade"])
cadastro["sexo"] = "M" #adiciona o elemento "sexo"
del cadastro["idade"] #apaga o elemento "idade"

filme = {"titulo": "Star Wars",
         "ano": 1977,
         "diretor": "George Lucas"
        }
print(filme.values()) # Irá retornar, todos os valores do dicionario 
print(filme.keys()) # Irá retornar, as chaves do dicionario 
print(filme.items()) # Irá retornar, as chaves e os valores do dicionario 

for k, v in filme.items():
    print(f"O {k} e {v}")

# DICIONARIO DENTRO DE LISTA
brasil = list()
estado1 = {"uf": "Rio de Janeiro", "sigla": "RJ"}
estado2 = {"uf": "São Paulo", "sigla": "SP"}
brasil.append(estado1)
brasil.append(estado2)

print(brasil)
print(brasil[0])
print(brasil[1]["uf"])