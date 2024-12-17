# Implemente duas classes, Pato e Pardal , que herdam de uma superclasse chamada Passaro as habilidades de voar e emitir som.


# Contudo, tanto Pato quanto Pardal devem emitir sons diferentes (de maneira escrita) no console, conforme o modelo a seguir.

# Pato
# Voando...
# Pato emitindo som...
# Quack Quack
# Pardal
# Voando...
# Pardal emitindo som...
# Piu Piu


class Passaro:
    def __init__(self, nome):
        self.nome = nome

    def voar(self):
        return f"Voando..."

    def emetir_som(self):
        pass


class Pato(Passaro):

    def emetir_som(self):
        return f"Quack Quack"


class Pardal(Passaro):

    def emetir_som(self):
        return f"Piu Piu"


pato = Pato("Pato")
pardal = Pardal("Pardal")

print("Pato")
print(pato.voar())
print(pato.emetir_som())
print("Pardal")
print(pardal.voar())
print(pardal.emetir_som())
