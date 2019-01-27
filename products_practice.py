#記帳程式
products = []
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	products.append([name, price])
print(products)

print(products[0][1]) #以中括號方式將不同變數存入同一筆清單中, 等於二維清單two-dimensional list

for product in products:
	print(product[0], '的價格是:', product[1])

#字串可加＆乘. 'abc' + 'abc' = 'abcabc' (字串合併).  'abc' x 3 = 'abcabcabc'

with open('products.csv', 'w', encoding='utf-8') as f: #打開CSV檔寫入前必須明確指定"utf-8"格式, 以防亂碼
	f.write('商品,價格\n') #在CSV檔開頭建立"欄位名稱"
	for product in products:
		f.write(product[0] + ',' + product[1] + '\n') #將商品與價格的資料(字串)分別寫入CSV
