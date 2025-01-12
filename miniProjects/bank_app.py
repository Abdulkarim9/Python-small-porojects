class Bank:

    abdulkarim_hesap = {
        'ad': 'Abdulkarim Maslouk',
        'hesapNo': '254698732115',
        'bakiye': 4000
    }

    ali_hesap = {
        'ad': 'Ali Nasiri',
        'hesapNo': '542689732156',
        'bakiye': 2000
    }

    def __init__(self):

        self.hesap_no = input("Lütfen hesap numaranızı giriniz: ")

        if self.hesap_no == self.abdulkarim_hesap['hesapNo']:
            print(f"Merhaba {self.abdulkarim_hesap['ad']}")
        if self.hesap_no == self.ali_hesap['hesapNo']:
            print(f"Merhaba {self.ali_hesap['ad']}")

        self.islem = input("Yapmak istadiğiniz işlem (para çekme/para yatırma): ")


    def para_cek(self, hesap):
        cek = int(input("Lütfen çekmek istediğiniz miktarı yazınız: "))
        if hesap['bakiye'] >= cek:
            print("Paranızı alabilirsiniz")
            print(f"bakiyeniz: {hesap['bakiye']}")
            print(f"Kalan bakiyeniz: {hesap['bakiye'] - cek}")
        else:
            print("Bakiyeniz yetersizdir")


    def para_yatir(self, hesap):
        yatir = int(input("Yatırmak istediğiniz miktarı yazınız: "))
        if yatir != '':
            hesap['bakiye'] += yatir
            print(f"Para yatırma işleminiz tamamlanmıştır\nYatırmış olduğunuz miktar {yatir} TL'dir")
            print(f"Yeni bakiyeniz: {hesap['bakiye']}")
        else:
            print("Lütfen yatırmak istediğiniz miktarı giriniz")


bank = Bank()

if bank.islem == 'para çekme':
    if bank.hesap_no == bank.abdulkarim_hesap['hesapNo']:
        bank.para_cek(bank.abdulkarim_hesap)
    else:
        bank.para_cek(bank.ali_hesap)
        
if bank.islem == 'para yatırma':
    if bank.hesap_no == bank.abdulkarim_hesap['hesapNo']:
        bank.para_yatir(bank.abdulkarim_hesap)
    else:
        bank.para_yatir(bank.ali_hesap)
