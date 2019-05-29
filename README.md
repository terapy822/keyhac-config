# keyhac-config

1. Open regedit
2. Move to `\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Keyboard Layout`
3. Create `Scancode Map` binary value
4. Edit value
```
00 00 00 00 00 00 00 00
02 00 00 00 38 00 3A 00
00 00 00 00
```
