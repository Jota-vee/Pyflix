banco_pyflix = []


letras_variaveis = ["cç", "aâáàã", "eêéè", "iîíì", "oôóòõ", "uûúù"]


def remover_acentos(string:str):
        string_aux = []
        string = remover_espaço(string).lower()
            
        for letra in string:
            for letras in letras_variaveis:
                letra_nao_adicionada = True
                if letras.count(letra) > 0:
                    string_aux.append(letras[0])
                    letra_nao_adicionada = False
                    break
            if letra_nao_adicionada:
                string_aux.append(letra)
        string = "".join(string_aux)
        return string


def remover_espaço(string:str):
     string = string.split()
     string = "".join(string)
     return string


def verifica_titulo():
    while True:
        titulo = input("Titulo: ").capitalize()
        if remover_espaço(titulo).isalnum():
             return titulo
        else:
            print("\nTitulo invalido\n")
            continue


def verifica_diretor():
    while True:
        diretor = input("Diretor: ").capitalize()
        if remover_espaço(diretor).isalpha():
            return diretor
        else:
            print("\nNome invalido\n")
            continue


def verifica_ano():
    while True:
        ano = input("Ano de lançamento: ") 
        if remover_espaço(ano).isdigit():
            if int(ano) < 1895 or int(ano) > 2024:
                print("\nano ínvalido\n")
                continue
            else:
                return int(ano)
        else:
            print("\nano ínvalido\n")
            continue


def verifica_genero():
    generos_de_filmes = [
    "Ação",
    "Aventura",
    "Comédia",
    "Drama",
    "Fantasia",
    "Ficção Científica",
    "Terror",
    "Mistério",
    "Romance",
    "Suspense",
    "Animação",
    "Musical",
    "Documentário",
    "Crime",
    "Policial",
    "Histórico",
    "Guerra",
    "Faroeste",
    "Biografia",
    "Família",
    "Esporte",
    "Thriller",
    "Arte",
    "Experimental"]
    while True:
        generos = input("Quais são os gêneros ?\n\n--:")
        generos_aux = []

        for letra in range(len(generos)):
            if generos[letra].isalpha():
                generos_aux.append(generos[letra])
            else:
                if letra > 0:
                    if generos[letra - 1].isalpha():
                        generos_aux.append("-")
    
        generos = " ".join(generos_aux)
        generos = generos.split("-")
        generos_aux = generos.copy()
        falsos_generos = []

        for genero in generos_aux:
            falso_genero = True
            if remover_espaço(genero.lower()) in ["e", "ê", "é", "è"]:
                generos.remove(genero)
                continue
                
            for genero_filme in generos_de_filmes:
                if comparador(genero_filme, genero, 2):
                    falso_genero = False
                    generos.remove(genero)
                    if genero_filme not in generos:
                        generos.append(genero_filme)
                        break
            if falso_genero:
                falsos_generos.append(genero) 
                generos.remove(genero)
                continue    
        generos.sort()
        
        if len(generos) > 0 and len(falsos_generos) == 0:
            return ", ".join(generos)
            
        elif len(falsos_generos) > 0 and len(generos) > 0:
            print(f"\n{falsos_generos}, não são gêneros\nGostaria de adicionar apenas, {generos}\n")
            while True:
                print("[s] sim")
                print("[n] não\n")
                escolha = input("--: ").lower()
                if escolha not in ["n", "s"]:
                    print("\nopção ínvalida\n")
                    continue
                else:
                    if escolha == "s":
                        return ", ".join(generos)
                    else:
                        break 
                        
        else:
            print("\nGênero inválido\n")
            continue     
         
def menu():
    while True:
        print("\n[1] Adicionar filme")
        print("[2] Listar filmes ")
        print("[3] Buscar filme ")
        print("[4] atualizar filme")
        print("[5] Remover filme ")
        print("[6] Sair\n")
        açao = (input("--: "))
        
        if açao not in ["1","2","3","4","5","6"]:
            print("\nFunção ínvalida")
            continue
        else:
            return açao


def adicionar():
    print("\n")
    titulo  =  verifica_titulo()
    diretor = verifica_diretor()
    ano     =     verifica_ano()
    genero  =  verifica_genero()

    filme = [titulo, diretor, ano, genero]
    banco_pyflix.append(filme)
    banco_pyflix.sort()
    print("\nFilme adicionado com sucesso :)\n")


