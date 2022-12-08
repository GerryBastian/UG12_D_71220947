jml_uang = int(input("Masukkan jumlah uang : RP"))

ketik = input("ketik Start untuk memulai : ")
ketik = ketik.upper()

while ketik == "START" and jml_uang != 0:
    barang = input("Apa barang yang akan anda beli?")
    if barang == "susu":
        sisauangsusu = jml_uang - 20000
        if jml_uang >= 20000:
            print("Sisa uang anda ",sisauangsusu)
        else: 
            print("Uang tidak cukup")
        jml_uang = sisauangsusu
        
    elif barang == "permen":
        sisauangpermen = jml_uang - 500
        if jml_uang >= 500:
            print("Sisa uang anda ",sisauangpermen)
        else: 
            print("Uang tidak cukup")
        jml_uang = sisauangpermen
        
    elif barang == "roti":
        sisauangroti = jml_uang - 15000
        if jml_uang >= 15000:
            print("Sisa uang anda ",sisauangroti)
        else: 
            print("Uang tidak cukup")
        jml_uang = sisauangroti
        
    elif barang == "indomie":
        sisauangmie = jml_uang - 3000
        if jml_uang >= 3000:
            print("Sisa uang anda ",sisauangmie)
        else: 
            print("Uang tidak cukup")
        jml_uang = sisauangmie
        
    elif barang == "vitamin":
        sisauangvita = jml_uang - 50000
        if jml_uang >= 50000:
            print("Sisa uang anda ",sisauangvita)
        else: 
            print("Uang tidak cukup")
        jml_uang = sisauangvita
    
    elif barang == "SUDAH":
        print(exit())
        
    else:
        print("Barang tidak tersedia")
    
    
    