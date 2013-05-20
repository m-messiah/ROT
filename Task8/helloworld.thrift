#!/usr/local/bin/thrift --gen py

namespace cpp Test

service HelloWorld {
  void ping(),
  i32 add(1:i32 a, 2:i32 b)
}
