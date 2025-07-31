# ThingsBoard

This project integrates environmental and healthcare sensors with ThingsBoard, an IoT platform, enabling data collection and publishing via MQTT protocol.

## Key Features

- **Telemetry Data Collection**: Gathers CPU usage, RAM, IP address, MAC address, active processes, battery level, boot time, and system load.
- **Healthcare Data (Simulated)**: Includes heart rate, SpO2, and a hardware-controlled alarm state via physical buttons and LED indicators.
- **Environmental Data**: Captures temperature, humidity, light (analog pin), and gas concentrations (MQ2, MQ9, MQ135 for smoke, CO/CH4/GPL, NH3/NOx).
- **Direct Sensor Management**: Supports sensors like DHT11, with timing-critical management using Microblaze and RTL code.
- **Publishing Data to ThingsBoard via MQTT**: Uses `TBDeviceMqttClient` to periodically send collected data.
- **Attribute Subscription and Requests**: Receives device attribute updates from ThingsBoard.

## Project Structure

- `ThingsBoards.ipynb`: Main notebook with logic for data collection, sensor management, and MQTT publishing.
- `publishing.py`, `subscription.py`, `request.py`: Scripts for MQTT interaction with ThingsBoard (publishing, subscribing, attribute requests).
- `thingsboard_files/readme.md`: Commands for exporting/importing Docker images and ThingsBoard data.
- Additional utility files for sensor management and hardware interfaces.

## Example: Start ThingsBoard via Docker

```sh
docker load -i thingsboard_files/thingsboard_image.tar

docker volume create mytb-data
docker volume create mytb-logs

docker run --rm -v mytb-data:/data -v thingsboard_files:/backup busybox sh -c "tar xzf /backup/mytb-data-backup.tgz -C /data"
docker run --rm -v mytb-logs:/logs -v thingsboard_files:/backup busybox sh -c "tar xzf /backup/mytb-logs-backup.tgz -C /logs"

docker run -d --name tb-test -p 1883:1883 -p 5683-5688:5683-5688/udp -p 7070:7070 -p 8080:9090 -v mytb-data-test:/data -v mytb-logs-test:/var/log/thingsboard thingsboard-image
```

## Requirements

- Python 3 (recommended >=3.10)
- Libraries: pynq, psutil, netifaces
- Docker for local ThingsBoard deployment

## Notes

This project is private and designed for testing on embedded devices (e.g., PYNQ Z2), integrating both physical and simulated sensors for IoT telemetry.
