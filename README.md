# MedIQ

# End-to-end-Medical-Chatbot-using-Llama2

# How to run?
### STEPS:

### STEP 01- Create the CONDA environment

Creating Environment:
```bash
conda create -n mchatbot python=3.11 -y
```

Activating Environment:
```bash
conda activate mchatbot
```

### STEP 02- install the requirements

Installing all frameworks and libraries listed in `requirements.txt`:
```bash
pip install -r requirements.txt
```


### Create a `.env` file in the root directory and add your Pinecone credentials as follows:

API Keys are not meant to be shared with others. As such, it is essential for it to not appear in code that will be publicly viewable on version control softwares.
`.env` is already put inside the .gitignore file, so it is not tracked by `Git`.
```ini
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```


### Download the Llama 2 LLM from the link below:

```ini
## Download the following model:

llama-2-7b-chat.ggmlv3.q4_0.bin


## From the following link:
https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main
```

The following command ensures vector embeddings are created and stored in Pincone (the Vector DB) for future retrieval.
```bash
# run the following command
python store_index.py
```

The following command will run the application, and you will be able to interact with _MedIQ_ in the chatting UI.
```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up localhost:
```


### Tech Stack Used:

- Python
- LangChain
- Flask
- Meta Llama2 LLM
- Pinecone Vector DB
- Hugging Face

