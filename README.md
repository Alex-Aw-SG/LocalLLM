## Background:

With availability of LLM models in [quantized](https://www.tensorops.ai/post/what-are-quantized-llms "What are Quantized LLMs?") versions, it is now possible to run LLM on your personal machine or laptop CPU. Having a local LLM cut away expensive API service charges by the likes of OpenAI. However, smaller or quantized LLM performances are not as comprehensive as ChatGPT. Hence it is vital to evaluate whether the local LLM performance meets the user requirement. 

In addition of unlimited usage of local LLM, using proprietary data can increase the domain knowledge of the model. After in-house data are stored in the vector database, it can be referenced by the LLM to answer queries specific to user’s domain. Hosting the vector database on premise will enhance the security of data if they are of high sensitivity, ensuring that no company secrets are transmitted out. For the purpose of this app, the data are stored in PineCone which is a cloud vector database (Free Tier available).



## Instructions:   

•	Request access to [Llama 2](https://ai.meta.com/llama) from Meta.   
•	Request access to quantized Llama 2 from [Hugging Face]( https://huggingface.co/meta-llama). (Use same email as Meta request)    
•	Download Llama 2 [7B](https://huggingface.co/TheBloke/nsql-llama-2-7B-GGUF) or [13B](https://huggingface.co/TheBloke/Llama-2-13B-GGUF) quantized version.   
•	Sign up for free account with [PineCone](https://www.pinecone.io). Note: When setting up index, dimension input is 384.   


## Minor file changes required:   

.env file: Enter your PineCone API keys, Environment and Index Name   

query_function.py: Change the path in line 37 to where your llama 2 model is saved

Finally in terminal, run the command > streamlit run app.py 

## *Hope you enjoy the app and get to learn more about LLM.* 



