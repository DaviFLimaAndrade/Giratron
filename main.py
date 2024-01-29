import random
import pyttsx3


class Jogo:
    regras = "regras do jogo..."
    pontuacao = 0

    @classmethod
    def get_mostrar_regras(cls):
        print("Regras do Jogo:")
        print(cls.regras)

    @classmethod
    def get_mostrar_pontuacao(cls):
        print(f"Sua pontuação atual é: {cls.pontuacao}")

    @classmethod
    def set_pontuacao(cls, pontos):
        cls.pontuacao += pontos
