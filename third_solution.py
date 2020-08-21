packet_data = list(map(int,input().split()))
buffer_size = packet_data[0]
number_of_packets = packet_data[1]

all_packet = []
for i in range(number_of_packets):
    packet = list(map(int,input().split()))
    all_packet.append(packet)

time = []
for i in all_packet:
    if i[0] not in time:
        print(i[0],end=" ")
        time.append(i[0])
    else:
        print(-1)