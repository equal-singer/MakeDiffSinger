import os, tqdm, re
from tqdm import tqdm
from glob import glob
import kog2p


def make_dictionary(asset_dir: str, dic_path: str):
    _dict = {}
    for f in tqdm(os.listdir(asset_dir)):
        if '.lab' in f:
            print(f)
            sentence = open(f'{asset_dir}/{f}', 'r', encoding='utf-8').readline()

            for s in sentence.split(' '):
                s = s.replace(' ', '')
                if s != '':
                    if s not in _dict:
                        _dict[s] = kog2p.runKoG2P(s)

    with open(f'{dic_path}/csd.txt', 'w', encoding='utf-8') as f:
        for key in ['AP', 'SP']:
            f.write(f'{key}\t{key}\n')

        for key in sorted(_dict.keys()):
            content = '{}\t{}\n'.format(key, _dict[key])
            f.write(content)

            
if __name__ == '__main__':
        
    dic_path = './dictionaries'
    if not os.path.exists(dic_path):
        os.makedirs(dic_path)
        
    asset_dir = './assets/segments'
    make_dictionary(asset_dir, dic_path)
