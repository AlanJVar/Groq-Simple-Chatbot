from langchain_groq import ChatGroq

llm = ChatGroq(
    temperature=0,
    groq_api_key="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",
    model = "meta-llama/llama-4-scout-17b-16e-instruct"
)

query = input("How can I help you today? \n")
response = llm.invoke(query)
print(response.content)
query = input("Do you need help with anything else? (type 'No' to exit) \n")
while (query!='No'):
    response = llm.invoke(query)
    print(response.content)
    query = input("Do you need help with anything else? (type 'No' to exit) \n")

