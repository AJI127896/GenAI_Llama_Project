# GenAI_Llama_Project
# LLaMA Chatbot using GROQ

## Overview
This project implements a chatbot using Meta's LLaMA model powered by GROQ's inference engine. The chatbot can answer queries, generate text, and assist in conversations with a natural language processing (NLP) pipeline.

## Features
- Utilizes LLaMA for generating responses
- Powered by GROQ for efficient inference
- Supports interactive chat interface
- Deployable as a web app or API

## Requirements
Make sure you have the following installed:
- Python 3.8+
- GROQ API access
- Required Python libraries (listed in `requirements.txt`)

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/AJI127896/GenAI_Llama_Project.git
   cd GenAI_Llama_Project
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Configuration
1. Set up your GROQ API key:
   ```sh
   export GROQ_API_KEY="your_api_key_here"
   ```
   Or create a `.env` file and add:
   ```env
   GROQ_API_KEY=your_api_key_here
   ```

## Usage
deploy as a web service:
```sh
streamlit run app.py
```

## File Structure
```
GenAI_Llama_Project/
│── app.py              # Web interface using Streamlit
│── requirements.txt    # List of dependencies
│── .env                # API key storage
│── README.md           # Project documentation
```

## Contributing
Feel free to submit issues, feature requests, or pull requests. Contributions are welcome!

## Contact
For any queries, reach out to `ameyj1278@gmail.com` or open an issue on GitHub.

