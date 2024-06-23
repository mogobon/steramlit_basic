import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

# 実行方法
# % streamlit run main.py


st.title('Streamlit 入門')

st.write('DataFrame')

df = pd.DataFrame({
    '1列目': [1,2,3,4],
    '2列目': [10, 20, 30, 40]
})

st.write(df) # 表のオプションなどの引数が指定できない。
# dataframeではそれができる

st.dataframe(df.style.highlight_max(axis=0))
# 列を指定する時はaxis=0

# 動的な表はdataframe, 静的な表はtableと覚える
st.table(df.style.highlight_max(axis=0))

# magic command
# Markdown記法を適用できる。

"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```

"""

# randで正規乱数
df2 = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a', 'b', 'c'])

st.dataframe(df2)
st.line_chart(df2)
st.area_chart(df2)
st.bar_chart(df2)

# mapのプロット

df3 = pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [35.69, 139.70], # 1度でもズレると大変だから50で割る
    columns=['lat', 'lon'] # 緯度けいど
)
df3

st.map(df3)

st.write('Display Image')

img = Image.open("/Users/hayashiyuki/Streamlit_basic/dl_basic.png")
st.image(img, caption='ゼロから学ぶDeepLearning表紙', use_column_width=True)

# Web のカラムに合わせてくれる. use_column_width
# --- --- --- #

# インタラクティブな実装
# checkbox, slidebox など値を動的に変化させていく

# st.checkboxは条件式. 状態に応じて, 真偽が決定するbool型を持つ
if st.checkbox('Show Image'): 
    img = Image.open('/Users/hayashiyuki/Streamlit_basic/dl_basic.png')
    st.image(img, caption='ゼロから学ぶDeepLearning', use_column_width=True)


# selectbox

option = st.selectbox(
    'あなたが好きな数字を教えてください、',
    list(range(1,11)) # 半開区間のリスト
)

'あなたの好きな数字は、 ',option, 'です。'



""" 
text = st.text_input('あなたの趣味を教えてください')
'あなたの趣味: ', text

最小値, 最大値, スタート位置
condition = st.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション: ', condition 
"""


# intractive widigtsを検索

# 調整

"""
## 調整
"""

st.sidebar.write('インタラクティブなウィジット')
text2 = st.sidebar.text_input('あなたの趣味を教えてください')
condition2 = st.sidebar.slider('あなたの今の調子は？')

'あなたの趣味: ', text2
'コンディション: ', condition2

"""
## 2 col
"""

left_column, right_column = st.columns(2)
button = left_column.button('ボタンを押してね')
if button:
    right_column.write('バァ')

st.write('st.beta_columns は死んでいる')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く1')
expander.write('問い合わせ内容を書く2')

"""
## プログレスバーの表示
"""

'start!'

latest_iteration =  st.empty() # 進捗度のテキスト
bar = st.progress(0)

# range(100) = [0,1,...,99]
for i in range(100):
    latest_iteration.text(f'Iteration{i+1}') # 進捗度のテキスト
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!'

# 1. git initで初期化
# 2. git remote add origin {URL}で紐付け
