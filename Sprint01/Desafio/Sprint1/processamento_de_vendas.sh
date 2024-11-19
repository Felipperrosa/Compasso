#!/bin/bash

# Define o diretório de trabalho
cd /home/felippe/Sprint1

#  Cria um diretório chamado vendas
mkdir -p /home/felippe/Sprint1/vendas

#  Copia o arquivo dados_de_vendas.csv de ecommerce para dentro do diretório vendas
cp /home/felippe/Sprint1/ecommerce/dados_de_vendas.csv /home/felippe/Sprint1/vendas/

#  Cria um subdiretório chamado backup dentro do diretório vendas
mkdir -p /home/felippe/Sprint1/vendas/backup

#  Data atual no formato YYYYMMDD
data_de_execucao=$(date +"%Y%m%d")

#  Copia o arquivo dados_de_vendas.csv para dentro do diretório backup com a data de execução
cp /home/felippe/Sprint1/vendas/dados_de_vendas.csv /home/felippe/Sprint1/vendas/backup/dados-${data_de_execucao}.csv

#  Renomeia o arquivo copiado para backup-dados-YYYYMMDD.csv
mv /home/felippe/Sprint1/vendas/backup/dados-${data_de_execucao}.csv /home/felippe/Sprint1/vendas/backup/backup-dados-${data_de_execucao}.csv

#  Obtendo o nome do arquivo de backup mais recente
arquivo_backup=$(ls /home/felippe/Sprint1/vendas/backup/backup-dados-*.csv | sort | tail -n 1)

#  Data do sistema em formato YYYY/MM/DD HH:MI
data_do_sistema=$(date +"%Y/%m/%d %H:%M")

#  Obter a data do primeiro registro de venda (primeira linha do arquivo)
# Aqui precisa pegar a segunda linha, pois a primeira é o cabeçalho
data_primeiro_venda=$(awk -F',' 'NR==2 {print $5}' "$arquivo_backup")

#  Obter a última data do registro de venda

data_ultimo_venda=$(awk -F ',' 'NF == 5 {data=$5} END {print data}' "$arquivo_backup")


# Quantidade total de itens diferentes vendidos

quantidade_itens=$(awk -F ',' 'NR > 1 {print $2}' "$arquivo_backup" | sort | uniq | wc -l)

# Criar um arquivo de relatório único com a data de execução
relatorio="/home/felippe/Sprint1/vendas/backup/relatorio-${data_de_execucao}.txt"

echo "Data do Sistema: $data_do_sistema" >> $relatorio
echo "Data do Primeiro Registro de Venda: $data_primeiro_venda" >> $relatorio
echo "Data do Último Registro de Venda: $data_ultimo_venda" >> $relatorio
echo "Quantidade total de itens diferentes vendidos: $quantidade_itens" >> $relatorio

echo "============================================" >> $relatorio

# 13. Exibir as 10 primeiras linhas do arquivo no relatório
echo "Primeiras 10 linhas do arquivo de vendas:" >> $relatorio
head -n 11 "$arquivo_backup" >> $relatorio

echo "============================================" >> $relatorio

#  Compactar o arquivo backup-dados-YYYYMMDD.csv para reduzir o espaço de armazenamento
zip /home/felippe/Sprint1/vendas/backup/backup-dados-${data_de_execucao}.zip "$arquivo_backup"

# Apagar os arquivos de dados de vendas e backup
rm /home/felippe/Sprint1/vendas/backup/backup-dados-${data_de_execucao}.csv
rm /home/felippe/Sprint1/vendas/dados_de_vendas.csv

echo "Processamento concluído com sucesso!"
