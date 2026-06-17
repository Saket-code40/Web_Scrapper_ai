from bs4 import BeautifulSoup
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import os


def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")

    body_content = soup.body

    if body_content:
        return str(body_content)

    return ""


def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")

    for tag in soup(["script", "style"]):
        tag.extract()

    cleaned_content = soup.get_text(separator="\n")

    cleaned_content = "\n".join(
        line.strip()
        for line in cleaned_content.splitlines()
        if line.strip()
    )

    return cleaned_content


def split_dom_content(dom_content):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    return splitter.split_text(dom_content)


template = """
You are tasked with extracting specific information from the following text content:

{dom_content}

Please follow these instructions carefully:

1. Extract only the information that directly matches:
   {parse_description}

2. Do not include explanations, comments, or extra text.

3. If no information matches, return an empty string.

4. Output only the requested information.
"""

model = OllamaLLM(
    model="qwen2.5:3b",
    temperature=0
)


def parse_with_gemini(dom_chunks, parse_description):
    prompt = ChatPromptTemplate.from_template(template)

    chain = prompt | model

    parsed_results = []

    for i, chunk in enumerate(dom_chunks, start=1):

        response = chain.invoke(
            {
                "dom_content": chunk,
                "parse_description": parse_description
            }
        )

        print(f"Parsed batch {i}/{len(dom_chunks)}")

        parsed_results.append(response)

    return "\n".join(parsed_results)
