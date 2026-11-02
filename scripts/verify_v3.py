import struct, csv, sys
d=sys.argv[1] if len(sys.argv)>1 else 'out'
M=open(f'{d}/MEMORY.dat','rb').read(); B=open(f'{d}/BACKUP.dat','rb').read()
I0=open('in/MEMORY.dat','rb').read(); B0=open('in/BACKUP.dat','rb').read()
TON=[67.0,69.3,71.9,74.4,77.0,79.7,82.5,85.4,88.5,91.5,94.8,97.4,100.0,103.5,107.2,110.9,114.8,118.8,123.0,127.3,131.8,136.5,141.3,146.2,151.4,156.7]
err=[]
assert struct.unpack('>I',M[43800:43804])[0]==sum(M[:43800])&0xffffffff; assert struct.unpack('>I',B[-4:])[0]==sum(B[:-4])&0xffffffff
assert B[5440:5440+41344]==M[:41344]
# changes outside expected regions?
for i in range(len(M)):
    if M[i]!=I0[i] and not (i<4800 or 4800<=i<5700 or 6144<=i<6144+900*32 or 43800<=i<43804): err.append(('M byte changed',i))
bank_ok=set(range(3828,3828+18*24))|set(range(1348,1348+48))|set(range(5440,5440+41344))|set(range(len(B)-4,len(B)))
for i in range(len(B)):
    if B[i]!=B0[i] and i not in bank_ok: err.append(('B byte changed',i))
dec={}
for i in range(900):
    fl=M[4800+i]
    if not fl&0x02: continue
    r=M[6144+32*i:6144+32*i+32]
    mode=['FM','AM','WFM','?'][r[1]>>6]; dup=['simplex','-','+','split'][(r[1]>>4)&3]
    f=int(r[2:5].hex())/1000
    tm=r[5]&0x0f; dig=(r[5]>>4)&3
    name=r[8:24].split(b'\xff')[0].decode()
    off=int(r[24:27].hex())/1000
    tone=TON[r[27]&0x3f] if tm==1 else ''
    nos=bool(fl&0x80); 
    if nos != (f<30 or 88<=f<=108 or f>580): err.append(('nosub',i+1))
    dec[i+1]=dict(name=name,f=f'{f:.3f}',mode=mode+(' (AMS)' if dig==1 else ''),dup=dup,off=f'{off:.3f}' if dup!='simplex' else '',tone=f'{tone:.1f}' if tone else '',step=r[1]&15)
banks={}
for k in range(24):
    nm=B[3830+18*k:3846+18*k].split(b'\xff')[0].decode()
    for j in range(100):
        v=struct.unpack('>H',M[k*200+2*j:k*200+2*j+2])[0]
        if v!=0xffff: banks.setdefault(v+1,[]).append(nm)
rows=list(csv.DictReader(open('FT5D_channel_plan_v3_final.csv')))
seen=set()
for r in rows:
    m=int(r['memory']); seen.add(m); x=dec.get(m)
    if not x: err.append(('missing',m)); continue
    exp=dict(name=r['name'],f=r['MHz'],mode=r['mode'],dup=r['duplex'],off=r['offset_MHz'],tone=r['tone_Hz'])
    for k,v in exp.items():
        if x[k]!=v: err.append(('mismatch',m,k,x[k],v))
    if ' + '.join(banks.get(m,[]))!=r['banks']: err.append(('bank',m,banks.get(m),r['banks']))
extra=set(dec)-seen
if extra: err.append(('extra memories',sorted(extra)))
print('decoded',len(dec),'csv rows',len(rows),'banks used',len({b for v in banks.values() for b in v}))
print('steps used',sorted({x['step'] for x in dec.values()}))
print('ERRORS',err if err else 'none')
