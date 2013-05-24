#!/usr/bin/env escript

serve() ->
    receive 
        ls ->
            case file:list_dir(".") of
                {ok, Filenames} ->
                    lists:foreach(fun(Name) -> io:format("... ~s~n", [Name]) end, Filenames);
                {error, enoent} ->
                    io:format("The directory(~s) does not exist.~n", ["."]),
                    ng
            end;
        {cat, File} ->
            io:fwrite("<~s>~n", [File])
    end,
    serve().

client() ->
    server ! {cat, "hello"},
    timer:sleep(1000),
    client().

main(_) ->
    register(server, spawn(fun() -> serve() end)),
    server ! ls,
    spawn(fun() -> client() end),
    timer:sleep(50000).
