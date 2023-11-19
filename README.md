# Text-Summarization-End-to-End

This LLm project provides text summarization for any PDF context.

# To use
1. Lunch and connect your AWS EC2 instance, add the following context to the secrects actions: AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION
2. Add the self-hosted runner for EC2 instance.
3. Install docker on your EC2 instance as follows:
    #optinal
    sudo apt-get update -y
    sudo apt-get upgrade

    #required
    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh
    sudo usermod -aG docker ubuntu
    newgrp docker

4. Run the github actions and then access the web app using the Public IPv4 address for your EC2 instance followed by the port 8501 (e.g. 55.55.555.55:8501)

