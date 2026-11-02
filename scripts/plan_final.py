# Final v3 plan = approved plan.py + checks/upgrades + additions (2 Nov 2026)
import csv, plan
E="Airservices ERSA FAC {} eff 03 SEP 2026"
SRC={}
def S(lo,hi,s):
    for m in range(lo,hi+1): SRC.setdefault(m,s)
ABC="ABC NT frequency data; NT Gov SecureNT radio list (2 Nov 2026)"
SNT="NT Gov SecureNT 'Listen to radio updates' station list (fetched 2 Nov 2026)"
DP="Darwin Port Harbour Control VHF table (darwinport.com.au, fetched 2 Nov 2026)"
ACMAV="ACMA VHF maritime mobile band channel allocations"
WIA="WIA Repeater Directory 260705 (5 Jul 2026)"
DARC="Darwin ARC vk8da.au repeaters page (fetched 2 Nov 2026)"
NZR="map.vhf.nz NZ amateur repeater licences (RSM register, updated 29/10/2026)"
SARTS="SARTS sarts.org.sg repeater page (fetched 2 Nov 2026)"
AMSAT="AMSAT FM satellite summary (updated 31 Oct 2026) + AMSAT live status (2 Nov 2026)"
ACMA_CB="ACMA CB class licence (upd 1 Oct 2025); ch freq = 476.400+0.025*n"
SRC.update({20:SNT,21:ABC,22:ABC,23:SNT,24:ABC,25:ABC,26:ABC,
 10:"ICAO international aeronautical emergency 121.5; ERSA",16:ACMAV})
S(101,119,E.format("YPDN")); SRC[114]=E.format("YMKT"); SRC[115]=E.format("YBTI"); SRC[116]=E.format("YDLV")
S(151,168,DP); SRC[163]=ACMAV+" (Ch71 professional fishing)"; SRC[167]=ACMAV+" (Ch77 fishing/non-commercial ship-ship)"
SRC[160]=DP+" (07:03/19:03); nt.gov.au Coast Radio Darwin (08:03/18:03)"
S(201,215,E.format("YBBN")); S(216,219,E.format("YBAF"))
SRC.update({251:"MSQ Brisbane Port Procedures Oct 2024 + msq.qld.gov.au VTS page",252:"sequestradio.org (club site only)",
 253:"mrq.qld.gov.au MRQ Sandgate",254:"mrq.qld.gov.au MRQ Sandgate",255:"mrq.qld.gov.au MRQ Sandgate",256:"mrq.qld.gov.au MRQ Sandgate",
 257:"mrq.qld.gov.au MRQ Jacobs Well (log on Ch 82, fetched 2 Nov 2026)"})
S(301,307,E.format("YMML")); SRC[308]=E.format("YMMB"); S(309,311,E.format("YMEN")); S(312,315,E.format("YMMB"))
S(351,357,"Ports Victoria Port Information Guide 6th ed Dec 2025"); SRC[356]="Port Phillip Sea Pilots guide Oct 2023 (Hastings VTS)"
S(401,404,"AIP NZ chart extracts 2018-19 + pilots.nz (Sep 2026); aip.net.nz returned HTTP 500 on 2 Nov 2026")
SRC.update({451:"Port Nelson Passage Plan v3 Mar 2025",452:"Maritime NZ Radio Handbook May 2025",453:"Maritime NZ Radio Handbook May 2025",454:"Coastguard NZ Nowcasting map Oct 2024"})
S(501,516,"CAAS Singapore eAIP AD 2.18 WSSS eff 29 OCT 2026"); S(517,521,"CAAS Singapore eAIP AD 2.18 WSSL eff 29 OCT 2026")
S(551,563,"MPA Singapore VHF table / STRAITREP page (fetched 2 Nov 2026)")
SRC.update({601:DARC+"; "+WIA,602:DARC+"; "+WIA,603:DARC+"; "+WIA+"; RepeaterBook 2026-06-27",604:WIA+" (status O)",605:"WIA 2 m band plan",
 611:"ARISS",612:"ARISS",613:"WIA 2 m band plan"})
S(701,740,ACMA_CB)

# --- edits to approved channels -------------------------------------------
R={}  # mem -> dict
for m,n,f,mo,b,u,v in plan.P:
    R[m]=dict(mem=m,name=n,f=f,mode=mo,banks=list(b),use=u,v=v,dup='',off=0,tone=None,dig=0)
