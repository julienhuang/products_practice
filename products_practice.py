import os # 首先匯入"作業系統"模組(為了取用接下來的step1尋找檔案"isfile"功能)

products = []

# step 1: (在特定資料夾底下)尋找檔案
if os.path.isfile('products.csv'): # os模組底下的 path模組底下的 isfile功能
	print('找到檔案了!')

# step 2: 讀取檔案
	with open('products.csv', 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue #繼續. 跳過此一回迴圈, 進入下一回
			name, price = line.strip().split(',')
			products.append([name, price])
	print(products)
else:
	print('找不到檔案...')

# step 3: 讓使用者輸入購買紀錄
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	products.append([name, price]) # 以中括號方式將不同變數存入同一筆清單中, 等於二維清單two-dimensional list

print(products)

print(products[0][1]) # 印出清單第一筆(包含兩項文字資料)的第二項資料

# 印出所有購買紀錄
for product in products:
	print(product[0], '的價格是:', product[1])

# 字串可加＆乘. 'abc' + 'abc' = 'abcabc' (字串合併).  'abc' x 3 = 'abcabcabc'

# 寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f: #打開CSV檔寫入前必須明確指定"utf-8"格式, 以防亂碼
	f.write('商品,價格\n') #在CSV檔開頭建立"欄位名稱"
	for product in products:
		f.write(product[0] + ',' + product[1] + '\n') #將商品與價格的資料(字串)分別寫入CSV
