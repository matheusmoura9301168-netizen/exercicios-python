# Exercícios em Python

Exercícios que fui fazendo para aprender Python, organizados por tema: desde o básico até interfaces gráficas com Tkinter, bases de dados SQLite, NumPy e Matplotlib.

## Requisitos

- Python 3.10 ou superior (alguns exercícios usam `match-case`)
- Bibliotecas extra usadas em algumas pastas:

```bash
pip install numpy matplotlib customtkinter tkcalendar pygame
```

## Como executar

Cada ficheiro é um programa independente. Entra na pasta do tema e corre, por exemplo:

```bash
cd 08-ficheiros
python ler_ficheiro.py
```

Os exercícios de ficheiros leem os dados de `08-ficheiros/dados/` e os de SQLite criam as bases de dados em `11-sqlite/BDs/`, por isso devem ser executados de dentro da respetiva pasta.

## Conteúdo

### [Fundamentos](01-fundamentos/)

Entrada e saída de dados, variáveis e operações.

| Ficheiro | O que faz |
|---|---|
| [`soma_dois_numeros.py`](01-fundamentos/soma_dois_numeros.py) | Soma dois números inteiros. |
| [`area_perimetro_quadrado.py`](01-fundamentos/area_perimetro_quadrado.py) | Área e perímetro de um quadrado. |
| [`media_quatro_notas.py`](01-fundamentos/media_quatro_notas.py) | Média aritmética de quatro notas. |
| [`percentagem_por_sexo.py`](01-fundamentos/percentagem_por_sexo.py) | Percentagem de alunos de cada sexo numa turma. |
| [`area_perimetro_circulo.py`](01-fundamentos/area_perimetro_circulo.py) | Área e perímetro de um círculo. |
| [`operacoes_basicas.py`](01-fundamentos/operacoes_basicas.py) | As operações aritméticas com dois inteiros. |
| [`formatar_data.py`](01-fundamentos/formatar_data.py) | Lê dia, mês e ano e mostra a data com barras. |
| [`imc.py`](01-fundamentos/imc.py) | Índice de massa corporal a partir do peso e da altura. |
| [`celsius_para_fahrenheit.py`](01-fundamentos/celsius_para_fahrenheit.py) | Converte graus Celsius para Fahrenheit. |
| [`conversor_moedas.py`](01-fundamentos/conversor_moedas.py) | Converte euros para dólares com uma taxa fixa. |
| [`login_simples.py`](01-fundamentos/login_simples.py) | Guarda uma senha e pede-a de novo para fazer login. |

### [Condicionais](02-condicionais/)

if/elif/else e match-case.

| Ficheiro | O que faz |
|---|---|
| [`aprovacao_disciplina.py`](02-condicionais/aprovacao_disciplina.py) | Aprovação direta ou por exame. |
| [`candidato_aprovado.py`](02-condicionais/candidato_aprovado.py) | Verifica se um candidato cumpre idade, nota e escolaridade. |
| [`desconto_por_quantidade.py`](02-condicionais/desconto_por_quantidade.py) | Fatura com desconto conforme a quantidade comprada. |
| [`maior_de_idade.py`](02-condicionais/maior_de_idade.py) | Calcula a idade pelo ano de nascimento. |
| [`requisitos_vaga.py`](02-condicionais/requisitos_vaga.py) | Verifica os requisitos de idade e experiência para uma vaga. |
| [`positivo_negativo_zero.py`](02-condicionais/positivo_negativo_zero.py) | Indica se um número é positivo, negativo ou zero. |
| [`calculadora_match.py`](02-condicionais/calculadora_match.py) | Calculadora com match-case. |
| [`equacao_segundo_grau.py`](02-condicionais/equacao_segundo_grau.py) | Raízes de uma equação do 2.º grau. |
| [`cor_da_fruta.py`](02-condicionais/cor_da_fruta.py) | Diz a cor de uma fruta com match-case. |
| [`par_ou_impar.py`](02-condicionais/par_ou_impar.py) | Par ou ímpar agrupando casos no match. |
| [`dia_da_semana.py`](02-condicionais/dia_da_semana.py) | Converte um número de 1 a 7 no dia da semana. |
| [`numero_por_extenso.py`](02-condicionais/numero_por_extenso.py) | Mostra por extenso números de 1 a 6, agrupados aos pares. |

### [Ciclos](03-ciclos/)

for, while e pequenos programas com menus em ciclo.

