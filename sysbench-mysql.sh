#!/bin/bash

sysbench --test=oltp --oltp-table-size=100000 --mysql-db=dbtest --mysql-user=root --db-driver=mysql prepare
sleep 1
sysbench --test=oltp --oltp-table-size=100000 --mysql-db=dbtest --mysql-user=root --db-driver=mysql run
