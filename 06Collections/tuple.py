# liste         => un nombre inderterminé d'élements accessible par leur indice
# dictionnaire  => un nombre inderterminé d'élements accessible par une clé
# tuple         => un nombre déterminé d'élements en lecteur seule

monTuple1 = ("un", 2, 3, "quatre")
print("monTuple1", monTuple1, type(monTuple1))
print("premier élément", monTuple1[0])
print("dernier élément", monTuple1[-1])

#(premier, deuxieme, troisieme, quatrieme) = monTuple1
premier, deuxieme, troisieme, quatrieme = monTuple1
print("premier", premier)
print("deuxieme", deuxieme)
print("troisieme", troisieme)
print("quatrieme", quatrieme)

maListe = []
maListe.append(11)
maListe.append(22)
maListe.append(33)

nb1, nb2, nb3, nb4, nb5 = 11, 22, 33, 44, 55
#nb1, nb2, nb3, nb4, nb5 = maListe
#nb1, nb2 = maListe

nb1 = 11
nb2 = 99
nb1, nb2 = 11, 99
print("nb1 =", nb1, "nb2 =", nb2)

(nb1, nb2) = (nb2, nb1)
print("nb1 =", nb1, "nb2 =", nb2)
