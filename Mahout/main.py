#!/usr/bin/python
# -*- coding: utf-8 -*-
from jpype import *
import numpy as np

jvmlib = "/usr/lib/jvm/java-7-openjdk-i386/jre/lib/i386/server/libjvm.so"
classpath = "/root/mahout/src/conf:/usr/lib/jvm/java-7-openjdk-i386/jre//lib/tools.jar:/root/mahout/mahout-*.jar:/root/mahout/examples/target/mahout-examples-*-job.jar:/root/mahout/mahout-examples-*-job.jar:/root/mahout/lib/*.jar:/root/mahout/examples/target/dependency/activation-1.1.jar:/root/mahout/examples/target/dependency/antlr-2.7.7.jar:/root/mahout/examples/target/dependency/antlr-3.2.jar:/root/mahout/examples/target/dependency/antlr-runtime-3.2.jar:/root/mahout/examples/target/dependency/asm-3.1.jar:/root/mahout/examples/target/dependency/avro-1.4.0-cassandra-1.jar:/root/mahout/examples/target/dependency/avro-1.5.3.jar:/root/mahout/examples/target/dependency/avro-ipc-1.5.3.jar:/root/mahout/examples/target/dependency/bson-2.9.1.jar:/root/mahout/examples/target/dependency/cassandra-all-1.1.5.jar:/root/mahout/examples/target/dependency/cassandra-thrift-1.1.5.jar:/root/mahout/examples/target/dependency/cglib-nodep-2.2.2.jar:/root/mahout/examples/target/dependency/commons-beanutils-1.7.0.jar:/root/mahout/examples/target/dependency/commons-beanutils-core-1.8.0.jar:/root/mahout/examples/target/dependency/commons-cli-1.2.jar:/root/mahout/examples/target/dependency/commons-cli-2.0-mahout.jar:/root/mahout/examples/target/dependency/commons-codec-1.4.jar:/root/mahout/examples/target/dependency/commons-collections-3.2.1.jar:/root/mahout/examples/target/dependency/commons-compress-1.4.1.jar:/root/mahout/examples/target/dependency/commons-configuration-1.6.jar:/root/mahout/examples/target/dependency/commons-dbcp-1.4.jar:/root/mahout/examples/target/dependency/commons-digester-1.8.jar:/root/mahout/examples/target/dependency/commons-el-1.0.jar:/root/mahout/examples/target/dependency/commons-httpclient-3.0.1.jar:/root/mahout/examples/target/dependency/commons-io-2.4.jar:/root/mahout/examples/target/dependency/commons-lang-2.6.jar:/root/mahout/examples/target/dependency/commons-logging-1.1.1.jar:/root/mahout/examples/target/dependency/commons-math-2.1.jar:/root/mahout/examples/target/dependency/commons-math3-3.1.1.jar:/root/mahout/examples/target/dependency/commons-net-1.4.1.jar:/root/mahout/examples/target/dependency/commons-pool-1.6.jar:/root/mahout/examples/target/dependency/compress-lzf-0.8.4.jar:/root/mahout/examples/target/dependency/concurrentlinkedhashmap-lru-1.3.jar:/root/mahout/examples/target/dependency/core-3.1.1.jar:/root/mahout/examples/target/dependency/easymock-3.1.jar:/root/mahout/examples/target/dependency/guava-13.0.1.jar:/root/mahout/examples/target/dependency/hadoop-core-1.1.1.jar:/root/mahout/examples/target/dependency/hamcrest-core-1.3.jar:/root/mahout/examples/target/dependency/hbase-0.94.1.jar:/root/mahout/examples/target/dependency/hector-core-1.0-5.jar:/root/mahout/examples/target/dependency/high-scale-lib-1.1.2.jar:/root/mahout/examples/target/dependency/httpclient-4.0.1.jar:/root/mahout/examples/target/dependency/httpcore-4.0.1.jar:/root/mahout/examples/target/dependency/icu4j-49.1.jar:/root/mahout/examples/target/dependency/jackson-core-asl-1.9.11.jar:/root/mahout/examples/target/dependency/jackson-jaxrs-1.8.8.jar:/root/mahout/examples/target/dependency/jackson-mapper-asl-1.9.11.jar:/root/mahout/examples/target/dependency/jackson-xc-1.8.8.jar:/root/mahout/examples/target/dependency/jakarta-regexp-1.4.jar:/root/mahout/examples/target/dependency/jamm-0.2.5.jar:/root/mahout/examples/target/dependency/jamon-runtime-2.3.1.jar:/root/mahout/examples/target/dependency/jasper-compiler-5.5.23.jar:/root/mahout/examples/target/dependency/jasper-runtime-5.5.23.jar:/root/mahout/examples/target/dependency/jaxb-api-2.1.jar:/root/mahout/examples/target/dependency/jaxb-impl-2.2.3-1.jar:/root/mahout/examples/target/dependency/jersey-core-1.8.jar:/root/mahout/examples/target/dependency/jersey-json-1.8.jar:/root/mahout/examples/target/dependency/jersey-server-1.8.jar:/root/mahout/examples/target/dependency/jettison-1.1.jar:/root/mahout/examples/target/dependency/jetty-6.1.26.jar:/root/mahout/examples/target/dependency/jetty-util-6.1.26.jar:/root/mahout/examples/target/dependency/jline-0.9.94.jar:/root/mahout/examples/target/dependency/jruby-complete-1.6.5.jar:/root/mahout/examples/target/dependency/json-simple-1.1.jar:/root/mahout/examples/target/dependency/jsp-2.1-6.1.14.jar:/root/mahout/examples/target/dependency/jsp-api-2.1-6.1.14.jar:/root/mahout/examples/target/dependency/junit-4.11.jar:/root/mahout/examples/target/dependency/libthrift-0.7.0.jar:/root/mahout/examples/target/dependency/lucene-analyzers-common-4.1.0.jar:/root/mahout/examples/target/dependency/lucene-benchmark-4.1.0.jar:/root/mahout/examples/target/dependency/lucene-core-4.1.0.jar:/root/mahout/examples/target/dependency/lucene-facet-4.1.0.jar:/root/mahout/examples/target/dependency/lucene-highlighter-4.1.0.jar:/root/mahout/examples/target/dependency/lucene-memory-4.1.0.jar:/root/mahout/examples/target/dependency/lucene-queries-4.1.0.jar:/root/mahout/examples/target/dependency/lucene-queryparser-4.1.0.jar:/root/mahout/examples/target/dependency/lucene-sandbox-4.1.0.jar:/root/mahout/examples/target/dependency/mahout-core-0.8-SNAPSHOT.jar:/root/mahout/examples/target/dependency/mahout-core-0.8-SNAPSHOT-tests.jar:/root/mahout/examples/target/dependency/mahout-integration-0.8-SNAPSHOT.jar:/root/mahout/examples/target/dependency/mahout-math-0.8-SNAPSHOT.jar:/root/mahout/examples/target/dependency/mahout-math-0.8-SNAPSHOT-tests.jar:/root/mahout/examples/target/dependency/metrics-core-2.0.3.jar:/root/mahout/examples/target/dependency/mongo-java-driver-2.9.1.jar:/root/mahout/examples/target/dependency/nekohtml-1.9.17.jar:/root/mahout/examples/target/dependency/netty-3.2.4.Final.jar:/root/mahout/examples/target/dependency/objenesis-1.2.jar:/root/mahout/examples/target/dependency/protobuf-java-2.4.0a.jar:/root/mahout/examples/target/dependency/servlet-api-2.5-6.1.14.jar:/root/mahout/examples/target/dependency/servlet-api-2.5.jar:/root/mahout/examples/target/dependency/slf4j-api-1.7.2.jar:/root/mahout/examples/target/dependency/slf4j-jcl-1.7.2.jar:/root/mahout/examples/target/dependency/snakeyaml-1.6.jar:/root/mahout/examples/target/dependency/snappy-java-1.0.4.1.jar:/root/mahout/examples/target/dependency/snaptree-0.1.jar:/root/mahout/examples/target/dependency/solr-commons-csv-3.5.0.jar:/root/mahout/examples/target/dependency/speed4j-0.9.jar:/root/mahout/examples/target/dependency/stax-api-1.0.1.jar:/root/mahout/examples/target/dependency/stringtemplate-3.2.jar:/root/mahout/examples/target/dependency/uuid-3.2.0.jar:/root/mahout/examples/target/dependency/velocity-1.7.jar:/root/mahout/examples/target/dependency/xercesImpl-2.9.1.jar:/root/mahout/examples/target/dependency/xmlpull-1.1.3.1.jar:/root/mahout/examples/target/dependency/xpp3_min-1.1.4c.jar:/root/mahout/examples/target/dependency/xstream-1.4.4.jar:/root/mahout/examples/target/dependency/zookeeper-3.4.3.jar"
jvm = None


