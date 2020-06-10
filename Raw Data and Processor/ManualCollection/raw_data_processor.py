#%% 
import csv
import numpy as np

content = []
label = []
source = []
time = []
author = []

#%% jianni

with open(r'./jianni/English_rumors.txt', "r", encoding='UTF-8') as csvfile:
    txt_reader_lines = csvfile.readlines()

for one_line in txt_reader_lines:
    label.append(one_line[0])
    content.append(one_line[2:].rstrip('\n'))
    time.append(None)
    source.append(None)
    author.append(None)

with open(r'./jianni/1000TandU.txt', "r", encoding='UTF-8') as csvfile:
    txt_reader_lines = csvfile.readlines()

for one_line in txt_reader_lines:
    label.append(one_line[0])
    content.append(one_line[2:].rstrip('\n'))
    time.append(None)
    source.append(None)
    author.append(None)

with open(r'./jianni/300false.txt', "r", encoding='UTF-8') as csvfile:
    txt_reader_lines = csvfile.readlines()

for one_line in txt_reader_lines:
    label.append(one_line[0])
    content.append(one_line[2:].rstrip('\n'))
    time.append(None)
    source.append(None)
    author.append(None)

# %% tianqi

with open('./tianqi/1000.csv', 'r', encoding='UTF-8') as csvfile:
    f_csv = csv.reader(csvfile, delimiter=',')
    for t in f_csv:
        if t[8] == 'unverified':
            label.append('U')
        elif t[8] == 'TRUE':
            label.append('T')
        else:
            label.append('F')
        content.append(t[4])
        time.append(t[0])
        source.append(t[1])
        author.append(t[5])


with open('./tianqi/google_factcheck.csv', 'r', encoding='UTF-8') as csvfile:
    f_csv = csv.reader(csvfile, delimiter=',')
    for t in f_csv:
        if t[6] == 'FALSE':
            label.append('F')
        elif t[6] == 'TRUE':
            label.append('T')
        else:
            label.append('U')
        content.append(t[2])
        time.append(None)
        source.append(t[1])
        author.append(None)

with open('./tianqi/poynter.csv', 'r', encoding='UTF-8') as csvfile:
    f_csv = csv.reader(csvfile, delimiter=',')
    for t in f_csv:
        if t[9] == 'FALSE':
            label.append('F')
        elif t[9] == 'TRUE':
            label.append('T')
        else:
            label.append('U')
        content.append(t[1])
        time.append(None)
        source.append(t[2])
        author.append(t[3])

# %% wenshuo
with open('./wenshuo/Wenshuo_twitter-true.csv', 'r', encoding='UTF-8') as csvfile:
    f_csv = csv.reader(csvfile, delimiter=',')
    for t in f_csv:
        if t[2] == 'unverified':
            label.append('U')
        elif t[2] == 'TRUE':
            label.append('T')
        else:
            label.append('F')
        content.append(t[5].rstrip('\n'))
        time.append(t[1])
        source.append(None)
        author.append(t[3])

with open('./wenshuo/Wenshuo_twitter-unverified.csv', 'r', encoding='UTF-8') as csvfile:
    f_csv = csv.reader(csvfile, delimiter=',')
    for t in f_csv:
        if t[2] == 'unverified':
            label.append('U')
        elif t[2] == 'TRUE':
            label.append('T')
        else:
            label.append('F')
        content.append(t[5].rstrip('\n'))
        time.append(t[1])
        source.append(None)
        author.append(t[3])

with open('./wenshuo/week4_wenshuo.csv', 'r', encoding='UTF-8') as csvfile:
    f_csv = csv.reader(csvfile, delimiter=',')
    for t in f_csv:
        if t[2] == 'unverified':
            label.append('U')
        elif t[2] == 'TRUE':
            label.append('T')
        else:
            label.append('F')
        content.append(t[4].rstrip('\n'))
        time.append(t[1])
        source.append(None)
        author.append(t[3])

#%% xiaofeng

with open('./xiaofeng/xiaofeng 407 records from twitter.csv', 'r', encoding='UTF-8') as csvfile:
    f_csv = csv.reader(csvfile, delimiter=',')
    for t in f_csv:
        if t[0] == 'FALSE':
            label.append('F')
        elif t[0] == 'TRUE':
            label.append('T')
        else:
            label.append('U')
        content.append(t[1].rstrip('\n'))
        time.append(t[4])
        source.append(t[5])
        author.append(None)

#%% remove duplications

newContent = []
newLabel = []
newSource = []
newTime = []
newAuthor = []

for i, text in enumerate(content):
    text = text.replace('\n',' ').replace('  ',' ').replace('  ',' ').replace('  ',' ').replace('  ',' ').strip() # 
    if len(text) < 2:
        continue
    if text[-1] == "." or text[-1] == "," or text[-1] == "?" or text[-1] == "!" or text[-1] == " ":
        text = text[:-1]
    if text not in newContent:
        newContent.append(text)
        newLabel.append(label[i])
        newSource.append(source[i])
        newTime.append(time[i])
        newAuthor.append(author[i])

content = newContent
label = newLabel
source = newSource
time = newTime
author = newAuthor



#%% shuffle

# p = np.random.permutation(len(label))
# content = list(np.array(content)[p])
# label = list(np.array(label)[p])
# source = list(np.array(source)[p])
# time = list(np.array(time)[p])
# author = list(np.array(author)[p])

#%% output

with open('./en.csv','w', newline='', encoding='UTF-8') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(('label', 'content','source', 'author', 'time')) # 
    for i in range(len(label)):
        f_csv.writerow([label[i], content[i], source[i], author[i], time[i]]) # 

# %% statistic
numF = 0
numT = 0
numU = 0
for l in label:
    if l == 'F':
        numF += 1
    elif l == 'T':
        numT += 1
    else:
        numU += 1
with open('./output.log','w', newline='', encoding='UTF-8') as f:
    f.write("Total Number: "+str(numF+numT+numU)+"\n")
    f.write("False Number: "+str(numF)+"\n")
    f.write("True Number: "+str(numT)+"\n")
    f.write("Unverified Number: "+str(numU)+"\n")

print("Total Number: "+str(numF+numT+numU)+"\n")
print("False Number: "+str(numF)+"\n")
print("True Number: "+str(numT)+"\n")
print("Unverified Number: "+str(numU)+"\n")

