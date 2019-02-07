#!/bin/sh

######## only root privilege ##########


sudo python $ROOT_DIR/sniffer/http-sniffer.py -i en0
#linux
#sudo python ./sniffer/http-sniffer.py -i eth0