| Ficheiro | O que faz |
|---|---|
| [`contar_ate_100.py`](03-ciclos/contar_ate_100.py) | Mostra os números de 1 a 100. |
| [`contar_ate_12.py`](03-ciclos/contar_ate_12.py) | Mostra os números de 1 a 12. |
| [`contar_ate_n.py`](03-ciclos/contar_ate_n.py) | Conta de 1 até ao número indicado. |
| [`contagem_decrescente.py`](03-ciclos/contagem_decrescente.py) | Conta do número indicado até 1. |
| [`soma_ate_n.py`](03-ciclos/soma_ate_n.py) | Soma de 1 até n. |
| [`repetir_palavra.py`](03-ciclos/repetir_palavra.py) | Repete uma palavra n vezes. |
| [`tabuada.py`](03-ciclos/tabuada.py) | Tabuada de um número. |
| [`pares_no_intervalo.py`](03-ciclos/pares_no_intervalo.py) | Mostra os números pares de um intervalo. |
| [`quantos_pares_no_intervalo.py`](03-ciclos/quantos_pares_no_intervalo.py) | Conta os números pares de um intervalo. |
| [`intervalo_de_dois_em_dois.py`](03-ciclos/intervalo_de_dois_em_dois.py) | Percorre um intervalo de dois em dois. |
| [`progressao_aritmetica.py`](03-ciclos/progressao_aritmetica.py) | Termos e soma de uma progressão aritmética. |
| [`progressao_aritmetica_continua.py`](03-ciclos/progressao_aritmetica_continua.py) | Mostra termos de uma PA enquanto o utilizador pedir mais. |
| [`progressao_geometrica.py`](03-ciclos/progressao_geometrica.py) | Termos e soma de uma progressão geométrica. |
| [`contar_pares_impares.py`](03-ciclos/contar_pares_impares.py) | Conta pares e ímpares até ser introduzido 0. |
| [`media_dez_notas.py`](03-ciclos/media_dez_notas.py) | Média de 10 notas entre 0 e 20, com validação. |
| [`media_ate_parar.py`](03-ciclos/media_ate_parar.py) | Lê números até o utilizador responder N e mostra a média. |
| [`media_dez_numeros.py`](03-ciclos/media_dez_numeros.py) | Média de 10 números. |
| [`soma_e_media.py`](03-ciclos/soma_e_media.py) | Soma e média de n valores. |
| [`soma_e_media_funcoes.py`](03-ciclos/soma_e_media_funcoes.py) | O mesmo exercício usando funções. |
| [`comparar_com_20.py`](03-ciclos/comparar_com_20.py) | Conta, soma e faz a média dos números acima e abaixo de 20. |
| [`intervalo_com_passo.py`](03-ciclos/intervalo_com_passo.py) | Percorre um intervalo com passo e conta os pares. |
| [`banco_com_senha.py`](03-ciclos/banco_com_senha.py) | Conta bancária simples protegida por senha. |
| [`caixa_multibanco.py`](03-ciclos/caixa_multibanco.py) | Depósitos, levantamentos e saldo. |

### [Funcoes e modulos](04-funcoes-e-modulos/)

Funções, recursividade, módulos próprios e tratamento de exceções.

| Ficheiro | O que faz |
|---|---|
| [`area_terreno.py`](04-funcoes-e-modulos/area_terreno.py) | Área de um terreno com uma função. |
| [`inverter_numero.py`](04-funcoes-e-modulos/inverter_numero.py) | Inverte os dígitos de um número. |
| [`potencia.py`](04-funcoes-e-modulos/potencia.py) | Potência calculada com um ciclo dentro de uma função. |
| [`fatorial_recursivo.py`](04-funcoes-e-modulos/fatorial_recursivo.py) | Fatorial com recursividade. |
| [`calculadora_sem_funcoes.py`](04-funcoes-e-modulos/calculadora_sem_funcoes.py) | Calculadora com menu, sem funções. |
| [`calculadora_com_funcoes.py`](04-funcoes-e-modulos/calculadora_com_funcoes.py) | A mesma calculadora organizada em funções. |
| [`calculadora_expressoes.py`](04-funcoes-e-modulos/calculadora_expressoes.py) | Avalia expressões escritas pelo utilizador até escrever 'sair'. |
| [`calculadora_com_excecoes.py`](04-funcoes-e-modulos/calculadora_com_excecoes.py) | Calculadora com tratamento de exceções. |
| [`menu_utilizadores.py`](04-funcoes-e-modulos/menu_utilizadores.py) | Registo, listagem e pesquisa de utilizadores. |
| [`calculadora_modulo/calculadora.py`](04-funcoes-e-modulos/calculadora_modulo/calculadora.py) | Módulo com as quatro operações. |
| [`calculadora_modulo/main.py`](04-funcoes-e-modulos/calculadora_modulo/main.py) | Menu que usa o módulo calculadora. |
| [`calculadora_validada/MD_CC.py`](04-funcoes-e-modulos/calculadora_validada/MD_CC.py) | Funções de leitura com validação dos números e da operação. |
| [`calculadora_validada/main.py`](04-funcoes-e-modulos/calculadora_validada/main.py) | Programa principal que importa o módulo MD_CC. |

