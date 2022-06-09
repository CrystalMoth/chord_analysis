def etsi_sointu(nuotit):
    tila = False
    i = 0
    while(tila != True and i < 3):
        sointu, tila = tutki_millainen_triadi(nuotit, i)
        i += +1
    print("Sointu on", sointu, "\n")
    syoto = input("Jatketaanko? (Kirjoita 'k')\n")
    if syoto == "k":
        main()

def tutki_millainen_triadi(nuotit, i):
        num_juuri = TWELVE_TONE[nuotit[TRIADI_PERMUTAATIOT[i]]]
        toinen_nuotti = TWELVE_TONE[nuotit[TRIADI_PERMUTAATIOT[1 + i]]]
        kolmas_nuotti = TWELVE_TONE[nuotit[TRIADI_PERMUTAATIOT[2+ i]]]
        #Duuri?
        if toinen_nuotti - num_juuri == 4 and kolmas_nuotti - num_juuri == 7:
            return nuotit[0] + "Maj", True
            #Molli?
        elif toinen_nuotti- num_juuri == 3 and kolmas_nuotti- num_juuri == 7:
            return nuotit[0] + "m", True
            #Diminished?
        elif toinen_nuotti- num_juuri == 3 and kolmas_nuotti- num_juuri == 6:
            return nuotit[0] + "dim", True
            #Augmented?
        elif toinen_nuotti- num_juuri == 4 and kolmas_nuotti- num_juuri == 8:
            return nuotit[0] + "aug", True
        else:
            return None, False

#Ohjelma kertoo mikä sointu on kyseessä kun avain ja nuotit on annettu
C_DUURI = ["C","D","E","F","G","A","B"]
TRIADI_PERMUTAATIOT = [0,1,2,0,1]
NELISOINTU_PERMUTAATIOT = [0,1,2,3,0,1,2,3]
#C puoliaskeleet kun sävellajina on C
TWELVE_TONE = {"C":0,"Cs":1, "Df":1,"D":2,"Ds":3,"Ef":3,"E":4, "Es":5,"Ff":4,"F":5,"Fs":6,"Gf":6, "G":7, "Gs":8, "Af":8 ,
"A":9,"As":10, "Bf":10, "B":11, "Bs":0}

#Syötön muokkaus
def main():
    syoto = input("Syötä nuotit pilkulla (,) erotettuna\n")
    nuotit =syoto.split(",")
    etsi_sointu(nuotit)
main()