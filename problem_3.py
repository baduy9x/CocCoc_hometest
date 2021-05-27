import sys

# assume that sample is a very large file (Terabyte of data).
# read by batch (for example 1000 lines), sort by batch then write to temp files.

path_to_sample_file = sys.argv[1]

sample = open(path_to_sample_file, 'r')
batch_size = 1000
obj_id_line_map = {}
count = 0
file_prefix = 0
while True:
    line = sample.readline()
    if line is None or line == '':
        break
    count += 1
    object_id = int(line.split('\t')[0])
    obj_id_line_map[object_id] = line
    if count == batch_size:
        sorted_key = sorted(obj_id_line_map.keys())
        with open("{}.temp".format(file_prefix), "w") as temp_file:
            for item in sorted_key:
                temp_file.write(obj_id_line_map[item])
        file_prefix += 1
        count = 0
        obj_id_line_map = {}

sorted_key = sorted(obj_id_line_map.keys())
with open("{}.temp".format(file_prefix), "w") as temp_file:
    for item in sorted_key:
        temp_file.write(obj_id_line_map[item])


# merge sorted files using priority queue
import heapq 

all_temp_file = [open("{}.temp".format(i), "r") for i in range(file_prefix)]
priority_queue = []
for item in all_temp_file:
    current_line = item.readline()
    object_id = int(current_line.split('\t')[0])
    priority_queue.append((object_id, current_line, item))

heapq.heapify(priority_queue)
with open("output.temp", "w") as output:
    while priority_queue:
        item, line, file_stream = heapq.heappop(priority_queue)
        output.write(line)
        new_line = file_stream.readline()
        if new_line == '' or new_line is None:
            continue
        else:
            new_object_id = int(new_line.split('\t')[0])
            heapq.heappush(priority_queue, (new_object_id, new_line, file_stream))

        







    
