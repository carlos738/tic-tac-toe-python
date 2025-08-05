# tic-tac-toe-python



jogo-da-velha-com-ia/ │ ├── README.md # Explicação do projeto ├── jogo_terminal.py # Versão terminal com IA Minimax ├── jogo_interface.py # Versão com interface gráfica (Tkinter) └── assets/ # Pasta para futuros ícones ou imagens (opcional)

Projeto: Jogo da Velha com Tkinter (Interface Gráfica em Python)

Descrição: Este projeto implementa o clássico jogo da velha (tic-tac-toe) usando a biblioteca Tkinter, que permite criar interfaces gráficas em Python. O jogo é jogado por dois jogadores (X e O) que se alternam clicando em botões dispostos em uma grade 3x3.

Componentes principais:

    Janela Principal (root):
        Criada com tk.Tk(), representa a janela principal da aplicação.
        Todos os elementos visuais (botões, textos) são adicionados a essa janela.

    Classe JogoDaVelha:
        Responsável por criar os botões do tabuleiro.
        Gerencia o estado do jogo (quem joga, se há vencedor, empate).
        Atualiza a interface conforme os jogadores fazem suas jogadas.

    Botões:
        Cada célula do tabuleiro é um botão.
        Ao clicar, o botão exibe "X" ou "O" dependendo do jogador atual.
        Após cada jogada, o jogo verifica se houve vitória ou empate.

    Lógica de Vitória:
        O jogo verifica todas as combinações possíveis de vitória (linhas, colunas e diagonais).
        Se um jogador vencer, uma mensagem é exibida e o tabuleiro é desabilitado.

    Reinício:
        Após o fim do jogo, o tabuleiro pode ser reiniciado para jogar novamente.

Execução: Para rodar o projeto, basta ter Python instalado e executar o arquivo principal com: python nome_do_arquivo.py

Observações:

    O projeto é ideal para iniciantes que desejam aprender sobre interfaces gráficas e lógica de jogos simples.
    Pode ser expandido com placar, modo contra o computador, ou animações.

Autor: [Seu Nome Aqui]
