dataDict = { 
    "plm" : "Palembang",
    "em" : "Muara Enim",
    "pr" : "Prabumulih",
    "llg" : "Lubuklinggaus"
}
for i in dataDict:
    print( f"i = { i }")

print( f"-" * 15, "KEYS")
print( f"Keys in dataDict = { dataDict.keys() }")
for z in dataDict.keys():
    print( f"z = { z }")

print( f"-" * 15, "VALUE")
print( f"Keys in dataDict = { dataDict.keys() }")
for x in dataDict.values():
    print( f"x = { x }")

print( f"-" * 15, "items")
print( f"items in dataDict = { dataDict.keys() }")
for K, V in dataDict.items():
    print( f"{ K } = { V }")

# print ( f"3 % 0 = {3 % 0}")
print ( f"3 % 1 = {3 % 1}") # 0
print ( f"3 % 2 = {3 % 2}") # 1
print ( f"3 % 3 = {3 % 3}") # 0