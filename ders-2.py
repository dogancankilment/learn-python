bos_liste = []
liste_isim = ['d', 'c', 'k']
print liste_isim

liste_isim[0]
liste_isim[1]
liste_isim[2]

len(liste_isim)
print len(liste_isim)

print liste_isim.index('d')
print liste_isim.index('c')
print liste_isim.index('k')

bos_liste = []
bos_liste.append('dogancankilment')
bos_liste.append('utopian-io')
print bos_liste

bos_liste[0]
bos_liste[1]

print "ilk_eleman: ", bos_liste[0], "ikinci_eleman: ", bos_liste[1]

for liste_elemanlari in bos_liste:
	print liste_elemanlari

bos_liste.remove('utopian-io')
bos_liste.append('test edilecek degisken ')

del bos_liste[1]

bos_liste.append('can')
bos_liste.append('can')

bos_liste.count('can')
bos_liste.count('dogancankilment')

sayi_listesi = ['1','3','5','2']
print sayi_listesi

sayi_listesi.sort()
