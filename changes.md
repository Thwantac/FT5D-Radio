# FT5D v3: changes and checks (2 Nov 2026, ACST)

**On the card:** 183 memories in 19 banks, written at 13:25 ACST. The sha256 of both files on the card matches the generated files:
- MEMORY.dat `12aa5005…96c8`
- BACKUP.dat `c0020754…29fd`

**Backups on the Mac:**
- `~/FT5D_SD_backup_20261102_1318_preV3.tgz`: the card before the write (whole card)
- `~/FT5D_SD_backup_20261102_1325_v3.tgz`: the card after the write

**Final list:** `FT5D_channel_plan_v3_final.csv`, which has duplex, offset, tone, verified and source columns.

## Added (34)
- **FM radio (27–30):**
  - MIX 104.9
  - 97 SEVEN 97.7
  - RADIO LARRAKIA 94.5
  - TOP COUNTRY 92.3
  - Source: NT Gov SecureNT list.
- **119 RAAF EMERGENCY 243.0 AM:** the military air distress channel, monitored H24 (ERSA YPDN).
- **606 HAM WICEN DARWIN 146.800:** VK8RWI, offset −0.6, tone 123.0.
- **Satellites (614–618), FM downlinks:**
  - SO-50 436.795
  - AO-123 435.400
  - IO-86 435.880
  - ISS REPEATER 437.800
  - AO-91 145.960
  - Source: AMSAT, 31 Oct 2026.
- **701 and 702, UHF CB repeater outputs (Darwin):** unverified (N).
- **Brisbane ham (291–297), WIA Jul 2026:**
  - Mt Coot-tha 146.650 (91.5 tone) and 438.200 (−7, 91.5 tone)
  - Mt Cotton 146.875 (91.5 tone)
  - Mt Gravatt 147.950 and 438.275 (−7)
  - Black Mtn WICEN 147.150 (+)
  - Springbrook 146.700 (123 tone)
- **Melbourne ham (391–397), WIA Jul 2026:**
  - Ferny Creek 146.700
  - Kinglake 146.850
  - Olinda 147.175 (+)
  - Mt St Leonard 147.375 (+) and 439.800 (−5)
  - Mt Macedon WICEN 147.250 (+)
  - City 438.025 (−5)
- **Nelson ham (491–495), map.vhf.nz RSM licence list, 29 Oct 2026:**
  - Grampians 147.025 (+)
  - Saddle Hill 147.200 (+)
  - Motueka 146.700 (−)
  - Golden Bay 147.375 (+, 71.9 tone)
  - Saddle Hill National System 434.800 (+5)
- **Singapore ham (591–592), SARTS:**
  - 9V1RS 145.625 (−0.6, 156.7 tone)
  - 9V1RMP 438.425 (−5, 156.7 tone)
- **New bank 15, DARWIN EMERGENCY:** 10, 16, 119, 160, 606, 705 and 735.
- **New banks 16–19:** HAM BRISBANE, HAM MELBOURNE, HAM NELSON and HAM SINGAPORE.

## Changed
- **Upgraded to verified, from ERSA 3 Sep 2026:**
  - 110–113 RAAF UHF. ERSA says they are retransmitted with 133.1, 125.2, 123.0 and 134.1.
  - 114 Emkaytee (YMKT), 115 Bathurst Island and 116 Delissaville.
  - 118 Darwin Fire 131.0 (RFFS, H24).
- **Other upgrades to verified:**
  - 257 CH82 (MRQ Jacobs Well).
  - 603 and 604 (WIA Jul 2026).
  - 710 CB 10 (the frequency is set by ACMA; its use is only a convention).
- **Renamed:**
  - 112 → RAAF DEPARTURE (the UHF pair of 123.0)
  - 157 → CH13 DARWIN TUGS (Darwin Port lists 12 and 13 as tugs)
  - 357 → CH67 VIC WEATHER (it clashed with 160 CH67 WEATHER)
- **160:** notes the broadcast times: 07:03 and 19:03 (Harbour Control), and 08:03 and 18:03 (Coast Radio Darwin).
- **Repeater settings:** 601, 602, 604, 606 and all the city repeaters now store duplex, offset and a tone (Tone = encode only, so receive is unaffected). 601, 602 and 604 use AMS (Fusion).
- **603 VK8RTE 70 cm:** left simplex, receive only, because its input is listed as 431.100 by DARC but 431.800 by WIA.

## Still unverified (N), 7 in total
- 252 CH20 TANGALOOMA (club site only).
- 401–404 Nelson air: aip.net.nz returned HTTP 500.
- 701 and 702 CB repeaters (a search summary of VKHam only).

## Not added
- **NOAA APT:** all NOAA satellites were decommissioned in Jun–Aug 2025.
- **Meteor LRPT:** a digital signal that the FT5D can't decode.
- **VOLMET:** HF SSB.
- **VK8VF beacons:** CW.
- **VK8RDA:** off air (WIA X).
- **VK8RDD and the D-STAR/DMR parts:** digital modes the radio can't decode.
- **NT police, fire and ambulance:** encrypted P25.
- **Redundant RAAF UHF (237.3, 265.3, 316.2):** retransmits of VHF frequencies already in the list.

## Encoding notes
- Offsets are BCD kHz in bytes 24–26 (600 → `000600`). This was confirmed from the radio's own Home records (144: 600, 430: 5000).
- The tone index is in byte 27 (CHIRP TONES; 123.0 = 18).
- Byte 5 holds tone_mode in the low nibble (1 = Tone) and digmode in bits 4–5 (1 = AMS).
- Duplex is bits 4–5 of byte 1.
- The original card had **no** Darwin repeater memories (601–604 were new in v3), so there was no existing repeater record to copy. The CHIRP ft1d layout was used, cross-checked against the radio-written Home records.
