import random
import pyttsx3
from main import Jogo


class Genius(Jogo):
    def __init__(self):
        super().__init__()
        self.cores = ['vermelho', 'azul', 'verde', 'amarelo', 'roxo', 'laranja', 'preto', 'branco', 'cinza', 'marrom',
                      'rosa', 'turquesa', 'violeta', 'bege']
        self.engine = pyttsx3.init()

    @staticmethod
    def gerar_sequencia(tamanho):
        return [random.choice(Genius().cores) for _ in range(tamanho)]

    def jogador_joga(self):
        return input("Digite a sequência (separe as cores por espaço): ").split()

    @staticmethod
    def verificar_sequencia(sequencia, jogador_sequencia):
        return sequencia == jogador_sequencia

    def dizer_sequencia(self, sequencia):
        self.engine.say("A sequência é: ")
        self.engine.say(" ".join(sequencia))
        self.engine.runAndWait()

    def jogar(self):
        tamanho_sequencia = 3

        print("\nVOCE ESCOLHEU GENIUS MAN!!!!!\n")

        while True:
            sequencia = self.gerar_sequencia(tamanho_sequencia)

            self.dizer_sequencia(sequencia)

            sequencia_jogador = self.jogador_joga()

            if self.verificar_sequencia(sequencia, sequencia_jogador):
                print("Parabéns! Você acertou a sequência.\n")
                self.set_pontuacao(100)  # Aumenta a pontuação se a sequência estiver correta
                #limpar terminal
            else:
                print("\nVocê errou a sequência. Fim do jogo.")
                print(f"A sequência era: {sequencia}\n")
                break


            self.get_mostrar_pontuacao()  # Mostra a pontuação final quando o jogo termina

            input("\nPressione Enter para continuar...\n")
            tamanho_sequencia += 1  # Incrementa o tamanho da sequência para a próxima rodada


if __name__ == "__main__":
    genius_game = Genius()
    genius_game.jogar()
