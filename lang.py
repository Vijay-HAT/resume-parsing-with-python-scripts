import os
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI language model
llm = OpenAI(temperature=0.7)

# Define a simple prompt
prompt = "What are the main responsibilities of a data scientist?"

# Create a chain using the LLM
chain = LLMChain(llm=llm, prompt=prompt)

# Execute the chain
response = chain.run()

print("Response:", response)
