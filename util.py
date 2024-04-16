import re
import matplotlib.pyplot as plt

def read_file(file_name, flag=True):
    content=str()
    vocab=dict()
    token=dict()
    with open(file_name) as file:
        for line in file:
            words=line.strip().split()
            for word in words:
                cur_word=' '.join(list(word)) + ' </w>'
                content+=(cur_word+' ')
                vocab[cur_word]=vocab.setdefault(cur_word,0)+1
            content+="\n"
    if flag:
        token=get_token(vocab)
        return content, vocab, token
    else:
        return content

def get_pair(vocab:dict):
    pairs=dict()
    for word,freq in vocab.items():
        alpha=word.split()
        le=len(alpha)
        for i in range(1,le):
            pair=(alpha[i-1],alpha[i])
            pairs[pair]=pairs.setdefault(pair,0)+freq
    return pairs

def get_token(vocab:dict):
    token=dict()
    for word,freq in vocab.items():
        alpha=word.split()
        for i in alpha:
            token[i]=token.setdefault(i,0)+freq
    return token

def concat_pair(bi_pair:tuple, content:str, vocab:dict=None, flag=True):
    res_vocab=dict()
    res_content=str()
    bi_token=''.join(bi_pair)
    bigram=re.escape(' '.join(bi_pair))
    pattern=re.compile(r'(?<!\S)'+bigram+r'(?!\S)') 
    # pattern=re.compile(r'{}'.format(bigram),
    #                          re.UNICODE)
    res_content=pattern.sub(bi_token,content)
    if flag:
        for word, freq in vocab.items():
            res=pattern.sub(bi_token,word)
            res_vocab[res]=res_vocab.setdefault(res,0)+freq
        # print(f'p {pair_num},f {freq_sum}')
        # token[bi_pair[0]]-=pair_num
        # token[bi_pair[1]]-=pair_num
        # if token[bi_pair[0]]==0:
        #     token.pop(bi_pair[0])
        # if token[bi_pair[1]]==0:
        #     token.pop(bi_pair[1])
        # token[bi_token]=token.setdefault(bi_token,0)+pair_num
        return res_content, res_vocab
    else:
        return res_content

def paint(x, y):
    plt.plot(x, y, marker='o')
    plt.xlabel('epoch')
    plt.ylabel('types size')
    
    plt.show()
    return 

def find_max(vocab:dict):
    max_key=max(vocab,key=vocab.get)
    max_num=vocab[max_key]
    return max_key,max_num
