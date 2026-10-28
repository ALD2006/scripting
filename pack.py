import sys 
import struct

if len(sys.argv) <= 1:
    print("Veuillez entrer un nombre", file=sys.stderr)
    sys.exit(1)

try:
    nombre= int(sys.argv[1])
    little= struct.pack('<I', nombre)
    big= struct.pack('>I', nombre)

    print("big-hexa:",big.hex(' '))
    print("little-hexa",little.hex(' '))

except ValueError:
    print(f"{sys.argv[1]} n'est pas un nombre",file=sys.stderr)
    sys.exit(1)

