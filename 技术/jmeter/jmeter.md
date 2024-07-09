---
title: jmeter
date: 2024-06-12 10:23:45
tags: 技术笔记
categories: 工具
---


1. **download address**

https://jmeter.apache.org/download_jmeter.cgi

2. **useful extensions to jmeter**

https://jmeter-plugins.org/downloads/old/

JMeterPlugins-Standard-1.4.0.jar
jpgc-autostop-0.1.jar

you need to add them to your jmeter/lib/ext directory


3. **peak test**

provide high tps test about 1 hour

4. **capacity test**

provide increasing tps test about 1 hour.aim to check the baseline to peak test or soak test

5. **soak test**

provide medium tps test about 8 hour. check system if stable

if your tesk token is expired in short time.you could use JSON Extractor,JSR223 PostProcessor,BeanShell Sampler to refresh token

Debug Sampler get env properties

some check sheet you could refer:

```groovy
props.put("tokenValue","123")

${__setProperty(token,${tokenValue},)}

${__P(token,)}
```

pt script you could refer below:

https://github.com/zljin/document/tree/master/%E6%8A%80%E6%9C%AF/jmeter
