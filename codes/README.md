# HEHO Health Myths

本檔案為 HEHO 健康迷思版由 2017 11 08 至 2023.07.30 共 192頁、1913 篇檔案之爬蟲。
資料夾結構如下：
```bash
├── codes
│   ├── HEHO.py
│   ├── README.md
│   ├── combine_dataframes.py
│   └── requirements.txt
└── data
    ├── combined_dataframe.tsv
    └── crawled_heho_myths
        ├── heho_page1.txt
        ├── heho_page10.txt
        ├── heho_page100.txt
        ├── heho_page101.txt
        ├── heho_page102.txt
        ├── heho_page103.txt
        ├── heho_page104.txt
        ├── heho_page105.txt
        ├── heho_page106.txt
        ├── heho_page107.txt
        ├── heho_page108.txt
        ├── heho_page109.txt
        ├── heho_page11.txt
        ├── heho_page110.txt
        ├── heho_page111.txt
        ├── heho_page112.txt
        ├── heho_page113.txt
        ├── heho_page114.txt
        ├── heho_page115.txt
        ├── heho_page116.txt
        ├── heho_page117.txt
        ├── heho_page118.txt
        ├── heho_page119.txt
        ├── heho_page12.txt
        ├── heho_page120.txt
        ├── heho_page121.txt
        ├── heho_page122.txt
        ├── heho_page123.txt
        ├── heho_page124.txt
        ├── heho_page125.txt
        ├── heho_page126.txt
        ├── heho_page127.txt
        ├── heho_page128.txt
        ├── heho_page129.txt
        ├── heho_page13.txt
        ├── heho_page130.txt
        ├── heho_page131.txt
        ├── heho_page132.txt
        ├── heho_page133.txt
        ├── heho_page134.txt
        ├── heho_page135.txt
        ├── heho_page136.txt
        ├── heho_page137.txt
        ├── heho_page138.txt
        ├── heho_page139.txt
        ├── heho_page14.txt
        ├── heho_page140.txt
        ├── heho_page141.txt
        ├── heho_page142.txt
        ├── heho_page143.txt
        ├── heho_page144.txt
        ├── heho_page145.txt
        ├── heho_page146.txt
        ├── heho_page147.txt
        ├── heho_page148.txt
        ├── heho_page149.txt
        ├── heho_page15.txt
        ├── heho_page150.txt
        ├── heho_page151.txt
        ├── heho_page152.txt
        ├── heho_page153.txt
        ├── heho_page154.txt
        ├── heho_page155.txt
        ├── heho_page156.txt
        ├── heho_page157.txt
        ├── heho_page158.txt
        ├── heho_page159.txt
        ├── heho_page16.txt
        ├── heho_page160.txt
        ├── heho_page161.txt
        ├── heho_page162.txt
        ├── heho_page163.txt
        ├── heho_page164.txt
        ├── heho_page165.txt
        ├── heho_page166.txt
        ├── heho_page167.txt
        ├── heho_page168.txt
        ├── heho_page169.txt
        ├── heho_page17.txt
        ├── heho_page170.txt
        ├── heho_page171.txt
        ├── heho_page172.txt
        ├── heho_page173.txt
        ├── heho_page174.txt
        ├── heho_page175.txt
        ├── heho_page176.txt
        ├── heho_page177.txt
        ├── heho_page178.txt
        ├── heho_page179.txt
        ├── heho_page18.txt
        ├── heho_page180.txt
        ├── heho_page181.txt
        ├── heho_page182.txt
        ├── heho_page183.txt
        ├── heho_page184.txt
        ├── heho_page185.txt
        ├── heho_page186.txt
        ├── heho_page187.txt
        ├── heho_page188.txt
        ├── heho_page189.txt
        ├── heho_page19.txt
        ├── heho_page190.txt
        ├── heho_page191.txt
        ├── heho_page192.txt
        ├── heho_page2.txt
        ├── heho_page20.txt
        ├── heho_page21.txt
        ├── heho_page22.txt
        ├── heho_page23.txt
        ├── heho_page24.txt
        ├── heho_page25.txt
        ├── heho_page26.txt
        ├── heho_page27.txt
        ├── heho_page28.txt
        ├── heho_page29.txt
        ├── heho_page3.txt
        ├── heho_page30.txt
        ├── heho_page31.txt
        ├── heho_page32.txt
        ├── heho_page33.txt
        ├── heho_page34.txt
        ├── heho_page35.txt
        ├── heho_page36.txt
        ├── heho_page37.txt
        ├── heho_page38.txt
        ├── heho_page39.txt
        ├── heho_page4.txt
        ├── heho_page40.txt
        ├── heho_page41.txt
        ├── heho_page42.txt
        ├── heho_page43.txt
        ├── heho_page44.txt
        ├── heho_page45.txt
        ├── heho_page46.txt
        ├── heho_page47.txt
        ├── heho_page48.txt
        ├── heho_page49.txt
        ├── heho_page5.txt
        ├── heho_page50.txt
        ├── heho_page51.txt
        ├── heho_page52.txt
        ├── heho_page53.txt
        ├── heho_page54.txt
        ├── heho_page55.txt
        ├── heho_page56.txt
        ├── heho_page57.txt
        ├── heho_page58.txt
        ├── heho_page59.txt
        ├── heho_page6.txt
        ├── heho_page60.txt
        ├── heho_page61.txt
        ├── heho_page62.txt
        ├── heho_page63.txt
        ├── heho_page64.txt
        ├── heho_page65.txt
        ├── heho_page66.txt
        ├── heho_page67.txt
        ├── heho_page68.txt
        ├── heho_page69.txt
        ├── heho_page7.txt
        ├── heho_page70.txt
        ├── heho_page71.txt
        ├── heho_page72.txt
        ├── heho_page73.txt
        ├── heho_page74.txt
        ├── heho_page75.txt
        ├── heho_page76.txt
        ├── heho_page77.txt
        ├── heho_page78.txt
        ├── heho_page79.txt
        ├── heho_page8.txt
        ├── heho_page80.txt
        ├── heho_page81.txt
        ├── heho_page82.txt
        ├── heho_page83.txt
        ├── heho_page84.txt
        ├── heho_page85.txt
        ├── heho_page86.txt
        ├── heho_page87.txt
        ├── heho_page88.txt
        ├── heho_page89.txt
        ├── heho_page9.txt
        ├── heho_page90.txt
        ├── heho_page91.txt
        ├── heho_page92.txt
        ├── heho_page93.txt
        ├── heho_page94.txt
        ├── heho_page95.txt
        ├── heho_page96.txt
        ├── heho_page97.txt
        ├── heho_page98.txt
        └── heho_page99.txt

```
## 檔案說明

### codes

HEHO.py：爬蟲所用之檔案，共爬了六個欄位，分別為 'id', 'time', 'link', 'title', 'content', 'summary'。其中 'id' 為文章之網址尾數，'content' 中文章之副標題則保留其原本 html 語法以區隔，'summary' 則是文章開頭的小方格中的摘要、前情提要內容，若無則為 NaN。

combine_dataframes.py：將每一頁所有文章整併成一份 dataframe 之檔案。

### data

combined_dataframe.tsv：使用 combine_dataframes.py 整併 .txt 檔案後之結果。

#### data-crawled_heho_myths

heho_page{1-192}.txt：爬蟲之原始資料，分成一頁一頁之檔案，共 192 頁，除最後一頁之外，每一頁共有 10 篇文章，加總為 1913 篇。
