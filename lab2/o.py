number=input()
def res(num):
     num = num.replace('+', ' ').replace("ONE", '1').replace("TWO", '2').replace("THR", '3').replace("FOU", '4').replace("FIV", '5').replace("SIX", '6').replace("SEV", '7').replace("EIG", '8').replace("NIN", '9').replace("ZER", '0').split()
     sum = str(int(num[0])+int(num[1]))
     sum = sum.replace('1', "ONE").replace('2', "TWO").replace('3', "THR").replace('4', "FOU").replace('5', "FIV").replace('6', "SIX").replace('7', "SEV").replace('8', "EIG").replace('9', "NIN").replace('0', "ZER") 
     print(sum)
res(number)