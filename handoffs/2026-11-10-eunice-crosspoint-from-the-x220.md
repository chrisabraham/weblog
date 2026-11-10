# Handoff — CrossPoint from the X220 (Nov 10, 2026, Eunice)

New post: src/posts/2026-11-10-crosspoint-from-the-x220.html — "Chris, Flash CrossPoint from the X220", byline eunice, 1,866 words. Doodle: src/media/crosspoint-flash.svg (original amber-ink SVG, Eunice).

Research, primary sources only (all read Nov 10, 2026):
- CrossPoint repo README (github.com/crosspoint-reader/crosspoint-reader): ESP32-C3 in X3/X4; web installer at crosspointreader.com/#flash-tools (recommended; wake/unlock device, select device, choose release; custom .bin supported; same flasher reverts to official firmware); esptool route verbatim (pip install esptool; find port via dmesg on Linux; esptool.py --chip esp32c3 --port /dev/ttyACM0 --baud 921600 write_flash 0x10000 firmware.bin); USB-locked units (third-party stores, e.g. AliExpress; xteink.com units not locked; try cable/port/browser before assuming locked); unlocker supports ONLY CrossPoint and CrossInk, anything else may permanently brick or strand; OTA update checks/installs from GitHub releases.
- crosspointreader.com/unlock ("Other Ways to Install CrossPoint"): SD route recommended for X3/X4 even on stock — download update.bin, copy to card root, plug USB into power, hold Power+Up (top-left button on X3), OEM bootloader flashes; same file for X3 and X4; check the approved/flagged list before flashing, unapproved firmware can permanently brick; OTA Unlocker for stock firmware that refuses SD flashing; X4 Pro note (Licorice OS / OTA Unlocker).
- Approved/flagged list: The Brick Club (brickclub.pages.dev), linked from the official /unlock page; a volunteer JS database (rows do not render in a text fetch; the article links it and prints the /unlock page's own framing, no invented rows).
- Liliputing, May 2, 2026 (read in full): blocks reported on units bought from Chinese retailers (Taobao); Xteink's stated reasons (poor optimization, crashes, screen damage); Xteink statement that overseas versions bought via the official website are not restricted.
- Supporting community sources for small mechanics, flagged as guides in the text where used: ongk.dev install guide and PocketInk (flash-twice-from-stock warning, Reset then hold Power 3–5 s to boot, sleeping device invisible as serial port, charge-only cables invisible); crosspoint.kr install guide (Settings → System → SD Card Firmware Update; wireless Check for Updates).
- Linux serial material: /dev/ttyACM* naming is from the README's own command; dialout group fix (sudo usermod -aG dialout $USER + re-login) is standard Debian/Mint practice. No BOOT-button step is printed for USB flashing because no primary source calls for one on X3/X4; the only button combo in the sources is Power+Up for the SD route.
- Landscape names verified before printing: Inx (CrossPoint fork, readme.club firmware page; PocketInk directory) and BookFusion Ink (bookfusion.ink, public beta, independent codebase, account-based). CrossInk per the README/unlocker warning. "inkMOD" from the catalyst paste could NOT be verified against any source found and is not printed.

Caveats for the desk:
- The header `prompt:` line is a faithful one-line rendering of the relayed commission; no verbatim dictation for this piece was supplied to this agent.
- Word count 1,866 (the brief set no range for this piece).

Binary debts (desk web-UI upload batch): docs/audio/crosspoint-from-the-x220.mp3 and src/audio/crosspoint-from-the-x220.mp3 (6,425,125 bytes each); docs/cards/2026-11-crosspoint-from-the-x220.png (44,319 bytes). The doodle SVG is text and was pushed with the article.
