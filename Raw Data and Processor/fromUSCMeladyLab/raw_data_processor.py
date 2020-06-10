#%% 
import csv
import numpy as np

content = []
label = []
time = []


#%% usc
keep_original_label = True
with open('./USC_Melady_Lab_upto_4_11.csv', 'r', encoding='UTF-8') as csvfile:
    f_csv = csv.reader(csvfile, delimiter=',')
    for t in f_csv:
        temp = t[1].rstrip('\n').rsplit('[2020')[0].rsplit('http')[0].replace('\n',' ').replace('  ',' ').replace('  ',' ').replace('  ',' ').strip()
        if len(temp) > 24:
            content.append(temp)
            time.append(("2020" + t[1].rstrip('\n').rsplit('[2020')[1]).rstrip(']'))
            if keep_original_label:
                label.append(t[0])
            else:
                if t[0] == 'unknown':
                    label.append('U')
                else:
                    label.append('F')
        

#%% remove duplications

newContent = []
newLabel = []
newTime = []

for i, text in enumerate(content):
    text = text.replace('\n',' ').replace('  ',' ').replace('  ',' ').replace('  ',' ').replace('  ',' ').strip() # 
    if len(text) < 2:
        continue
    if text[-1] == "." or text[-1] == "," or text[-1] == "?" or text[-1] == "!" or text[-1] == " ":
        text = text[:-1]
    if text not in newContent:
        newContent.append(text)
        newLabel.append(label[i])
        newTime.append(time[i])

content = newContent
label = newLabel
time = newTime


#%% shuffle

# p = np.random.permutation(len(label))
# content = list(np.array(content)[p])
# label = list(np.array(label)[p])
# time = list(np.array(time)[p])

#%% output

with open('./en.csv','w', newline='', encoding='UTF-8') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(('label', 'content', 'time')) # 
    for i in range(len(label)):
        f_csv.writerow([label[i], content[i], time[i]]) # 

# %%
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


# %%
