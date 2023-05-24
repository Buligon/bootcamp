import glob
import cv2 as cv
import os
import pandas as pd

index = {}
images = {}

for imagePath in glob.glob(os.getcwd()+'/pre_processamento/*.jpg'):

    filename = imagePath[imagePath.rfind('/')+1:]
    image = cv.imread(imagePath)
    images[filename] = cv.cvtColor(image, cv.COLOR_BGR2RGB)

    hist = cv.calcHist([image], [1, 2], None, [8, 8], [0, 256, 0, 256])
    hist = cv.normalize(hist, hist).flatten()
    index[filename] = hist


# Metodos para calculo do histograma
OPENCV_METHODS = (
    ("Correlation", cv.HISTCMP_CORREL),
    ("Chi-Squared", cv.HISTCMP_CHISQR),
    ("Intersection", cv.HISTCMP_INTERSECT),
    ("Bhattacharyya", cv.HISTCMP_BHATTACHARYYA))

imagem_analisada = 'pre_processamento\\apple1.jpg'

lista_resultados = []
lista_methodName = []

for (methodName, method) in OPENCV_METHODS:

    results = {}
    reverse = False

    # se estivermos usando a Correlation ou Intersection
    # classificar os resultados na ordem inversa
    if methodName in ("Correlation", "Intersection"):
        reverse = True

    for (k, hist) in index.items():
        # Calcular a distancia entre os dois histogramas usando os metodos
        # Atualizar o dicionario de resultados
        d = cv.compareHist(index[imagem_analisada], hist, method)
        results[k] = d

    # Ordenar os resultados
    # print(methodName)
    lista_methodName.append(methodName)
    results = sorted([(v, k) for (k, v) in results.items()], reverse=reverse)
    lista_resultados.append(results)

# Criar o dataframe

for i in range(len(lista_methodName)):
    lista_resultados[i] = pd.DataFrame(lista_resultados[i])
    lista_resultados[i]['Metodo'] = lista_methodName[i]


df = pd.concat(lista_resultados)
df.to_csv('Resultado_compareHist.csv', sep=';', encoding='latin1')

# Analise do DataFrame

# Correlacao
correlation = df.loc[df['Metodo'] == 'Correlation']
correlation.sort_values(0)

print("\n# Correlacao\n")

for i in range(len(correlation)):
    print(correlation[1][i])

print("\n\n")

# Chi-Quadrado
ChiSquared = df.loc[df['Metodo'] == 'Chi-Squared']
ChiSquared.sort_values(0)

print("\n# Chi-Quadrado\n")

for i in range(len(ChiSquared)):
    print(ChiSquared[1][i])

print("\n\n")

# Intersecao
Intersection = df.loc[df['Metodo'] == 'Intersection']
Intersection.sort_values(0)

print("\n# Intersecao\n")

for i in range(len(Intersection)):
    print(Intersection[1][i])

print("\n\n")

# Bhattacharyya
Bhattacharyya = df.loc[df['Metodo'] == 'Bhattacharyya']
Bhattacharyya.sort_values(0)

print("\n# Bhattacharyya\n")

for i in range(len(Bhattacharyya)):
    print(Bhattacharyya[1][i])

print("\n\n")
