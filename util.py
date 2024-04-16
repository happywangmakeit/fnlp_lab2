import re

def read_file(file_name):
    vocab=dict()
    token=dict()
    with open(file_name) as file:
        for line in file:
            words=line.strip().split()
            for word in words:
                cur_word=' '.join(list(word)) + ' </w>'
                vocab[cur_word]=vocab.setdefault(cur_word,0)+1
    for word,freq in vocab.items():
        alpha=word.split()
        for i in alpha:
            token[i]=token.setdefault(i,0)+freq
    return vocab, token

def get_pair(vocab:dict):
    pairs=dict()
    for word,freq in vocab.items():
        alpha=word.split()
        le=len(alpha)
        for i in range(1,le):
            pair=(alpha[i-1],alpha[i])
            pairs[pair]=pairs.setdefault(pair,0)+freq
    return pairs

def concat_pair(bi_pair:tuple, vocab:dict, token:dict, pair_num:int):
    res_vocab=dict()
    bi_token=''.join(bi_pair)
    bigram=re.escape(' '.join(bi_pair))
    pattern=re.compile(r'(?<!\S)'+bigram+r'(?!\S)')
    for word, freq in vocab.items():
        res=pattern.sub(bi_token,word)
        res_vocab[res]=res_vocab.setdefault(res,0)+freq
    token[bi_pair[0]]-=pair_num
    token[bi_pair[1]]-=pair_num
    if token[bi_pair[0]]==0:
        token.pop(bi_pair[0])
    if token[bi_pair[1]]==0:
        token.pop(bi_pair[1])
    token[bi_token]=token.setdefault(bi_token,0)+pair_num
    return res_vocab, token


# def preprocess(content:str):
#     vocab=dict()
#     type_vocab=set()
#     data=content
#     datalist=[]
#     for i in data:
#         datalist.append(i)

#     le=len(datalist)
#     type_vocab[datalist[0]]=1
#     for i in range(1,le):
#         key=(datalist[i-1],datalist[i])
#         vocab[key]=vocab.setdefault(key,0)+1
#         type_vocab[datalist[i]]=type_vocab.setdefault(datalist[i],0)+1
#     return datalist, vocab, type_vocab

def find_max(vocab:dict):
    max_key=max(vocab,key=vocab.get)
    max_num=vocab[max_key]
    return max_key,max_num
