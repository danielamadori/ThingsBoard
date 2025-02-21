import time
from tb_device_mqtt import TBDeviceMqttClient

THINGSBOARD_HOST = '127.0.0.1'
ACCESS_TOKEN = 'pg4iiosxgbkonzwpxpfb'

def on_attributes_change(client,result, exception):
	if exception is not None:
		print("Exception: " + str(exception))
	else:
		print(result)

def main():
	client = TBDeviceMqttClient(THINGSBOARD_HOST, username=ACCESS_TOKEN)
	client.connect()
	client.request_attributes(["cpu_usage","ram_usage"], callback=on_attributes_change)

	try:
		while True:
			time.sleep(1)
	except KeyboardInterrupt:
		print("Exiting...")
	finally:
		client.disconnect()

if __name__ == "__main__":
	main()