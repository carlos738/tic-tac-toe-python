import tkinter as tk
from tkinter import messagebox
import math

class JogoDaVelha:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Velha com IA")
        self.tabuleiro = [['' for _ in range(3)] for _ in range(3)]
        self.botoes = [[None for _ in range(3)] for _ in range(3)]
        self.turno = 'X'
        self.criar_interface()

    def criar_interface(self):
        for i in range(3):
            for j in range(3):
                btn = tk.Button(self.root, text='', font=('Arial', 24), width=5, height=2,
                                command=lambda i=i, j=j: self.jogada(i, j))
                btn.grid(row=i, column=j)
                self.botoes[i][j] = btn

    def jogada(self, i, j):
        if self.tabuleiro[i][j] == '' and self.turno == 'X':
            self.tabuleiro[i][j] = 'X'
            self.botoes[i][j].config(text='X', state='disabled')
            if self.verificar_vitoria('X'):
                messagebox.showinfo("Fim de jogo", "Você venceu!")
                self.reiniciar()
            elif self.verificar_empate():
                messagebox.showinfo("Fim de jogo", "Empate!")
                self.reiniciar()
            else:
                self.turno = 'O'
                self.jogada_ia()

    def jogada_ia(self):
        melhor_pontuacao = -math.inf
        melhor_jogada = None
        for i in range(3):
            for j in range(3):
                if self.tabuleiro[i][j] == '':
                    self.tabuleiro[i][j] = 'O'
                    pontuacao = self.minimax(0, False)
                    self.tabuleiro[i][j] = ''
                    if pontuacao > melhor_pontuacao:
                        melhor_pontuacao = pontuacao
                        melhor_jogada = (i, j)
        if melhor_jogada:
            i, j = melhor_jogada
            self.tabuleiro[i][j] = 'O'
            self.botoes[i][j].config(text='O', state='disabled')
            if self.verificar_vitoria('O'):
                messagebox.showinfo("Fim de jogo", "A IA venceu!")
                self.reiniciar()
            elif self.verificar_empate():
                messagebox.showinfo("Fim de jogo", "Empate!")
                self.reiniciar()
            else:
                self.turno = 'X'

    def minimax(self, profundidade, is_max):
        if self.verificar_vitoria('O'):
            return 1
        elif self.verificar_vitoria('X'):
            return -1
        elif self.verificar_empate():
            return 0

        if is_max:
            melhor = -math.inf
            for i in range(3):
                for j in range(3):
                    if self.tabuleiro[i][j] == '':
                        self.tabuleiro[i][j] = 'O'
                        pontuacao = self.minimax(profundidade + 1, False)
                        self.tabuleiro[i][j] = ''
                        melhor = max(melhor, pontuacao)
            return melhor
        else:
            melhor = math.inf
            for i in range(3):
                for j in range(3):
                    if self.tabuleiro[i][j] == '':
                        self.tabuleiro[i][j] = 'X'
                        pontuacao = self.minimax(profundidade + 1, True)
                        self.tabuleiro[i][j] = ''
                        melhor = min(melhor, pontuacao)
            return melhor

    def verificar_vitoria(self, jogador):
        for linha in self.tabuleiro:
            if all(c == jogador for c in linha):
                return True
        for col in range(3):
            if all(self.tabuleiro[linha][col] == jogador for linha in range(3)):
                return True
        if all(self.tabuleiro[i][i] == jogador for i in range(3)) or all(self.tabuleiro[i][2 - i] == jogador for i in range(3)):
            return True
        return False

    def verificar_empate(self):
        return all(c in ['X', 'O'] for linha in self.tabuleiro for c in linha)

    def reiniciar(self):
        self.tabuleiro = [['' for _ in range(3)] for _ in range(3)]
        self.turno = 'X'
        for i in range(3):
            for j in range(3):
                self.botoes[i][j].config(text='', state='normal')

if __name__ == "__main__":
    root = tk.Tk()
    jogo = JogoDaVelha(root)
    root.mainloop()
