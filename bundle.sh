#!/bin/bash
#
#  bundle.sh
#

dest=cjkdata-$(date +%Y-%m-%d)-$(git rev-parse --short HEAD).tgz
tar cfz $dest cjkdata
echo $dest
s3cmd put -P $dest s3://files.gakusha.info/
