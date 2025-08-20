from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os 

# so ideally each project in langsmith will have diff names so to change them from here : 
os.environ["LANGCHAIN_PROJECT"] = "sequential app" # this will over write the .env one 
#(setting different project name )

load_dotenv()
key = os.getenv("GROQ_API_KEY")

model1 = ChatGroq(model="llama-3.3-70b-versatile", api_key=key, temperature=0.7)
model2 = ChatGroq(model="llama-3.3-70b-versatile", api_key=key, temperature=0.4)


prompt1 = PromptTemplate(
    template='Generate a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a 5 pointer summary from the following text \n {text}',
    input_variables=['text']
)

parser = StrOutputParser()

chain = prompt1 | model1 | parser | prompt2 | model2 | parser

# we can also add/set tags and metadata here for our trace 
config = {
    "run_name": "sequiential chain", # to give your own name to the trace or run
    'tags':{'llm app', "report generation", "summarization"},
    'meta_data':{'model':"llama-3.3-70b-versatile", 'parser':"StrOutputParser"}
}

result = chain.invoke({'topic': 'Unemployment in India'}, config=config)

print(result)
