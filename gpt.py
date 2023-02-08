import openai
import os
import json
import sys 
import streamlit as st
import openai
import datetime

# chatgpt_demo
st.title("chatgpt_demo")

# Set your API key
openai.api_key = st.secrets["api_key"][0]
prompt = st.text_input("请输入内容", value="", max_chars=None, key=None, type="default")

f = open("./prompt.txt", "a+")
now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
f.write(now + " Question: \n" +  prompt + "\n")

if st.button("提交"):
    with st.spinner("等待生成中..."):
        completion = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=1024,
            temperature=0.5,
            top_p=1,
            frequency_penalty=0,
        )
    # 创建一个文本框，用于显示生成的文本
    try:
        result = completion.choices[0].text.strip()
    except:
        st.error("出错了，请重新提交问题")
        sys.exit(1)
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    f.write(now + " Answer: \n" + result)
    st.text_area("生成的文本", value=result,height=500, max_chars=None, key=None)
f.close()
