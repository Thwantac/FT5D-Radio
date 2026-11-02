# FT5D channel plan: other cities and other bands (draft, 2 Nov 2026)

These files are a plan only. Nothing has been written to the SD card or the Mac.
- `channel_plan.csv` has 113 rows: 105 new memories, plus 8 rows that add the existing memory 32 (AIR EMERGENCY 121.5) and memory 49 (CH16 DISTRESS) to the new banks.
- The FT5D advanced manual (p. 17) confirms that one memory can be registered in two or more banks, so 121.5 and Ch 16 don't need duplicate memories.

## Radio limits (from the manuals in /workspace/radio)
- **Receive range:**
  - A-band: 520 kHz – 999.995 MHz. "USA Cellular Blocked" applies to the US model only.
  - B-band: 108 – 579.995 MHz.
  - So all of these are fine: airband 108–137 MHz, 137–174 MHz (marine, 2 m), 222–420 MHz (Seletar UHF 270.4), 430 MHz, and UHF CB 476–477 MHz.
  - The AM broadcast band (657 kHz) is **A-band only**.
- **Limits:** memory tags and bank names are max 16 characters; 24 banks; max 100 memories per bank; 900 memories.
- **No SSB:** HF VOLMET (6676/11387 kHz USB, listed in the ERSA) is **not receivable**.
- **FM narrow:** "NARROW" is a transmit deviation setting only. Narrow 12.5 kHz signals (UHF CB) still play, just a little quieter.
- **Modes:** AM for airband, including 270.4. FM for everything else. For the Fusion repeaters (VK8RTE 2 m, VK8RPD, VK8RZZ), use AMS so the radio also decodes C4FM digital.

## Naming scheme
- **Aviation:** `<CITY> <FUNCTION>`, using IATA city codes (BNE, MEL, NSN = Nelson, SIN). Secondary airports use their own name (ARCHER, ESSENDON, MOORABBIN, SELETAR).
- **Marine:** `<CITY> CHnn <SHORT>`, e.g. `SIN CH14 VTIS C`. Darwin marine keeps its existing `CHnn ...` names.
- **Ham:** callsign + place. **CB:** `CBnn ...`.
- **Name clash:** existing memory 29 is "BNE CENTRE" (Brisbane Centre heard in Darwin, 118.150). The new Brisbane centre channels are named `BNE CENTRE 121.2` / `BNE CENTRE 125.7`. Suggest renaming 29 to `DRW BNE CENTRE` for clarity (optional).

## Memory and bank allocation
| Bank | Name | Memories | New | + existing |
|---|---|---|---|---|
| 3 | FM RADIO (suggest renaming to RADIO DRW) | 7 | 1 | – |
| 4 | AIR BNE | 100-123 | 19 | 32 |
| 5 | MARINE BNE | 150-156 | 7 | 49 |
| 6 | AIR MEL | 200-218 | 15 | 32 |
| 7 | MARINE MEL | 250-256 | 7 | 49 |
| 8 | AIR NSN | 300-303 | 4 | 32 |
| 9 | MARINE NSN | 350-353 | 4 | 49 |
| 10 | AIR SIN | 400-424 | 21 | 32 |
| 11 | MARINE SIN | 450-462 | 13 | 49 |
| 12 | HAM DRW | 500-504 | 5 | – |
| 13 | SAT APRS | 520-522 | 3 | – |
| 14 | UHF CB | 600-605 | 6 | – |

The gaps in each block leave room to add more. Keep SAT APRS out of everyday scanning, because APRS data bursts would stop the scan every few seconds.

## Sources (fetched 2 Nov 2026 unless stated)
- **Airservices ERSA, effective 03 SEP 2026:** FAC YBBN, YBAF, YMML, YMEN, YMMB (airservicesaustralia.com/aip/current/ersa/FAC_xxxx_03SEP2026.pdf). This is the current edition on the AIP page.
- **Singapore eAIP (CAAS), effective 29 OCT 2026:** AD 2.18 for WSSS and WSSL (aim-sg.caas.gov.sg). This is the current edition. It is unchanged from 03 SEP 2026 for these items.
- **Nelson NZNS:** aip.net.nz returned HTTP 500 / terms page only, so the current edition was **not** checked.
  - Tower 127.4, ATIS 129.1 and Delivery 123.3 come from AIP NZ chart extracts (NZNS AD 2-45/33/62, effective 2008-2019) and pilots.nz (reviewed Sep 2026). They are consistent, but marked N.
  - Christchurch Control 123.7 is from SkyVector/VATNZ only.
