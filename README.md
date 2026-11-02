# FT5D Radio

Channel plan and SD card files for my Yaesu FT5D.

## Restore the radio from these files
1. Copy `sd_card/current_v3/BACKUP.dat` to the SD card as `FT5D/BACKUP/BACKUP.dat`, and `sd_card/current_v3/MEMORY.dat` as `FT5D_MEMORY-CH/MEMORY.dat`.
2. In the radio: press and hold F MENU > SD CARD > 1 BACKUP > Read from SD > F MENU > OK > OK.

## Numbering
- 10 Air Emergency 121.5, 16 Ch16 Distress
- 20-30 broadcast radio
- 100s Darwin, 200s Brisbane, 300s Melbourne, 400s Nelson, 500s Singapore (air x01+, marine x51+, ham repeaters x91+)
- 600s Darwin ham, satellites; 7xx UHF CB (xx = CB channel)

## Contents
- `FT5D_channel_plan_v3_final.csv`: every memory with frequency, mode, offset, tone, bank, source and verification
- `changes.md`: what changed in v3
- `sd_card/current_v3/`: card files written 2 Nov 2026 13:25 ACST
- `sd_card/original_2026-11-02/`: the card as it was before any edits
- `scripts/`: plan, generator and verifier (format follows CHIRP's ft1d driver)
