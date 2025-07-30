# PfSenseAliasImporter
Mass import PfSense aliases from a hosts file, e.g. StevenBlack's lists, strip out the unnecessary stuff so we can import easily

Usage:

```
usage: importer.py [-h] --hosts HOSTS [-o OUT]

Script to append hosts to an exported configuration of PfSense aliases

options:
  -h, --help         show this help message and exit
  --hosts HOSTS      Path to a hosts file
  -o OUT, --out OUT  Output path name
```

Then Firewall > Aliases > Import
