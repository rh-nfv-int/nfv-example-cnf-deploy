from trex_stl_lib.api import *
 
class STLS1(object):
 
    def __init__ (self):
        self.fsize  =64; # the size of the packet
 
 
    def create_stream (self):
 
        # Create base packet and pad it to size
        size = self.fsize - 4; # HW will add 4 bytes ethernet FCS
        base_pkt =  Ether()/IP(src="16.0.0.1",dst="48.0.0.1")/UDP(dport=32768,sport=1025)
        base_pkt1 =  Ether()/IP(src="26.0.0.1",dst="58.0.0.1")/UDP(dport=22768,sport=2025)
        base_pkt2 =  Ether()/IP(src="16.0.0.3",dst="48.0.0.1")/UDP(dport=12,sport=1025)
        # pad = max(0, size - len(base_pkt)) * 'x'
        pad = (size- len(base_pkt)) * 'x'
        vm = STLScVmRaw( [ STLVmFlowVar(name="ip_src",
                                              min_value="16.0.0.1",
                                              max_value="16.0.0.1",
                                              size=4, op="inc"),
                           STLVmFlowVar(name="src_port",
                                              min_value=1025,
                                              max_value=1025,
                                              size=2, op="inc"),
 
                           STLVmWrFlowVar(fv_name="ip_src", pkt_offset= "IP.src" ),
                           STLVmWrFlowVar(fv_name="src_port", pkt_offset= "UDP.sport"),
 
                           STLVmFlowVar(name="ip_dst",
                                              min_value="48.0.0.1",
                                              max_value="48.0.0.1",
                                              size=4, op="inc"),
                           STLVmFlowVar(name="dst_port",
                                              min_value=32768,
                                              max_value=32768,
                                              size=2, op="inc"),
 
                           STLVmWrFlowVar(fv_name="ip_dst", pkt_offset= "IP.dst" ),
                           STLVmWrFlowVar(fv_name="dst_port", pkt_offset= "UDP.dport"),
                           STLVmFixIpv4(offset = "IP"), # fix checksum
 
                          ]
                       )
 
 
        vm1 = STLScVmRaw( [ STLVmFlowVar(name="ip_src",
                                              min_value="26.0.0.1",
                                              max_value="26.0.0.1",
                                              size=4, op="inc"),
                           STLVmFlowVar(name="src_port",
                                              min_value=2025,
                                              max_value=2025,
                                              size=2, op="inc"),
 
                           STLVmWrFlowVar(fv_name="ip_src", pkt_offset= "IP.src" ),
                           STLVmWrFlowVar(fv_name="src_port", pkt_offset= "UDP.sport"),
 
                           STLVmFlowVar(name="ip_dst",
                                              min_value="58.0.0.1",
                                              max_value="58.0.0.1",
                                              size=4, op="inc"),
                           STLVmFlowVar(name="dst_port",
                                              min_value=22768,
                                              max_value=22768,
                                              size=2, op="inc"),
 
                           STLVmWrFlowVar(fv_name="ip_dst", pkt_offset= "IP.dst" ),
                           STLVmWrFlowVar(fv_name="dst_port", pkt_offset= "UDP.dport"),
                           STLVmFixIpv4(offset = "IP"), # fix checksum
 
                          ]
                       )
 
        return STLProfile( [ STLStream(  # start in delay in usec
                                        packet = STLPktBuilder(pkt = base_pkt/pad,vm = vm),
                                        mode = STLTXCont( ),
                                        ),
                             STLStream(
                                        packet  = STLPktBuilder(pkt = base_pkt1/pad,vm = vm1),
                                        mode    = STLTXCont( ),
                                        )
 
                            ]).get_streams()
 
 
    def get_streams (self, direction = 0, **kwargs):
        # create 1 stream
        return self.create_stream()
 
 
# dynamic load - used for trex console or simulator
def register():
    return STLS1()
