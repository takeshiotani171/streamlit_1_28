import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('1')
st.title('Streamlit 超入門')
st.write('DataFrame')
#########################################
st.title('2')
df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
})

st.write(df)
st.dataframe(df.style.highlight_max(axis=0))
st.table(df.style.highlight_max(axis=0))
#########################################
st.title('3')
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
#########################################
st.title('4')
df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a','b','c']
)
st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)
#########################################
st.title('5')
df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat','lon']
)
st.map(df)
#########################################
st.title('6')
st.title('Streamlit 超入門')
st.write('Display Image')

img = Image.open('soccer.jpeg')
st.image(img, caption='Messi', use_column_width=True)
######################　　動的　#########################
st.title('7')
st.title('Streamlit 超入門')
st.write('Display Image')

if st.checkbox('Show Image'):
    img = Image.open('soccer.jpeg')
    st.image(img, caption='Messi', use_column_width=True)
#########################################
st.title('8')
st.title('Streamlit 超入門')
st.write('Display Image')

option = st.selectbox(
    'あなたが好きな数字を教えてください',
    list(range(1, 11))
)
'あなたの好きな数字は', option, 'です。'
#########################################
st.title('9')
st.title('Streamlit 超入門')
st.write('Interactive Widgets')

text = st.text_input('あなたの趣味を教えてください')
'あなたの趣味: ', text
#########################################
st.title('10')

condition = st.slider('あなたの今の調子は?', 0, 100, 50)
'コンディション: ', condition
#########################################
st.title('11')

st.sidebar.write('Interactive Widgets')
text_2 = st.sidebar.text_input('あなたの趣味を教えてください__')
condition_2 = st.sidebar.slider('あなたの今の調子は?__', 0, 100, 50)
'あなたの趣味__: ', text_2
'コンディション__: ', condition_2

#########################################
st.title('12')

st.write('Interactive Widgets')

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')
#########################################
st.title('13')

st.write('プログレスバーの表示')
'Start!'
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!!'