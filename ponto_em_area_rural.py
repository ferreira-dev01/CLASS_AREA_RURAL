import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
import fiona
from fiona import Feature, Geometry


# leitura do shapefile do IBGE que contem os setores rurais e urbanos em Minas Gerais
#MAPAS SETORES RURAIS
#https://www.ibge.gov.br/geociencias/downloads-geociencias.html?caminho=organizacao_do_territorio/malhas_territoriais/malhas_de_setores_censitarios__divisoes_intramunicipais/censo_2022/setores/shp/UF
try:
    arquivo = r"./MG_setores_CD2022/MG_setores_CD2022.shp"
    setores_rurais = gpd.read_file(arquivo)
except Exception as Argument:

    f = open("errolog.txt", "a")
    f.write(str(Argument))
    f.close()



#separa somente os poligonos dos setores rurais
setores_rurais=setores_rurais[setores_rurais['SITUACAO'] == 'Rural']

# ler dados de entrada que, OBRIGATORIAMENTE, devem ter as colunas COM NOMES: LATITUDE e LONGITUDE
try:
    dados_entrada= pd.read_csv('./dados_entrada.csv', sep=';')
except Exception as Argument:

    f = open("errolog.txt", "a")
    f.write(str(Argument))
    f.close()


# cria uma coluna para indicar se um local está em área rural ou nao
# sendo  1 para rural 0 para nao
dados_entrada['RURAL'] = '0'
dados_entrada=dados_entrada.fillna(0)# coloca 0 nas latitudes e longitudes que estão vazias

for index, linha in dados_entrada.iterrows():

   # verifica se a latitude e longitude são diferentes de 0
   # não classifica pontos com latitude ou longitude 0
   if linha['LATITUDE'] != 0 and linha['LONGITUDE'] != 0:

        lat=float(linha['LATITUDE'].replace(',','.'))
        long=float(linha['LONGITUDE'].replace(',','.'))

        ponto = Point(long,lat)

        for index2, linha2 in setores_rurais.iterrows():
            if linha2['geometry'].contains(ponto):
                dados_entrada.loc[index,'RURAL'] = '1'
                break



try:
    # salva o resultado em um novo arquivo CSV
    dados_entrada.to_csv('./dados_saida.csv', sep=';', index=False,encoding='utf-8')
except Exception as Argument:

    f = open("errolog.txt", "a")
    f.write(str(Argument))
    f.close()