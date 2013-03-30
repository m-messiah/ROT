#!/bin/bash
export HADOOP_HOME=/usr/local/hadoop
export JAVA_HOME=/usr/lib/jvm/java-7-openjdk-i386/jre/
export HADOOP_USER=hduser

case "$1" in 
    run)
        sudo -u ${HADOOP_USER} ${HADOOP_HOME}/bin/hadoop jar ${HADOOP_HOME}/contrib/streaming/hadoop-streaming.jar \
         -file mapper.py -mapper mapper.py -file reducer.py -reducer reducer.py \
         -input books/* -output books-output
        ;;
    show)
        sudo -u ${HADOOP_USER} ${HADOOP_HOME}/bin/hadoop fs -cat books-output/part-00000 | less
        ;;
    delete)
        sudo -u ${HADOOP_USER} ${HADOOP_HOME}/bin/hadoop fs -rmr books-output
        ;;
    copy)
        sudo -u ${HADOOP_USER} ${HADOOP_HOME}/bin/hadoop dfs -copyFromLocal books books 
        ;;
    *)
        echo "Usage $0 {run|show|delete|copy}" >&2
        exit 3
        ;;
esac

