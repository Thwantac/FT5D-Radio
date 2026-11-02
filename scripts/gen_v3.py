import struct, hashlib
from plan_final import CH, BANKS
M=bytearray(open('in/MEMORY.dat','rb').read()); B=bytearray(open('in/BACKUP.dat','rb').read())
REC=6144; FLG=4800; N=900
def rec(i): return bytes(M[REC+32*i:REC+32*i+32])
T_AIR=rec(31); T_MAR=rec(48); T_WFM=rec(0)   # mem 32 AIR EMERGENCY, mem 49 CH16, mem 1 HOT 100
assert T_AIR[1]==0x47 and T_AIR[2:5]==bytes.fromhex('121500'), T_AIR.hex()
assert T_MAR[1]==0x07 and T_MAR[2:5]==bytes.fromhex('156800'), T_MAR.hex()
assert T_WFM[1]==0x89 and T_WFM[2:5]==bytes.fromhex('100100'), T_WFM.hex()
TONES=[67.0,69.3,71.9,74.4,77.0,79.7,82.5,85.4,88.5,91.5,94.8,97.4,100.0,103.5,107.2,110.9,114.8,118.8,123.0,127.3,131.8,136.5,141.3,146.2,151.4,156.7]
def bcd(n,digits=6):
    s=f'{n:0{digits}d}'; assert len(s)==digits; return bytes.fromhex(s)
# wipe
for i in range(N): M[REC+32*i:REC+32*i+32]=b'\xff'*32; M[FLG+i]=0
M[0:4800]=b'\xff'*4800
for c in CH:
    i=c['mem']-1; f=c['f']; khz=round(f*1000)
    if c['mode']=='AM' and f<2: t=bytearray(T_WFM); b1=0x4a
    elif c['mode']=='AM': t=bytearray(T_AIR); b1=0x47
    elif c['mode']=='WFM': t=bytearray(T_WFM); b1=0x89
    else: t=bytearray(T_MAR); b1=0x07
    if c['mode']=='AM' and 222<=f<420: t[0]=0x07           # as the radio itself wrote for 257.8/363.8
    if c['mode']=='FM' and f>=222: t[0]=0x07
    dup={'':0,'-':1,'+':2}[c['dup']]
    t[1]=(b1&0xCF)|(dup<<4)
    t[2:5]=bcd(khz)
    tm=1 if c['tone'] else 0
    t[5]=(t[5]&0xC0)|(c['dig']<<4)|tm
    t[6:8]=b'\x00\x00'
    nm=c['name'].encode('ascii'); t[8:24]=nm+b'\xff'*(16-len(nm))
    if c['dup']: t[24:27]=bcd(c['off'])
    if c['tone']: t[27]=(t[27]&0xC0)|TONES.index(c['tone'])
    M[REC+32*i:REC+32*i+32]=t
    nosub = f<30 or 88<=f<=108 or f>580
    M[FLG+i]= (0xc3 if c['mode']=='WFM' else 0x83) if nosub else 0x03
for k in BANKS:
    mem=[c['mem']-1 for c in CH if k in c['banks']]; assert len(mem)<=100
    for j,ix in enumerate(mem): M[(k-1)*200+2*j:(k-1)*200+2*j+2]=struct.pack('>H',ix)
    nm=BANKS[k].encode(); o=3828+18*(k-1); B[o+2:o+18]=nm+b'\xff'*(16-len(nm))
    B[1348+2*(k-1):1350+2*(k-1)]=b'\x00\x00'
struct.pack_into('>I',M,43800,sum(M[:43800])&0xffffffff)
B[5440:5440+41344]=M[:41344]
struct.pack_into('>I',B,len(B)-4,sum(B[:-4])&0xffffffff)
import os; os.makedirs('out',exist_ok=True)
open('out/MEMORY.dat','wb').write(M); open('out/BACKUP.dat','wb').write(B)
for p in ('out/MEMORY.dat','out/BACKUP.dat'): print(p,len(open(p,'rb').read()),hashlib.sha256(open(p,'rb').read()).hexdigest())
