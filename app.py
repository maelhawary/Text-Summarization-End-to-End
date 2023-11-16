import streamlit as st
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.chains.summarize import load_summarize_chain
from transformers import T5Tokenizer, T5ForConditionalGeneration
from transformers import pipeline
import torch
import pdfplumber
import tempfile

### model and tokenizer

checkpoint = "MBZUAI/LaMini-Flan-T5-248M"
tokenizer=T5Tokenizer.from_pretrained(checkpoint)
base_model=T5ForConditionalGeneration.from_pretrained(checkpoint,device_map='auto', torch_dtype=torch.float32)

# file loader and preprocessing
def file_preprocessing(file):
    loader=PyPDFLoader(file)
    pages=loader.load_and_split()
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=200,chunk_overlap=50)
    texts=text_splitter.split_documents(pages)
    final_texts=""
    for text in texts:
        print(text)
        final_texts=final_texts + text.page_content
    return final_texts

#print('done')
#textt=file_preprocessing('cross-validation_open_pg.pdf')
#print(textt)

## LLm_ pipeline
def llm_pipeline(filepath):
    pipe_sum=pipeline('summarization',                      
        model=base_model,
        tokenizer= tokenizer,
        max_length=500,
        min_length=50 
    ) 
    input_text=file_preprocessing(filepath)
    result=pipe_sum(input_text)
    result=result[0]['summary_text']
    return result

## streamlit code
def read_pdf(file):
    with pdfplumber.open(file) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text


## streamlit code
st.set_page_config(layout='wide',page_title='Summarization APP')
def main():
    st.title('Document Summarization APP using LLMs')

    uploaded_file=st.file_uploader("Upload your PDF File Here",type=['pdf'])
    if uploaded_file is not None:
        if st.button("summarize"):
            col1,col2=st.columns(2)
            filepath =uploaded_file.name
           # with open (filepath, 'wb') as temp_file:
            #    temp_file.write(uploaded_file.read())
            with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
                tmp_file.write(uploaded_file.read())
                filepath = tmp_file.name
            with col1:
                st.info("Uploaded File")
                st.write("PDF content:")
                text = read_pdf(filepath)
                st.text(text)
            with col2:
                st.info("Summarization is below")
                summary=llm_pipeline(filepath)
                st.success(summary)

        st.success("File successfully uploaded.")


if __name__ == '__main__':
    main()


