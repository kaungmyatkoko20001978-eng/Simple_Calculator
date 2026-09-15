echo "1"
echo "2"
#################
#Author => Kaung Myat Ko Ko
#Date => 19.8.2026
#Version : 1.0
#Language => Bash
#################

set -x
echo "Number of processors: $(nproc)"
echo "Memory usage:"
free -h
echo "Disk usage:"
df -h
echo "Current directory: $(pwd)"
echo "List of files: $(ls -l)"
echo "Meta data of files: $(ls -ltr)"
echo "Live view of system health: "
top
