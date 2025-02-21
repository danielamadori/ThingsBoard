import time

from ambiental_sensors import collect_ambiental_data
from healthcare_sensors import collect_healthcare_data
from io import button_idle
from telemetry import collect_telemetry_data
from tb_device_mqtt import TBDeviceMqttClient, TBPublishInfo

THINGSBOARD_HOST = '127.0.0.1'
ACCESS_TOKEN = 'pg4iiosxgbkonzwpxpfb'

last_telemetry_time = time.time()
TELEMETRY_INTERVAL = 1  # Seconds

def mqtt_pub_idle(client: TBDeviceMqttClient):
	global last_telemetry_time
	current_time = time.time()
	if current_time - last_telemetry_time >= TELEMETRY_INTERVAL:
		telemetry_data = collect_telemetry_data()
		telemetry_data.update(collect_healthcare_data())
		telemetry_data.update(collect_ambiental_data())

		result = client.send_telemetry(telemetry_data)
		success = result.get() == TBPublishInfo.TB_ERR_SUCCESS
		if not success:
			print("Failed to send telemetry data.")
		last_telemetry_time = current_time


def main():
	client = TBDeviceMqttClient(THINGSBOARD_HOST, username=ACCESS_TOKEN)
	client.connect()
	try:
		while True:
			button_idle()
			mqtt_pub_idle(client)
			time.sleep(0.01)
	except KeyboardInterrupt:
		print("Exiting...")
	finally:
		client.disconnect()

if __name__ == "__main__":
	main()
