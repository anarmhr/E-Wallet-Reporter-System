import os
import json
import chromadb

chroma_client = chromadb.PersistentClient(path='llm/model/chroma_db')
chroma_client.create_collection(name='tables', get_or_create=True)

tables_collection = chroma_client.get_collection(name='tables')


def add_table_knowledge():
    with open('knowledge base/table-knowledge-base.json', 'r') as f:
        tables = json.load(f)

    ids = [table['table_name'] for table in tables]
    docs = [str(table) for table in tables]

    tables_collection.delete(ids=ids)
    tables_collection.add(documents=docs, ids=ids)


def query_chroma(query_text):
    result = tables_collection.query(query_texts=[query_text], n_results=2)
    return str(result['documents'])

