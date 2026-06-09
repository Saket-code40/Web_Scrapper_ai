import streamlit as st
from scrape import scrape_website

st.title("Web Scraper AI")
url = st.text_input("Enter the URL of the website you want to scrape:")

if st.button("Scrape"):
    st.write("scraping the website...")
    result = scrape_website(url)
    print(result)

    