#!/bin/bash
export HADOOP_HOME=/usr/local/hadoop
export JAVA_HOME=/usr/lib/jvm/java-7-openjdk-i386/jre/
export HADOOP_USER=hduser

case "$1" in 
    run)
        sudo -u ${HADOOP_USER} ${HADOOP_HOME}/bin/hadoop jar ${HADOOP_HOME}/contrib/streaming/hadoop-streaming.jar \
         -file mapper${2}.py -mapper mapper${2}.py -file reducer.py -reducer reducer.py \
         -input books/* -output books-output-$2
        ;;
    show)
        sudo -u ${HADOOP_USER} ${HADOOP_HOME}/bin/hadoop fs -cat books-output-$2/part-00000
        ;;
    delete)
        sudo -u ${HADOOP_USER} ${HADOOP_HOME}/bin/hadoop fs -rmr books-output-$2
        #sudo -u ${HADOOP_USER} ${HADOOP_HOME}/bin/hadoop fs -rmr books
        ;;
    ls)
        sudo -u ${HADOOP_USER} ${HADOOP_HOME}/bin/hadoop fs -ls $2
        ;;
    copy)
        sudo -u ${HADOOP_USER} ${HADOOP_HOME}/bin/hadoop dfs -copyFromLocal books books 
        ;;
    *)
        echo "Usage $0 {run|show|delete|copy|ls} <path>" >&2
        exit 3
        ;;
esac

