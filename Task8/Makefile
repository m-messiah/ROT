.PHONY: build thrift client clean

build: thrift client

thrift: parser.thrift
	thrift --gen cpp parser.thrift
	thrift --gen py  parser.thrift

client: thrift client.cpp
	CFLAGS="-O3" g++ -DHAVE_INTTYPES_H -DHAVE_NETINET_IN_H -Wall -I/usr/local/include/thrift -lthrift -lcurl gen-cpp/Parser.cpp -o client.elf client.cpp

clean:
	rm -rf ./gen-*/ client
