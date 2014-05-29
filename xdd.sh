#!/bin/bash

if [ $# -le 4 ]; then
  echo "Format: Workload(MB) Reqsize Filerange Thread RWratio"
  exit
fi  

WORKLOAD_SIZE=$1
REQ_SIZE=$2
FILE_RANGE=$3
THREAD=$4
RWRATIO=$5

FILE_RANGE=$((${FILE_RANGE}*1024*1024/${REQ_SIZE}))

LOGDIR="log"

LOGFILE="${LOGDIR}/xdd"

echo "xdd: Workload ${WORKLOAD_SIZE}MB, Reqsize ${REQ_SIZE}, File range ${FILE_RANGE}MB, Thread ${THREAD}, RWratio ${RWRATIO}"  

XDDEXEC=~/benchmarks/xdd/bin/xdd.linux

XDDFLAGS="-mbytes ${WORKLOAD_SIZE} -minall -verbose -noproclock -nomemlock -runtime 0 -reqsize 1 -blocksize ${REQ_SIZE} -timelimit 0 -seek random -seek range ${FILE_RANGE} -seek seed 333 -queuedepth ${THREAD} -passes 10"

${XDDEXEC} ${XDDFLAGS} -targets 1 /mnt/ramdisk/test1 -rwratio ${RWRATIO} | tee ${LOGFILE}

