import re
import pandas as pd
from textblob import Blobber
from textblob_fr import PatternTagger, PatternAnalyzer

tb = Blobber(pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
import torch
import numpy as np
from sklearn import metrics
from sklearn.model_selection import train_test_split
from keras.preprocessing.sequence import pad_sequences
from torch.utils.data import TensorDataset, random_split, \
    DataLoader, RandomSampler, SequentialSampler
from transformers import CamembertForSequenceClassification, CamembertTokenizer, \
    AdamW, get_linear_schedule_with_warmup

import model
from scrap import *


def prediction(comments):
    global data
    AComment = []
    for comment in comments:
        mots = []
        for word in re.sub("\W", " ", comment).split():
            mots.append(word)
        AComment.append(mots)

    # Defining constants
    MAX_LEN = 128
    device = torch.device('cpu')

    # Initialize CamemBERT tokenizer
    tokenizer = CamembertTokenizer.from_pretrained('camembert-base', do_lower_case=True)

    # Encode the comments
    tokenized_comments_ids = [tokenizer.encode(AComment, add_special_tokens=True, max_length=MAX_LEN) for comment in
                              comments]
    # Pad the resulted encoded comments
    tokenized_comments_ids = pad_sequences(tokenized_comments_ids, maxlen=MAX_LEN, dtype="long", truncating="post",
                                           padding="post")

    # Create attention masks
    attention_masks = []
    for seq in tokenized_comments_ids:
        seq_mask = [float(i > 0) for i in seq]
        attention_masks.append(seq_mask)

    prediction_inputs = torch.tensor(tokenized_comments_ids)
    prediction_masks = torch.tensor(attention_masks)

    # Apply the finetuned model (Camembert)
    flat_pred = []
    with torch.no_grad():
        # Forward pass, calculate logit predictions
        outputs = model(prediction_inputs.to(device), token_type_ids=None, attention_mask=prediction_masks.to(device))
        logits = outputs[0]
        logits = logits.detach().cpu().numpy()
        flat_pred.extend(np.argmax(logits, axis=1).flatten())

    comment = []
    for i in range(len(flat_pred)):
        data = {'Comment': [comment[i]],
                'Labels': [flat_pred[i]]
                }

    df = pd.DataFrame(data, columns=['Comment', 'Labels'])

    return df
