# HEHO Health Myths

本檔案為 HEHO 健康迷思版由 2017 11 08 至 2023.07.30 共 192頁、1913 篇檔案之爬蟲。
由於原始 .txt 檔案過多，故在此僅附上整併後之 .tsv 檔案供參考。
資料夾結構如下：
```bash
├── codes
│   ├── HEHO.py
│   ├── README.md
│   ├── combine_dataframes.py
│   └── requirements.txt
└── data
    └── combined_dataframe.tsv

```
## 檔案說明

### codes

HEHO.py：爬蟲所用之檔案，共爬了六個欄位，分別為 'id', 'time', 'link', 'title', 'content', 'summary'。
其中 'id' 為文章之網址尾數，'content' 中文章之副標題則保留其原本 html 語法以區隔，'summary' 則是文章開頭的小方格中的摘要、前情提要內容，若無則為 NaN。
直接使用此檔案即可進行爬蟲，回傳結果以網頁的頁數為單位，一頁為一個 .txt 檔案，每一頁共有 10 篇文章。

combine_dataframes.py：將每一頁所有文章整併成一份 dataframe 之檔案。

### data

combined_dataframe.tsv：使用 combine_dataframes.py 整併 .txt 檔案後之結果。

#### 原始檔案說明

heho_page{1-192}.txt：爬蟲之原始資料，分成一頁一頁之檔案，共 192 頁，除最後一頁之外，每一頁共有 10 篇文章，加總為 1913 篇。
