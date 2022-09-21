# class Dom():
#     '''
#     Plan domu
#     @author: Tomasz Kaniecki
#     @:param
#     '''
#
#     kolor_domu = None
#     ilosc_okien = 0
#     basen = False
#
#     def zacznij(self):
#         print("Zaczynam budowanie...")
#         print("Czy dom ma basen?", self.basen)
#
#     def wstaw_okna(self):
#         print("Wstawiam", self.ilosc_okien, "okien")
#
#     def maluj(self):
#         print("Maluje dom na kolor:", self.kolor_domu)

# **********************************************************

class Dom():
    '''
    Plan domu
    @author: Tomasz Kaniecki
    @:param kolor_domu, ilosc_okien,basen
    '''

    def __init__(self, kolor_domu: str, ilosc_okien: int, basen=True):
        self.kolor_domu = kolor_domu
        self.ilosc_okien = ilosc_okien
        self.basen = basen

    def zacznij(self):
        print("Zaczynam budowanie...")
        print("Czy dom ma basen?", self.basen)

    def wstaw_okna(self):
        print("Wstawiam", self.ilosc_okien, "okien")

    def maluj(self):
        print("Maluje dom na kolor:", self.kolor_domu)