def up(m,**k): R[m].update(k)
up(110,use="Darwin Tower military UHF (retransmits 133.1)",v='Y')
up(111,use="Darwin Approach East UHF (retransmits 125.2)",v='Y')
up(112,name="RAAF DEPARTURE",use="Darwin Approach/Departures UHF (retransmits 123.0)",v='Y')
up(113,use="Darwin Approach West UHF (retransmits 134.1)",v='Y')
up(114,use="Emkaytee CTAF",v='Y'); up(115,use="Bathurst Island CTAF (AFRU)",v='Y'); up(116,use="Delissaville CTAF",v='Y')
up(118,use="Airport rescue & firefighting, 131.0 H24 (ERSA)",v='Y')
up(157,name="CH13 DARWIN TUGS",use="Tugs (Darwin Port lists Ch 12 and 13 as tugs)")
up(357,name="CH67 VIC WEATHER")
up(160,use="Darwin weather & notices: Harbour Control 07:03/19:03, Coast Radio Darwin 08:03/18:03")
up(257,v='Y',use="MRQ Jacobs Well log-on channel, southern Moreton Bay/Gold Coast")
up(603,v='Y',use="VK8RTE 70 cm (D-STAR/FM, 'testing'); receive only: input listed as 431.100 (DARC) vs 431.800 (WIA)")
up(604,v='Y',dup='-',off=1600,tone=123.0,dig=1,use="VK8RZZ Fusion repeater; input 145.775")
up(601,dup='-',off=600,tone=123.0,dig=1,use="VK8RTE repeater (CDU, city), carries WIA weekly broadcast")
up(602,dup='-',off=600,tone=123.0,dig=1,use="VK8RPD repeater, northern suburbs")
up(710,v='Y',use="UHF CB ch 10 (4WD clubs by convention, Radio Rescue)")
# --- additions --------------------------------------------------------------
def add(m,n,f,mode,banks,use,src,v='Y',dup='',off=0,tone=None,dig=0):
    assert m not in R,m; assert len(n)<=16,n
    R[m]=dict(mem=m,name=n,f=f,mode=mode,banks=banks,use=use,v=v,dup=dup,off=off,tone=tone,dig=dig); SRC[m]=src
add(27,'MIX 104.9',104.9,'WFM',[14],'FM broadcast, Darwin',SNT)
add(28,'97 SEVEN',97.7,'WFM',[14],'Community FM, Darwin',SNT)
add(29,'RADIO LARRAKIA',94.5,'WFM',[14],'Indigenous community FM, Darwin',SNT)
add(30,'TOP COUNTRY',92.3,'WFM',[14],'Country music FM, Darwin',SNT)
add(119,'RAAF EMERGENCY',243.0,'AM',[1,15],'Military air distress (UHF guard), monitored H24',E.format("YPDN"))
add(606,'HAM WICEN DARWIN',146.8,'FM',[11,15],'VK8RWI WICEN NT emergency-comms repeater, Karama',
    WIA+" (licensed, LN) + vk8da.com + RepeaterBook on-air 2026-08-20",dup='-',off=600,tone=123.0)
for m,n,f,u in [(614,'SO-50 SATELLITE',436.795,'FM satellite downlink, passes only (Doppler +/-10 kHz)'),
                (615,'AO-123 SATELLITE',435.4,'FM satellite downlink, passes only'),
                (616,'IO-86 SATELLITE',435.88,'Low-inclination FM satellite, many Darwin passes'),
                (617,'ISS REPEATER',437.8,'ISS cross-band FM repeater downlink'),
                (618,'AO-91 SATELLITE',145.96,'FM satellite downlink, sunlit passes only, intermittent')]:
    add(m,n,f,'FM',[12],u,AMSAT)
add(701,'CB 1 DARWIN RPT',476.425,'FM',[13],'UHF CB repeater output ch 1 (Darwin repeater listed by VKHam)',ACMA_CB+"; VKHam list via search only",v='N')
add(702,'CB 2 DARWIN RPT',476.45,'FM',[13],'UHF CB repeater output ch 2 (Darwin CBD repeater listed by VKHam)',ACMA_CB+"; VKHam list via search only",v='N')
for m in (10,16,160,705,735): R[m]['banks'].append(15)
# City ham repeaters (bank 16-19)
H=[(291,'HAM BRIS COOT 2M',146.65,'-',600,91.5,'VK4RMC Mt Coot-tha'),
   (292,'HAM BRIS COTTON',146.875,'-',600,91.5,'VK4RDB Mt Cotton, Brisbane south'),
   (293,'HAM BRIS GRAVATT',147.95,'-',600,None,'VK4RBR Mt Gravatt'),
   (294,'HAM BRIS WICEN',147.15,'+',600,None,'VK4RAG Black Mtn, Brisbane WICEN'),
   (295,'HAM GOLD COAST',146.7,'-',600,123.0,'VK4RGC Springbrook 1010 m, WIA broadcast'),
   (296,'HAM BRIS COOT 70',438.2,'-',7000,91.5,'VK4RZB Mt Coot-tha 70 cm'),
   (297,'HAM BRIS GRAV 70',438.275,'-',7000,None,'VK4RBR Mt Gravatt 70 cm')]
