print("~~~~~ Table Matematika Nich ~~~~~")
print("Pilihan Model Matematika")
print("1. Perkalian")
print("2. Pembagian")
a = (int(input("Masukan model matematika yang diinginkan 1/2 :")))
if(a>2):
    print("Pilihan tidak tersedia jangan ngasal!")
    exit()
b = (int(input("Menampilkan table matematika dari angka : ")))
if(a==1):
    for i in range (1,11):
      print(b,"x", i , "=" , b*i)
elif(a==2):
    for i in range (50,66):
      print(i,":", b , "=" , i/b)
