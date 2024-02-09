import os

#Coloque o nome correto do diretório onde estão os seus arquivos
os.chdir('C:\\Users\\User\\Documents\\Directory')
print(f'Diretório atual: {os.getcwd()}')

padrao_nome = input('Qual o padrão de nomes de arquivos a usar (sem a extensão)?')

for contador, arq in enumerate(os.listdir()):
    if os.path.isfile(arq):
        nome_arq, exten_arq = os.path.splitext(arq)
        nome_arq = padrao_nome + ' ' + str(contador)
        
        nome_novo = f'{nome_arq}{exten_arq}'
        os.rename(arq, nome_novo)

print(f'\nArquivos renomeados')