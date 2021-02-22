# Creation

def dstBit(mass, rot, vel):
    bMass = mass
    bRot = rot
    bVel = vel


def dstCld(mass, rot):
    mass = mass
    rot = rot


def Stir(dstBit1, dstBit2):
    CldMass = dstBit1.mass + dstBit2.mass
    CldRot = dstBit1.vel * dstBit2.vel
    return dstCld(CldMass, CldRot)


def Sprk(dstCld): return StellarObject(dstCld.mass)


def Life(planet, seed): return None


dstBit1 = dstBit(8.3, 5.2, -7.1)
dstBit2 = dstBit(5.3, 3.2, 5.4)
Cld = Stir(dstBit1, dstBit2)
Planets = []
for i in range(8):
    Planets[i] = Stir(Cld, dstBit1)
Sol = Sprk(Cld)
Life(Planets[2])
