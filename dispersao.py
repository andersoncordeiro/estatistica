import numpy as np
from scipy import stats
import math # Importando a biblioteca math para utilizar a função da raiz quadrada (sqrt)

l = [5, 7, 8, 10, 12, 15, 18, 20, 28, 35, 40, 44]

def amplitude(lista):
    lista.sort()
    return lista[-1] - lista[0]


def desvio_medio(lista):
    media = np.mean(lista) # Calculando a média utilizando o scipy.
    aux = 0
    for i in lista:
        aux+=abs(media-i) # Utilizando o abs para salvar o valor absoluto, independente de sinal + ou -
    return aux/len(lista)


def desvio_padrao(lista):
    media = np.mean(lista)
    aux = 0
    for i in lista:
        aux += (media-i)*(media-i) # Acumulando o quadrado dos desvios

    resultado = aux/(len(lista)-1) # Resultado / Tamanho da lista - 1
    return math.sqrt(resultado) # Raiz quadrada do resultado


def variancia(lista):
    dp = desvio_padrao(lista)
    return dp * dp


def coeficiente_variacao(lista):
    media = np.mean(lista)
    # Calculando o desvio padrão utilizando o scipy. ddof = Delta Degrees of Freedom;
    # O ddof é utilizando para ser o divisor (N - ddof). ddof default é 0.
    dp = np.std(lista, ddof=1)
    return dp/media


def escore_z(valor, lista):
    media = np.mean(lista)
    dp = np.std(lista, ddof=1)
    return (valor - media)/dp\


def intervalo_interquartil(lista):
     print( np.percentile(lista,75))
     return np.percentile(lista,75) - np.percentile(lista,25)


print("\nLista: " + str(l))
print("Amplitude: " + str(amplitude(l)))
print("Desvio Médio: " + str(desvio_medio(l)))
print("Desvio Padrão: " + str(desvio_padrao(l)))
print("Variância: " + str(variancia(l)))
print("Coeficiente de Variação: " + str(coeficiente_variacao(l)))
print("Escore Padronizado: " + str(escore_z(60.0,l)))
print("Intervalo Interquartil: " + str(intervalo_interquartil(l)))
