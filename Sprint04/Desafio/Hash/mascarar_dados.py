import hashlib

while True:
    input_data = input(
        "Digite uma string para gerar o hash SHA-1(ou 'sair' para encerrar): "
    )
    if input_data.lower() == "sair":
        break

    hash_result = hashlib.sha1(input_data.encode()).hexdigest()
    print(f"Hash SHA-1: {hash_result}")