import time
start =  time.time()

## LATIHAN OPERASI BITWISE
# or(|), and(%), xor(^), not(~)

a = 5
b = 9

## OR(|)
print("=======OR=========")
c = a | b
print("Nilai :",a," Binary",format(a,'08b'))
print("Nilai :",b," Binary",format(b,'08b'))
print("--------------------------(|)")
print("Nilai :",c,"Binary",format(c,'08b'))

## AND(&)
print("\n=======AND=========")
c = a & b
print("Nilai :",a,"Binary",format(a,'08b'))
print("Nilai :",b,"Binary",format(b,'08b'))
print("--------------------------(&)")
print("Nilai :",c,"Binary",format(c,'08b'))

## XOR(^)
print("\n=======XOR=========")
c = a ^ b
print("Nilai :",a," Binary",format(a,'08b'))
print("Nilai :",b," Binary",format(b,'08b'))
print("--------------------------(^))")
print("Nilai :",c,"Binary",format(c,'08b'))

## NOT(~)
print("\n=======NOT=========")
c = ~a
print("Nilai :",a," Binary",format(a,'08b'))
print("--------------------------(~)")
print("Nilai :",c,"Binary",format(c,'08b'))

print("\n=======FLIP=========")
a = 0b00000101
b = 0b11111111
c = a ^ b
print("Nilai :",a,"  Binary",format(a,'08b'))
print("Nilai :",b,"Binary",format(b,'08b'))
print("--------------------------(^))")
print("Nilai :",c,"Binary",format(c,'08b'))

## SHIFTRIGHT(>>)
print("\n=======SHIFTRIGHT=========")
c = a >> 2
print("Nilai :",a,"Binary",format(a,'08b'))
print("--------------------------(>>))")
print("Nilai :",c,"Binary",format(c,'08b'))

## SHIFTLEFT(<<)
print("\n=======SHIFTLEFT=========")
c = a << 2
print("Nilai :",a," Binary",format(a,'08b'))
print("--------------------------(<<))")
print("Nilai :",c,"Binary",format(c,'08b'))

print(time.time() - start, "Detik")