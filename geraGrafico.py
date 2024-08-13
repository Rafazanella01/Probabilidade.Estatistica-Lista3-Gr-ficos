import matplotlib.pyplot as plt
import numpy as np

"""
Esse arquivo serve para eu gerar os gráficos solicitados na lista 3, nele contem as funções com os tipos de gráficos eles recebem os parâmetros da função e depois geram o gráfico

Esta sendo utilizada a biblioteca Matplotlib
"""
def graficoDeLinha(nomeColunas, valores, titulo, cor, xlabel, ylabel):
    plt.figure(figsize=(10, 6))
    plt.plot(nomeColunas, valores, marker='o', color=cor)
    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    #plt.xticks(rotation=45) 
    plt.savefig(titulo + ".png")
    plt.show()

def graficoDeColunas(nomeColunas, valores, titulo, cor, xlabel, ylabel):
    plt.figure(figsize=(10, 6))
    plt.bar(nomeColunas, valores, color=cor)
    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(fontsize=7)
    #plt.xticks(rotation=45) 
    plt.savefig(titulo + ".png")
    plt.show()

def graficoDeBarras(nomeColunas, valores, titulo, cor, xlabel, ylabel):
    plt.figure(figsize=(10, 6))
    plt.barh(nomeColunas, valores, color=cor)
    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    #plt.xticks(rotation=45) 
    plt.savefig(titulo + ".png")
    plt.show()

def graficoDePizza(nomes, valores, titulo, cores=None):
    plt.figure(figsize=(8, 8))
    plt.pie(valores, labels=nomes, colors=cores, autopct='%1.1f%%', startangle=140)
    plt.title(titulo)
    plt.axis('equal')
    plt.savefig(titulo + ".png")
    plt.show()

def graficoDeBarrasMultiplas(categorias, valores_ano1, valores_ano2, titulo, xlabel, ylabel, legenda, cor1='blue', cor2='green'):
    largura = 0.35
    indice = np.arange(len(categorias))
    plt.figure(figsize=(10, 6))
    plt.bar(indice, valores_ano1, largura, label=legenda[0], color=cor1)
    plt.bar(indice + largura, valores_ano2, largura, label=legenda[1], color=cor2)
    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(fontsize=6)
    plt.xticks(indice + largura / 2, categorias, rotation=45, ha='right')
    plt.legend()
    plt.savefig(titulo + ".png")
    plt.show()