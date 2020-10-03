import os # operating system

products = []
if os.path.isfile('products.csv'): #path模組的isfile功能 (檢查檔案在不在)
	print('yeah! 找到檔案了!')
	#讀取檔案
	products = []
	with open('products.csv', 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue #直接跳迴圈的下一圈，不執行之後的，但是又沒有跳出迴圈
			name, price = line.strip().split(',') #切成兩塊的字串，直接存到name, price 
			#先strip 再split (功能由左至右執行)
			#strip用來切掉\n
			#split用逗點來切割把一行字串分塊
			#unicode error就是編碼錯誤的問題
			products.append([name, price])
			#再把name, price存進products 清單
	for p in products:
		print(p[0], '的價格是: ', p[1])
	print(products)

else:
	print('找不到檔案...')

#練習二維清單 (清單裡可以放小清單)


#讓使用者輸入商品名稱

while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	price = int(price)
	#
	#p = []
	#p.append(name)
	#p.append(price)
	
	#p = [name, price] #可以不用append
	#products.append(p)
	#
	products.append([name, price]) 
	#可以這樣就建立二維清單，就連 p = [] 都不用寫
for p in products:
	print(p[0], '的價格是', p[1])
print(products)
products[0][0] #[大清單][小清單]

#存入清單
with open('products.csv', 'w', encoding = 'utf-8') as f:
	#utf-8 是最廣泛使用的編碼方式，讓中文可以顯示
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ', ' + str(p[1]) + '\n') 
		#加法只能加字串，數字的資料用str()轉換成文字再合併