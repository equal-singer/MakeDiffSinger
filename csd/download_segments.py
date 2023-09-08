from tqdm import tqdm
import requests
import zipfile
import os


def download(asset_path: str, url: str):
    response = requests.get(url, stream=True)
    total_size_in_bytes= int(response.headers.get('content-length', 0))
    block_size = 1024 #1 Kibibyte
    progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
    
    with open(f'{asset_path}/segments.zip', 'wb') as file:
        for data in response.iter_content(block_size):
            progress_bar.update(len(data))
            file.write(data)
    
    progress_bar.close()
    
    if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
        print("ERROR, something went wrong")
        

def unzip(asset_path: str):
    with zipfile.ZipFile(f'{asset_path}/segments.zip', 'r') as zip_ref:
        zip_ref.extractall(f'{asset_path}/segments')

        
if __name__ == '__main__':
    asset_path = './assets'
    if not os.path.exists(asset_path):
        os.makedirs(asset_path)
    
    print('### start download csd segments')
    url = 'https://github.com/equal-singer/CSD/releases/download/diffSinger/segments.zip'
    download(asset_path, url)
    print('### end download csd segments')
    
    print('### start unzip csd segments')
    unzip(asset_path)
    print('### end unzip csd segments')
    