from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os 
load_dotenv()
key = os.getenv("GROQ_API_KEY")
# Simple one-line prompt
prompt = PromptTemplate.from_template("{question}")

model = ChatGroq(model="llama-3.3-70b-versatile", api_key=key)
parser = StrOutputParser()

# Chain: prompt → model → parser
chain = prompt | model | parser

# Run it
result = chain.invoke({"question": "What is the capital of Peru?"})
print(result)
