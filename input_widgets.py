import streamlit as st

st.title("ウィジェットを使ってみる")

# ボタン
# (True/Falseで値が入ってくるのでif文で)
if st.button('ためになった'):
    st.write('LGTMを押そう！')
else:
    st.write('ストックしておこう…')

# チェックボックス
if st.checkbox('こんにちは'):
    st.write('こんにちは！')

# Radio
genre = st.radio(
    "好きな映画のジャンルは何ですか？",
    ('コメディ', 'ドラマ', 'ドキュメンタリー'))

if genre == 'コメディ':
    st.write('あなたはコメディを選びました')
else:
    st.write("あなたはコメディを選びませんでした")

# セレクトボックス
option = st.selectbox(
    '好きなSNSは？',
    ('Twitter', 'Instagram', 'LINE', 'Qiita'))
st.write('あなたの選択:', option)

# スライダー
values = st.slider(
    '数字の範囲を選んでください',
    0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

# テキスト入力
title = st.text_input('好きな映画を教えてください')
st.write('あなたが好きな映画は', title, "ですね！")
