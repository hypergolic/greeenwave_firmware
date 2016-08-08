NOTES:
YOU CAN BRICK YOUR STUFF VERY EASILY, PLAY CAREFUL.
Extracted rootfs + kernel is included in the rootfs.tar.bz2.
if you want to modifiy it, be sure you have experience with uboot/uboot scripts, otherwise, its easy to brick and a pain to recover, or if you're like me and bricked
it in the first 5 minutes of owning it, these files can help you recover it!

TODO:
Write this how to better. 4AM isnt a good time to be writing this stuff out.
Make a modified rootfs/squashfs image that doesnt try to upgrade opon every boot.

HOW TO:

Put the download folder and update.php files in a folder called "roxy", then use https.py to with a self signed .pem certificate (generate it with openssl or grab the .pem certs in the rootfs archive.)
then redirect update.greenwavereality.com and update.greenwavereality.eu via spoofing on a local dns server and firewall rules to block both hosts once updated, as if it
can contact the update serves again it will update its self, I just blocked all outgoing traffic from my lighting controller to the web.

after executing python https.py hold the sync button as the bridge boots up for about 10 seconds once it starts to blink and flash red on the sync button you should see this:

ERROR:root:Host: update.greenwavereality.com
Accept: */*
Content-Length: 99
Content-Type: application/x-www-form-urlencoded

ERROR:root:MiniFieldStorage('mac', 'D4:A9:28:02:07:54')
ERROR:root:MiniFieldStorage('secret', '14bd2088419a828ec0d8f336a7939fa1')
ERROR:root:MiniFieldStorage('project', 'Apollo3')
ERROR:root:MiniFieldStorage('current_version', '0.0.0')
10.1.1.45 - - [26/Apr/2016 11:59:49] "POST /roxy/update.php HTTP/1.1" 200 -
ERROR:root:Host: update.greenwavereality.com
Accept: */*
Content-Length: 110
Content-Type: application/x-www-form-urlencoded

10.1.1.45 - - [26/Apr/2016 11:59:49] "GET /roxy/download/1349139456/rootfs.bin HTTP/1.1" 200 -

then it will hopefully download the "updated" rootfs from your spoofed update server, downgrading it to the last version that had ssh enabled,
root/thinkgreen.  this works on all firmware versions even the ones with uboot input disabled :).

as I only have 1 unit to test it on, I've only tested downgrading my specific unit, so I'm not sure what other variables may be involved, but either way this will reply statically with a correct checksum and file URL.
