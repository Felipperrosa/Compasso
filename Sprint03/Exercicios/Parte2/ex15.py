# Exercícios Parte 2
# Implemente a classe Lampada. A classe Lâmpada recebe um booleano no seu construtor, Truese a lâmpada estiver ligada, False caso esteja desligada. A classe Lampada possuí os seguintes métodos:

# liga(): muda o estado da lâmpada para ligada

# desliga(): muda o estado da lâmpada para desligada

# esta_ligada(): retorna verdadeiro se a lâmpada estiver ligada, falso caso contrário

# Para testar sua classe:

# Ligue a Lampada

# Imprima: A lâmpada está ligada? True

# Desligue a Lampada

# Imprima: A lâmpada ainda está ligada? False


class Lampada:
    def __init__(self, ligada: bool):
        # Inicializa a lâmpada com o estado fornecido (ligada ou desligada)
        self.ligada = ligada

    def liga(self):
        # Método para ligar a lâmpada
        self.ligada = True

    def desliga(self):
        # Método para desligar a lâmpada
        self.ligada = False

    def esta_ligada(self) -> bool:
        return self.ligada


lampada = Lampada(False)


lampada.liga()
print(f" A lâmpada está ligada?{lampada.esta_ligada()}")

lampada.desliga()
print(f" A lâmpada ainda está ligada?{lampada.esta_ligada()}")
