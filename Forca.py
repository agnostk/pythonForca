from random import randrange

palavras = {}
palavras["Fruta"] = ['ABACATE', 'AMORA', 'AMEIXA', 'ACEROLA', 'ABACAXI', 'BANANA', 'CARAMBOLA', 'CAJU',
                     'CEREJA', 'CACAU', 'CAQUI', 'CUPUAÇU', 'DAMASCO', 'FIGO', 'FRAMBOESA', 'GRAVIOLA',
                     'GOIABA', 'GROSELHA', 'GUARANA', 'JACA', 'KIWI', 'LARANJA', 'LIMAO', 'LIXIA', 'MELANCIA',
                     'MAMAO', 'MELAO', 'MARACUJA', 'MANGA', 'MACADAMIA', 'MEXERICA', 'NECTARINA', 'PERA', 'PESSEGO',
                     'PITANGA', 'TANGERINA', 'TORANJA', 'UVA']

palavras["Animal"] = ['ARIRANHA', 'ALCE', 'ANTA', 'AGUIA', 'ARARA', 'AVESTRUZ', 'BALEIA ', 'BUFALO', 'PREGUIÇA',
                      'COELHO', 'COBRA', 'CAMALEAO', 'CAO', 'CACHORRO', 'CADELA', 'CHIMPANZE', 'CROCODILO', 'COALA',
                      'CARANGUEJO', 'CAMELO', 'CAVALO', 'CISNE', 'CASTOR', 'DROMEDARIO', 'EMA', 'ELEFANTE', 'ESQUILO',
                      'FOCA', 'GAVIAO', 'GAIVOTA', 'GAMBA', 'GALINHA', 'GALO', 'GOLFINHO', 'GATO', 'HIPOPOTAMO', 'HIENA',
                      'HAMSTER', 'IGUANA', 'JABUTI', 'JACARE', 'JAGUATIRICA', 'JABURU', 'LONTRA', 'LHAMA', 'LULA', 'LOBO',
                      'LEOPARDO', 'LEBRE', 'LEAO', 'LAMBARI', 'LAGARTO', 'LAGARTIXA', 'MACACO', 'MARRECO', 'MORSA', 'MICO',
                      'NAJA', 'OVELHA', 'OSTRA', 'ONÇA', 'ORANGOTANGO', 'ORCA', 'ORNITORRINCO', 'PATO', 'PERIQUITO', 'PEIXE',
                      'POMBO', 'PORCO', 'PANDA', 'POLVO', 'PAPAGAIO', 'PAVAO', 'RATO', 'RATAZANA', 'RAPOSA', 'RINOCERONTE',
                      'SAPO', 'SAPA', 'SURICATO', 'SALMAO', 'SARDINHA', 'TATU', 'TAMANDUA', 'TIGRE', 'TOURO', 'URSO', 'URUBU',
                      'VEADO', 'VACA', 'ZEBRA']

palavras["Profissão"] = ['AÇOUGUEIRO', 'ADVOGADO', 'AEROMOÇA', 'ATLETA', 'ASTRONOMO', 'ASTRONAUTA', 'ATENDENTE', 'ACESSORA',
                         'ARTISTA', 'ARTESAO', 'ARQUITETO', 'ARQUIVISTA', 'BIOLOGO', 'BIBLIOTECARIA', 'BIOTECNOLOGO', 'BALCONISTA',
                         'BARBEIRO', 'BANCARIO', 'BABA', 'CARTEIRO', 'CIRURGIAO', 'CIENTISTA', 'CARPINTEIRO', 'COSTUREIRA', 'COMPOSITOR',
                         'CABELEIREIRO', 'CAIXA', 'CANTOR', 'DENTISTA', 'DESIGNER', 'DIRETOR', 'DIRIGENTE', 'DUBLE', 'DUBLADOR',
                         'DIARISTA', 'DEPUTADO', 'DELEGADO', 'DERMATOLOGISTA', 'DESENHISTA ', 'DESEMBARGADOR', 'ENGENHEIRO', 'EMPACOTADOR',
                         'ENFERMEIRA', 'ENCANADOR', 'EMPRESÁRIO', 'ELETRICISTA', 'ESTILISTA', 'ESTOQUISTA', 'FARMACEUTICO', 'FEIRANTE',
                         'FAXINEIRA', 'FISICO', 'FERREIRO', 'FISCAL', 'FLORISTA', 'FONOAUDIÓLOGO', 'FISIOTERAPEUTA', 'FOTOGRAFO', 'GARI',
                         'GARÇOM', 'GOVERNADOR', 'GOVERNANTA', 'GERIATRA', 'GINECOLOGISTA', 'GUARDA', 'GERENTE', 'HISTORIADOR', 'HEMATOLOGISTA',
                         'ILUSTRADOR', 'INSPETOR', 'INSTRUTOR', 'INVESTIGADOR', 'INFECTOLOGISTA', 'JARDINEIRO', 'JOGADOR', 'JORNALISTA',
                         'JORNALEIRO', 'JUIZ', 'LAVRADOR ', 'LEGISTA', 'LIXEIRO', 'LOCUTOR', 'LUTADOR', 'LENHADOR', 'MARCENEIRO', 'MAESTRO',
                         'MATEMATICO', 'MUSICO', 'MOTORISTA', 'METALURGICO', 'MEDICO', 'MECANICO', 'MAQUIADOR', 'MASSAGISTA', 'MAQUINISTA',
                         'MANICURE', 'NADADOR', 'NUTRICIONISTA', 'NEUROLOGISTA', 'NUMEROLOGO', 'NEUROCIRURGIAO', 'OFTALMOLOGISTA', 'OCULISTA',
                         'ORTODONTISTA', 'OBSTETRA', 'OTORRINOLARINGOLOGISTA', 'PARAQUEDISTA', 'PARAMEDICO', 'PESCADOR', 'PERITO', 'PINTOR',
                         'PIANISTA', 'PIZZAIOLO', 'PUBLICITARIA', 'PSICOLOGO', 'PILOTO', 'PINTOR', 'POLITICO', 'PREFEITO', 'PRESIDENTE',
                         'QUIMICO', 'RADIALISTA', 'REVENDEDOR', 'ROTEIRISTA', 'REPORTER', 'RECEPCIONISTA', 'RECREADORA', 'RADIOLOGISTA',
                         'SENADOR', 'SONOPLASTA', 'SOCIOLOGO', 'SOLDADO', 'SERREIRO', 'SARGENTO', 'SAPATEIRO', 'TABELIAO', 'TENENTE',
                         'TERAPEUTA', 'TATUADOR', 'TRAPEZISTA', 'UROLOGISTA', 'URBANISTA', 'VIGILANTE', 'VETERINARIO', 'VENDEDORA', 'VIGIA',
                         'VEREADOR', 'VIOLINISTA', 'ZOOLOGO', 'ZOOTECNISTA', 'ZELADOR']

