# agent.py
from langchain.agents import Tool, initialize_agent
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA

def build_agent_from_vectorstore(vectordb):
    retriever = vectordb.as_retriever()
    llm = OpenAI(temperature=0)

    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

    summarizer_tool = Tool(
        name="DocSummarizer",
        func=lambda q: qa_chain.run(q),
        description="Summarize or answer questions about the uploaded PDF"
    )

    agent = initialize_agent(
        tools=[summarizer_tool],
        llm=llm,
        agent="zero-shot-react-description",
        verbose=True
    )
    return agent