### [Listas e dicionarios](05-listas-e-dicionarios/)

Listas, dicionários e alguns algoritmos clássicos (ordenação e pesquisa).

| Ficheiro | O que faz |
|---|---|
| [`listas_com_range.py`](05-listas-e-dicionarios/listas_com_range.py) | Criação de listas com range. |
| [`min_max_soma.py`](05-listas-e-dicionarios/min_max_soma.py) | Mínimo, máximo e soma de uma lista. |
| [`verificar_elemento.py`](05-listas-e-dicionarios/verificar_elemento.py) | Verifica se um elemento existe na lista. |
| [`media_lista.py`](05-listas-e-dicionarios/media_lista.py) | Média feita à mão e com statistics.mean. |
| [`comandos_de_lista.py`](05-listas-e-dicionarios/comandos_de_lista.py) | Menu com os principais métodos de listas. |
| [`menu_lista.py`](05-listas-e-dicionarios/menu_lista.py) | Menu de operações sobre uma lista com contador de elementos. |
| [`abaixo_da_media.py`](05-listas-e-dicionarios/abaixo_da_media.py) | Valores abaixo da média. |
| [`separar_pares_impares.py`](05-listas-e-dicionarios/separar_pares_impares.py) | Separa números pares e ímpares em listas diferentes. |
| [`lista_ordenada_e_pares.py`](05-listas-e-dicionarios/lista_ordenada_e_pares.py) | Ordena uma lista e extrai os números pares. |
| [`remover_duplicados.py`](05-listas-e-dicionarios/remover_duplicados.py) | Remove elementos repetidos mantendo a ordem. |
| [`filtrar_maiores.py`](05-listas-e-dicionarios/filtrar_maiores.py) | Filtra os números maiores que um valor. |
| [`maior_e_menor.py`](05-listas-e-dicionarios/maior_e_menor.py) | Maior e menor de uma lista. |
| [`soma_lista.py`](05-listas-e-dicionarios/soma_lista.py) | Soma dos elementos de uma lista. |
| [`numeros_aleatorios.py`](05-listas-e-dicionarios/numeros_aleatorios.py) | Lista de números aleatórios. |
| [`bubble_sort.py`](05-listas-e-dicionarios/bubble_sort.py) | Ordenação pelo método da bolha. |
| [`pesquisa_binaria.py`](05-listas-e-dicionarios/pesquisa_binaria.py) | Pesquisa binária numa lista ordenada. |
| [`diagonal_matriz.py`](05-listas-e-dicionarios/diagonal_matriz.py) | Diagonal principal de uma matriz 3x3. |
| [`soma_matriz.py`](05-listas-e-dicionarios/soma_matriz.py) | Soma de todos os elementos de uma matriz. |
| [`inverter_dicionario.py`](05-listas-e-dicionarios/inverter_dicionario.py) | Troca as chaves pelos valores de um dicionário. |
| [`controlo_stock.py`](05-listas-e-dicionarios/controlo_stock.py) | Controlo de stock de uma mercearia com dicionário. |
| [`letra_mais_frequente.py`](05-listas-e-dicionarios/letra_mais_frequente.py) | Letra mais frequente de uma frase. |

### [Strings](06-strings/)

Manipulação de texto.