for m,n,f,d,o,t,u in H: add(m,n,f,'FM',[16],u,WIA,dup=d,off=o,tone=t)
H=[(391,'HAM MELB FERNY',146.7,'-',600,91.5,'VK3RML Ferny Creek, WIA broadcast'),
   (392,'HAM KINGLAKE VIC',146.85,'-',600,91.5,'VK3RMN Kinglake, Melbourne north'),
   (393,'HAM MELB OLINDA',147.175,'+',600,91.5,'VK3REC Olinda, WIA broadcast'),
   (394,'HAM MELB ST LEON',147.375,'+',600,91.5,'VK3RMU Mt St Leonard 1028 m'),
   (395,'HAM MELB WICEN',147.25,'+',600,None,'VK3RMM Mt Macedon, Melbourne WICEN'),
   (396,'HAM MELB CITY 70',438.025,'-',5000,91.5,'VK3RCC Melbourne city 70 cm'),
   (397,'HAM MELB LEON 70',439.8,'-',5000,None,'VK3RMU Mt St Leonard 70 cm, WIA broadcast')]
for m,n,f,d,o,t,u in H: add(m,n,f,'FM',[17],u,WIA,dup=d,off=o,tone=t)
H=[(491,'HAM NELSON CITY',147.025,'+',600,None,'ZL2BCA Grampians, Nelson city'),
   (492,'HAM SADDLE HILL',147.2,'+',600,None,'Nelson 720, Saddle Hill 1214 m, wide area'),
   (493,'HAM MOTUEKA',146.7,'-',600,None,'Motueka 670, Mt Campbell'),
   (494,'HAM GOLDEN BAY',147.375,'+',600,71.9,'Takaka Hill, linked to Blenheim/Picton'),
   (495,'HAM NELSON 70CM',434.8,'+',5000,None,'Saddle Hill National System 70 cm')]
for m,n,f,d,o,t,u in H: add(m,n,f,'FM',[18],u,NZR,dup=d,off=o,tone=t)
H=[(591,'HAM SING WEST 2M',145.625,'-',600,156.7,'9V1RS SARTS VHF (west), linked to 9V1RMP'),
   (592,'HAM SING EAST 70',438.425,'-',5000,156.7,'9V1RMP SARTS UHF (east), Sunday net 16:00 SGT')]
for m,n,f,d,o,t,u in H: add(m,n,f,'FM',[19],u,SARTS,dup=d,off=o,tone=t)

BANKS=dict(plan.BANKS); BANKS.update({15:'DARWIN EMERGENCY',16:'HAM BRISBANE',17:'HAM MELBOURNE',18:'HAM NELSON',19:'HAM SINGAPORE'})
for k,v in BANKS.items(): assert len(v)<=16,v
CH=[R[m] for m in sorted(R)]
for c in CH: c['src']=SRC[c['mem']]
def write_csv(path):
    with open(path,'w',newline='') as fh:
        w=csv.writer(fh); w.writerow(['memory','name','MHz','mode','duplex','offset_MHz','tone_Hz','banks','what it is','verified','source'])
        for c in CH:
            w.writerow([c['mem'],c['name'],f"{c['f']:.3f}",c['mode']+(' (AMS)' if c['dig'] else ''),c['dup'] or 'simplex',
                        f"{c['off']/1000:.3f}" if c['dup'] else '',f"{c['tone']:.1f}" if c['tone'] else '',
                        ' + '.join(BANKS[x] for x in c['banks']),c['use'],c['v'],c['src']])
if __name__=='__main__':
    write_csv('/workspace/radio/v3/FT5D_channel_plan_v3_final.csv')
    print(len(CH),'channels')
    for k,v in sorted(BANKS.items()): print(k,v,sum(1 for c in CH if k in c['banks']))
