import streamlit as st
from scrape import (scrape_website,extract_body_content,clean_body_content,split_dom_content)
from parse import parse_with_ollama

st.title("AI web scraper")
url=st.text_input("enter a website url")

if st.button("scrape site"):
    st.write("scraping the site")
    data=scrape_website(url)
    body_content=extract_body_content(data)
    cleaned_content=clean_body_content(body_content)

    st.session_state.dom_content=cleaned_content

    with st.expander("view DOM content"):
        st.text_area("DOM content",cleaned_content,height=300)
    
if "dom_content" in st.session_state:
    parse_description=st.text_area("describe what you want to parse")

    if st.button("parse content"):
        if parse_description:
            st.write("parsing the content")

            dom_chunks=split_dom_content(st.session_state.dom_content)
            result=parse_with_ollama(dom_chunks,parse_description)
            st.write(result)