| Ficheiro | O que faz |
|---|---|
| [`inverter_texto.py`](06-strings/inverter_texto.py) | Inverte um texto. |
| [`palindromo.py`](06-strings/palindromo.py) | Verifica se uma palavra é um palíndromo. |
| [`contar_vogais.py`](06-strings/contar_vogais.py) | Conta as vogais de um texto. |
| [`vogais_e_consoantes.py`](06-strings/vogais_e_consoantes.py) | Conta vogais e consoantes. |
| [`contar_letras.py`](06-strings/contar_letras.py) | Conta as letras de uma frase, sem espaços nem símbolos. |
| [`alternar_maiusculas.py`](06-strings/alternar_maiusculas.py) | Alterna maiúsculas e minúsculas numa palavra. |
| [`analisar_letra.py`](06-strings/analisar_letra.py) | Quantas vezes aparece a letra E e em que posições. |
| [`analisar_nome.py`](06-strings/analisar_nome.py) | Primeiro e último nome, maiúsculas e minúsculas. |
| [`contem_apelido.py`](06-strings/contem_apelido.py) | Verifica se o nome contém o apelido Pereira. |
| [`gerar_email.py`](06-strings/gerar_email.py) | Gera um endereço de e-mail a partir do nome. |
| [`validar_senha.py`](06-strings/validar_senha.py) | Verifica se uma senha é forte. |
| [`gerar_senha.py`](06-strings/gerar_senha.py) | Gera uma senha aleatória de 10 caracteres. |
| [`cifra_codificar.py`](06-strings/cifra_codificar.py) | Codifica um texto deslocando cada carácter 3 posições. |
| [`cifra_descodificar.py`](06-strings/cifra_descodificar.py) | Descodifica o texto da cifra anterior. |
| [`subsequencia.py`](06-strings/subsequencia.py) | Verifica se as letras de uma palavra aparecem por ordem numa frase. |

### [Regex e datas](07-regex-e-datas/)

Validações com expressões regulares e trabalho com datas.

| Ficheiro | O que faz |
|---|---|
| [`validar_telefone.py`](07-regex-e-datas/validar_telefone.py) | Valida um número de telefone com regex. |
| [`validar_telefone_funcao.py`](07-regex-e-datas/validar_telefone_funcao.py) | A mesma validação dentro de uma função. |
| [`validar_numero.py`](07-regex-e-datas/validar_numero.py) | Verifica se um texto representa um número inteiro ou decimal. |
| [`validar_nome_completo.py`](07-regex-e-datas/validar_nome_completo.py) | Obriga a introduzir nome e apelido. |
| [`validar_senha_regex.py`](07-regex-e-datas/validar_senha_regex.py) | Regras de senha verificadas com regex. |
| [`validar_dados_pessoais.py`](07-regex-e-datas/validar_dados_pessoais.py) | Formulário na consola que valida nome, data de nascimento e código de perfil. |
| [`validar_data.py`](07-regex-e-datas/validar_data.py) | Aceita datas com / ou - e verifica se são válidas. |
| [`datetime_basico.py`](07-regex-e-datas/datetime_basico.py) | Exemplos com datetime, date e time. |
| [`calendario_do_mes.py`](07-regex-e-datas/calendario_do_mes.py) | Mostra o calendário de um mês. |

### [Ficheiros](08-ficheiros/)

Leitura e escrita de ficheiros de texto.

| Ficheiro | O que faz |
|---|---|
| [`criar_e_acrescentar.py`](08-ficheiros/criar_e_acrescentar.py) | Cria um ficheiro, acrescenta linhas e lê o conteúdo. |
| [`escrever_com_print.py`](08-ficheiros/escrever_com_print.py) | Escreve num ficheiro usando print(file=...). |
| [`ler_ficheiro.py`](08-ficheiros/ler_ficheiro.py) | Lê um ficheiro inteiro. |
| [`ler_tres_caracteres.py`](08-ficheiros/ler_tres_caracteres.py) | Lê apenas os três primeiros caracteres. |
| [`ler_linhas_for.py`](08-ficheiros/ler_linhas_for.py) | Lê linha a linha com for. |
| [`ler_linhas_while.py`](08-ficheiros/ler_linhas_while.py) | Lê linha a linha com while. |
| [`voltar_ao_inicio.py`](08-ficheiros/voltar_ao_inicio.py) | Volta ao início do ficheiro com seek(0). |
| [`avancar_posicao.py`](08-ficheiros/avancar_posicao.py) | Avança a posição de leitura com seek e tell. |
| [`recuar_posicao.py`](08-ficheiros/recuar_posicao.py) | Recua a posição de leitura com seek e tell. |
| [`escrever_e_ler.py`](08-ficheiros/escrever_e_ler.py) | Escreve um texto num ficheiro e lê-o de volta. |
| [`registar_movimento.py`](08-ficheiros/registar_movimento.py) | Acrescenta um movimento à lista de compras. |
| [`calcular_saldo.py`](08-ficheiros/calcular_saldo.py) | Calcula o saldo final a partir dos movimentos do ficheiro. |
| [`substituir_texto.py`](08-ficheiros/substituir_texto.py) | Copia um ficheiro para outro substituindo um texto. |

