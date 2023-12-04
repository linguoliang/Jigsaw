#!/usr/bin/env python
# coding: utf-8

# In[1]:


## 这个脚本用于模拟数据，产生片段化scaffold
##生成 200k，400k，600k，800k，1000k序列长度片段

from Bio import SeqIO
import pandas as pd
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-i', '--input', required=True, type=str, help='input fasta file!')
parser.add_argument('-o', '--output', required=True, type=str, help='output fasta file!')
parser.add_argument("-r","--random", required=True,type=bool,default='')
args = parser.parse_args()
# In[3]:


def GenerateScaffold(Seq,size):
    Seqlist=[]
    length=len(Seq.seq)
    for i in range(0,length,size):
        end=min(i+size,length)
        name="{}_{}_{}".format(Seq.name,i,end)
        Rc=SeqRecord(Seq.seq[i:end],id=name,name=name,description=name)
        Charac=set(Rc.seq)
        if ("N" in Charac) and (len(Charac)==1):
            continue
        Seqlist.append(Rc)
    return Seqlist


# In[4]:


length_dict={"200k":200000,"400k":400000,"600k":600000,"800k":800000,"1M":1000000}

# In[5]:

list_chrom=[str(x) for x in range(1,23)]
for name in length_dict:
    all_seq_list=[]
    hindle=SeqIO.parse(args.input,"fasta")
    for Seq in hindle:
        all_seq_list.extend(GenerateScaffold(Seq,length_dict[name]))
    # with open("./ref/human_{}.chrom.sizes".format(name),'w') as
    SeqIO.write(all_seq_list,"{}_{}.fasta".format(args.output,name),"fasta")


# In[25]:


all_seq_list[0][0:10000]


# In[7]:


all_seq_list[-1]


# In[27]:


# list_chrom=[str(x) for x in range(1,23)]
for name in length_dict:
    hindle=SeqIO.parse("{}_{}.fasta".format(args.output,name),"fasta")
    with open(".{}_{}.chrom.sizes".format(args.output,name),'w') as outputfile:
        for Seq in hindle:
            outputfile.write("{}\t{}\n".format(Seq.name,len(Seq.seq)))
#     SeqIO.write(all_seq_list,"./ref/human_{}.fasta".format(name),"fasta")
