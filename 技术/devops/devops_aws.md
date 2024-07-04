***

title: aws
date: 2022-07-23 12:00:45
tags: 运维技术
categories: devops
------------------

> 参考视频和官方文档进行的知识扫盲

## doc

> <https://docs.aws.amazon.com/>

## aws基础知识

> <https://aws.amazon.com/cn/getting-started/fundamentals-core-concepts/>

> <https://www.bilibili.com/video/BV1NJ411n7LB?p=4&vd_source=88f2d67f21120fbed5f365a6638870f5>

### summary

    aws基于五大支柱

    1. 安全性 
    ####IAM
        通过IAM policy 对主体(基于身份的策略) 操作 资源(基于资源的策略)进行管理
        你是否有权限做，和资源是否准你做
    ####网络安全
        VPC,安全组(防火墙)
    #### 数据加密
        ssl(传输的加密)

    2. 性能效率
    3. 可靠性
    #### 故障隔离
        region,az 

    4. 卓越运营
    #### 基础设施即代码terraform,脚本管理infra

    #### 观测,可监控
        CloudWatch自定义指标收集
    5. 成本优化
    按量付费


    计算服务：
    1. ec2
    2. ecs
    3. auto scaling
    4. elastic load balancing
    5. eks

    存储服务:
    1. s3

    网络服务:
    1. VPC (endpoint)
    2. VPN
    3. DirectConnect
    4. CloudFront CDN

    数据库服务：
    1.RDB

    无服务：不需要管理底层的操作系统，依赖环境，我们只需要写好我们语言的代码
    ，然后上传我们的代码到无服务的产品，之后执行代码存放到对应的数据库中
    代表是Aws lambda

## VPC创建私有网络

> <https://www.bilibili.com/video/BV1wk4y1r7gX?spm_id_from=333.999.0.0&vd_source=88f2d67f21120fbed5f365a6638870f5>

#### step follow

    1. 在一个region中创建一个VPC,设置cidr为10.1.0.0/16
    tip:vpc自带本地路由,vpc内的子网都可通过本地路由进行访问


    cidr:基于子网掩码的方式,进行ip分配
    10.1.0.0/16  --16代表子网掩码,指前面16位不变


    2. 在此的VPC中创建三个子网，并定义子网的cidr网段和可用区域
    https://docs.aws.amazon.com/zh_cn/vpc/latest/userguide/VPC_Scenario1.html

    公有子网 inner-public  10.1.0.0/24
    私有子网,但可以访问互联网 inner-private & public  10.1.1.0/24
    私有子网 inner-private 10.1.2.0/24

    3. 在此vpc中创建互联网网关，作为互联网的出入口

    4. 创建NAT网关

    NAT:网络地址转换,将私网ip通过nat网络地址转换为公有的ip进行互联网访问(家庭路由器)

    必须在公有子网创建

    5. 设置路由

        a. 首先创建公有子网的路由,
        先设置 0.0.0.0(互联网的所有请求) 都走刚刚创建的互联网网关 规则
        之后将创建好的公有子网路关联到公有子网中

            之后inner-public就有了访问外网的能力

        b. 再创建私有子网路由m通过nat实现内网访问外网   0.0.0.0--->nat

    6. 将你的ec2加入到你的vpc网段

