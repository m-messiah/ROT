#!/usr/bin/env escript

serve() ->
    receive 
        ls ->
            case file:list_dir(".") of
                {ok, Filenames} ->
                    client ! {list, Filenames};
                {error, enoent} ->
                    io:format("The directory(~s) does not exist.~n", ["."]),
                    ng
            end;
        {cat, File} ->
            {_, Content} = file:read_file(File),
            client ! {file, File, Content}
    end,
    serve().

getfile() ->
    receive
        {list, Filenames} ->
            %lists:foreach(fun(Name) -> io:format("... ~s~n", [Name]) end, Filenames);
            delivery ! {cat, lists:nth(random:uniform(length(Filenames)), Filenames)};
        {file, File, Content} ->
            io:fwrite("~s: ~w bytes~n", [File, byte_size(Content)]),
            delivery ! ls
    end,
    timer:sleep(1000),
    getfile().

main(_) ->
    register(delivery, spawn(fun() -> serve() end)),
    register(client, spawn(fun() -> getfile() end)),
    delivery ! ls,
    timer:sleep(50000).
