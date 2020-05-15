# 初期変数の値おきば #################################
name1 = "Name" 
age1 = "Age"
color1 = "Color code" # 指定カラーコードが無ければイメージ色を入れるようにラベルを出す
size1 = [0, 0, 0]

name2 = "Name"
age2 = "Age"
color2 = "Color code"
size2 = [0, 0, 0]

name3 = "Name"
age3 = "Age"
color3 = "Color code"
size3 = [0, 0, 0]
# おきば終わり #################################
##################################


name1 = "天海春香" # この4種をユーザーに入力させる
age1 = 17
color1 = "e33830" # スポイトで持ってこられたら良いね
size1 = [83, 56, 82] # 大きな値なので直に入力させる
# 文字を入れられても出せるようにする？

chara1 = (name1, age1, color1, size1)

# chara1.extend([name1, age1, color1, size1]) # リストに情報を上書き

##################################


name2 = "如月千早"
age2 = 16
color2 = "0075c2"
size2 = [72, 55, 78]

chara2 = (name2, age2, color2, size2)

# chara2.extend([name2, age2, color2, size2])

##################################


name3 = "星井美希"
age3 = 15
color3 = "a9d053"
size3 = [86, 55, 83]

chara3 = (name3, age3, color3, size3)

# chara3.extend([name3, age3, color3, size3])

##################################
print(chara1, chara2, chara3) # テスト用