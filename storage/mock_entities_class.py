from storage.duck_db_class import DuckDB
from storage.entities import entities
from tqdm import tqdm
import json
import os


class MockConsincoAPI(object):
    def __init__(self):
        self.duck_db = DuckDB()
        self.my_path = os.getcwd() 
        self.entities = entities
        self.mocking_count = {
            "fornecedores": 200,
            "produtos": 2000,
            "estoque_atual": 3000,
            "estoque_historico": 5000,
            "vendas": 4500
        }

    def init_db(self) -> None:
        self.duck_db.set_new_connection("consinco")
        self.duck_db.create_tables(self.entities)

    def mock_entities(self, entities: dict = None) -> None:
        self.duck_db.set_new_connection("consinco")
        mock_entities = entities if entities else self.mocking_count
        for entity in mock_entities:
            if entity in self.entities:
                print(f"[LOG] - Mocking {entity}")
                data_count = mock_entities.get(entity) if type(mock_entities.get(entity))\
                is int else 10
                data = [
                    {field: str(func()) for field, func in self.entities.get(entity).items()}
                    for _ in tqdm(range(data_count), desc=entity)
                ]
                keys = self.entities.get(entity).keys()
                values = list()
                for row in data:
                    row = {element[0]: f"'{element[1]}'" for element in row.items()}
                    temp_values = f"({', '.join([str(row[key]) for key in keys])})"
                    values.append(temp_values)
                self.query = f"""INSERT INTO {entity} ({', '.join(list(keys))}) VALUES {", ".join(values)};"""
                #print(self.query)
                self.duck_db.db_sql(self.query)

    def get(self, query: str) -> dict:
        self.duck_db.set_new_connection("consinco")
        self.duck_db.db_sql(query)
        return self.duck_db.results
