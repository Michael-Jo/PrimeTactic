# Bilangan prima = 2, 3, 5, 7, 11, .. (Bilangan yang hanya bisa dibagi habis diri sendiri dan 1)
# Bilangan komposit = 1, 4, 6, 8, 9, 10, ... (Lawan dari bilangan prima)
# Input : number ( min )
#         number ( max )
# Proses : bilangan Prima (ke dalam list) List pakai []
#           bilangan Komposit (Ke dalam dictionarys) Dict pakai {}
# Output : Tampilkan list bilangan prima
print("\t<<<\tBilngan Prima & Komposit\t>>>\t")
print("-"*15)
min = int(input("Masukan bilangan minimum : "))
max = int(input("Masukan bilangan maximum : "))
print("-"*15)
# angka : [i for i in range(min, max)]
# prima: [prime for prime in range(min, max) if prime % 1 == 0 and prime % prime == 0]
# prima = []
# komposit = dict()
# komposit : [composite for composite in range(min, max) if composite % 1 != 0 or composite % composite != 0]
def is_prime(input):
    if input <= 1: # untuk ..., -1, 0. 1
        return False
    for i in range(2, int(input**0.5) + 1):
        if input % i == 0:
            return False
    return True
prima = [i for i in range (min,max+1) if is_prime(i) ]
komposit = { i for i in range (min,max+1) if not is_prime(i) }
print(f"Prima = {prima}")
print(f"Komposit = dict_values{komposit}")