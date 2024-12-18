import numpy as np

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score, classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearns.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

import nltk
from nltk.corpus import stopwords
stopwords.words(’english’)
#download once 
nltk.download(’stopwords’)
nltk.download(’punkt’)
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import  PorterStemmer, WordNetLemmatizer
