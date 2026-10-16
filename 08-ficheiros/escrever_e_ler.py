# Escreve um texto num ficheiro e lê-o de volta.

f=open("arquivo.txt","w");f.write(input());f.close();print(open("arquivo.txt").read())
