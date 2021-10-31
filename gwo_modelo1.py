#import benchmarks as bench
import random
import numpy
import math
#sw = 0 #soma de resursos

#nao estou usando
def euclidiana(y,z):
    # x, y, z = C, XP, X
    return (numpy.sqrt(sum((y - z) ** 2))) #distancia euclidiana

def update_Coeficientes(a):
    
    r1 = random.randrange(0,11)/10
    r2 = random.randrange(0,11)/10
    C = 2*r2
    A = 2*a*r1-a
    
    return A,C

#função ackley
def F10(x):
    dim=len(x);
    o=-20*numpy.exp(-.2*numpy.sqrt(numpy.sum(x**2)/dim))-numpy.exp(numpy.sum(numpy.cos(2*math.pi*x))/dim)+20+numpy.exp(1);
    return o;

def gwo_solution(sw, Serv_List):
    Fog_nro = sw
    MaxIter = 5
    dim = 4
    
    Pos = {}
    Nro_serv = len(Serv_List)

    Alpha = numpy.zeros(1)
    Alpha_pos = numpy.zeros(dim)
    Alpha_score = float("inf")

    Beta = numpy.zeros(1)
    Beta_pos = numpy.zeros(dim)
    Beta_score = float("inf")

    Delta = numpy.zeros(1)
    Delta_pos = numpy.zeros(dim)
    Delta_score = float("inf")

    Positions = numpy.zeros((Nro_serv,4))
    l=0
    for j in Serv_List:
        for i in range(0,dim):
            #for l in range(0,dim):
            #print ("Fog j  i:   ",[Serv_List[j][i]], j)
            #print ("Carro l:   ", [sw[0][i]], l)
            y = numpy.array([Serv_List[j][i] / 100])
            z = numpy.array([sw[0][i]])
            Positions[i, l] = y #euclidiana(z,y)
            #print ("posicao  l  i :", Positions[l, i], l, i)
        l += 1
    #print (Positions)
    aux = (2/MaxIter)
    a = 2
    A, C = update_Coeficientes(a)
    
    for l in range(0,MaxIter): #máximo de iterações
        for j in range(0,Nro_serv): #passar por todos os serviços
            #print ("Posição fitness:   ", Positions[j,:])
            fitness = F10(Positions[j,:])
            
            if (fitness < Alpha_score):
                
                Alpha = j
                Alpha_score = fitness
                Alpha_pos=Positions[j,:].copy()
            elif (fitness > Alpha_score and fitness < Beta_score):
                
                Beta = j
                Beta_score = fitness
                Beta_pos=Positions[j,:].copy()
            elif (fitness > Alpha_score and fitness > Beta_score and fitness < Delta_score):
            
                Delta = j
                Delta_score = fitness
                Delta_pos=Positions[j,:].copy()
            
        a = a - aux 
        
        for i in range(0,Nro_serv):
            for j in range (0,dim):
                A1, C1 = update_Coeficientes(a)
                D_alpha=abs(C1*Alpha_pos[j]-Positions[i,j]); # Equation ()-part 1
                X1=Alpha_pos[j]-A1*D_alpha; # Equation ()
                A2, C2 = update_Coeficientes(a)
                D_beta=abs(C2*Beta_pos[j]-Positions[i,j]); # Equation ()
                X2=Beta_pos[j]-A2*D_beta; # Equation ()       
                A3, C3 = update_Coeficientes(a)
                D_delta=abs(C3*Delta_pos[j]-Positions[i,j]); # Equation ()
                X3=Delta_pos[j]-A3*D_delta; # Equation ()             

                Positions[i,j] =(X1+X2+X3)/3  # Equation ()
                
        #print(['At iteration '+ str(l)+ ' the best fitness is '+ str(Alpha_score)]);
    sel = ""
    if (Alpha==0):
        sel = "Edge0"
    elif (Alpha==1):
        sel = "Edge1"
    elif (Alpha==2):
        sel = "Edge2"
    elif (Alpha==3):
        sel = "Edge3"
    else:
        sel = "erro"
    #print ("Selecionado:   ", sel, Serv_List[sel])
    return sel
