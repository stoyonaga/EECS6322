from torchvision import datasets
from torchvision.transforms import ToTensor
from torch.utils.data import DataLoader
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torch
import plotly.express as px
import numpy as np
import pandas as pd
import os, shutil



device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f'Data and model will be loaded on the {device}')

annotations = pd.read_csv(
    f'C:\\Users\\Momotaro\\Desktop\\Test\\colon_annotations.csv',
    header = None,
    index_col = None
    )


for index, label in annotations.iterrows():
    img = label[0].split(".")[0]
    old_pos = f"C:\\Users\\Momotaro\\Desktop\\Test\\Classification\\{img}\\{img}.bmp"
    new_pos = f"C:\\Users\\Momotaro\\Desktop\\Test\\Negative" if label[1] == 0 else "C:\\Users\\Momotaro\\Desktop\\Test\\Positive"
    shutil.move(old_pos, new_pos)