def start_jpype():
    global jvm
    if jvm is None:
        cpopt = "-Djava.class.path=%s" % classpath
        startJVM(jvmlib, "-ea", cpopt)
        jvm = "Started"


def create_inputs(ifile, *args, **param):
    """Create a sequence file containing some normally distributed
           ifile - path to the sequence file to create
    """

    #matrix of the cluster means
    cmeans = np.array([[1, 1], [-1, -1]], np.int)

    #number of points per cluster
    nperc = 30

    vecs = []

    vnames = []
    for cind in range(cmeans.shape[0]):
        pts = np.random.randn(nperc, 2)
        pts = pts + cmeans[cind, :].reshape([1, cmeans.shape[1]])
        vecs.append(pts)

        #names for the vectors
        #names are just the points with an index
        #we do this so we can validate by cross-refencing the name with the vector
        vn = np.empty(nperc, dtype=(np.str, 30))
        for row in range(nperc):
            vn[row] = "c" + str(cind) + "_" + pts[row, 0].astype((np.str, 4)) + "_" + pts[row, 1].astype((np.str, 4))
        vnames.append(vn)

    vecs = np.vstack(vecs)
    vnames = np.hstack(vnames)

    #start the jvm
    start_jpype()

    #create the sequence file that we will write to
    io = JPackage("org").apache.hadoop.io
    FileSystemCls = JPackage("org").apache.hadoop.fs.FileSystem

    PathCls = JPackage("org").apache.hadoop.fs.Path
    path = PathCls(ifile)

    ConfCls = JPackage("org").apache.hadoop.conf.Configuration
    conf = ConfCls()

    fs = FileSystemCls.get(conf)

    #vector classes
    VectorWritableCls = JPackage("org").apache.mahout.math.VectorWritable
    DenseVectorCls = JPackage("org").apache.mahout.math.DenseVector
    NamedVectorCls = JPackage("org").apache.mahout.math.NamedVector
    writer = io.SequenceFile.createWriter(fs, conf, path, io.Text, VectorWritableCls)

    vecwritable = VectorWritableCls()
    for row in range(vecs.shape[0]):
        nvector = NamedVectorCls(DenseVectorCls(JArray(JDouble, 1)(vecs[row, :])), vnames[row])
        #need to wrap key and value because of overloading
        wrapkey = JObject(io.Text("key " + str(row)), io.Writable)
        wrapval = JObject(vecwritable, io.Writable)

        vecwritable.set(nvector)
        writer.append(wrapkey, wrapval)

    writer.close()


