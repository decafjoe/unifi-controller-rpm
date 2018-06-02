
# Unifi Controller RPM Build Scripts

**Use at your own risk.** I published these because they're small,
they worked for me, and they might help someone else. This repo is not
"officially" supported/developed by me. (And _definitely_ not by
Ubiquiti! **I have no affiliation with Ubiquiti and they do not
endorse this project in any way.**)

That said, the following steps should produce a CentOS 6 RPM in
`rpmbuild/RPMS/x86_64/unifi-5.7.20-1.x86_64.rpm` (assuming you build
the 5.7.20 version and don't make any other changes to the spec file).

1. Download the controller software `.zip`. (This is left as an
   exercise to the reader but here's a hint that's not guaranteed to
   continue to work:
   http://dl-origin.ubnt.com/unifi/5.7.20/UniFi.unix.zip.)
2. Put the file in the same directory as this README, named
   `unifi-<VERSION>.zip`. For example, for 5.7.20 you'd name the file
   `unifi-5.7.20.zip`.
3. If the version you downloaded _is not 5.7.20_, open the `Makefile`
   and `unifi.spec`, search for 5.7.20, and update the file as
   appropriate.
4. Spin up a new CentOS 6 server in the cloud. Make sure you have
   key-based SSH access.
5. Run `make IP=<IP-OF-CLOUD-SERVER>`. This will install required
   tools on the server, rsync sources up, build the rpm, then rsync
   the rpm back down. (The script is almost shorter than the
   explanation. See `remote-build`.)
6. Spin down the cloud server. Admire for a moment that we live in a
   day and age where you got a fresh server spun up just for you,
   moved 75MB up and back (presumably through a stack of technologies
   that are amazing in and of themselves – internet _through the
   air wuuuuuut_?!), and spun it down just as easily. Seven clicks,
   fifteen minutes, and one sixth of one penny later, it's done. Wow.
