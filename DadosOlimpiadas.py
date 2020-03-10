import pandas as pd

df = pd.read_csv('olympics.csv', index_col=0, skiprows=1) #Importando a tabela de dados de um arquivo csv.

for col in df.columns: #alterando a nomenclatura das colunas para nomes intuitivos.
    if col[:2]=='01':
        df.rename(columns={col:'Ouro'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Prata'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#'+col[1:]}, inplace=True)

df.rename(columns={'# Summer':'Verão','# Games':'Jogos', '# Winter':'Inverno','Combined total':'Combinacao total'}, inplace=True) #Renomeando as colunas

names_ids = df.index.str.split('\s\(') # Separando o index em paises e suas siglas.
df.index = names_ids.str[0] # Atualizando o index com os nomes da coluna 0 do name_ids
df['ID'] = names_ids.str[1].str[:3] # salvando na coluna ID a coluna 1 da tabela names_ids, sendo as 3 primeiras primeiras letras. Exemplo 'BRA'
df = df.drop('Totals') #retirando a coluna de totais

#Qual país tem mais medalhas de ouros nos jogos de verão ?
print( df.index[df['Ouro']== max(df['Ouro']) ) 

#Qual país tem a maior diferença de medalhas entre os jogos de verão e inverno ?
df.index[df['Ouro']-df['Ouro.1']== max(df['Ouro']-df['Ouro.1'])]

#Qual país tem a maior diferença entre medalhas de ouro verão menos as medalhas de ouro no inverno dividido pelo total de medalhas de ouros.
ouro= df.where( df['Ouro']   >  0)
ouro= df.where( df['Ouro.1'] > 0)
ouro= ouro.dropna()
ouro.index[(ouro['Ouro']-ouro['Ouro.1']) /ouro['Ouro.2']  == max( (ouro['Ouro']-ouro['Ouro.1'])/ ouro['Ouro.2'])]

#Crie uma coluna, a qual deve ter a soma de pontos. Ouro = 3 pontos, Prata= 2 Pontos e Bronze = 1 ponto.
points= df['Ouro']*3 +df['Prata']*2 + df['Bronze']+df['Ouro.2']*3 +df['Prata.2']*2 + df['Bronze.2'] #como o dataframe tem como indice a coluna de nomes, a variavel importará esse index também.
df.rename(columns={1:'#'+col[1:]}, inplace=True)

#Continuara as questões do Census.
