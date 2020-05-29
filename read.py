data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(count)
print('檔案讀取完了, 總共有', len(data), '筆資料！')

sum_len = 0
for d in data:
    sum_len += len(d)

print('留言的平均長度為', sum_len / len(data))

new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('一共有', len(new), '筆留言長度小於100')


good =[]
for d in data:
    if 'good' in d:
        good.append(d)
print('一共有', len(good), '筆留言中有提到good')


#文字計數，並且增加查詢功能
wc = {}
for d in data: # 先從百萬留言清單中取出每一條留言
    words = d.split() # 再用空格分開哪一個字，並成為一個字的清單
    for word in words: # 再從字的清單當中取出每一個字
        if word in wc: # 如果字典中有這個字的話
            wc[word] += 1 # 就在這個字原本有數量加一
        else:
            wc[word] = 1 # 反之如果沒有這個字，就給他數字一開始算

for word in wc:
    if wc[word] > 1000000:
        print(word, wc[word])
print('總共有', len(wc), '個字！')

while True:
    word = input('請問你想查什麼字？ ')
    if word == '886':
        break
    if word in wc:
        print(word, '出現過的次數為： ', wc[word])
    else:
        print('查無', word, '此字！')
    
print('感謝您使用本查詢功能')
