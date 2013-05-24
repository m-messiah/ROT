#include "./gen-cpp/Parser.h"
#include <iostream>
#include <curl/curl.h>
#include <thrift/transport/TSocket.h>
#include <thrift/transport/TBufferTransports.h>
#include <thrift/protocol/TBinaryProtocol.h>

using namespace apache::thrift;
using namespace apache::thrift::protocol;
using namespace apache::thrift::transport;
using namespace std;
using namespace Parser;


int somecallback(char * data, int size, int nmemb, std::string* buffer){
       buffer->append(std::string(data));
       return (size* nmemb);
    }


int main(int argc, char **argv) {
    if (argc < 3) {
        cout << "Using: " << argv[0] << " <URL> <tag>" << endl;
        return 1;
    }
    string buffer;
    CURL * curl = curl_easy_init();
    curl_easy_setopt(curl, CURLOPT_URL, argv[1]);
    curl_easy_setopt(curl, CURLOPT_FOLLOWLOCATION, 1);
    curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, somecallback);
    curl_easy_setopt(curl, CURLOPT_WRITEDATA, &buffer);
    curl_easy_perform(curl);
    
    string tag = argv[2];

    boost::shared_ptr<TSocket> socket(new TSocket("localhost", 9090));
    boost::shared_ptr<TTransport> transport(new TBufferedTransport(socket));
    boost::shared_ptr<TProtocol> protocol(new TBinaryProtocol(transport));

    ParserClient client(protocol);
    transport->open();
    //client.ping();
    int c = client.count(buffer, tag);
    cout << tag << " = " << c << endl;
    transport->close();
    return 0;
}
