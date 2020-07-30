# On importe les librairies dont on aura besoin pour ce tp
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

house_data = pd.read_csv('house.csv')

data_size = len(house_data)

sample = np.random.randint(data_size, size=int(data_size*0.1) )
#sampled_data = house_data[sample]

xtrain, xtest, ytrain, ytest = train_test_split(house_data['loyer'], house_data['surface'], train_size=0.8)