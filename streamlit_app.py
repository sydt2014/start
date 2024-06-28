import streamlit as st
import pandas as pd

st.title("我的第一个 Streamlit 应用")
st.write('Hello, world!')
st.markdown('**This** is some Markdown *text*.')
tab1, tab2, tab3 = st.tabs(["猫", "狗", "猫头鹰"])

with tab1:
    st.header("一只猫")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
    st.header("一只狗")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
    st.header("一只猫头鹰")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

@st.cache_data
def load_file(file):
    print("load file")
    return pd.read_excel(file, None)
upload_file = st.file_uploader('excel文件', type=['xlsx'])
if upload_file is None:
    st.stop()
dfs = load_file(upload_file)
# st.dataframe(dfs)
names = list(dfs.keys())
sheet_selects = st.multiselect('工作表', names, [])
if len(sheet_selects) == 0:
    st.stop()

tabs = st.tabs(sheet_selects)
for tab, name in zip(tabs, sheet_selects):
    with tab:
        df = dfs[name]
        st.dataframe(df)

# 添加文本
st.text("欢迎使用 Streamlit！")

# 添加一个输入框
name = st.text_input("请输入您的姓名", "匿名")

# 添加一个按钮
button = st.button("提交")

# 在按钮被点击时执行的操作
if button:
    st.text("你好，" + name + "！欢迎使用 Streamlit！")
