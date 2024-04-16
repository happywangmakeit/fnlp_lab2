import numpy, argparse, time
from util import read_file, get_pair, concat_pair, find_max

def args():
    parse=argparse.ArgumentParser()
    parse.add_argument('-f','--file',type=str,default='./bpe-training-data.txt'
                       ,help='file name')
    parse.add_argument('-m','--mode',type=str,default='train'
                       ,help='train or test')
    
    return parse.parse_args()

def train(arg=None):
    vocab, token=read_file(arg.file)
    pairs=get_pair(vocab)
    epochs=0
    start_time=time.time()
    while max(pairs.values())>1:
        epochs+=1
        bi_pair, pair_num=find_max(pairs)
        vocab,token=concat_pair(bi_pair,vocab,token,pair_num)
        pairs=get_pair(vocab)
        if epochs%50==0:
            print(f'epochs {epochs}: merge {bi_pair} token number: {len(token)}')
    end_time=time.time()
    print(f'time: {end_time-start_time}')

def main():
    arg=args()
    train(arg)


if __name__ == '__main__':
    main()
