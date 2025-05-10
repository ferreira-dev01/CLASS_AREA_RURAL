Este sistema tem o objetivo de classificar se um ponto pertence a zona rural ou não
de acordo com os mapas censitários do IBGE de 2022 conforme link abaixo:

https://www.ibge.gov.br/geociencias/downloads-geociencias.html?caminho=organizacao_do_territorio/malhas_territoriais/malhas_de_setores_censitarios__divisoes_intramunicipais/censo_2022/setores/shp/UF

Sistema:

Windows 10 pro, python 3.12.3, VScode 1.97.2

Bibliotecas python utilizadas:

pip install geopandas

pip install shapely

pip install pandas


Requisitos dados de entrada:

O nome do arquivo de entrada dever ser exatamente: dados_entradas.csv

Os dados de entrada devem conter as colunas: LATITUDE ; LONGITUDE, com escrita em maiúsculo.
ainda as latitude e longitudes devem ser pontos flutuantes com casas decimais separados por virgulas.

Dados de saida:
Ao final do processamento, o sistema gera um arquivo chamado dados_saida.csv que contem
uma coluna com o nome de "RURAL" que indica se o ponto pertence a zona rural ou não.

Observação:

O processamento pode demorar dependendo da quantidade de pontos a serem processados, pois
a complexidade do processamento é O(n*m), onde n é a quantidade de pontos a serem processados e m
a quantidade de setores censitários a serem processados.