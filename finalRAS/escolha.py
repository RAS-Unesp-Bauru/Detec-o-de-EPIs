def escolha():
    global num
    num = [1,2,3,4,5]
    print('='*50)
    print('No \t Menu de escolha')
    print('1. \t Detector de Máscara')
    print('2. \t Detector de Óculos de proteção')
    print('3. \t Detector de Fone de proteção')
    print('4. \t Detector de Capacete')
    print('5. \tCaso queira encerrar a detecção aperte a letra Q')
    print('='*50)
#Menu de informação

def enq(n):
    while True:
        if n not in num:
            n = int(input('Digite um valor válido: '))
        elif n == 5:
            break
        elif n in num:
            break
        else:
            continue
    return n
# Suporte para o Menu

