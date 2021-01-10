from django.shortcuts import render
from .models import Tejidos, Grafo
from django_pandas.io import read_frame
from math import sqrt

def home(request):
    return render(request, 'app/home.html')


def datos(request):
    datos = Tejidos.objects.all()
    procesado = procesa_tabla(datos)
    return render(request, 'app/datos.html', {'misTejidos': datos, 'proceso': procesado})


def procesa_tabla(qs):
    df = read_frame(qs)
    return df


def resultados(request):
    tejido = Tejidos.objects.all()
    print('longitud: ' + str(len(tejido)))
    df = read_frame(tejido)

    mediaTemperatura = df['temperatura'].mean()

    mediaColor = df['color'].mean()
    
    mediaInflamacion = df['inflamacion'].mean()

    # diccionario={'mediaT':mediaTemperatura, 'mediaC':mediaColor}
    m = df.iloc[0, 2:5].mean()
    # print(m)
    # diccionario['mediaPorRegistro']=m
    
    
    # fila1 = df.iloc[0, 2:5]
    # lista = []

    # for j in range(0,4):
    # for i in range(j+1, 5):
    # lista.append({'registro1': j, 'registro2': i, 'distancia':abs(df.iloc[j, 2:5]-df.iloc[i, 2:5]).sum() })

    # lista=[{'registro1': j, 'registro2': i, 'distancia':abs(df.iloc[j, 2:5]-df.iloc[i, 2:5]).sum() } for j in range (0,4) for  i in range (j+1, 5) ]

    # lista = [{'registro1: ': df['id'][j], 'registro2: ': df['id'][i], 'distancia': abs(df.iloc[j, 2:5]-df.iloc[i, 2:5]).sum()} for j in range(0, len(tejido)-1) for i in range(j+1, len(tejido))]
    lista = [{'r1: ': df['id'][j], 'r2: ': df['id'][i], 'distancia': sqrt((abs(df.iloc[j, 2:5]-df.iloc[i, 2:5]).sum())*2)} for j in range(0, len(tejido)-1) for i in range(j+1, len(tejido))]
    lista2 = [{'r1: ': df['id'][j], 'r2: ': df['id'][i], 'conectado: ': True if sqrt((abs(df.iloc[j, 2:5]-df.iloc[i, 2:5]).sum())*2)<5 else False} for j in range(0, len(tejido)-1) for i in range(j+1, len(tejido))]
    
    listafinal = [{'nodo': Grafo.objects.create(origen=Tejidos.objects.get(pk=df.iloc[j,0:1]), destino=Tejidos.objects.get(pk=df.iloc[i,0:1]), conectado= True if sqrt((abs(df.iloc[j, 2:5]-df.iloc[i, 2:5]).sum())*2)<5 else False).save() }for j in range(0, len(tejido)-1) for i in range(j+1, len(tejido))]
    # origen = Tejidos.objects.create(partes=20, temperatura=20, color=20, inflamacion=20)
    # destino = Tejidos.objects.create(partes=40, temperatura=40, color=40, inflamacio=40)
    # origen = Tejidos.objects.get(pk=lista2[1]['r1'])
    # destino = Tejidos.objects.get(pk=lista2[1]['r2'])
    # nodo = Grafo.objects.create(origen=origen, destino=destino, conectado=lista2[1]['conectado'])
    # nodo.save()
    
    # print(lista)
         
    # grafo = []
    # umbral = 5
    # for elemento in lista:
    #     # grafo['vertice '+str(i)] = elemento['registro1']
    #     # grafo['vertice '+str(i+1)] = elemento['registro2']

    #     if elemento['distancia'] < umbral:
    #         tupla = (elemento['registro1: '],
    #                  elemento['registro2: '], elemento['distancia'], 'Si')
    #     else:
    #         tupla = (elemento['registro1: '],
    #                  elemento['registro2: '], elemento['distancia'], 'No')
    #         grafo.append(tupla)

    # print(grafo)
    # print("lllll")
    # df.iloc[0, 2:5]-df.iloc[1, 2:5]
    # df.iloc[0, 2:5]-df.iloc[2, 2:5]
    # df.iloc[0, 2:5]-df.iloc[3, 2:5]
    # df.iloc[0, 2:5]-df.iloc[4, 2:5]

    # fila2 = df.iloc[1, 2:5]
    # fila3 = df.iloc[2, 2:5]
    # fila4 = df.iloc[3, 2:5]

    # filaRes = abs(fila2-fila1)
    # filaRes1 = abs(fila3-fila1)

    # resultadoSuma = filaRes.sum()
    # print("************************************")
    # print(fila1)
    # print(fila2)
    # print(resultadoSuma)
    # print(fila4)
    # print(filaRes1)
    # print("*************************************")

    diccionario = {'mediaT': mediaTemperatura, 'mediaC': mediaColor, 'm': m, 'mediaI': mediaInflamacion}
    diccionario['lista2']=lista2
    diccionario['lista']=lista
    diccionario['max'] = df.iloc[0, 2:5].max()
    # diccionario['miLista1'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # diccionario['miLista'] = [(i, i) for i in range(0, 100)]
    # diccionario['miLista2'] = [(x, y) for y in range(0, 6)for x in range(0, 11) if x == y]

    # print(df)
    return render(request, 'app/resultados.html', diccionario)
