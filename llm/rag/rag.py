import os
import json
import chromadb
from chromadb.config import Settings


chroma_client = chromadb.PersistentClient(path=os.path.join(os.getcwd(), "chroma_db"))
chroma_client.create_collection(name='tables', get_or_create=True)

tables_collection = chroma_client.get_collection(name='tables')
# tables_collection.add(documents=['user_info table contains users'], ids=['1'])


