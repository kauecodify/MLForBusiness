import csv
import random
from datetime import datetime, timedelta

#gerar datas aleatórias dentro de um intervalo
def random_date(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)

#gerar dados fictícios
def generate_fake_data(num_rows):
    data = []
    start_date = datetime(2023, 1, 1)  # data inicial
    end_date = datetime(2024, 12, 31)  # data final

    for i in range(1, num_rows + 1):
        id_cliente = i
        cliente = f"empresa_{i}"
        risk_on = round(random.uniform(1_000_000, 50_000_000))  # valor entre 1.000.000 e 50.000.000
        data_ult_pag = random_date(start_date, end_date).strftime('%d/%m/%Y')  # data aleatória
        rating = f"{round(random.uniform(1.0, 10.0), 1)}%"  # rating entre 1.0% e 10.0%
        
        data.append([id_cliente, cliente, risk_on, data_ult_pag, rating])
    
    return data

# gera 100 linhas de dados fictícios
fake_data = generate_fake_data(100)

# salva os dados em um arquivo csv
with open("dados_clientes.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file, delimiter="\t")
    writer.writerow(["id_cliente", "cliente", "risk_on", "data_ult_pag", "rating"])  # cabeçalho
    writer.writerows(fake_data)  # escreve os dados

print("arquivo 'dados_clientes.csv' gerado com sucesso!")