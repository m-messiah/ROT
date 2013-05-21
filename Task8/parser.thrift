#!/usr/local/bin/thrift

namespace cpp Parser
namespace py Parser

service Parser {
  void ping(),
  i32 count(1:string page, 2:string tag)
}