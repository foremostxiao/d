﻿作业名称：ATM+购物车程序
测试环境：win7系统，python3.7.0，工具:pycharm-community-2018.1.4
作者：foremost
博客地址：https://www.cnblogs.com/foremostxl/
程序文件：ATM+Shopping.py

作业要求：
1 额度 15000或自定义
2 实现购物商城，买东西加入 购物车，调用信用卡接口结账
3 可以提现，手续费5%
4 支持多账户登录
5 支持账户间转账
6 记录每月日常消费流水
7 提供还款接口
8 ATM记录操作日志
9 提供管理接口，包括添加账户、用户额度，冻结账户等。。。
10用户认证用装饰器

说明：对于ATM普通用户账户、ATM管理员账户、购物商城账户。我是以用户名进行的区分。
规定：购物商城帐户名：为纯数字组成
信用卡帐户名为字母或者数字组成，不能为纯数字，且信用卡普通帐户名为长度<=5,管理员帐户名长度>5

思考：在都能认证成功的前提下：考虑过使用id区间进行区别不同用户，暂时使用用户名区分不同账户

疑惑：
1、对于每月日常的消费流水我使用的是日志删选，（1）是购物商城的支付（2）ATM自己的交易记录。只能看日期区分每月，没想到其他办法！
2、对于调用信用卡接口结账，这使用的是再次输入购物账户，通过该账户调用购物车记录进行结算，
这个再次输入感觉有点繁琐，但自己又没有想到其他解决办法！a\