import pandas as pd


table = {'aluno': ['aluno_1', 'aluno_2', 'aluno_3', 'aluno_4'],
         'nota_1': [7, 3, 9, 10],
         'nota_2': [7, 10, 4, 6],
         'faltas': [1, 7, 2, 9]
        }
df = pd.DataFrame(table)

df['media'] = df['nota_1'] + df['nota_2']
df['media'] = df['media'] / 2
df['situação'] = 0

df.loc[df['media'] >= 7, 'situação'] = "APROVADO"
df.loc[df['media'] < 7, 'situação'] = "REPROVADO"
df.loc[df['faltas'] > 5, 'situação'] = "REPROVADO"

media = df['media'].median()
falta = df['faltas'].max()
maior_media = df['media'].max()

print(df)

print('A média geral dos alunos foi: ' +str (media))
print('O maior numero de faltas foi: ' +str (falta))
print('A maior média foi: ' +str (maior_media))






