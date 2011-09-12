#!/usr/bin/env python
def read_file_by_chunks(filename, chunksize=100):
	fileobject=open(filename, 'rb')
	while True:
		chunk = fileobject.read(chunksize)
		if not chunk:
			break
		yield chunk
	fileobject.close();

for line in read_file_by_chunks("list", 10):
	print line;

