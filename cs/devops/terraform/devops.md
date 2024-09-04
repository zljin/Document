## terraform
wiki:
https://lonegunmanb.github.io/introduction-terraform/
https://registry.terraform.io/providers/hashicorp/aws/latest/docs
https://docs.aws.amazon.com/

cheatsheet command:
terraform init
terraform plan
terraform apply
terraform destory
terraform docs


### terraform的状态管理

terraform apply--->terraform.tfstate (持久化到本地,保存apply后的状态）

由于tfstate文件的存在，我们在terraform apply之后立即再次apply是不会执行任何变更的，那么如果我们删除了这个tfstate文件，然后再执行apply会发生什么呢？Terraform读取不到tfstate文件，会认为这是我们第一次创建这组资源，所以它会再一次创建代码中描述的所有资源。更加麻烦的是，由于我们前一次创建的资源所对应的状态信息被我们删除了，所以我们再也无法通过执行terraform destroy来销毁和回收这些资源，实际上产生了资源泄漏。所以妥善保存这个状态文件是非常重要的

tfstate是明文的，不安全

如何解决：使用Vault或是AWS Secret Manager这样的动态机密管理工具生成临时有效的动态机密(比如有效期只有5分钟，即使被他人读取到，机密也早已失效)；
另一种 Terraform Backend。

### Terraform Backend

在 Terraform 中配置 S3 作为后端存储是一种常见的做法，可以用于存储 Terraform 状态文件，以便团队成员共享和协作。

以下是配置 Terraform 使用 S3 作为后端存储的步骤：

创建 S3 存储桶：首先，在 AWS 管理控制台或使用 AWS CLI 创建一个 S3 存储桶。这个存储桶将用于保存 Terraform 状态文件。确保选择合适的区域，并设置适当的权限以便 Terraform 可以访问该存储桶。

在 Terraform 配置中添加后端配置：在您的 Terraform 配置文件中，添加以下配置块来指定 S3 作为后端存储：

```hcl
terraform {
  backend "s3" {
    bucket = "your-s3-bucket-name"
    key    = "path/to/your/terraform.tfstate"
    region = "your-aws-region"
  }
}
```

替换上面的内容：

"your-s3-bucket-name"：将其替换为您在第一步中创建的 S3 存储桶的名称。
"path/to/your/terraform.tfstate"：这是 Terraform 状态文件的存储路径和名称。可以自定义，但建议使用有意义的路径和名称，以区分不同的 Terraform 配置。
"your-aws-region"：将其替换为您选择的 S3 存储桶所在的 AWS 区域。

1. 初始化 Terraform 后端：在添加了后端配置后，需要运行 terraform init 命令来初始化 Terraform 后端。Terraform 将尝试连接到 S3 存储桶并设置状态文件的位置。

2. 使用 Terraform：完成初始化后，您可以像平常一样使用 Terraform 命令来创建、修改和销毁基础设施。Terraform 状态将被保存在指定的 S3 存储桶中，以便团队成员可以共享和协作。

请注意，使用 S3 作为 Terraform 后端存储时，需要确保适当的权限设置，以防止未经授权的访问。建议仅授权需要访问 Terraform 后端的团队成员，并遵循最佳安全实践来保护敏感信息。



## 代码书写

### 数据类型

基本类型：string、number、bool
复杂类型：list map set object turtle

any：占位符 相当于java Object,可以传任意值


```hcl
variable "buckets" {
  type = list(object({
    name    = string
    enabled = optional(bool, true)
    website = optional(object({
      index_document = optional(string, "index.html")
      error_document = optional(string, "error.html")
      routing_rules  = optional(string)
    }), {})
  }))
}
```

### 变量赋值

terraform.tfvars 参数文件，可做命令行的入参，当前模块包含这个文件可以不传

对输入变量赋值
$ terraform apply -var="image_id=ami-abc123"
$ terraform apply -var-file="testing.tfvars"

export TF_VAR_${?}=ami-abc123  //设置环境变量