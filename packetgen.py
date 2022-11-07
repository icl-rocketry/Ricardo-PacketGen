import argparse
import json
from pylibrnp import rnppacket
from pylibrnp.json_rnp_packet_parser import *
import sys


class PacketDescriptor(JsonRnpPacketParser):
    def __init__(self,packetJson):
        self.name = packetJson["packet_name"]
        self.type = packetJson['packet_type']
        self.filename = self.name.lower()
        super().__init__(packetJson['packet_descriptor'])
      

def generate_cpp(PacketDescriptorObj):
    cpp_header = ''
    cpp_source = ''
    try:
        with open("resources/cpp_header_boilerplate.txt",'r',encoding='utf-8') as file:
            cpp_header = file.read()
        with open('resources/cpp_source_boilerplate.txt','r',encoding='utf-8') as file:
            cpp_source = file.read()
    except FileNotFoundError as e:
        print("Reource Missing!")
        raise(e)

    subs={}
    subs['classname'] = PacketDescriptorObj.name
    subs['memberVariableList'] = '\n'.join([ "\t\t"+var_type + " " + var_name + ";" for var_name,var_type in PacketDescriptorObj.packet_structure.items()])
    subs['memberVariableClassPointerList'] = ',\n'.join(["\t\t\t\t&"+PacketDescriptorObj.name+"::"+var_name for var_name in PacketDescriptorObj.packet_structure.keys()])
    subs['filename'] = PacketDescriptorObj.filename
   
    cpp_header = cpp_header.format(**subs)
    cpp_source = cpp_source.format(**subs)

    with open(PacketDescriptorObj.filename+".h",'w',encoding='utf-8') as file:
        file.write(cpp_header)

    with open(PacketDescriptorObj.filename+".cpp",'w',encoding='utf-8') as file:
        file.write(cpp_source)
    

def generate_python(PacketDescriptorObj):
    py_file = ''
    try:
        with open("resources/py_boilerplate.txt",'r',encoding='utf-8') as file:
            py_file = file.read()
    except FileNotFoundError as e:
        print("Reource Missing!")
        raise(e)

    subs={}
    subs['classname'] = PacketDescriptorObj.name
    subs['memberVariableList'] = '\n'.join(['        self.'+var_name+' = 0' for var_name in PacketDescriptorObj.packet_structure.keys()]) #have to use spaces because python doesnt like tab character?/
    subs['filename'] = PacketDescriptorObj.filename
    subs['structstr'] = "'"+PacketDescriptorObj.struct_str+"'"
    py_file = py_file.format(**subs)

    with open(PacketDescriptorObj.filename+".py",'w',encoding='utf-8') as file:
        file.write(py_file)
    

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