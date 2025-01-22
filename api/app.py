from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv


load_dotenv()

os.environ['GROQ_API_KEY']=os.getenv('GROQ_API_KEY')

app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API server"
)

add_routes(
    app,
    ChatGroq(),
    path="/groq"
)

model = ChatGroq(model="llama-3.3-70b-versatile", api_key=os.getenv("GROQ_API_KEY"))

llm = ChatGroq(model="gemma2-9b-it",api_key=os.getenv("GROQ_API_KEY"))

prompt1=ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")

prompt2 = ChatPromptTemplate.from_template("write me a poem about {topic} with 100 words")

add_routes(
    app,
    prompt1|model,
    path="/essay_llama"
)

add_routes(
    app,
    prompt2|llm,
    path="/poem_gemma"
)


if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)