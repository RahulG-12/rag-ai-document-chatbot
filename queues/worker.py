from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore

from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
client=OpenAI()

embedding_model=OpenAIEmbeddings(
    model="text-embedding-3-large",
)
vector_embedding=QdrantVectorStore.from_existing_collection(
    collection_name="demo_collection",
    embedding=embedding_model,
    url="http://localhost:6333",

)



def proceesquery(query:str):
 
    serach_results=vector_embedding.similarity_search(query=query)
    context="\n\n\n".join([f"page Content:{result.page_content}\n page Number:{result.metadata['page_label']}\n file Location:{result.metadata['source']}"for result in serach_results])
    SYSTEM_PROMPT=f"""  
    you are a helpful ai assiatant who answers user query based on available 
    context retrived from a pdf file along with page_content and page number
    you should only ans the user based on following context and navigate
    to open the right page number to know more

    context:
    {context}

    """

    response=client.chat.completions.create(
        model="gpt-4o",
        messages=[
        {"role":"system","content":SYSTEM_PROMPT},
        {"role":"user","content":query}
        ]
    )
    print(response.choices[0].message.content)
    return response.choices[0].message.content
    