- **MSQ Brisbane Port Procedures (Oct 2024) and the msq.qld.gov.au VTS page:** Brisbane VTS on Ch 12 (and 16).
- **mrq.qld.gov.au, MRQ Sandgate:** monitors 67, 73, 81, 21 and 16. Ch 82 and Ch 20 (Tangalooma) come from sequestradio.org only, so they are marked N.
- **Ports Victoria Port Information Guide, 6th ed Dec 2025:** Ch 12 VTS, 09/10/13 pilots, 06 port ops, 67 weather.
  - Port Phillip Sea Pilots guide (Oct 2023): Hastings VTS Ch 14.
- **Port Nelson Port Passage Plan v3 (Mar 2025):** Nelson Harbour Radio Ch 12.
  - Maritime NZ Radio Handbook (May 2025): Ch 67/68 working channels and broadcast times.
  - Coastguard NZ Nowcasting map (Oct 2024): Nelson Ch 79 (2079).
- **MPA Singapore:** "Vessels arriving in Singapore" VHF table and STRAITREP operational areas.
- **Amateur:**
  - Darwin ARC repeater page (vk8da.au).
  - WIA Repeater Directory updated 25/09/2025, the newest one found.
  - WIA 2 m band plan (29/07/2015): 146.500 calling, 145.175 APRS.
  - ARISS: ISS 145.800 voice, 145.825 packet.
- **UHF CB:**
  - ACMA CB class licence page (updated 1 Oct 2025): band 476.425-477.4125, Ch 5/35 emergency, 22/23 data-only.
  - Ch 11/18/40/10 uses are conventions (Radio Rescue), not ACMA rules.
- **ABC NT frequency data:** Darwin ABC RN 657 kHz AM. This is the only Darwin AM station ABC lists. ABC local radio is 105.7 FM.

## Frequency derivations
- **Duplex marine channels:** the plan stores the **shore/repeater output** side, i.e. what you hear from the station (ITU RR Appendix 18):
  - Ch 05 = 160.850, Ch 18 = 161.500, Ch 20 = 161.600, Ch 21 = 161.650, Ch 22 = 161.700
  - Ch 81 = 161.675, Ch 82 = 161.725
- **NZ "2079":** simplex 156.975 (ITU four-digit convention, per Coastguard NZ).

## Unverified or conflicting (verified = N, or worth knowing)
1. **Nelson aviation (all 4):** the official current AIP NZ was not reachable. Re-check at aip.net.nz before relying on these.
2. **BNE CH82 RPT / BNE CH20 RPT:** from a club site only.
3. **VK8RTE 438.100:** listed as TESTING (D-STAR/FM). Its input is 431.100 (DARC, -7 MHz) vs 431.800 (WIA). The receive frequency isn't affected.
4. **VK8RZZ 147.375 (Wagait Beach):** listed in the WIA Fusion section only, not on the DARC page.
5. **CB10 4WD CLUBS:** a convention only.
6. **Omitted:**
   - VK8RDA 146.900: WIA status X, off air since 9/25.
   - VK8RDD 438.800: DMR, which the FT5D can't decode.
   - Old VK8RAD listings: no longer current.
7. **Ports Victoria PIG:** lists "Channel 67 156.7 MHz". That's a typo; Ch 67 is 156.375 (156.700 is Ch 14). It also gives forecast times as 0648 and 1858 in one place, but 06:48 and 18:48 EST elsewhere.
8. **MPA:** lists Ch 07 (Port Marine Safety) as "156.450 160.950". It isn't included, to avoid the ambiguity.
   - Secondary Singapore Arrival/Departure/Approach frequencies are also left out: 119.4/119.55, 133.0/132.15, 124.6/126.3.
9. **Brisbane ATIS:** also broadcast on the BN VOR 113.2, and Melbourne ATIS on the ML VOR 114.1. The plan uses the VHF COM frequencies 125.5 and 118.0.
10. **NT Police/Fire/Ambulance:** use a Motorola P25 Phase 2 digital trunked network, encrypted (govmarket contract notices; Wikipedia "Government radio networks in Australia"). **Not receivable** on the FT5D; no channels included.
11. **"DRW FIRE" 131.000 (existing memory 31):** still not in the ERSA.
