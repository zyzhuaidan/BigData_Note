## a





| HDFS | NameNode、DataNode | DataNode    | SecondaryNameNode、DataNode  |
|------|:------------------|-------------|-----------------------------|
| YARN | NodeManager       | NodeManager | NodeManager、ResourceManager |
| 机器 | centos_01         | centos_02   | centos_03                   |


- HDFS集群配置
1. 将JDK路径明确配置给HDFS（修改hadoop-env.sh） 
进入文件夹: /opt/xingzhou/servers/hadoop-2.10.2/etc/hadoop
   
修改:
```shell
vi hadoop-env.sh
```
添加 java_home
```shell
export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.352.b08-2.el7_9.aarch64/jre
```

2. 指定NameNode节点以及数据存储目录（修改core-site.xml）

文件地址   /opt/xingzhou/servers/hadoop-2.10.2/etc/hadoop

```xml
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<!--
  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License. See accompanying LICENSE file.
-->

<!-- Put site-specific property overrides in this file. -->

<configuration>
    <!-- 指定HDFS中NameNode的地址 -->
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://centos1:9000</value>
    </property>

    <!-- 指定Hadoop运行时产生文件的存储目录 -->

    <property>
        <name>hadoop.tmp.dir</name>
        <value>/opt/xingzhou/servers/hadoop-2.10.2/data/tmp</value>
    </property>
</configuration>
```

3. 指定SecondaryNameNode节点（修改hdfs-site.xml） 
```xml
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<!--
  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License. See accompanying LICENSE file.
-->

<!-- Put site-specific property overrides in this file. -->

<configuration>
<!-- 指定Hadoop辅助名称节点主机配置 -->
<property>
    <name>dfs.namenode.secondary.http-address</name>
    <value>centos3:50090</value>
</property>
 <!--副本数量 -->
<property>
    <name>dfs.replication</name>
    <value>3</value>
</property>
</configuration>
```   

4. 指定DataNode从节点（修改etc/hadoop/slaves文件，每个节点配置信息占一行）
```shell
localhost
centos1
centos2
centos3
```

- MapReduce集群配置
1. 将JDK路径明确配置给MapReduce（修改mapred-env.sh）

```shell
vim mapred-env.sh
```

2. 指定MapReduce计算框架运行Yarn资源调度框架（修改mapred-site.xml） 
```xml
<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<!--
  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License. See accompanying LICENSE file.
-->

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>mapreduce.framework.name</name>
 <value>yarn</value>
 </property>
</configuration>
```

   
- Yarn集群配置
1. 将JDK路径明确配置给Yarn（修改yarn-env.sh） 

```shell
vim yarn-env.sh
```

2. 指定ResourceManager老大节点所在计算机节点（修改yarn-site.xml）

```xml
<?xml version="1.0"?>
<!--
  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License. See accompanying LICENSE file.
-->
<configuration>
<!-- 指定YARN的ResourceManager的地址 -->
<property>
<name>yarn.resourcemanager.hostname</name>
<value>centos3</value>
</property>
<!-- Reducer获取数据的方式 -->
<property>
<name>yarn.nodemanager.aux-services</name>
<value>mapreduce_shuffle</value>
</property>
<!-- Site specific YARN configuration properties -->

</configuration>
```
   
3. 指定NodeManager节点（会通过slaves文件内容确定）




```shell

23/02/24 01:14:42 INFO namenode.FSImage: Allocated new BlockPoolId: BP-1794247377-172.16.93.129-1677219282628
23/02/24 01:14:42 INFO common.Storage: Storage directory /opt/xingzhou/servers/hadoop-2.10.2/data/tmp/dfs/name has been successfully formatted.
23/02/24 01:14:42 INFO namenode.FSImageFormatProtobuf: Saving image file /opt/xingzhou/servers/hadoop-2.10.2/data/tmp/dfs/name/current/fsimage.ckpt_0000000000000000000 using no compression
23/02/24 01:14:42 INFO namenode.FSImageFormatProtobuf: Image file /opt/xingzhou/servers/hadoop-2.10.2/data/tmp/dfs/name/current/fsimage.ckpt_0000000000000000000 of size 323 bytes saved in 0 seconds .
23/02/24 01:14:42 INFO namenode.NNStorageRetentionManager: Going to retain 1 images with txid >= 0
23/02/24 01:14:42 INFO namenode.FSImage: FSImageSaver clean checkpoint: txid = 0 when meet shutdown.

```
