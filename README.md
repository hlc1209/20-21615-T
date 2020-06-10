# File Structure
```
├── Data Collecting Tools
│   ├── snopes.py
├── Data Processing Tools
│   └── data_process.ipynb
├── Raw Data and Processor
│   ├── fromUSCMeladyLab
│   └── ManualCollection
├── Processed Data
│   ├── en_dup.csv
│   └── USC_Melady_Lab_hasDup.csv
├── LICENSE.txt
└── README.md
```

# Data Collecting Tools
- `snopes.py` by Tianqi
  - It is used to collect data from website www.snopes.com and qc.wa.news.cn (departed)

# Data Processing Tools
`data_process.ipynb` is written on Jupyter Notebook.
P

# Raw Data
- Manual Collection
  - These parts of data are collected manually. Their sources are mainly twitter.com. The rest of them come from keywords searching in web search engines.
  - How to run the processing program: `python raw_data_processor.py`


- fromUSCMeladyLab
  - These data comes from usc-melady.github.io/COVID-19-Tweet-Analysis/misinfo.html
  - How to run the processing program: `python raw_data_processor.py`

# Processed Data
- `en_dup.csv` is the processed data set corresponding to the "ManualCollection" section.
  - The number of records: 7179


- `USC_Melady_Lab_hasDup.csv` is the processed data set corresponding to the "fromUSCMeladyLab" section.
  - The number of records: 35134

# The MIT License (MIT)