def listar():
    if len(banco_pyflix) == 0:
        print("\nCatálogo vazio\n")
    else:
        print("\nCatálogo de filmes\n")
        for filme in banco_pyflix:
            print("-" * 54)
            print(f"Filme    | {filme[0]}" )
            print(f"Ano      | {filme[2]}" )
            print(f"Gênero   | {filme[3]}" )
            print(f"Diretor  | {filme[1]}\n")


def comparador(string1: str, string2: str, categoria: str):
    
    string1 = remover_espaço(string1).lower()
    string2 = remover_espaço(string2).lower()
    
    if len(string2) > len(string1) or string2 == "":
        return False
  
    string1 = remover_acentos(string1)
    string2 = remover_acentos(string2)
    
    if categoria == 1:
        
        if string1.count(string2) > 0:
            return True
        else:
            return False
            
    elif categoria == 2: 
           
        if len(string1) == len(string2):
            
            if string1 == string2:
                return True 
            else:
                return False
                

def busca_titulo():
    print("\nDigite o titulo do filme ou parte dele\n")
    busca = input("--: ").lower()
    tem_filme = False
    for filme in banco_pyflix:
        if comparador(filme[0], busca, 1):
            print("\n")
            print(f"Filme    | {filme[0]}" )
            print(f"Ano      | {filme[2]}" )
            print(f"Gênero   | {filme[3]}" )
            print(f"Diretor  | {filme[1]}\n" )
            tem_filme = True
    if not tem_filme:
         print("\nNão encontramos nenhum filme\n")


def menu_atualizar():
    while True:
        print("\nO que você quer atualizar\n")
        print("[1] Titulo" )
        print("[2] Diretor" )
        print("[3] Ano de lançamento")
        print("[4] Gênero do filme" )
        print("[5] Sair\n" )
        print('-'*45)
        açao = (input("--: "))
        print("\n")
            
        if açao not in ["1","2","3","4","5"]:
            print("\nFunção ínvalida")
            continue
        else:
            return açao


def atualizar():
    if len(banco_pyflix) > 0:
        while True:
            busca_atualizar = input("\nqual o título do filme?\n--: ").lower()
            nao_tem_filme = True
            for filme in banco_pyflix:
                if comparador(filme[0], busca_atualizar, 2):
                    nao_tem_filme = False
                    print("\n")
                    print(f"Filme.  | {filme[0]}" )
                    print(f"Ano.    | {filme[2]}" )
                    print(f"Gênero  | {filme[3]}" )
                    print(f"Diretor | {filme[1]}\n" )
                    while True:
                        açao = menu_atualizar()
                        if açao == "1":
                            filme[0] = verifica_titulo()
                        elif açao == "2":
                            filme[1] = verifica_diretor()
                        elif açao == "3":
                            filme[2] = verifica_ano()
                        elif açao == "4":
                            filme[3] = verifica_genero()
                        elif açao == "5":
                            return False
            if nao_tem_filme:
                print("\nNão encontramos o filme :(\n")
                continue
    else:
        print("\nCatálogo vazio, adicione filmes primeiro\n")


def remover():
    print("\nDigite o titulo do filme\n")
    busca = input("--: ").lower()
    for filme in banco_pyflix:
        if comparador(filme[0], busca, 2):
            while True:
                print(f"\nvocê quer mesmo remover '{filme[0]}' ?\n")
                print("[s] sim")
                print("[n] não\n")
                escolha = input("--: ").lower()
                if escolha not in ["n", "s"]:
                    print("\nopção ínvalida\n")
                    continue
                else:
                    if escolha == "s":
                        banco_pyflix.remove(filme)
                        print("\nFilme excluido com sucesso\n")
                        return True
                    else:
                        return True

print('\nEsse é seu catálogo de filmes, seja bem vindo!')    
while True:
    açao = menu()   
    if açao == "1":
        adicionar()
    elif açao == "2":
        listar()
    elif açao == "3":
        busca_titulo()
    elif açao == "4":
        atualizar()
    elif açao == "5":
        remover()
    else:
        print("\nPrograma finalizado :)")
        break