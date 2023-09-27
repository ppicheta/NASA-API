import streamlit as st
from content import Content

if __file__ == 'main.py':
    api_key = '3myxdcYF2OHHtImtsOdeoBigQiL51VOsLM9WJGCl'
    content = Content(api_key)
    details = content.get_content()

    title = details[0]
    text = details[1]

    st.set_page_config(layout='wide')
    st.title(title)
    st.image('images.jpg')
    st.write(text)







