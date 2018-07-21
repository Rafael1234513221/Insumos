"""
Interface gráfica do programa.
"""

from funções import *
from tkinter import *
from tkinter import messagebox
from functools import partial


class Aplicativo:
    """
    Classe que faz a interface ter vida.
    """
    def __init__(self, master):
        """
        Inicia as funções/Frames com o construtor.
        """
        self.fonte = ('Monaco', 13)
        # Criando os Frames.
        self.frame0 = Frame(master) 
        self.frame1 = Frame(master) 
        self.frame2 = Frame(master) 
        self.frame3 = Frame(master)
        self.frame4 = Frame(master) 
        # Ativando os Frames
        self.frame0.grid()
        self.frame1.grid()
        self.frame2.grid()
        self.frame3.grid()
        self.frame4.grid()
        # Chamandos os elementos gráficos separados por tipagem (botões, entradas, salário).
        self.entradas()
        self.botoes()
        self.mostrar_salário()

    def entradas(self):
        """
        Cria todos as caixas de input para recolhimento de dados passados pelo usuário.
        """
        # Cria uma caixa de entrada para usuário digitar o nome do produto.
        Label(self.frame0, text='CADASTRE SUAS COMPRAS', height=2, font=self.fonte).grid(row=0, column=1)
        Label(self.frame1, text='PRODUTO', font=('Arial', 10), bg='gray', width=8).grid(row=0, column=1)
        self.ent_produto = Entry(self.frame1, width=20, font=self.fonte)
        self.ent_produto.focus_force()
        self.ent_produto.grid(row=0, column=2)
        # Cria uma caixa de entrada para usuário digitar o valor(R$) do produto.
        Label(self.frame1, text='VALOR: R$', font=('Arial', 10), bg='gray', width=8).grid(row=1, column=1)
        self.ent_valor = Entry(self.frame1, width=20, font=self.fonte)
        self.ent_valor.grid(row=1, column=2)
        # Cria uma caixa de entrada para usuário digitar a quantidade de parcelas.
        Label(self.frame1, text='Vezes', font=('Arial', 10), bg='gray', width=8).grid(row=2, column=1)
        self.ent_parcelas = Entry(self.frame1, width=20, font=self.fonte)
        self.ent_parcelas.grid(row=2, column=2)


    def botoes(self):
        """
        Cria todos os botões e atribui a eles seus devidos comandos.
        """
        # Cria o botão de limpar os dados digitados na tela caso haja algum erro de digitação.
        limpar = Button(self.frame1, text='LIMPAR', bg='red', fg='white', width=11)
        limpar.grid(row=3, column=1, columnspan=2)
        limpar['command'] = self.limpar
        # Cria o botão com função de cadastrar os dados digitados nas entradas pelo usuário.
        cadastrar = Button(self.frame1, text='CADASTRAR', bg='green', fg='white', width=11)
        cadastrar['command'] = partial(self.cadastramento, self.ent_produto, self.ent_valor, self.ent_parcelas)
        cadastrar.grid(row=4, column=1, columnspan=2)
        # Botão referente a verificar o histórico de compras feita no mês em que foi clicado.
        self.ver_compras = Button(self.frame1, text='EXTRATO', bg='orange', fg='white', width=11)
        self.ver_compras['command'] = self.vver_compras
        self.ver_compras.grid(row=5, column=1, columnspan=2)
        'Futuro'
        # window.bind('<Return>', partial(cadastramento, 'Sumiu', self.ent_produto, self.ent_valor))

    def limpar(self):
        """
        Função responsável por limpar os dados que estão na tela.
        """
        self.ent_produto.delete(0, END)  # Deleta o que foi digitado na entrada: produto.
        self.ent_valor.delete(0, END)  # Deleta o que foi digitado na entrada: valor.
        self.ent_parcelas.delete(0, END)  # Deleta o que foi digitado na entrada: parcelas
        self.ent_produto.focus_force()  # Faz o foco(cursor) voltar pra caixa de entrada do produto.

    
    def cadastramento(self, produto, valor, parcelas):
        """
        Pega os dois valores passado pelo usuário e chama uma função externa para cadastra-los.
        """
        produto = produto.get()  # Pega os dados que foram digitados pelo usuário e salva numa variável.
        valor = valor.get()  # Pega os dados que foram digitados pelo usuário e salva numa variável.
        parcelas = parcelas.get()
        cadastrar_dados(produto, valor, parcelas)  # Chama a função externa e passa as 3 entradas(produto, valor, parcelas).
        self.salario['text'] = f'Salário: R${atualiza_salário()}'  # Atualiza o Label que mostra o salário.
        self.limpar()  # Chama a função responsável por limpar os campos digitados pelo usuário
        compras_mensais()

    def mostrar_salário(self):
        """
        É retornado o valor do seu salário menos as compras feitas, usando função  externa.
        """
        self.salario = Label(self.frame1, text=f'Salário: R${atualiza_salário()}', height=2, font=self.fonte)
        self.salario.grid(row=7, column=1, columnspan=2)

    def vver_compras(self):
        """
        Chama uma função externa que consulta as últimas compras (Mês em questão).
        """
        if self.ver_compras['text'] == 'Minimizar extrato':
            window.geometry('300x252+104+104')
            self.ver_compras['text'] == 'EXTRATO'
            self.entradas()
            self.botoes()
            self.mostrar_salário()

        elif self.ver_compras['text'] == 'EXTRATO':
            window.geometry('300x500+104+104')
            self.ver_compras['text'] = 'Minimizar extrato'
            self.ver_extrato = Label(self.frame3, text=f'EXTRATO\n{compras_mensais()}')
            self.ver_extrato.grid(row=8, column=1, columnspan=2)


window = Tk()
window.title('INSUMOS')
window.geometry('300x252+104+104')
Aplicativo(window)
window.mainloop()
