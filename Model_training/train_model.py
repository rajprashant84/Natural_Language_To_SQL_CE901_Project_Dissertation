from __future__ import division, print_function, unicode_literals

import random

import torch
import torch.nn as nn
from torch import optim
from Common.common_utility import *
from Common.DataConversion import DataConversion
#from Common.graph_plotter import showPlot
from Common.SQL_Language import (prepareData, prepareValData, tensorFromSentence,tensorsFromPair)


from baseline.model.decoder import AttnDecoderRNN, DecoderRNN
from baseline.model.encoder import EncoderRNN


def run_baseline():
    hidden_size = 256
    x = DataConversionUtil()
    lr_best = hyperparam(hidden_size)

    global input_lang
    global output_lang
    global pairs
    input_lang, output_lang, pairs = prepareData("en", "sql")
    encoder1 = EncoderRNN(input_lang.n_words, hidden_size).to(device)
    decoder1 = DecoderRNN(hidden_size, output_lang.n_words).to(device)
    attn_decoder1 = AttnDecoderRNN(hidden_size, output_lang.n_words, dropout_p=0.1).to(device)
    trainIters(encoder1, attn_decoder1, 250000, print_every=1000, plot_every=1000 ,learning_rate=lr_best)
    acc = evaluateRandomly(encoder1, attn_decoder1, n=1000)
    print("Accuracy achieved:", acc)


if __name__ == '__main__':
    run_baseline()
