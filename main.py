import numpy, argparse, time, json
from tqdm import tqdm
from collections import OrderedDict
from util import read_file, get_pair, concat_pair, find_max, paint, get_token

def args():
    parse=argparse.ArgumentParser()
    parse.add_argument('-f','--file',type=str,default='./bpe-training-data.txt'
                       ,help='file name')
    parse.add_argument('-m','--mode',type=str,default='test'
                       ,help='train or test')
    parse.add_argument('-v','--vocab',type=str,default='vocab.json',
                       help='the file path to keep the vocab')
    parse.add_argument('-tok','--token',type=str,default='token.json',
                       help='the file path to keep the token')
    parse.add_argument('-typ','--type',type=str,default='type.txt',
                       help='the file path to keep the type vocabulary')
    
    return parse.parse_args()

def train(arg=None):
    content, vocab, token=read_file(arg.file)
    type_vocab=[]
    pairs=get_pair(vocab)
    epochs=0
    start_time=time.time()
    x=[]
    y=[]
    while max(pairs.values())>3:
        x.append(epochs)
        y.append(len(type_vocab))
        epochs+=1
        bi_pair, pair_num=find_max(pairs)
        type_vocab.append(bi_pair)
        content, vocab=concat_pair(bi_pair,content, vocab)
        token=get_token(vocab)
        pairs=get_pair(vocab)
        if epochs%100==0:
            # print(vocab)
            print(f'epochs {epochs}: merge {bi_pair} token number: {len(token)}')
            print(min(token.values()))
    end_time=time.time()

    print(f'time: {end_time-start_time}')
    # paint iteration and corresponding types size
    x.append(epochs)
    y.append(len(type_vocab))
    paint(x,y) #draw pos of (x,y)
    print(f'content length:{len(content)}')

    with open(arg.token, 'w') as f:
        json.dump(token, f)
    with open(arg.vocab, 'w') as f:
        json.dump(vocab, f)
    with open(arg.type, 'w') as f:
        f.write(str(type_vocab))
    
    with open('train_result.txt', 'w') as file:
        file.write(content)
    return content

def test(arg=None):
    with open('type.txt', 'r') as f:
        type_vocab = eval(f.read())
    print(type(type_vocab))
    content=read_file(arg.file,0)

    for bi_word in tqdm(type_vocab):
        content=concat_pair(bi_word,content, flag=False)

    with open('test_result.txt', 'w') as file:
        file.write(content)
    return content
    

def main():
    arg=args()
    if arg.mode=='train':
        txt=train(arg)
    else:
        txt=test(arg)


if __name__ == '__main__':
    main()
