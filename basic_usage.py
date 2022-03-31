import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image


"""
## [Streamlit](https://docs.streamlit.io/)ではマークダウンを使用できます
### この記法の詳細は[こちら](https://docs.streamlit.io/library/api-reference/write-magic/magic)

#### 他にも[API reference](https://docs.streamlit.io/library/api-reference)に色んな機能が載っています
```python
print("hello world!")
"""

st.title("st.titleでも文字を表示できます")

# data frameを表形式で表示
df = pd.DataFrame({
    "名称": ["東京タワー", "スカイツリー", "エッフェル塔", "自由の女神"],
    "高さ[m]": [333, 634, 300, 93]
}).astype(str)
st.table(df)

# data frameを棒グラフで表示
df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=["a", "b", "c"]
)
st.bar_chart(df)

# map上へのプロット
df = pd.DataFrame(
    np.random.rand(50, 2) / [80, 80] + [36.95, 138.78],
    columns=["lat", "lon"]
)
st.map(df)

# 画像の表示
img = Image.open("landscape.jpg")
st.image(img, caption="スキー場", use_column_width=True)