### [Numpy e matplotlib](09-numpy-e-matplotlib/)

Arrays com NumPy e gráficos com Matplotlib.

| Ficheiro | O que faz |
|---|---|
| [`numpy_array_1d.py`](09-numpy-e-matplotlib/numpy_array_1d.py) | Array unidimensional: tipo, tamanho e acesso. |
| [`numpy_array_2d.py`](09-numpy-e-matplotlib/numpy_array_2d.py) | Array bidimensional: dimensões e formato. |
| [`numpy_operacoes.py`](09-numpy-e-matplotlib/numpy_operacoes.py) | Operações aritméticas sobre um array. |
| [`numpy_entre_arrays.py`](09-numpy-e-matplotlib/numpy_entre_arrays.py) | Operações entre dois arrays e produto escalar. |
| [`numpy_matrizes.py`](09-numpy-e-matplotlib/numpy_matrizes.py) | Soma, produto e transposta de matrizes. |
| [`numpy_estatisticas.py`](09-numpy-e-matplotlib/numpy_estatisticas.py) | Média, mediana e desvio padrão de uma matriz aleatória. |
| [`numpy_menu_array.py`](09-numpy-e-matplotlib/numpy_menu_array.py) | Menu de operações sobre um array NumPy. |
| [`grafico_valores_y.py`](09-numpy-e-matplotlib/grafico_valores_y.py) | Gráfico de linha só com valores de y. |
| [`grafico_x_y.py`](09-numpy-e-matplotlib/grafico_x_y.py) | Gráfico de linha com x e y. |
| [`grafico_pontos.py`](09-numpy-e-matplotlib/grafico_pontos.py) | Gráfico apenas com pontos. |
| [`grafico_estilos.py`](09-numpy-e-matplotlib/grafico_estilos.py) | Três séries com estilos de linha diferentes. |
| [`grafico_funcoes.py`](09-numpy-e-matplotlib/grafico_funcoes.py) | Funções linear, quadrática e cúbica no mesmo gráfico. |
| [`grafico_varios_tipos.py`](09-numpy-e-matplotlib/grafico_varios_tipos.py) | Linha, dispersão e barras lado a lado. |
| [`grafico_lista.py`](09-numpy-e-matplotlib/grafico_lista.py) | Lê 8 números, mostra o máximo e o mínimo e desenha o gráfico. |

### [Tkinter](10-tkinter/)

Interfaces gráficas com Tkinter e CustomTkinter.