def read_clustered_pts(ifile, *args, **param):
    """Read the clustered points
    ifile - path to the sequence file containing the clustered points
    """

    #start the jvm
    start_jpype()

    #create the sequence file that we will write to
    io = JPackage("org").apache.hadoop.io
    FileSystemCls = JPackage("org").apache.hadoop.fs.FileSystem

    PathCls = JPackage("org").apache.hadoop.fs.Path
    path = PathCls(ifile)

    ConfCls = JPackage("org").apache.hadoop.conf.Configuration
    conf = ConfCls()

    fs = FileSystemCls.get(conf)

    #vector classes
    VectorWritableCls = JPackage("org").apache.mahout.math.VectorWritable
    NamedVectorCls = JPackage("org").apache.mahout.math.NamedVector

    ReaderCls = io.__getattribute__("SequenceFile$Reader")
    reader = ReaderCls(fs, path, conf)

    key = reader.getKeyClass()()

    valcls = reader.getValueClass()
    vecwritable = valcls()
    while reader.next(key, vecwritable):
        weight = vecwritable.getWeight()
        nvec = vecwritable.getVector()

        cname = nvec.__class__.__name__
        if cname.rsplit('.', 1)[1] == "NamedVector":
            print "cluster={key} Name={name} x={x} y={y}".format(key=key.toString(), name=nvec.getName(), x=nvec.get(0),
                                                                 y=nvec.get(1))
        else:
            raise NotImplementedError("Vector isn't a NamedVector. Need to modify/test the code to handle this case.")


def getClusters(ifile, *args, **param):
    """Read the centroids from the clusters outputted by kmenas
              ifile - Path to the sequence file containing the centroids
    """

    #start the jvm
    start_jpype()

    #create the sequence file that we will write to
    io = JPackage("org").apache.hadoop.io
    FileSystemCls = JPackage("org").apache.hadoop.fs.FileSystem

    PathCls = JPackage("org").apache.hadoop.fs.Path
    path = PathCls(ifile)

    ConfCls = JPackage("org").apache.hadoop.conf.Configuration
    conf = ConfCls()

    fs = FileSystemCls.get(conf)

    #vector classes
    VectorWritableCls = JPackage("org").apache.mahout.math.VectorWritable
    NamedVectorCls = JPackage("org").apache.mahout.math.NamedVector
    ReaderCls = io.__getattribute__("SequenceFile$Reader")
    reader = ReaderCls(fs, path, conf)

    key = io.Text()

    valcls = reader.getValueClass()

    vecwritable = valcls()

    while reader.next(key, vecwritable):
        center = vecwritable.getCenter()

        print "id={cid} center={center}".format(cid=vecwritable.getId(), center=center.values)
        pass