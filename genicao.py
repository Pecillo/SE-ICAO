
seicao = "010010101"
registration = input('Enter registration: SE-')


reg = {
    'A' : '00001',
    'B' : '00010',
    'C' : '00011',
    'D' : '00100',
    'E' : '00101',
    'F' : '00110',
    'G' : '00111',
    'H' : '01000',
    'I' : '01001',
    'J' : '01010',
    'K' : '01011',
    'L' : '01100',
    'M' : '01101',
    'N' : '01110',
    'O' : '01111',
    'P' : '10000',
    'Q' : '10001',
    'R' : '10010',
    'S' : '10011',
    'T' : '10100',
    'U' : '10101',
    'V' : '10110',
    'W' : '10111',
    'X' : '11000',
    'Y' : '11001',
    'Z' : '11010'
}


res = list(registration.upper())



icao24 = seicao + reg[res[0]]+reg[res[1]]+reg[res[2]]
icaoresult = "{0:0>4X}".format(int(icao24,2))

print("Aircraft Registration  : SE-" + registration.upper())
print("ICAO HEX Code          : " + icaoresult)
print("ICAO 24-bit Binary code: " + icao24 )
