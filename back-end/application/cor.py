clrs = [
    [(0,255,0),(255,255,0)],
    [(255,127,0),(255,0,0)]
]
# Função pra definir o tipo do alerta:
# caso pelo menos 1 pessoa esteja sem máscara e pelo menos 1 esteja aglomerado na imagem: Sinal Vermelho
# caso ninguém esteja sem máscara e pelo menos 1 esteja aglomerado na imagem: Sinal Amarelo
# caso ninguém esteja sem máscara e ninguém aglomerado na imagem: Sinal Verde
# caso pelo menos 1 pessoa esteja sem máscara e ninguém esteja aglomerado na imagem: Sinal Laranja
def tipo(qtdMaskOff,qtdCrowded):
    if qtdMaskOff and qtdCrowded:
        return 'Vermelho'
    elif not qtdMaskOff and qtdCrowded:
        return 'Amarelo'
    elif not qtdMaskOff and not qtdCrowded:
        return 'Verde'
    else:
        return 'Laranja'

## COLOR
#   0 1   for Green,Yellow,Orange,Red
# 0 G Y 
# 1 O R

#Laranja: Nao aglomerado sem mascara
#Verde: Com mascara e nao aglomerado
#Amarelo: Aglomerado com mascara
#Vermelho: Aglomerado e sem mascara

def clr(maskOff,crowded):
    global clrs
    return clrs[maskOff][crowded]