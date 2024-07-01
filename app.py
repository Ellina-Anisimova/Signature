
import streamlit as st
from PIL import Image
from segment import process
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
st.title('Recognition of a dynamic handwritten signature')
# Добавление загрузчика файлов
columns=['x', 'y', 'z', 'az', 'in','us','num']
image_file = st.file_uploader('Load a signature')
#image_file='1.txt'
# Выполнение блока, если загружено изображение
if image_file is not None:
  with open(f'{image_file}', 'r') as f:
       datas = pd.read_csv(f, sep="	", names=columns)
  datas['us']=0
  datas['num']=0 #int(m[0])
  Text_test=datas.to_numpy()
  WIN_SIZE   = 1000
  text_test00=np.reshape(Text_test,(1,1000,7))
  x_testt=text_test00[:,:,0:5]
  x_test = np.asarray(x_testt).astype(np.float32)
  col1, = st.columns(1)
  x=[]
  y=[]
  for z in range (0,1000):
     x+=[x_test[0][z][0]]
     y+=[x_test[0][z][1]]
  d = {"x": x, "y": y}
  # метки строк создаются автоматически
  chart_data = pd.DataFrame(d)
  st.line_chart(chart_data, x="x", y="y", color="#FF0000")
  results = process(image_file)
  col1.text(f'Person id {results[0]}')
  #col1.image(results[1])
