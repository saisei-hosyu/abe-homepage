# app.py
import streamlit as st
import datetime

st.title("📝 みんなの掲示板")

# セッション内でメッセージ一覧を保持
if "messages" not in st.session_state:
    st.session_state.messages = []

# 入力フォーム
name = st.text_input("名前")
message = st.text_area("メッセージ")
if st.button("投稿する") and name and message:
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    st.session_state.messages.append((now, name, message))
    st.success("投稿しました！")

# 表示
st.subheader("📋 投稿一覧")
for time, user, msg in reversed(st.session_state.messages):
    st.markdown(f"**{user} ({time})**  \n{msg}")

