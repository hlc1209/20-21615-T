The data here comes from different sources.
All the csv file encoding is utf_8_sig
*******************************************************************************************************************************************************************
0.1 all.csv is the completed dataset contain all the data below. It has {'fake': 1490, 'TRUE': 299, 'unverified': 100} 1889 in total.
It contains title, date, author, result, id (link to specific website) 
Some of the author, time id is empty because the websites don't provide that information. The author here refers to the one who verifies the information.

**************************************
0.2 all_no_weibo_xinhua.csv is the data set without the data from xinhua news agency and weibo because the data from these two source is relatively
bad organized and less incredible. It has 1106 cases in total.

*******************************************************************************************************************************************************************
1. Tecent verifying platform (腾讯较真平台)    (./separate data/wechat/)  508 in total
    I.rumor_wechat_chinese_original.csv is the original chinese version of data collected from https://vp.fact.qq.com/home using python spider
It contains title, date, author, result, id (link to specific website)
    II. rumor_wechat_chinese_RemoveOldData.csv removes the data before 12/01/2019
    III. rumor_wechat_english_translated.csv is the translated version of the above one, it contains {'fake': 380, 'unverified': 96, 'true': 32}

*******************************************************************************************************************************************************************
2. piyao platform (中国互联网联合辟谣平台)     (./separate data/piyao/)  534 in total
     I. rumor_piyao_chinese_original.csv is the original chinese version of data collected from http://www.piyao.org.cn/2020yqpy/ using python spider
     II. rumor_piyao_english_original is the translated version of the above one, it contains {'rumor': 371, 'fact': 75, 'Misunderstanding': 54, 'Rumor': 34}
     III. rumor_piyao_english_modified.csv is the final version which I convert 'rumor'. 'Rumor', 'Misunderstanding' to 'false' and convert 'fact' to 'true'. 
It gives Counter({'fake': 459, 'true': 75}). It contains title, date, author, result, id (link to specific website)

*******************************************************************************************************************************************************************
3. snopes (./separate data/snopes/)  63 in total
     I. rumor_snopes_original.csv is the original chinese version of data collected from https://www.snopes.com/tag/covid-19/ using python spider, 
it contains {'False': 33, 'Mixture': 10, 'True': 5, 'Unproven': 4, 'Correct Attribution': 4, 'Mostly False': 2, 'Miscaptioned': 2, 'Labeled Satire': 2, 'Outdated': 1} 
     II. rumor_snopes_modified.csv is the final version which I convert different result to standard true/false cases which turn out to have {'fake': 50, 'true': 9, 'unverified': 4}
It contains title, date, author, result, id (link to specific website)

*******************************************************************************************************************************************************************
4. xinhua news agency (新华网) (./separate data/xinhua_news_agency/)     
     It contains {'fake': 95, 'true': 185}. It's collected from https://xhpfmapi.zhongguowangshi.com/vh512/proof?channel=weixinp&from=timeline using houyi collector (后裔采集器)
The dataset has corresponding Chinese and English version. This dataset doesn't have id and author tag.

*******************************************************************************************************************************************************************
5. weibo (微博)  (./separate data/weibo/)  
     It contains 506 false news. It's collected from sina weibo using houyi collector (后裔采集器). Some of the date data is absent.
The dataset has corresponding Chinese and English version. This dataset doesn't have id and author tag.
     





