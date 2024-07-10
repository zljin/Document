### 如何端到端部署到k8s上

1. 准备好SpringBoot application达成jar包

https://github.com/zljin/Spring-Boot-In-Action/tree/master/springboot_dev

```
mvn clean package -Dmaven.test.skip=true

java -jar coreJava-1.0.0.jar

curl localhost:8090/info
```

2. 准备好dockerFile,在项目根目录，将jar包打成image

https://github.com/zljin/Spring-Boot-In-Action/blob/master/springboot_dev/Dockerfile

```
docker build -t='corejava' .

docker run -di --name=coreJava-app -p 8090:8090 core-java:latest

docker images
```

3. minikube启动，下载registry插件,插件部分看官网操作

https://minikube.sigs.k8s.io/docs/handbook/registry/#docker-on-windows

minukube start

4. 开始将image上传minikube的私服仓库中

```
docker tag corejava 127.0.0.1:5000/corejava
docker push 127.0.0.1:5000/corejava
```

5. 准备好deployment.yaml部署到kubernetes上，并打开dashboard查看是否运行成功

https://github.com/zljin/Spring-Boot-In-Action/blob/master/springboot_dev/deployment.yaml

kubectl apply -f deployment.yaml
minukube dashboard

6. 开始进行内部service层访问

minikube service coreJava-service --url
curl http://172.17.0.15:31637

7. 创建ingress访问,先要在minikube中安装ingress controller插件

https://kubernetes.io/zh-cn/docs/tasks/access-application-cluster/ingress-minikube/#create-ingress

准备好ingress.yaml
https://github.com/zljin/Spring-Boot-In-Action/blob/master/springboot_dev/ingress.yaml
minikube addons enable ingress
kubectl apply -f ingress.yaml
curl http://hello-world.info