![img](https://note.youdao.com/yws/api/personal/file/WEBe5489fd882c56dcb41dc44f81d1021bd?method=download\&shareKey=5d0d89badf256d5d2375ea7ec0b7c562)

## IAM

#### IAM introduce

> <https://www.bilibili.com/video/BV1wR4y1F7YM?p=9&spm_id_from=pageDriver&vd_source=88f2d67f21120fbed5f365a6638870f5>

what is IAM?

1.  IAM=Identity and Access Manager,(Global Service,no need to select region)
2.  Root account created by default,shoudn't be used or shared
3.  Users are people within your organization,and can be grouped
4.  Groups only contain users,no other groups
5.  user can belong to multiple groups or without any group

what is IAM\:Permissions

1.  Users or Groups can be assigned JSON document called policies,it's describe what a user is allowed to do
2.  these policies define the permissions of the users
3.  In Aws apply least privilege principle

#### IAM policies

> <https://www.bilibili.com/video/BV1wR4y1F7YM?p=10&vd_source=88f2d67f21120fbed5f365a6638870f5>

In group,IAM policies inheritance can make users inheritance by group

inline policy is used to one user without group

IAM policy sample and structure:

    {
      "Version": "2012-10-17",
      "Id": "S3-Account-Permissions"
      "Statement": [
        {
          "Sid": "1",
          "Effect": "Allow",
          "Principal":{
            "AWS": ["arn:aws:iam::123456789012:root"]
          },
          "Action": [
            "s3:GetObject",
            "s3:PutObject",
            "s3:DeleteObject"
          ],
          "Resource": "arn:aws:s3:::productionapp/*"
        }
      ]
    }

#### IAM security

> <https://www.bilibili.com/video/BV1wR4y1F7YM?p=12&vd_source=88f2d67f21120fbed5f365a6638870f5>

1.  you can setup a password policy

2.  MFA=Multi Factor Authentication
    MFA=password you know + security device you own(
    Virtual MFA deviced such as google authenticator to create a device token
    )

#### IAM AWS Access key

> <https://www.bilibili.com/video/BV1wR4y1F7YM?p=14&vd_source=88f2d67f21120fbed5f365a6638870f5>

how can user access access?

1.  Aws web console use by password+MFA
2.  aws cli used by accesskey
3.  sdk used by accesskey

aws access key is security,don't share

#### IAM Roles for Service

> <https://www.bilibili.com/video/BV1wR4y1F7YM?p=20&vd_source=88f2d67f21120fbed5f365a6638870f5>

IAM role are secure way to grant permissions to entities that you trust.
for instance,Application code running on an ec2 instance that needs to perform actions on Aws resources

add IAM ROle into ec2 sample video

> <https://www.bilibili.com/video/BV1wR4y1F7YM?p=37&vd_source=88f2d67f21120fbed5f365a6638870f5>

#### IAM Security Tools

> audit
> <https://www.bilibili.com/video/BV1wR4y1F7YM?p=23&vd_source=88f2d67f21120fbed5f365a6638870f5>

IAM Credentials Report(account level):
list all account's user and the status of their various credentials

IAM Access Advisor(user level):
show the user service permissions and lasted access date
revice your policies

#### IAM Best practice and summary

> <https://www.bilibili.com/video/BV1wR4y1F7YM?p=24&vd_source=88f2d67f21120fbed5f365a6638870f5>

> <https://www.bilibili.com/video/BV1wR4y1F7YM?p=25&vd_source=88f2d67f21120fbed5f365a6638870f5>

Users Groups Policies Roles Security Access Key Audit

## EC2

> 云中的弹性 虚拟服务器

#### Overview

how to create ec2? it's very important

> <https://www.bilibili.com/video/BV1wR4y1F7YM?p=28&vd_source=88f2d67f21120fbed5f365a6638870f5>

security Group is used to firewall in ec2,it's can control inbound or outbound traffic

ssh can login in ec2 inner
ssh -i Ec2.pem ec2-user\@35.180.242.162
or user Session manager in web console

#### EC2 instance roles

if you ec2 want to use aws command,it should add roles by IAM role policy

> <https://www.bilibili.com/video/BV1wR4y1F7YM?p=37&vd_source=88f2d67f21120fbed5f365a6638870f5>

#### private IP,public IP,Elastic IP

> <https://www.bilibili.com/video/BV1wR4y1F7YM?p=41&vd_source=88f2d67f21120fbed5f365a6638870f5>

```
public ip:
  it's means the machine can be identified on the internet
  it's unique across the whole web
  geo-located easily

private ip:
  it's mean the machine can only be identified on a private network only
  it's unique across the private network
  machine connect to www using a NAT+internet gateway(a proxy)
  Only a specify range of ips can be used as private ip

elastic ip:
  please avoid this way,instead,you can use a ramdom public ip and register dns name to it

when you destory you ec2 instance,you public ip will renew and change.if you want to unchange your public ip,you can use elastic ip,it's stable

```

#### EC2 placement Groups

> <https://www.bilibili.com/video/BV1wR4y1F7YM?p=43&vd_source=88f2d67f21120fbed5f365a6638870f5>

设置ec2安放在那里，虽然我们不能直接操作机架，但aws提供了策略给我们选择，that strategy can be defined using placement groups

#### ENI\:Elastic network interface

可以理解为ec2的网卡如eth0,一台ec2可以建很多网卡,且网卡可以迁移到其他ec2中
方便容灾处理的时候，网络访问迁移,ifconfig查看网卡信息

> <https://www.bilibili.com/video/BV1wR4y1F7YM?p=45&vd_source=88f2d67f21120fbed5f365a6638870f5>

    1. Logical component in a VPC that represents a vitual network card
    2. ENI have this attribute:
        primary private ipv4 or more secondary ipv4
        one elastic ip per private ipv4
        one public ipv4
        one or more security group
        A MAC address
    3. you can create ENI independently and attach them on the fly(move them) on ec2 instance for failover(故障迁移)
    4. bound to a specfic az

#### ec2 hiberate

> <https://www.bilibili.com/video/BV1wR4y1F7YM?p=47&vd_source=88f2d67f21120fbed5f365a6638870f5>

如果销毁ec2,内存数据和磁盘数据都会销毁，我们可以用EBS来保存磁盘数据，用hiberate恢复内存的数据，此数据也保存在磁盘中，后面直接提取

#### ec2 adcvanced Concepts

> <https://www.bilibili.com/video/BV1wR4y1F7YM?p=49&vd_source=88f2d67f21120fbed5f365a6638870f5>

vcpu\:each thread is represented as a virtual CPU

## EBS

> <https://docs.aws.amazon.com/zh_cn/ebs/?id=docs_gateway>

## EFS

> <https://docs.aws.amazon.com/zh_cn/efs/?id=docs_gateway>

## Elastic Load Balancing

> <https://docs.aws.amazon.com/zh_cn/elasticloadbalancing/index.html>

## Auto Scaling Group(ASG)

> <https://docs.aws.amazon.com/zh_cn/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html>

### overview

> <https://www.bilibili.com/video/BV1wR4y1F7YM?p=77&vd_source=88f2d67f21120fbed5f365a6638870f5>

```
ASG可以随着流量的多少，动态扩展ec2实例或者减少ec2实例
ASG in aws
  minimun count(scaling in)
  desired count
  max count(scalling out)

扩展实例时会自动加到ELB中

ASG have these attributes
  1. A launch configuration
    AMI+Instance type/EC2 user data/EBS/sg/ssh key pair

  2. min/max size,initial capacity

  3. network+subnet information

  4. loadbalaner information

  5. scaling policy

auto scaling alarm by metrics you define
if your ec2 unhealthy the asg will terminal it and create new instance

```

### hands on

> <https://www.bilibili.com/video/BV1wR4y1F7YM?p=78&vd_source=88f2d67f21120fbed5f365a6638870f5>

## S3

> 对象存储服务

### overview

    Buckets:
    存储桶是对象的容器，s3 object = 具体文件内容+文件的metadata 
    1. S3 allows people to store objects(file) in "buckets" (directories)
    2. Buckets must have a globally unique name and defined at the region level

    Objects:
    1. objects(file) have a key,the key is the full path
      s3://my-bucket/(my_file.txt)
      s3://my-bucket/(my_folder/another_folder/my_file.txt)
      the key is composed of prefix + object name
      prefix: my_folder/another_folder
      object name: my_file.txt

    ！！！注意s3没有目录的概念，只有key的概念

    2. object values are the content of the body (unlimit 5TB)
    3. metedata: this is information onto your object
    4. tags
    5. version id


    1. Amazon S3 Access Points are named network endpoints with dedicated access policies that describe how data can be accessed using that endpoint

### hands on

1.  how to create bucket

> <https://docs.aws.amazon.com/zh_cn/AmazonS3/latest/userguide/creating-bucket.html>

> <https://www.bilibili.com/video/BV1wR4y1F7YM?p=120&vd_source=88f2d67f21120fbed5f365a6638870f5>

1.  S3 Security & Bucket policies

> <https://www.bilibili.com/video/BV1wR4y1F7YM?p=126&spm_id_from=pageDriver&vd_source=88f2d67f21120fbed5f365a6638870f5>

    So if your user through IAM is allowed to access your s3 bucket,but your bucket policy is explicitly denying,you can't access it.

    Support VPC Endpoints(for instance in vpc without www internet)

1.  S3 bucket website

> <https://www.bilibili.com/video/BV1wR4y1F7YM?p=127&vd_source=88f2d67f21120fbed5f365a6638870f5>

1.  IAM roles and policies hand on

> <https://www.bilibili.com/video/BV1wR4y1F7YM?p=131&vd_source=88f2d67f21120fbed5f365a6638870f5>

## Route 53

#### overview

> <https://www.bilibili.com/video/BV1wR4y1F7YM?p=93&vd_source=88f2d67f21120fbed5f365a6638870f5>

```
Route 53 is aws dns,is also a domain register and ablity to check the health of your resources

each record contain:

DomainName (example.com)
recordType (A(ipv4),AAAA(ipv6),CNAME(转发，alias更好)，NS)
  NS:Name service for the Hosted Zone
  Control how traffic is routed for a domain
  存放了ip集合和域名集合的服务器，可以响应在托管区域的dns查询

  什么是Hosted Zone?
  A container for records that define how to route traffic to a domain

  分为public和private Hosted Zone,第一个用在公网,第一个用在VPC中(私有网络)

value (1.1.1.1)
Routing policy (simple)
TTL (dns cache time to live)

```

#### hands on

> <https://www.bilibili.com/video/BV1wR4y1F7YM?p=94&vd_source=88f2d67f21120fbed5f365a6638870f5>

## ECS

### overview

> <https://www.bilibili.com/video/BV1wR4y1F7YM?p=191&vd_source=88f2d67f21120fbed5f365a6638870f5>

    1. ECS = elastic container service
    2. launch docker containers on aws

    there are two method to use ecs:
    1. ecs cluster dependent many ec2 instance insfrastration(Auto Scaling),and each ec2 instance need register to ecs cluster
    2. ecs cluster use fargate(serverless,faas,you don't care about infra,just to use send farget task)


    you should consider your ec2 instance to add role when your instance want to connect s3 or rdb.
    and each instance inner have ecs agent,it can register ecs sevice,push image by ecr service and send log to cloudwatch 

    fargate:
    you just send fargate task to run docker container,when you create one fargate task,it's also create eni at the same time 
    and you should care about vpc cidr bound can't useless

    ECS Data volumes use efs file system to share data

### hands on

how to create ecs fargate?

> <https://www.bilibili.com/video/BV1wR4y1F7YM?p=193&vd_source=88f2d67f21120fbed5f365a6638870f5>

## ECR

> aws image registry

## EKS

    1. EKS = elastic kubernetes service
    2. manage kubernetes clusters on aws
    3. it's an alternative to ECS,更加推荐用eks来管理docker容器

    k8s是开源的自动化部署，扩展，管理容器的应用系统

    4. EKS的两种模式
      eks supports EC2 if you want to deloy your worker nodes or Fargate to deploy serverless containers 

![img](https://note.youdao.com/yws/api/personal/file/WEB2959ca21775d60c3fa6db28c76a7c304?method=download\&shareKey=2cdf4dc259436ddcd7cea0ba8cb25593)

## aws SQS

> <https://docs.aws.amazon.com/zh_cn/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html>

## aws SNS

> <https://docs.aws.amazon.com/zh_cn/sns/latest/dg/welcome.html>

## aws lambda

> 是一项计算服务，可使您无需预置或管理服务器即可运行代码

### what is serverless

    Serverless is a new paradiam in which the developers don't have to manage servers anymore
    thet just deploy code,function(Function as a service)

### overview

virtual functions - no servers to manage

> <https://www.bilibili.com/video/BV1wR4y1F7YM?p=199&vd_source=88f2d67f21120fbed5f365a6638870f5>

### hands on

> <https://www.bilibili.com/video/BV1wR4y1F7YM?p=200&spm_id_from=pageDriver&vd_source=88f2d67f21120fbed5f365a6638870f5>

