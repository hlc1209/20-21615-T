#%%
label=[]
input_text=[]

file = open('English_rumors.txt', encoding='utf-8')
txt_reader_lines = file.readlines()

for one_line in txt_reader_lines:
    label.append(one_line[0])
    input_text.append(one_line[2:-1])

tNum=0
fNum=0
uNum=0

for i in label:
    if i == 'T':
        tNum = tNum + 1
    elif i == 'F':
        fNum = fNum + 1
    elif i == 'U':
        uNum = uNum + 1
    else:
        print(i)
        print('Error')

print('The label array is:')
print(label)
print('The input_text array is:')
print(input_text)

print('True num: '+str(tNum))
print('False num: '+str(fNum))
print('Unverified num: '+str(uNum))
