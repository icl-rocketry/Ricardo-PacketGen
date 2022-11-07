import struct

from pylibrnp.rnppacket import RnpPacket

class TelemetryPacket(RnpPacket):
	
    struct_str = '<ffffffffffffffffffiBfffffffffffffffHHffiIQhf'
    size = struct.calcsize(struct_str)
    packet_type = 0
   
    def __init__(self):
        self.pn = 0
        self.pe = 0
        self.pd = 0
        self.vn = 0
        self.ve = 0
        self.vd = 0
        self.an = 0
        self.ae = 0
        self.ad = 0
        self.roll = 0
        self.pitch = 0
        self.yaw = 0
        self.q0 = 0
        self.q1 = 0
        self.q2 = 0
        self.q3 = 0
        self.lat = 0
        self.lng = 0
        self.alt = 0
        self.sat = 0
        self.ax = 0
        self.ay = 0
        self.az = 0
        self.h_ax = 0
        self.h_ay = 0
        self.h_az = 0
        self.gx = 0
        self.gy = 0
        self.gz = 0
        self.mx = 0
        self.my = 0
        self.mz = 0
        self.baro_temp = 0
        self.baro_press = 0
        self.baro_alt = 0
        self.batt_voltage = 0
        self.batt_percent = 0
        self.launch_lat = 0
        self.launch_lng = 0
        self.launch_alt = 0
        self.system_status = 0
        self.system_time = 0
        self.rssi = 0
        self.snr = 0
        super().__init__(list(vars(self).keys()),TelemetryPacket.struct_str,TelemetryPacket.size,TelemetryPacket.packet_type)

    def __str__(self):
        header_str = self.header.__str__() + '\ns'
        return header_str