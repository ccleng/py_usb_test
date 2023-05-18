import sys
import usb.core
import usb.util


# find our device
dev = usb.core.find(idVendor=0x1235, idProduct=0x0002)

print(dev)

# was it found?
if dev is None:
    raise ValueError('Device not found')


for cfg in dev:
    sys.stdout.write(str(cfg.bConfigurationValue) + '\n')
    for intf in cfg:
        sys.stdout.write('\t' + \
                         str(intf.bInterfaceNumber) + \
                         ',' + \
                         str(intf.bAlternateSetting) + \
                         '\n')
        for ep in intf:
            sys.stdout.write('\t\t' + \
                             str(ep.bEndpointAddress) + \
                             '\n')


dev.set_configuration()
try:
    dev.set_interface_altsetting(interface = 4, alternate_setting = 0)
except USBError:
    pass

msg=[0xa5,0x5a,0xfc,0x02,0x30,0x00,0x16,0x00]
dev.ctrl_transfer(0x21, 0x09, 0x200, 0x3, msg)
ret = dev.ctrl_transfer(0xa1, 0x01, 0x100, 0x3, 0x7)

for i in ret:
    print("0x%02x" %i, end=" ")
print()


