
img2 = np.copy(ar)
x = random.randint(0, 254)
y = random.randint(0, 254)
img2[x][y] = random.randint(0, 254)
img2 = key.keyxor(img2, keys)
analysis.histogram(ar, s)
npcr, uaci = analysis.NPCR_UACI_worker(ar, img2)
print("npcr: ", npcr, "%\tUaci: ", uaci, "%")
print("Entropy", analysis.entropy(shuffled))