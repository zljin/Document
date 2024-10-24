terraform {
  required_version = "~>0.13.5"
  required_providers {
    ucloud = {
      source  = "ucloud/ucloud"
      version = "~>1.22.0"
    }
  }
}



/**
Provider 是 Terraform 的核心概念之一，它负责与不同的云服务提供商（如 AWS、Azure、Google Cloud 等）或其他后端系统进行交互，
实现资源的创建、管理和销毁。
每个云服务提供商都有对应的 Terraform Provider。Terraform Provider 是一个插件，
它与 Terraform 核心引擎进行交互，提供了资源的定义、创建和管理的功能
*/
provider "ucloud" {
  public_key  = "JInqRnkSY8eAmxKFRxW9kVANYThg1pcvjD2Aw5f5p"
  private_key = "IlJn6GlmanYI1iDVEtrPyt5R9noAGz41B8q5TML7abqD8e4YjVdylwaKWdY61J5TcA"
  project_id  = "org-tgqbvi"
  region      = "cn-bj2"
}

data "ucloud_security_groups" "default" {
  type = "recommend_web"
}

/**
data代表利用UCloud插件定义的data模型对UCloud进行查询，例如我们在代码中利用data查询cn-bj2-04机房UCloud官方提供的CentOS 6.5 x64
主机镜像的id，以及官方提供的默认Web服务器适用的安全组(可以理解成防火墙)的id，这样我们就不需要人工在界面上去查询相关id，再硬编码到代码中
*/
data "ucloud_images" "default" {
  availability_zone = "cn-bj2-04"
  name_regex        = "^CentOS 6.5 64"
  image_type        = "base"
}


/**
resource代表我们需要在云端创建的资源，在例子里我们创建了三个资源，分别是主机、弹性公网ip，以及主机和公网ip的绑定
*/
resource "ucloud_instance" "web" {
  availability_zone = "cn-bj2-04"
  image_id          = data.ucloud_images.default.images[0].id
  instance_type     = "n-basic-2"
  root_password     = "supersecret1234"
  name              = "tf-example-instance"
  tag               = "tf-example"
  boot_disk_type    = "cloud_ssd"

  security_group = data.ucloud_security_groups.default.security_groups[0].id

  delete_disks_with_instance = true

  user_data = <<EOF
#!/bin/bash
yum install -y nginx
service nginx start
EOF
}

resource "ucloud_eip" "web-eip" {
  internet_type = "bgp"
  charge_mode   = "bandwidth"
  charge_type   = "dynamic"
  name          = "web-eip"
}

resource "ucloud_eip_association" "web-eip-association" {
  eip_id      = ucloud_eip.web-eip.id
  resource_id = ucloud_instance.web.id
}


/**
* 输出：声明了一个output，名字是eip，它的值就是我们创建的弹性公网ip的值
*/
output "eip" {
  value = ucloud_eip.web-eip.public_ip
}