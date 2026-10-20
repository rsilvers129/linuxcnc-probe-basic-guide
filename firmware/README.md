# Mesa 7I96S firmware

The card runs **7i96s_pktv3.bin**. It is the same as Mesa's default 7I96S configuration, except the RS-422 port on TB2-16..19 is a **PktUART** (packet UART) instead of Smart Serial. LinuxCNC's `hm2_modbus` driver needs the PktUART for Modbus RTU to the spindle VFD. Its man page recommends PktUART v3.

## Where to get it

From Mesa's support files for the 7I96S: the `7i96s.zip` download on mesanet.com. The copy used here came from the zip downloaded 2026-10-18. The binary isn't redistributed in this repository; get it from Mesa so you have the current version and its licence terms.

| File (from that zip) | SHA-256 |
|---|---|
| 7i96s_pktv3.bin (flashed) | `2b4a2066249fe2934a2ccb22c226c959dccf072d6647273e5b6696e488646c30` |
| 7i96s_d.bin (factory default, to go back) | `fd3b4cfc11fae6d887dfeb9de93eba0694684d40c60bc77ebf006f06cfb1695c` |
| 7i96sd_pktv2.bin (not used) | `b3a8b38515cc75054412fb9ab966a78b92b5c6caa3ab8ace23e04e7346bfdd06` |

If Mesa has since updated the file, the hash will differ. That's fine, as long as `readhmid` shows `PktUARTTX`/`PktUARTRX` on TB2-16..19 like `after-readhmid.txt`.

## Network

Jumpers **W4 down, W5 up** → the card uses the IP stored in its EEPROM, **10.10.10.10**. With both down it would use 192.168.1.121. The PC's dedicated Ethernet port is set to **10.10.10.1/24**, with no gateway (`system/NetworkManager/mesa-7i96s.nmconnection`).

## Flashing

```bash
mesaflash --device 7i96s --addr 10.10.10.10 --readhmid > before-readhmid.txt
mesaflash --device 7i96s --addr 10.10.10.10 --write 7i96s_pktv3.bin
mesaflash --device 7i96s --addr 10.10.10.10 --reload
mesaflash --device 7i96s --addr 10.10.10.10 --readhmid > after-readhmid.txt
```

Close LinuxCNC before flashing. To undo, write `7i96s_d.bin` the same way and `--reload`.

## Files here

- `before-readhmid.txt`: the card with factory firmware (Smart Serial on TB2).
- `after-readhmid.txt`: after flashing pktv3. `TB2-16,17` = PktUARTRX, `TB2-18,19` = PktUARTTX.
- `7i96s_pktv3.pin`, `7i96s_d.pin`: Mesa's pin files for the two configurations.
