import os
import sys
import math
import torch
import random
import datetime
import numpy as np
import torch.distributed as dist
from torch.optim import AdamW
from torch.nn.utils.rnn import pad_sequence
from tqdm import tqdm
from torch.nn.parallel import DistributedDataParallel as DDP
from tokenizer import Tokenizer
from transformers import (
    BertTokenizer, 
    BertConfig, 
    is_torch_available,
)


def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    if is_torch_available():
        torch.manual_seed(seed)
        torch.cuda.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False
        
class Config():
    
    ## 1. high
    epoch = 3
    lr = 5e-5
    batch_size = 4
    num_steps = 1024
    max_length = 10240
    
    ## 2. mid

    
    ## 3. low
    device = "cuda" if torch.cuda.is_available() else "cpu"
    log_dir = "./logs"
    

if __name__ == "__main__":
    set_seed(6)
    config = Config
    
    tokenizer = Tokenizer()
    print(tokenizer.encode("te"))
    print(tokenizer.decode([1,2]))
    
    
    
    
    
    
    