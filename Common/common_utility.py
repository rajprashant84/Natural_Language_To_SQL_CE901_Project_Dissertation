MAX_LENGTH = 100
SOS_token = 0
EOS_token = 1
teacher_forcing_ratio = 1
GPU = True
BATCH_SIZE = 64
TRAINING_EPOCHS = 50
LEARNING_RATE = 1e-3  #0.001


def line_Count(filename):
    with open(filename) as fname:
        return sum(1 for line in fname)


def de_tokenize(tokens):
    ret = ''
    for g, a in zip(tokens['gloss'], tokens['after']):
        ret += g + a
    return ret.strip()
