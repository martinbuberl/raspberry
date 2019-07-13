# raspberry

### Hardware

- Raspberry Pi 3 Model B
- SanDisk Extreme Pro Micro SD 32GB

### Some Pi wisdom

```
sudo raspi-config
sudo poweroff
sudo reboot
```

# rsync files via SSH

`rsync -avz -e ssh src/pi pi@192.168.86.40:src`

# Mount file system via SSHFS

SSHFS allows you to mount the Raspberry Pi's file system on your local machine.

First, install sshfs on your Mac using `$ brew install sshfs`.

Mount the Raspberry Pi's file system to your local directory `pi`:
`sshfs pi@192.168.86.40: pi`

Unmount it via:
`umount pi`
Remove folder:
`rmdir pi`

Troubleshooting
```
pgrep -lf sshfs
kill -9 <process_id>
```
