from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.prompts import PromptTemplate
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import CTransformers
from langchain.chains import RetrievalQA
from Pdf_Generator.pdf_generator import run
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

DB_FAISS_PATH = os.path.join(current_dir, 'vectorstore', 'science_faiss')

custom_prompt_template = """Use the following pieces of information to answer the user's question.
If you don't know the answer, just say that you don't know, don't try to make up an answer.

Context: {context}
Question: {question}

Only return the helpful answer below and nothing else.
Helpful answer:

Generate large content for the requested prompt in exactly 15 sentences, don't keep it simple and small.
I need fifteen exact sentences as a paragraph.
"""

def set_custom_prompt():

    prompt = PromptTemplate(template=custom_prompt_template,
                            input_variables=['context', 'question'])
    return prompt


def retrieval_qa_chain(llm, prompt, db, k):
    retriever = db.as_retriever(search_kwargs={'k': k})  # Adjust k parameter here
    qa_chain = RetrievalQA.from_chain_type(llm=llm,
                                           chain_type='stuff',
                                           retriever=retriever,
                                           return_source_documents=True,
                                           chain_type_kwargs={'prompt': prompt}
                                          )
    return qa_chain


def load_llm():
    
    llm = CTransformers(
        model="TheBloke/Llama-2-7B-Chat-GGML",
        model_type="llama",
        max_new_tokens=2048,
        temperature=0.1,
        config={'context_length': 8192}
    )
    return llm


def qa_bot(k=1):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2",
                                       model_kwargs={'device': 'cpu'})
    db = FAISS.load_local(DB_FAISS_PATH, embeddings, allow_dangerous_deserialization=True)
    llm = load_llm()
    qa_prompt = set_custom_prompt()
    qa = retrieval_qa_chain(llm, qa_prompt, db, k=k)
    return qa


def final_result(query):
    qa_result = qa_bot()
    response = qa_result.invoke({'query': query})
    return response

def send_answer(score, query):
    print("Loading...")
    try:
        score = 1
        query = query
        contents = []
        for i in query:
            
            querys = i

            if score == 5:
                k = 1  # Fetch more documents for score 5
            elif score == 4:
                k = 3   # Fetch fewer documents for score 4
            elif score == 3:
                k = 5   # Fetch even fewer documents for score 3
            elif score == 2:
                k = 7   # Fetch even fewer documents for score 2
            else:
                k = 9   # Fetch very few documents for score 1

            chain = qa_bot(k)
            
            res = chain.invoke({'query': querys})
            answer = res["result"]
            sources = res["source_documents"]
            print(answer)
            value = answer.split(".")
            print(value)
            answer = '. '.join(value[:score+1])
            contents.append(answer)
            '''if sources:
                source_content = " ".join([doc.page_content for doc in sources])
                #answer += f"\n\nAdditional Content:\n{source_content}"
            else:
                answer += "\nNo sources found"'''
        
        run(query, contents)
        # run(['What is magnitude'], ["Magnitude of force refers to the size or amount of a force. It can be measured in units such as Newtons (N) or pound-force (lb). The magnitude of a force does not affect its direction but does impact how strong it is. For example, a force with a larger magnitude will cause an object to move faster or farther than one with a smaller magnitude. The size of the magnitude depends on the size of the object being acted upon by the force. For instance, a bigger elephant will respond more strongly to a given force than a smaller mouse due to their differences in mass. A force's magnitude can be used to compare the strength of various forces, such as the strength needed for a person to lift an automobile or the amount of force required to move a large rock. The more significant the magnitude of a force, the more it will affect how something moves or changes shape."])
        # return f"Score: {score}\n{answer}"
    except Exception as e:
        print("Failed:", e)
