import hashlib

while True:
    entrada = input("Digite uma string (ou 'S' para sair): ")
    if entrada.lower() == "s":
        break

    hash_resultado = hashlib.sha1(entrada.encode()).hexdigest()
    print(f"Hash SHA-1: {hash_resultado}")
