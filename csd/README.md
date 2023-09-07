# CSD Segments로 DiffSinger학습을 위한 Dataset 만들기

## 1. Clone repo and install dependencies

```
git clone https://github.com/equal-singer/MakeDiffSinger.git
cd MakeDiffSinger/csd
conda create -n mfa python=3.8 --yes  # you must use a Conda environment!
conda activate mfa
conda install -c conda-forge montreal-forced-aligner==2.0.6 --yes  # install MFA
pip install -r requirements.txt  # install other requirements
```
* conda activate mfa가 안되면 source activate mfa

## 2. Download CSD Segments

```
python download_segments.py
```
* assets/segments폴더에 segments데이터가 다운로드 됨

## 3. CSD lab 데이터로 dictionary 생성

```
python make_dictionary.py
```
* dictionaries 폴더에 csd.txt 파일 생성됨

## 4. MFA acoustic Model train 
```
mfa train assets/segments dictionaries/csd.txt textgrids/raw
```
* textgrids/raw 폴더에 textgird 파일들 생성됨

## 5. Enhance and finish the TextGrids

```
python enhance_tg.py --wavs assets/segments --dictionary dictionaries/csd.txt --src textgrids/raw --dst textgrids/final
```
* textgrids/final 폴더에 수정된 textgird 파일들 생성됨

## 6. Build the final dataset

```
python build_dataset.py --wavs assets/segments --tg textgrids/final --dataset dataset
```
* dataset 폴더에 최종 데이터셋 생성됨

transcriptions.csv 구조
- name: the segment name
- ph_seq: the phoneme sequence
- ph_dur: the phoneme duration
