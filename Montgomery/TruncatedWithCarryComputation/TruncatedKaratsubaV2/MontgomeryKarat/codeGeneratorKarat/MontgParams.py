#!/usr/bin/sage


import random

SIZE = 4096#2048#1024

SIZE_M_GMP = 4096#2048#1024

SIZE_M_512 = 4154#4158#2078#1038

M_GMP = 2**SIZE_M_GMP

M_512 = 2**SIZE_M_512



n = random.randint(2**SIZE_M_GMP//2,2**SIZE_M_GMP-1)


#n+=(n-1)%2

print("M_GMP =",hex(M_GMP), hex(2**SIZE//2))

#print("n =",n)

n=next_prime(n)
	
#n=int(0x938F565032B28D8925B622E63821CE895A3A61AE377FCF33616EE5BFD2DA5C286123BE7C02376627A4BEB002DB718046706918CF137B753FBF7D733C2BDCCD4F27473F88DF39374D5799C6FCED7D4D9DEBECF4263C3BA860B43979CA182CAF2E32A66F4DB6E6315BBEBA25579F95CC36B017C25B3EC914F2A15F79F865471277)



#n=103620093203496370727261360994109075262312063022575872152499885113554673369441017201090018678385632649060805706851887639888737651045820758677284193703764980638472926677224861525610954431800543852467060668774394463727482816880847671286752112301477453159067742837950551302309426870531284885478039887524041003639

#n = 157418550878241187639261479241803639306666714317106610484945432144562069911038467230631515423932011545955210977860746032561156524274661664694525356306414572017895245127965811579183041791568369315362256714061165612265568416475069346602647590511545513475425583944379059130971734705033937251256283809154696622551

F = IntegerModRing(M_GMP)


F2 = IntegerModRing(M_512)

n512=F2(n)
n_gmp=F(n)


print("n =",n,"; is_prime()", is_prime(n))

n_prime_gmp = (-n_gmp%M_GMP)**(-1)%M_GMP

print("n_prime =",n_prime_gmp)

print("check",(-n_gmp*n_prime_gmp)%M_GMP)

n_prime_512 = (-n512)**(-1)%M_512

print("n_prime =",n_prime_512)

print("check",(-n512*n_prime_512)%M_512)

r2_512 = (M_512*M_512)%n

print("r2_512 =",r2_512)


A= randint(2**SIZE_M_GMP//2,2**SIZE_M_GMP-1)

print("A     =",hex(A))

r2_gmp = (M_GMP*M_GMP)%n

T = A*int(r2_gmp)

Q = (T*int(n_prime_gmp))%int(M_GMP)

C = T+Q*n

print("C_gmp =",hex(C))

C=C>>SIZE_M_GMP
print("C_gmp =",hex(C))

T = C

Q = (T*int(n_prime_gmp))%int(M_GMP)
C = T+Q*n

print("C_gmp =",hex(C))

C=C>>SIZE_M_GMP
print("C_gmp =",hex(C))

print()

T = A*int(r2_512)

Q = (T*int(n_prime_512))%int(M_512)

C = T+Q*n
print("C_512 =",hex(C))
C=C>>SIZE_M_512

print("C_512 =",hex(C))

T = C

Q = (T*int(n_prime_512))%int(M_512)
C = T+Q*n

print("C_512 =",hex(C))
C=C>>SIZE_M_512

print("C_512 =",hex(C))


f= open("montParam.c","w")

f.write("/*   Montgomery parameters !*/\n\n")

line = "\tmpz_set_str(modul_p, \""+str(n)+"\",10);\n"
f.write(line)

line = "\tmpz_set_str(p_prime, \""+str(n_prime_512)+"\",10);\n"
f.write(line)


line = "\tmpz_set_str(r2_gmp_512, \""+str(r2_512)+"\",10);\n"
f.write(line)



f.close()
