
import numpy as np
from tensorflow.keras.models import load_model
import pandas as pd
from PIL import Image
import re
import gdown
import os
import matplotlib.pyplot as plt
MODEL_NAME = 'model.h5';
model = load_model(MODEL_NAME)

def process(img_path):
     classes = {0: '0000', 1: '0001', 2: '0002', 3: '0003', 4: '0004', 5: '0005', 6: '0006', 7: '0007', 8: '0008', 9: '0009', 10: '0010', 11: '0011', 12: '0012', 13: '0013', 14: '0014', 15: '0015', 16: '0016', 17: '0017', 18: '0018', 19: '0019', 20: '0020', 21: '0021', 22: '0022', 23: '0023', 24: '0024', 25: '0025', 26: '0026',27: '0027', 28: '0028', 29: '0029', 30: '0030',  31: '0031', 32: '0032', 33: '0033', 34: '0034', 35: '0035', 36: '0036', 37: '0037', 38: '0038', 39: '0039', 40: '0040', 41: '0041', 42: '0042', 43: '0043', 44: '0044', 45: '0045', 46: '0046',47: '0047', 48: '0048', 49: '0049', 50: '0050', 51: '0051', 52: '0052', 53: '0053', 54: '0054', 55: '0055', 56: '0056', 57: '0057', 58: '0058', 59: '0059', 60: '0060', 61: '0061', 62: '0062', 63: '0063', 64: '0064', 65: '0065', 66: '0066',67: '0067', 68: '0068', 69: '0069', 70: '0070', 71: '0071', 72: '0072', 73: '0073', 74: '0074', 75: '0075', 76: '0076', 77: '0077', 78: '0078', 79: '0079', 80: '0080', 81: '0081', 82: '0082', 83: '0083', 84: '0084', 85: '0085', 86: '0086',87: '0087', 88: '0088', 89: '0089', 90: '0090', 91: '0091', 92: '0092', 93: '0093', 94: '0094', 95: '0095', 96: '0096', 97: '0097', 98: '0098', 99: '0099', }
     columns=['x', 'y', 'z', 'az', 'in']#,'us','num']
     fl=img_path
     #m=re.match('\d+(?=.txt(?!.txt))', fl)
     with open(f'{fl}', 'r') as f:
       datas = pd.read_csv(f, sep="	", names=columns)
    ## datas['us']=0
     ##datas['num']=0 #int(m[0])
     text_test=datas.to_numpy()
     WIN_SIZE   = 1000
     merged_list = []
     for l in text_test:
        merged_list.extend(l)
     text_test0=np.array(merged_list)
     text_test00=np.reshape(text_test0,(1,1000,5))
     x_testt=text_test00[:,:,0:5]
     x_test = np.asarray(x_testt).astype(np.float32)
     cls_image = np.argmax(model.predict(x_test))
     return classes[cls_image], x_test;
