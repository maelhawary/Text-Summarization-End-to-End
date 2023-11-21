# Text-Summarization-End-to-End

This is an LLM project for text summarization of any PDF context. The LLM model is based on LaMini‑Flan‑T5‑248M (https://huggingface.co/MBZUAI/LaMini-Flan-T5-248M). The end-to-end implementation includes the following packages: Langchain and Huggingface for data preprocessing and model integeration, Docker for containarization, AWS EC2 for deployment, Github action for CI/CD, and Streamlit for webapp interface. 

# To use
1. Lunch and connect your AWS EC2 instance, add the following context to the secrects actions: AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION
2. Add the self-hosted runner commands from Github to your EC2 instance.
3. Install docker on your EC2 instance as follows:
4. 
```bash
    sudo apt-get update -y
    sudo apt-get upgrade
```
```bash
    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh
    sudo usermod -aG docker ubuntu
    newgrp docker
```

4. Run the github actions and then access the web-app using the Public IPv4 address of your EC2 instance followed by the port number (e.g. 55.55.555.55:8000)

