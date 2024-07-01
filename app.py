
import streamlit as st
from PIL import Image
from segment import process
import numpy as np
import pandas as pd
st.title('Нейросетевой модуль биометрической аутентификации личности по динамике рукописной подписи')
# Добавление загрузчика файлов
columns=['x', 'y', 'z', 'az', 'in']
image_file = st.file_uploader('Загрузите файл подписи', type={"csv", "txt"})
#image_file='1.txt'
# Выполнение блока, если загружено изображение
if image_file is not None:
  datas = pd.read_csv(image_file, sep="	", names=columns)
  Text_test=datas.to_numpy()
  WIN_SIZE   = 1000
  text_test00=np.reshape(Text_test,(1,1000,5))
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
  st.scatter_chart(chart_data, x="x", y="y", color="#0000FF",size=6)
  results = process(x_test)
  col1.text(f'Идентификатор пользователя id {results[0]}')
  #col1.image(results[1])
