provider "aws" {
  region = "your_aws_region"
}

resource "aws_vpc" "my_vpc" {
  cidr_block = "10.1.0.0/16"
}

resource "aws_subnet" "inner_public_subnet" {
  vpc_id            = aws_vpc.my_vpc.id
  cidr_block        = "10.1.0.0/24"
  availability_zone = "your_az_1"
}

resource "aws_subnet" "inner_private_public_subnet" {
  vpc_id            = aws_vpc.my_vpc.id
  cidr_block        = "10.1.1.0/24"
  availability_zone = "your_az_2"
}

resource "aws_subnet" "inner_private_subnet" {
  vpc_id            = aws_vpc.my_vpc.id
  cidr_block        = "10.1.2.0/24"
  availability_zone = "your_az_3"
}

resource "aws_internet_gateway" "my_internet_gateway" {
  vpc_id = aws_vpc.my_vpc.id
}

resource "aws_nat_gateway" "my_nat_gateway" {
  allocation_id = aws_eip.my_eip.id
  subnet_id     = aws_subnet.inner_public_subnet.id
}

resource "aws_eip" "my_eip" {
  vpc = true
}

resource "aws_route_table" "public_route_table" {
  vpc_id = aws_vpc.my_vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.my_internet_gateway.id
  }
}

resource "aws_route_table_association" "public_subnet_association" {
  subnet_id      = aws_subnet.inner_public_subnet.id
  route_table_id = aws_route_table.public_route_table.id
}

resource "aws_route_table" "private_route_table" {
  vpc_id = aws_vpc.my_vpc.id
}

resource "aws_route" "private_subnet_route" {
  route_table_id         = aws_route_table.private_route_table.id
  destination_cidr_block = "0.0.0.0/0"
  nat_gateway_id         = aws_nat_gateway.my_nat_gateway.id
}

resource "aws_instance" "my_ec2_instance" {
  ami           = "your_ami_id"
  instance_type = "t2.micro"
  subnet_id     = aws_subnet.inner_public_subnet.id
  key_name      = "your_key_pair_name"
  security_groups = [
    aws_security_group.allow_all.id,
  ]
}

resource "aws_security_group" "allow_all" {
  name_prefix = "allow_all-"
}

resource "aws_security_group_rule" "allow_all_ingress" {
  type        = "ingress"
  from_port   = 0
  to_port     = 65535
  protocol    = "tcp"
  cidr_blocks = ["0.0.0.0/0"]
  security_group_id = aws_security_group.allow_all.id
}

resource "aws_security_group_rule" "allow_all_egress" {
  type        = "egress"
  from_port   = 0
  to_port     = 65535
  protocol    = "tcp"
  cidr_blocks = ["0.0.0.0/0"]
  security_group_id = aws_security_group.allow_all.id
}