def setup():
    print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("░░Bem-vindo ao jogo da Forca!░░")
    print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n")

    erros = 0
    dica, palavra = sorteiaPalavra(palavras)
    letrasUsadas = []
    letrasPrevistas = defineObjetivo(palavra)

    if len(palavra) <= 5:
        print("Nível: Fácil")
    elif len(palavra) <= 9:
        print("Nível: Médio")
    elif len(palavra) <= 14:
        print("Nível: Difícil")
    else:
        print("Nível: Expert")
    
    print("\nSua dica é", dica)
    print("\nA palavra tem", len(palavra), "letras:")

    imprime = listaImprime(palavra)
    
    desenhaLacuna(palavra, "", imprime)

    while not set(letrasPrevistas).issubset(letrasUsadas) and erros < 5:
        letra = digitaLetra()
        while letra in letrasUsadas:
            print("\nEssa letra já foi usada, tente novamente!\n")
            letra = digitaLetra()
        checa, posicao = checaLetra(letra, palavra)

        if checa:
            imprimePosicao(posicao)
            feedBack(letra, letrasUsadas, erros)
            desenhaLacuna(palavra, letrasUsadas, imprime)
        else:
            print("\nLetra não existe!\n")
            erros += 1
            feedBack(letra, letrasUsadas, erros)
            desenhaLacuna(palavra, letrasUsadas, imprime)
    if (erros >= 5):
        print("Você perdeu!")
        print("A palavra era:", palavra)
    else:
        print("Você acertou!")
        print("A palavra era:", palavra)
    a = int(input("\nDigite 1 para jogar Novamente!\nDigite 2 para sair.\n"))
    if a == 1:
        setup()
    else:
        print("Obrigado por jogar!")
    

def sorteiaPalavra(palavras):
    tipos = []
    for tipo in palavras:
        tipos.append(tipo)
    selTipo = randrange(0, len(tipos), 1)
    tipo = tipos[selTipo]

    selPalavra = randrange(0, len(palavras[tipo]), 1)
    palavra = palavras[tipo][selPalavra]

    return tipo, palavra

def digitaLetra():
    letra = input("Digite uma letra: ")
    print("\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    return letra.upper()

def checaLetra(letra, palavra):
    posicao = []
    if letra in palavra:
        for l, lacuna in enumerate(palavra, 1):
            if (lacuna == letra):
                posicao.append(l)
        return True, posicao
    else:
        return False, posicao

def desenhaLacuna(palavra, letrasUsadas, imprime):
    i = 0
    print("\n")
    for a in letrasUsadas:
        for b in palavra:
            if a == b:
                imprime[i] = a
            i += 1
        i = 0
    for j in imprime:
        if j == "_":
            print(" _ ", end = "")
        else:
            print(j, "", end = "")
    print("\n")
            
def listaImprime(palavra):
    imprime = []
    for letra in palavra:
        imprime.append("_")
    return imprime

def imprimePosicao(posicao):
    i = 0
    if len(posicao) == 1:
        print("\nSua letra existe na posição", posicao[0])
    else:
        print("\nSua letra existe nas posições ", end = "")
        for pos in posicao:
            i += 1
            if i <= len(posicao) - 2:
                print(str(pos) + ", ", end = "")
            elif i <= len(posicao) - 1:
                print(str(pos) + " e ", end = "")
            else:
                print(str(pos) + ".")

def imprimeLetrasUsadas(letrasUsadas):
    a = 0
    for letra in letrasUsadas:
        a += 1
        if a <= len(letrasUsadas) - 2:
            print (letra + ", ", end = "")
        elif a <= len(letrasUsadas) - 1:
            print (letra + " e ", end = "")
        else:
            print (letra + ".")
    

def defineObjetivo(palavra):
    objetivo = []
    for letra in palavra:
        if not letra in objetivo:
            objetivo.append(letra.upper())
    objetivo.sort()
    return objetivo

def feedBack(letra, letrasUsadas, erros):
    letrasUsadas.append(letra)
    letrasUsadas.sort()
    print("\nLetras Usadas: ", end = "")
    imprimeLetrasUsadas(letrasUsadas)
    print("\nErros:", str(erros) + "/5")
    
setup()
