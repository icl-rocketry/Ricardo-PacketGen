import argparse
import json
from pylibrnp import rnppacket,
from pylibrnp.json_rnp_packet_parser import *
import sys


class PacketDescriptor(JsonRnpPacketParser):
    def __init__(self,packetJson):
        self.name = packetJson["packet_name"]
        self.type = packetJson['packet_type']
        super(JsonRnpPacketParser,self).__init__(packetJson)


def generate_cpp():
    pass

def generate_python():
    pass

# Argument Parsing
ap = argparse.ArgumentParser()
ap.add_argument("-c", "--packet_descriptor_file", required=True, help="Filepath to packet descriptor", type=str)
ap.add_argument("--cpp", required=False, help="Generate Cpp code", action='store_true')
ap.add_argument("--py", required=False, help="Generate py code", action='store_true')

args = vars(ap.parse_args())

if __name__ == "__main__":


    packetJson = {}
    try:
        with open(args["packet_descriptor_file"],'r',encoding='utf-8') as file:
        
            packetJson = json.load(file)
            
    except FileNotFoundError as e:
        print('Bad File Provided!')
        raise(e) 

    packet_descriptor = PacketDescriptor(packetJson)

    if not args['cpp'] and not args['py']:
        print("No generation option selected, Exiting!")
        sys.exit(0)
    
    if args['cpp']:
        generate_cpp(packet_descriptor)
    
    if args['py']:
        generate_python(packet_descriptor)