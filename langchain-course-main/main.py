import os
from socketserver import ThreadingMixIn

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
#from langchain.ollama import ChatOllama
load_dotenv()

def main():
    print("Hello, LangChain!")
    information ="""
Born to a wealthy family in Pretoria, South Africa, Musk emigrated in 1989 to Canada; he had obtained Canadian citizenship at birth through his Canadian-born mother. He received bachelor's degrees in 1997 from the University of Pennsylvania in Philadelphia, United States, before moving to California to pursue business ventures. In 1995, Musk co-founded the software company Zip2. Following its sale in 1999, he co-founded X.com, an online payment company that later merged to form PayPal, which was acquired by eBay in 2002. That year, Musk also became an American citizen.

In 2002, Musk founded the space technology company SpaceX, becoming its CEO and chief engineer; the company has since led innovations in reusable rockets and commercial spaceflight. Musk joined the automaker Tesla as an early investor in 2004 and became its CEO and product architect in 2008; it has since become a leader in electric vehicles. In 2015, he co-founded OpenAI to advance artificial intelligence (AI)

    """

    summary_template = """
    given the information {information} about a person I want you to create:
    1. A short summary
    2. Two Interesting fact about them
    """
    summary_prompt_template= PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model="gpt-5")
   #llm = ChatOllama(temperature=0, model="gemma3:270m")
    chain = summary_prompt_template | llm
    response = chain.invoke(input={"information": information})

    print(response.content)


if __name__ == "__main__":
    main()
