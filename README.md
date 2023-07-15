# Timing Checkin


1. 依赖：`Selenium-4`、`Chrome Driver`（[下载链接](https://chromedriver.chromium.org/downloads)，`Chrome Driver`的版本选择尽可能与`Google Chrome`的版本相近即可）。
> 代码在`Ubuntu-18.04`、`Selenium-4.10.0`、`Google Chrome-114.0.5735.198`上通过功能测试。

2. 将`config.py`中修改对应变量。

3. 在**有显示器的环境下**，在目录`TimingCheckin\`中，运行以下命令并手动扫码登录，获取一个初始的cookie，以保证后续的免密登录。
```
python ParseCookie.py
```

4. 在目录`TimingCheckin\`中，运行以下命令，即可完成当天的签到。
```
python TimingCheckin.py
```