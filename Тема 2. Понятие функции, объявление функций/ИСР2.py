print('              1. (A∨B)∧ ¬C')

def gran1():
 pass
 return print(chr(9500)+chr(9472)*5+chr(9532)+chr(9472)*5+chr(9532)+chr(9472)*5+chr(9532)+chr(9472)*5+chr(9532)+chr(9472)*7+chr(9532)+chr(9472)*10+chr(9508))

def tab1(a,b,c):
  pass
  return print(chr(9474)+'  '+str(int(a))+'  '+chr(9474)+'  '+str(int(b))+'  '+chr(9474)+'  '+str(int(c))+'  '+chr(9474)+'  '+str(int(not(c)))+'  '+chr(9474)+'   '+str(int(a or b))+'   '+chr(9474)+'    '+str(int((a or b) and not(c)))+'     '+chr(9474))

print(chr(9484)+chr(9472)*5+chr(9516)+chr(9472)*5+chr(9516)+chr(9472)*5+chr(9516)+chr(9472)*5+chr(9516)+chr(9472)*7+chr(9516)+chr(9472)*10+chr(9488))
print(chr(9474)+'  A  '+chr(9474)+'  B  '+chr(9474)+'  C  '+chr(9474)+' '+chr(172)+'C  '+chr(9474)+'  AvB  '+chr(9474)+' (AvB)&'+chr(172)+'C '+chr(9474))
gran1()
tab1(True,True,True)
gran1()
tab1(True,True,False)
gran1()
tab1(True,False,True)
gran1()
tab1(True,False,False)
gran1()
tab1(False,True,True)
gran1()
tab1(False,True,False)
gran1()
tab1(False,False,True)
gran1()
tab1(False,False,False)
print(chr(9492)+chr(9472)*5+chr(9524)+chr(9472)*5+chr(9524)+chr(9472)*5+chr(9524)+chr(9472)*5+chr(9524)+chr(9472)*7+chr(9524)+chr(9472)*10+chr(9496))


print('                  2. ((A→B)∧A) ↔ A∧B')

def gran2():
 pass
 return print(chr(9500)+chr(9472)*5+chr(9532)+chr(9472)*5+chr(9532)+chr(9472)*5+chr(9532)+chr(9472)*9+chr(9532)+chr(9472)*7+chr(9532)+chr(9472)*15+chr(9508))

def tab2(a,b):
  ab= a and b
  aba=(not a or b) and a
  return print(chr(9474)+'  '+str(int(a))+'  '+chr(9474)+'  '+str(int(b))+'  '+chr(9474)+'  '+str(int(not a or b))+'  '+chr(9474)+'    '+str(int(aba))+'    '+chr(9474)+'   '+str(int(ab))+'   '+chr(9474)+'       '+str(int(aba and ab or not(aba) and not(ab)))+'       '+chr(9474))


print(chr(9484)+chr(9472)*5+chr(9516)+chr(9472)*5+chr(9516)+chr(9472)*5+chr(9516)+chr(9472)*9+chr(9516)+chr(9472)*7+chr(9516)+chr(9472)*15+chr(9488))
print(chr(9474)+'  A  '+chr(9474)+'  B  '+chr(9474)+' A→B '+chr(9474)+' (A→B)&A '+chr(9474)+'  A&B  '+chr(9474)+' ((A→B)&A)↔A&B '+chr(9474))

gran2()
tab2(True,True)
gran2()
tab2(True,False)
gran2()
tab2(False,True)
gran2()
tab2(False,False)
print(chr(9492)+chr(9472)*5+chr(9524)+chr(9472)*5+chr(9524)+chr(9472)*5+chr(9524)+chr(9472)*9+chr(9524)+chr(9472)*7+chr(9524)+chr(9472)*15+chr(9496))

print('                       3. A∨(B∧C)↔(A∨B)∧(A∨C)')

def gran3():
 pass
 return print(chr(9500)+chr(9472)*5+chr(9532)+chr(9472)*5+chr(9532)+chr(9472)*5+chr(9532)+chr(9472)*5+chr(9532)+chr(9472)*9+chr(9532)+chr(9472)*5+chr(9532)+chr(9472)*5+chr(9532)+chr(9472)*21      +chr(9508))

def tab3(a,b,c):
 abc= a or (b and c)
 abac=(a or b) and (a or c) 
 return print(chr(9474)+'  '+str(int(a))+'  '+chr(9474)+'  '+str(int(b))+'  '+chr(9474)+'  '+str(int(c))+'  '+chr(9474)+'  '+str(int(b and c))+'  '+chr(9474)+'    '+str(int(a or(b and c)))+'    '+chr(9474)+'  '+str(int(a or b))+'  '+chr(9474)+'  '+str(int(a or c))+'  '+chr(9474)+'          '+str(int(abc and abac or not(abc) and not(abac)))+'          '+chr(9474))

print(chr(9484)+chr(9472)*5+chr(9516)+chr(9472)*5+chr(9516)+chr(9472)*5+chr(9516)+chr(9472)*5+chr(9516)+chr(9472)*9+chr(9516)+chr(9472)*5+chr(9516)+chr(9472)*5+chr(9516)+chr(9472)*21      +chr(9488))
print(chr(9474)+'  A  '+chr(9474)+'  B  '+chr(9474)+'  С  '+chr(9474)+' B&C '+chr(9474)+' Av(B&C) '+chr(9474)+' AvB '+chr(9474)+' AvC '+chr(9474)+' Av(B&C)↔(AvB)&(AvC) '   +chr(9474))

gran3()
tab3(True,True,True)
gran3()
tab3(True,True,False)
gran3()
tab3(True,False,True)
gran3()
tab3(True,False,False)
gran3()
tab3(False,True,True)
gran3()
tab3(False,True,False)
gran3()
tab3(False,False,True)
gran3()
tab3(False,False,False)
print(chr(9492)+chr(9472)*5+chr(9524)+chr(9472)*5+chr(9524)+chr(9472)*5+chr(9524)+chr(9472)*5+chr(9524)+chr(9472)*9+chr(9524)+chr(9472)*5+chr(9524)+chr(9472)*5+chr(9524)+chr(9472)*21      +chr(9496))