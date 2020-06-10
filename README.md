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


# Data
- `en_dup.csv` 
  - The number of records: 7179.   
  - Part of data are collected manually by keywords searching from sources such as twitter.com.  
  - Data from www.snopes.com and qc.wa.news.cn are collected by 'snopes.py'.  

- `USC_Melady_Lab_hasDup.csv` 
  - The number of records: 35134.  
  - Data come from usc-melady.github.io/COVID-19-Tweet-Analysis/misinfo.html, accessed in May.  
  - Reference: Sharma, Karishma, et al. "Coronavirus on social media: Analyzing misinformation in Twitter conversations."   arXiv preprint arXiv:2003.12309 (2020).

# The MIT License (MIT)

