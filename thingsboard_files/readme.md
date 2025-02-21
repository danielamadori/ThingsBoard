# Export Commands
mkdir -p thingsboard_files

docker run --rm -v mytb-data:/data -v thingsboard_files:/backup busybox sh -c "tar czf /backup/mytb-data-backup.tgz -C /data ."
docker run --rm -v mytb-logs:/logs -v thingsboard_files:/backup busybox sh -c "tar czf /backup/mytb-logs-backup.tgz -C /logs ."

docker save -o thingsboard_files\thingsboard_image.tar thingsboard-image

# Import Commands
docker load -i thingsboard_files\thingsboard_image.tar

docker volume create mytb-data
docker volume create mytb-logs

docker run --rm -v mytb-data:/data -v thingsboard_files:/backup busybox sh -c "tar xzf /backup/mytb-data-backup.tgz -C /data"
docker run --rm -v mytb-logs:/logs -v thingsboard_files:/backup busybox sh -c "tar xzf /backup/mytb-logs-backup.tgz -C /logs"

docker run -d --name tb-test -p 1883:1883 -p 5683-5688:5683-5688/udp -p 7070:7070 -p 8080:9090 -v mytb-data-test:/data -v mytb-logs-test:/var/log/thingsboard thingsboard-image
