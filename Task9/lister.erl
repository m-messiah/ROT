#!/usr/bin/env escript

serve() ->
    receive 
        File ->
            io:fwrite("<~s>~n", [File]),
            serve();
        ls ->
            io:fwrite(">ls~n", []),
            serve()
    end.

client() ->
    server ! "hello",
    timer:sleep(1000),
    client().

main(_) ->
    register(server, spawn(fun() -> serve() end)),
    server ! ls,
    spawn(fun() -> client() end),
    timer:sleep(50000).
