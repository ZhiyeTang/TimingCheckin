# Timing Checkin


1. 依赖：`Selenium-4`、`Chrome Driver`。

> 代码在`Ubuntu-18.04`、`Selenium-4.10.0`、`Google Chrome-114.0.5735.198`上通过功能测试。

2. 在**有头环境下**运行`ParseCookie.py`，手动扫码登录，获取一个初始的`cookies.json`。

3. 将`TimingCheckin.py`设置为后台定时任务即可。