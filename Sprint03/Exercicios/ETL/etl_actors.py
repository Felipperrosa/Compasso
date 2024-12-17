import csv
from collections import Counter


# Função para criar os arquivos de saída
def criar_arquivos_saida(qtd):
    for i in range(1, qtd + 1):
        with open(f"etapa-{i}.txt", "w", encoding="utf-8") as f:
            pass


# Criar os arquivos de saída
criar_arquivos_saida(5)

# Ler o arquivo usando o módulo CSV
with open("actors.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    lines = list(reader)

# Ignorar cabeçalho e processar os dados
header = lines[0]  # Cabeçalho (se necessário)
data = lines[1:]  # Dados sem cabeçalho

# Limpar espaços, remover "Jr." com ponto e tratar colunas numéricas
for row in data:
    row[0] = row[0].replace("Jr.", "Jr").strip()  # Remover ponto em "Jr."
    row[1] = row[1].replace(",", "").strip()  # Receita total
    row[2] = row[2].strip()  # Número de filmes
    row[3] = row[3].strip()  # Média de receita
    row[5] = row[5].strip()  # Bilheteira bruta

# Etapa 1: Ator com o maior número de filmes
max_movies = max(data, key=lambda x: int(x[2]) if x[2].isdigit() else 0)
with open("etapa-1.txt", "w", encoding="utf-8") as f:
    f.write(f"{max_movies[0]} - {max_movies[2]} filmes\n")

# Etapa 2: Média de bilheteira bruta dos principais filmes
gross_values = []
for row in data:
    try:
        gross_values.append(float(row[5]))  # Convertendo bilheteira bruta
    except ValueError:
        continue  # Ignorar valores não numéricos

gross_avg = (
    sum(gross_values) / len(gross_values) if gross_values else 0
)  # Evitar divisão por zero
with open("etapa-2.txt", "w", encoding="utf-8") as f:
    f.write(f"Média de bilheteira bruta: {gross_avg:.2f}\n")

# Etapa 3: Ator com maior média de receita por filme
max_avg = max(
    data, key=lambda x: float(x[3]) if x[3].replace(".", "", 1).isdigit() else 0
)
with open("etapa-3.txt", "w", encoding="utf-8") as f:
    f.write(f"{max_avg[0]} - {max_avg[3]} média por filme\n")

# Etapa 4: Contagem de aparições de filmes na coluna "#1 Movie"
movies_count = Counter(row[4] for row in data)
sorted_movies = sorted(movies_count.items(), key=lambda x: (-x[1], x[0]))
with open("etapa-4.txt", "w", encoding="utf-8") as f:
    for movie, count in sorted_movies:
        f.write(f"O filme {movie} aparece {count} vez(es) no dataset\n")

# Etapa 5: Ordenar atores por receita total bruta
data_sorted = sorted(
    data,
    key=lambda x: float(x[1]) if x[1].replace(".", "", 1).isdigit() else 0,
    reverse=True,
)
with open("etapa-5.txt", "w", encoding="utf-8") as f:
    for row in data_sorted:
        f.write(f"{row[0]} - {row[1]}\n")

print(
    "Processamento concluído. Resultados armazenados nos arquivos etapa-1.txt a etapa-5.txt."
)
