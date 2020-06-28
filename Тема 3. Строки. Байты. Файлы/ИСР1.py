#Разработка сценария с реализацией операции поиска подстроки в тексте

text="1658 3846 8494 0457 sdfssf sddff svvsef xbsdf sdfwwe"
print(text)
print("Подстрока:")
v=input()
if v in text:
    print(v, "входит в текст")
else: print(v, "не входит в текст")