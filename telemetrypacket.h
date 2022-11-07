#pragma once

#include "rnp_packet.h"
#include "rnp_serializer.h"


class TelemetryPacket : public RnpPacket{
    private:
    //serializer framework
        static constexpr auto getSerializer()
        {
            auto ret = RnpSerializer(
				&TelemetryPacket::pn,
				&TelemetryPacket::pe,
				&TelemetryPacket::pd,
				&TelemetryPacket::vn,
				&TelemetryPacket::ve,
				&TelemetryPacket::vd,
				&TelemetryPacket::an,
				&TelemetryPacket::ae,
				&TelemetryPacket::ad,
				&TelemetryPacket::roll,
				&TelemetryPacket::pitch,
				&TelemetryPacket::yaw,
				&TelemetryPacket::q0,
				&TelemetryPacket::q1,
				&TelemetryPacket::q2,
				&TelemetryPacket::q3,
				&TelemetryPacket::lat,
				&TelemetryPacket::lng,
				&TelemetryPacket::alt,
				&TelemetryPacket::sat,
				&TelemetryPacket::ax,
				&TelemetryPacket::ay,
				&TelemetryPacket::az,
				&TelemetryPacket::h_ax,
				&TelemetryPacket::h_ay,
				&TelemetryPacket::h_az,
				&TelemetryPacket::gx,
				&TelemetryPacket::gy,
				&TelemetryPacket::gz,
				&TelemetryPacket::mx,
				&TelemetryPacket::my,
				&TelemetryPacket::mz,
				&TelemetryPacket::baro_temp,
				&TelemetryPacket::baro_press,
				&TelemetryPacket::baro_alt,
				&TelemetryPacket::batt_voltage,
				&TelemetryPacket::batt_percent,
				&TelemetryPacket::launch_lat,
				&TelemetryPacket::launch_lng,
				&TelemetryPacket::launch_alt,
				&TelemetryPacket::system_status,
				&TelemetryPacket::system_time,
				&TelemetryPacket::rssi,
				&TelemetryPacket::snr
               
            );
            return ret;
        }
        
    public:
        ~TelemetryPacket();

        TelemetryPacket();
        /**
         * @brief Deserialize Packet
         * 
         * @param data 
         */
        TelemetryPacket (const RnpPacketSerialized& packet);

        /**
         * @brief Serialize Packet
         * 
         * @param buf 
         */
        void serialize(std::vector<uint8_t>& buf) override;

		float pn;
		float pe;
		float pd;
		float vn;
		float ve;
		float vd;
		float an;
		float ae;
		float ad;
		float roll;
		float pitch;
		float yaw;
		float q0;
		float q1;
		float q2;
		float q3;
		float lat;
		float lng;
		int alt;
		uint8_t sat;
		float ax;
		float ay;
		float az;
		float h_ax;
		float h_ay;
		float h_az;
		float gx;
		float gy;
		float gz;
		float mx;
		float my;
		float mz;
		float baro_temp;
		float baro_press;
		float baro_alt;
		uint16_t batt_voltage;
		uint16_t batt_percent;
		float launch_lat;
		float launch_lng;
		int launch_alt;
		uint32_t system_status;
		uint64_t system_time;
		int16_t rssi;
		float snr;

        static constexpr size_t size(){
            return getSerializer().member_size();
        }

};


