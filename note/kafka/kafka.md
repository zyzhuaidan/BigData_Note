# kafka

- 环境准备
  java openjdk11
  gradle Gradle 6.9.2
  scala version 2.13.10

- 修改 init.gradle

  ```gr
  allprojects {
      repositories {
          maven { url 'https://maven.aliyun.com/repository/public/' }
          maven {
              url 'https://maven.aliyun.com/nexus/content/repositories/google'
          }
          maven {
              url 'https://maven.aliyun.com/nexus/content/groups/public/'
          }
          maven {
              url 'https://maven.aliyun.com/nexus/content/repositories/jcenter'
          }
  		maven{url 'https://jitpack.io'}
          all { ArtifactRepository repo ->
              if (repo instanceof MavenArtifactRepository) {
                  def url = repo.url.toString()
                  if (url.startsWith('https://repo.maven.apache.org/maven2/')
                          || url.startsWith('https://repo.maven.org/maven2') ||
                          url.startsWith('https://repo1.maven.org/maven2') ||
                          url.startsWith('https://jcenter.bintray.com/')) {
  //project.logger.lifecycle "Repository ${repo.url} replaced by $REPOSITORY_URL . "
                      remove repo
                  }
              }
          }
      }
      buildscript {
          repositories {
              maven { url 'https://maven.aliyun.com/repository/public/' }
              maven {
                  url 'https://maven.aliyun.com/nexus/content/repositories/google'
              }
              maven {
                  url 'https://maven.aliyun.com/nexus/content/groups/public/'
              }
              maven {
                  url 'https://maven.aliyun.com/nexus/content/repositories/jcenter'
              }
              all { ArtifactRepository repo ->
                  if (repo instanceof MavenArtifactRepository) {
                      def url = repo.url.toString()
                      if (url.startsWith('https://repo1.maven.org/maven2') ||
                              url.startsWith('https://jcenter.bintray.com/')) {
  //project.logger.lifecycle "Repository ${repo.url} replaced by $REPOSITORY_URL . "
                          remove repo
                      }
                  }
              }
          }
      }
  }
  ```

  



- 执行`gradle`

在源码目录`/apache-kafka/kafka`下执行gradle命令

```shell
gradle
```

- 执行'gradle idea'

在源码目录`/apache-kafka/kafka`下执行gradle idea命令

```shell
gradle idea
```







