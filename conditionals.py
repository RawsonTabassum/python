spin = input()
charge = input()

if spin == '1/2' and charge == '-1/3':
    print('Strange Quark')
elif spin == '1/2' and charge == '2/3':
    print('Charm Quark')
elif spin == '1/2' and charge == '-1':
    print('Electron Lepton')
elif spin == '1/2' and charge == '0':
    print('Muon Lepton')
elif spin == '1' and charge == '0':
    print('Photon Boson')
elif spin == '0' and charge == '0':
    print('Higgs boson Boson')

seq = []

while True:
    INPUT = input()
    if INPUT == '.':
        break
    seq.append(int(INPUT))

sum = 0
for x in seq:
    sum = sum + x;

print(sum / len(seq))