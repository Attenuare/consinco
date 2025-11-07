from storage.mock_entities_class import MockConsincoAPI
from flask import Flask, jsonify, request, abort
from dotenv import load_dotenv
import pandas as pd
import duckdb
import os


load_dotenv()

app = Flask(__name__)

MOCK_OBJECT = MockConsincoAPI()

VALID_TOKEN = os.environ.get("VALID_TOKEN")
VALID_KEY = os.environ.get("VALID_KEY")


def check_auth():
    token = request.headers.get("Token")
    key = request.headers.get("Key")
    if token != VALID_TOKEN or key != VALID_KEY:
        abort(401, description="Unauthorized: Invalid or missing headers")

def query_to_json(query: str, entity: str):
    return_ = MOCK_OBJECT.get(query)
    keys = list(MOCK_OBJECT.entities[entity].keys())
    return [dict(zip(keys, values)) for values in return_.fetchall()]

def make_list_route(table_name):
    def list_table():
        check_auth()
        page = int(request.args.get("page", "1"))
        limit = int(request.args.get("limit", "500"))
        offset = (page - 1) * limit

        sql = f"SELECT * FROM {table_name} LIMIT {limit} OFFSET {offset}"
        records = query_to_json(sql, table_name)

        return jsonify({
            "page": page,
            "limit": limit,
            "count": len(records),
            "has_more": len(records) == limit,
            "data": records
        })

    app.add_url_rule(
        f"/api/v1/{table_name}",
        endpoint=f"{table_name}_list",
        view_func=list_table,
        methods=["GET"]
    )

for table in list(MOCK_OBJECT.entities.keys()):
    make_list_route(table)

@app.route("/")
def index():
    return jsonify({
        "status": "ok",
        "message": "Mock API Consinco running",
        "endpoints": [
            f"/api/v1/{table}" for table in MOCK_OBJECT.entities
        ]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
