import os
from secret import OAI_KEY, SERP_API

os.environ["OPENAI_API_KEY"] = OAI_KEY
os.environ["SERPAPI_API_KEY"] = SERP_API
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

lang_model = OpenAI(temperature=0.9)

text = "What would be a good company name for a company that makes colorful socks?"
# print(llm("What's a good name for a guitar company that makes pink guitars"))


prompt_llm = PromptTemplate(
    input_variables=["input"],
    template="answer the human in a business style of writing {input}?",
)


chain = LLMChain(llm=lang_model, prompt=prompt_llm, verbose=True)

# print(chain.run(input="what is todays date"))


print(chain.run("what is the largest dog breed?"))