| Ficheiro | O que faz |
|---|---|
| [`01_janela_basica.py`](10-tkinter/01_janela_basica.py) | Cria uma janela vazia. |
| [`02_hello_world.py`](10-tkinter/02_hello_world.py) | Janela com uma mensagem. |
| [`03_label_com_estilo.py`](10-tkinter/03_label_com_estilo.py) | Label com fonte, cor de fundo e largura. |
| [`04_label_e_entry.py`](10-tkinter/04_label_e_entry.py) | Label e Entry ligados a StringVar, atualizados por um botão. |
| [`05_alinhar_texto.py`](10-tkinter/05_alinhar_texto.py) | Alinhamento do texto dentro de um Label com anchor. |
| [`06_texto_justificado.py`](10-tkinter/06_texto_justificado.py) | Texto justificado e propriedades do label. |
| [`07_propriedades_label.py`](10-tkinter/07_propriedades_label.py) | Lista as propriedades disponíveis de um Label. |
| [`08_valores_propriedades.py`](10-tkinter/08_valores_propriedades.py) | Mostra cada propriedade do Label com o seu valor. |
| [`09_propriedades_frame.py`](10-tkinter/09_propriedades_frame.py) | Mostra a documentação da classe Frame com help(). |
| [`10_frames_formulario.py`](10-tkinter/10_frames_formulario.py) | Formulário de nome e morada dividido em frames. |
| [`11_frame_com_botoes.py`](10-tkinter/11_frame_com_botoes.py) | Frame com vários botões. |
| [`12_layout_grid.py`](10-tkinter/12_layout_grid.py) | Posicionamento com grid. |
| [`13_botao_com_argumento.py`](10-tkinter/13_botao_com_argumento.py) | Botão que chama uma função com argumento (lambda). |
| [`14_scale.py`](10-tkinter/14_scale.py) | Controlo deslizante (Scale) que mostra o valor escolhido. |
| [`15_widget_message.py`](10-tkinter/15_widget_message.py) | Texto em várias linhas com o widget Message. |
| [`16_imagem_num_label.py`](10-tkinter/16_imagem_num_label.py) | Mostra uma imagem dentro de um Label (precisa de img/nome.png). |
| [`17_checkbutton.py`](10-tkinter/17_checkbutton.py) | Caixa de seleção e leitura do seu estado. |
| [`18_radiobutton.py`](10-tkinter/18_radiobutton.py) | Escolha única com Radiobutton. |
| [`19_combobox.py`](10-tkinter/19_combobox.py) | Lista pendente com Combobox. |
| [`20_listbox.py`](10-tkinter/20_listbox.py) | Listbox com seleção múltipla. |
| [`21_estilos_relief.py`](10-tkinter/21_estilos_relief.py) | Os vários estilos de borda (relief) de um Label. |
| [`22_option_menu.py`](10-tkinter/22_option_menu.py) | Menu pendente (OptionMenu) que mostra a opção escolhida. |
| [`23_barra_de_menu.py`](10-tkinter/23_barra_de_menu.py) | Barra de menus no topo da janela. |
| [`24_ecra_login.py`](10-tkinter/24_ecra_login.py) | Ecrã de login simples. |
| [`25_ecra_login_centrado.py`](10-tkinter/25_ecra_login_centrado.py) | Ecrã de login centrado na janela. |
| [`26_login_em_frame.py`](10-tkinter/26_login_em_frame.py) | Login organizado dentro de um Frame. |
| [`27_formulario_produtos.py`](10-tkinter/27_formulario_produtos.py) | Formulário de produtos com cálculo do valor a pagar. |
| [`28_calendario_data_maxima.py`](10-tkinter/28_calendario_data_maxima.py) | Calendário que não deixa escolher datas futuras. |
| [`29_selecionar_horario.py`](10-tkinter/29_selecionar_horario.py) | Escolha de horas e minutos com Spinbox. |
| [`30_calcular_total.py`](10-tkinter/30_calcular_total.py) | Quantidade e preço com validação e total a pagar. |
| [`31_combobox_distritos.py`](10-tkinter/31_combobox_distritos.py) | Combobox com os distritos de Portugal e validação. |
| [`32_login_customtkinter.py`](10-tkinter/32_login_customtkinter.py) | Login com CustomTkinter em modo escuro. |

### [Sqlite](11-sqlite/)

Bases de dados SQLite na consola.

| Ficheiro | O que faz |
|---|---|
| [`criar_tabela_clientes.py`](11-sqlite/criar_tabela_clientes.py) | Cria a tabela de clientes. |
| [`gestao_clientes.py`](11-sqlite/gestao_clientes.py) | Adicionar, listar, procurar e remover clientes. |
| [`criar_bd_formulario.py`](11-sqlite/criar_bd_formulario.py) | Cria a base de dados usada pelo formulário de clientes. |
| [`formulario_clientes.py`](11-sqlite/formulario_clientes.py) | Menu de clientes com id automático. |
| [`exercicios_agenda.py`](11-sqlite/exercicios_agenda.py) | Exercícios com uma agenda: inserir, consultar e filtrar. |
| [`loja_consola.py`](11-sqlite/loja_consola.py) | Loja na consola com clientes, fornecedores, produtos e pedidos. |

### [Jogos](12-jogos/)

Jogos de consola e o Snake em Pygame.

| Ficheiro | O que faz |
|---|---|
| [`numero_secreto.py`](12-jogos/numero_secreto.py) | Adivinhar um número de 1 a 10. |
| [`adivinha_com_pontuacao.py`](12-jogos/adivinha_com_pontuacao.py) | Adivinhar um número até 1000 com pontuação. |
| [`pedra_papel_tesoura.py`](12-jogos/pedra_papel_tesoura.py) | Pedra, papel ou tesoura contra o computador. |
| [`blackjack_multiplayer.py`](12-jogos/blackjack_multiplayer.py) | Blackjack para vários jogadores. |
| [`menu_de_jogos.py`](12-jogos/menu_de_jogos.py) | Menu com jogos de adivinha e blackjack. |
| [`snake.py`](12-jogos/snake.py) | Jogo da cobra feito com Pygame. |
