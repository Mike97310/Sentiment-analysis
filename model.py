from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from textblob import Blobber
from textblob_fr import PatternTagger, PatternAnalyzer

tb = Blobber(pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
from os import path
from tqdm import tqdm, trange
import time
import torch
import datetime
from sklearn import metrics
from sklearn.model_selection import train_test_split
from keras.preprocessing.sequence import pad_sequences
from torch.utils.data import TensorDataset, random_split, \
    DataLoader, RandomSampler, SequentialSampler
from transformers import CamembertForSequenceClassification, CamembertTokenizer, \
    AdamW, get_linear_schedule_with_warmup


def model():
    model = torch.load('sentiments.pt')
    return model
