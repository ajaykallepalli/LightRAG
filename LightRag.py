from lightrag import LightRAG, QueryParam
from lightrag.llm import gpt_4o_mini_complete, gpt_4o_complete
import os
from dotenv import load_dotenv

load_dotenv()

WORKING_DIR = "./Ilya_papers"

if not os.path.exists(WORKING_DIR):
    os.mkdir(WORKING_DIR)

rag = LightRAG(
    working_dir=WORKING_DIR,
    llm_model_func=gpt_4o_complete  # Use gpt_4o_mini_complete LLM model
    # llm_model_func=gpt_4o_complete  # Optionally, use a stronger model
)
import sys

if len(sys.argv) > 1:
    input_file = sys.argv[1]
    with open(input_file, 'r') as f:
        rag.insert(f.read())

# Perform naive search
print(rag.query("What are the fundamental themes throughout these papers that would be important to someone looking to build AGI?", param=QueryParam(mode="naive")))
# print(rag.query("What are the most underappreciated themes throughout these papers?", param=QueryParam(mode="naive")))
# print(rag.query("What predictions for the future of AGI can you glean from these papers?", param=QueryParam(mode="naive")))

# Perform local search
print(rag.query("What are the fundamental themes throughout these papers that would be important to someone looking to build AGI?", param=QueryParam(mode="local")))
# print(rag.query("What are the most underappreciated themes throughout these papers?", param=QueryParam(mode="local")))
# print(rag.query("What predictions for the future of AGI can you glean from these papers?", param=QueryParam(mode="local")))

# Perform global search
print(rag.query("What are the fundamental themes throughout these papers that would be important to someone looking to build AGI?", param=QueryParam(mode="global")))
# print(rag.query("What are the most underappreciated themes throughout these papers?", param=QueryParam(mode="global")))
# print(rag.query("What predictions for the future of AGI can you glean from these papers?", param=QueryParam(mode="global")))

# Perform hybrid search
print(rag.query("What are the fundamental themes throughout these papers that would be important to someone looking to build AGI?", param=QueryParam(mode="hybrid")))
# print(rag.query("What are the most underappreciated themes throughout these papers?", param=QueryParam(mode="hybrid")))
# print(rag.query("What predictions for the future of AGI can you glean from these papers?", param=QueryParam(mode="hybrid")))