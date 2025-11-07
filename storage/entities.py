from faker import Faker
import random
from datetime import datetime

fake = Faker("pt_BR")


entities = {
    "fornecedores": {
        "id": lambda: random.randint(1, 9999),
        "codigo": lambda: f"F{random.randint(1000,9999)}",
        "nome": lambda: fake.company(),
        "cnpj": lambda: fake.cnpj(),
        "inscricao_estadual": lambda: str(random.randint(10000000, 99999999)),
        "telefone": lambda: fake.phone_number(),
        "email": lambda: fake.company_email(),
        "endereco": lambda: fake.street_address(),
        "cidade": lambda: fake.city(),
        "uf": lambda: fake.state_abbr(),
        "cep": lambda: fake.postcode(),
        "data_cadastro": lambda: fake.date_time_between(start_date="-2y", end_date="-1y").strftime("%Y-%m-%d %H:%M:%S"),
        "data_atualizacao": lambda: fake.date_time_between(start_date="-1y", end_date="now").strftime("%Y-%m-%d %H:%M:%S"),
        "status": lambda: random.choice(["ATIVO", "INATIVO", "BLOQUEADO"])
    },

    "produtos": {
        "id": lambda: random.randint(1, 99999),
        "sku": lambda: f"SKU-{random.randint(10000,99999)}",
        "codigo_barras": lambda: fake.ean13(),
        "descricao": lambda: fake.catch_phrase(),
        "categoria": lambda: random.choice(["Alimentos", "Limpeza", "Higiene", "Bebidas", "Eletrônicos"]),
        "subcategoria": lambda: random.choice(["Premium", "Econômico", "Tradicional"]),
        "marca": lambda: fake.company(),
        "unidade_medida": lambda: random.choice(["UN", "KG", "L", "CX"]),
        "peso_liquido": lambda: round(random.uniform(0.1, 10.0), 2),
        "peso_bruto": lambda: round(random.uniform(0.1, 12.0), 2),
        "preco_custo": lambda: round(random.uniform(5, 500), 2),
        "preco_venda": lambda: round(random.uniform(10, 800), 2),
        "id_fornecedor": lambda: random.randint(1, 9999),
        "estoque_minimo": lambda: random.randint(10, 50),
        "estoque_maximo": lambda: random.randint(100, 500),
        "data_cadastro": lambda: fake.date_time_between(start_date="-2y", end_date="-1y").strftime("%Y-%m-%d %H:%M:%S"),
        "data_atualizacao": lambda: fake.date_time_between(start_date="-1y", end_date="now").strftime("%Y-%m-%d %H:%M:%S"),
        "ativo": lambda: random.choice([True, False])
    },

    "estoque_atual": {
        "id": lambda: random.randint(1, 99999),
        "id_produto": lambda: random.randint(1, 99999),
        "local_estoque": lambda: random.choice(["CD São Paulo", "CD Rio de Janeiro", "Loja Campinas", "Loja Curitiba"]),
        "quantidade_disponivel": lambda: round(random.uniform(0, 1000), 2),
        "quantidade_reservada": lambda: round(random.uniform(0, 300), 2),
        "quantidade_em_pedido": lambda: round(random.uniform(0, 200), 2),
        "lote": lambda: f"L{random.randint(1000,9999)}",
        "data_atualizacao": lambda: fake.date_time_between(start_date="-1y", end_date="now").strftime("%Y-%m-%d %H:%M:%S")
    },

    "estoque_historico": {
        "id": lambda: random.randint(1, 99999),
        "id_produto": lambda: random.randint(1, 99999),
        "tipo_movimento": lambda: random.choice(["ENTRADA", "SAIDA", "AJUSTE"]),
        "quantidade": lambda: round(random.uniform(1, 500), 2),
        "origem_movimento": lambda: random.choice(["Fornecedor", "Transferência", "Ajuste manual"]),
        "destino_movimento": lambda: random.choice(["Loja", "Centro de Distribuição", "Cliente"]),
        "responsavel": lambda: fake.name(),
        "documento_referencia": lambda: f"DOC-{random.randint(1000,9999)}",
        "data_movimento": lambda: fake.date_time_between(start_date="-1y", end_date="now").strftime("%Y-%m-%d %H:%M:%S"),
        "observacao": lambda: fake.sentence(nb_words=6)
    },

    "vendas": {
        "id": lambda: random.randint(1, 999999),
        "numero_pedido": lambda: f"PED{random.randint(100000,999999)}",
        "data_venda": lambda: fake.date_time_between(start_date="-6M", end_date="now").strftime("%Y-%m-%d %H:%M:%S"),
        "id_cliente": lambda: random.randint(1, 99999),
        "nome_cliente": lambda: fake.name(),
        "cpf_cnpj": lambda: random.choice([fake.cpf(), fake.cnpj()]),
        "valor_total": lambda: round(random.uniform(50, 2000), 2),
        "desconto_total": lambda: round(random.uniform(0, 100), 2),
        "forma_pagamento": lambda: random.choice(["Crédito", "Débito", "Pix", "Dinheiro", "Boleto"]),
        "status_pedido": lambda: random.choice(["PAGO", "PENDENTE", "CANCELADO", "DEVOLVIDO"]),
        "canal_venda": lambda: random.choice(["Loja Física", "E-commerce"]),
        "vendedor": lambda: fake.name(),
        "id_produto": lambda: random.randint(1, 99999),
        "quantidade": lambda: round(random.uniform(1, 10), 2),
        "valor_unitario": lambda: round(random.uniform(10, 500), 2),
        "data_atualizacao": lambda: fake.date_time_between(start_date="-6M", end_date="now").strftime("%Y-%m-%d %H:%M:%S")
    }
}