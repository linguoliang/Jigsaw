import os
import PIL
import torch.utils.data as data
from torchvision import datasets, transforms
import h5py
# import

# from timm.data import create_transform
# from timm.data.constants import IMAGENET_DEFAULT_MEAN, IMAGENET_DEFAULT_STD
import torch
from torch.utils.data import Dataset


class MyDataset(Dataset):
    def __init__(self):
        pass

    def __getitem__(self, index):
        pass

    def __len__(self):
        pass


import torch
# from torch.utils.data import Dataset

class data_iter:
    # Constructor
    def __init__(self, datasize,data,data_len):
        self.datasize = datasize
        self.data=data
        self.data_len=data_len
    # Creates iterator object
    # Called when iteration is initialized
    def __iter__(self):
        self.x = 0
        return self
    # To move to next element. In Python 3,
    # we should replace next with __next__
    def __next__(self):
        # Store current value ofx
        x = self.x
        # Stop iteration if limit is reached
        if x > self.datasize:
            raise StopIteration
        # Else increment and return old value
        self.x = x + 1;
        return x
# 构建数据集，每个数据包含,从h5数据读取数据，通过
class GetTrainTestData(Dataset):
    def __init__(self, input_len, output_len, train_rate,data_path, is_train=True):
        super().__init__()
        self.f = h5py.File(data_path, "r")
        # self.x = torch.sin(torch.arange(0, 1000, 0.1))
        self.sample_num = len(self.x)
        self.input_len = input_len
        self.output_len = output_len
        self.train_rate = train_rate
        self.src, self.trg = [], []
        if is_train:
            # for i in range(int(self.sample_num * train_rate) - self.input_len - self.output_len):
            #     self.src.append(self.x[i:(i + input_len)])

    def __getitem__(self, index):
        pass

    def __len__(self):
        return len(self.src)  # 或者return len(self.trg), src和trg长度一样


data_train = GetTrainTestData(input_len=3, output_len=1, train_rate=0.8, is_train=True)
data_test = GetTrainTestData(input_len=3, output_len=1, train_rate=0.8, is_train=False)

import torch
from torch.utils.data import TensorDataset

src = torch.sin(torch.arange(1, 1000, 0.1))
trg = torch.cos(torch.arange(1, 1000, 0.1))