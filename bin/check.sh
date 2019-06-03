#!/bin/bash

for i in ../data/*.json; do all=`jq -r '.[] |[.Maximumprijs] |@csv' $i |wc -l`; noprice=`jq -r '.[] |[.Maximumprijs] |@csv' $i |grep -v '""' |wc -l`; echo "$i: $all $noprice"; done
