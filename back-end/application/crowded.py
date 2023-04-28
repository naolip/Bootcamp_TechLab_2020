import numpy as np
#Distância Euclidiana Simples
def distance(p1,p2):
    return ((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)**(1/2)


#Pontos que iremos fazer as distâncias euclidianas
def createCenters(faces): 
    centers = [] 
    for frame in faces:
        (sx,sy,ex,ey) = frame
        center = ((sx+ex)/2,(sy+ey)/2)
        centers.append(center)
    return centers


#Criando uma Matriz de distâncias, onde a posição i,j significa a distância do centro da face "i" pra face "j"
def distArr(faces):
    centers = createCenters(faces) 
    n = len(centers)
    dist = np.zeros((n,n))
    for i in range(len(centers)):
        for j in range(len(centers)):
            if i == j:
                continue
            if j > i:
                break
            # A matriz é reflexiva, a distância de "i" pra "j " é igual a distância de "j" pra "i" 
            dist[i][j] = distance(centers[i],centers[j])
            dist[j][i] = dist[i][j] 
    return dist   