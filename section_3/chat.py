import os
from secret import OAI_KEY, SERP_API

os.environ["OPENAI_API_KEY"] = OAI_KEY
os.environ["SERPAPI_API_KEY"] = SERP_API
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.utilities import SerpAPIWrapper
from langchain.agents import Tool, AgentType, initialize_agent
from langchain.memory import ConversationBufferMemory




lang_model = OpenAI(temperature=0.9)

chat_memory = ConversationBufferMemory(memory_key='chat_history')

search = SerpAPIWrapper()

tools = [
    Tool(
    name="Search",
    func=search.run,
    description="useful for searching the internet and getting information about dates"
    ),
]

agent_chain = initialize_agent(tools=tools, 
                               llm=lang_model, 
                               agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION, 
                               verbose=True,
                               memory=chat_memory)

print(agent_chain.run(input="what is the largest dog breed?"))
