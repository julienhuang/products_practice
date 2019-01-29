import os # 首先匯入"作業系統"模組(為了取用接下來的step1尋找檔案"isfile"功能)

# function中心思想: 只做一件事！ BE FOCUSED! BE SIMPLE!

# step 1: 讀取檔案
def read_file(filename):
	products = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue #繼續. 跳過此一回迴圈, 進入下一回
			name, price = line.strip().split(',')
			products.append([name, price])
	return products
	
# step 2: 讓使用者輸入購買紀錄
def user_input(products):
	while True:
		name = input('請輸入商品名稱:')
		if name == 'q':
			break
		price = input('請輸入商品價格:')
		products.append([name, price]) # 以中括號方式將不同變數存入同一筆清單中, 等於二維清單two-dimensional list
	print(products)
	return products

#print(products[0][1]) # 印出清單第一筆(包含兩項文字資料)的第二項資料

# step 3: 印出所有購買紀錄
def print_products(products):
	for product in products:
		print(product[0], '的價格是:', product[1])

# 字串可加＆乘. 'abc' + 'abc' = 'abcabc' (字串合併).  'abc' x 3 = 'abcabcabc'

# step 4: 寫入檔案
def write_file(filename, products):
	with open(filename, 'w', encoding='utf-8') as f: #打開CSV檔寫入前必須明確指定"utf-8"格式, 以防亂碼
		f.write('商品,價格\n') #在CSV檔開頭建立"欄位名稱"
		for product in products:
			f.write(product[0] + ',' + product[1] + '\n') #將商品與價格的資料(字串)分別寫入CSV


# 以下才是主要執行的部分(上面都是在定義各functions而已). 主要執行的部分通常稱作 main function
def main():
	# step 0: (在特定資料夾底下)尋找檔案
	filename = 'products.csv'
	if os.path.isfile(filename): # os模組底下的 path模組底下的 isfile功能
		print('找到檔案了!')
		products = read_file(filename)  # 如果有找到檔案, 接下來才進入step 1.
	else:
		print('找不到檔案...')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()
