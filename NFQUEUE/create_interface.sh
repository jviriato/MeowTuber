#!/bin/bash

ifconfig enp0s3:0 10.0.2.16
ifconfig enp0s3:0 netmask 255.255.255.0

ifconfig enp0s3:1 10.0.2.17
ifconfig enp0s3:1 netmask 255.255.255.0
