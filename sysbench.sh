#!/bin/bash

sysbench --test=fileio --file-num=1 --file-total-size=512M --file-block-size=4096 --file-test-mode=seqrd --file-fsync-freq=0 --file-fsync-end=off run
