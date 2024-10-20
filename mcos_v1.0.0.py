import os
import time
import random

# 系统引导页面
os.system("clear")
print("\033[92m ")
print("====Bios引导程序====")
print("请选择启动系统")
print("1.自研发OS")
print("====================")
system = 1
systeminput = input("请输入编号:")
os.system("clear")
print(" ")
# 系统启动页面
time.sleep(2.0)
print("[MCOS]版权所有:B站 @攻击yingopp")
print("[MCOS]仅供娱乐")
print(" ")
print("/=====\ /=====\ /=====\ /=====\ ")
print("|     | |     | |     | |     | ")
print("| / \ | | /===/ | /=\ | | ====| ")
print("| | | | | |     | | | | |     | ")
print("| | | | | \===\ | \=/ | |==== | ")
print("| | | | |     | |     | |     | ")
print("\=====/ \=====/ \=====/ \=====/ ")
print(" ")
print("正在启动MCOS...")
time.sleep(7.5)
# 硬件自检
print(" ")
print("====================")
print("本机ip:127.0.0.1")
print("本机端口:8000")
print("外网端口:10663")
print("驱动版本:Unknown")
print("MCOS版本:1.0.0")
print("MCOS版本号:100010000")
print("====================")
print(" ")
time.sleep(1.0)
print("[MCOS]已完成硬件自检")
print(" ")
print("[MCOS]进入系统中...")
time.sleep(5.0)
# 命令行页面
os.system("clear")
print("MCOS Command System")
print("Version:0.0.1_02")
print(" ")
print("请先输入help看一下帮助文档")
print(" ")
# %1%
for i in range(9999):
    # 设定命令变量
    command2 = input("C:/")
    cd = "cd"
    chkdskc = "chkdsk C:/"
    chkdskct = "chkdsk C:/ /t"
    cls1 = "cls"
    dir1 = "dir"
    exit1 = "exit"
    help1 = "help"
    list1 = "list"
    logoff = "logoff"
    mc = "mc"
    OptionalFeatures = "OptionalFeatures"
    ping = "ping"
    python = "python"
    startgameexe = "start game.exe"
    tell = "tell"
    test = "test"
    url = "url"
    cdhelp = "cd help"
    chkdskhelp = "chkdsk help"
    listhelp = "list help"
    tellhelp = "tell help"
    ver = "ver"
    # 设置输入命令后显示的东西
    if command2 == cd:
        print("Error:“cd”is not command")
    else:
        time.sleep(0.0)
    
    if command2 == dir1:
        print("system.py----8.36KB----py文件")
        print("game.exe----95.75KB---exe文件")
    else:
        time.sleep(0.0)
    
    if command2 == exit1:
        os.system("clear")
        exit
    else:
        time.sleep(0.0)
    
    if command2 == list1:
        print(" ")
        print("用户列表")
        print("1.admin<当前登录用户>--管理员")
        print(" ")
    else:
        time.sleep(0.0)
    
    if command2 == mc:
        print("ERROR:尚未安装java8以上的版本")
        print("请安装后在执行此命令")
    else:
        time.sleep(0.0)
    
    if command2 == python:
        print("此命令没啥用")
    else:
        time.sleep(0.0)
    
    if command2 == tell:
        print("无法连接到mcserver.xhtml.mom/api/mcos/servertell.py")
    else:
        time.sleep(0.0)
    
    if command2 == listhelp:
        print(" ")
        print("list 命令帮助文档")
        print("list - 列出MCOS中的用户")
        print(" ")
    else:
        time.sleep(0.0)
    
    if command2 == tellhelp:
        print(" ")
        print("tell 命令帮助文档")
        print("tell [信息] - 向服务器发送信息<未开发>")
        print(" ")
    else:
        time.sleep(0.0)
    
    if command2 == ver:
        print("关于MCOS")
        print("MCOS开发作者:B站 @攻击yingopp")
        print("gitee:https://gitee.com/desktop09n492k/mcos/")
        print("MCOS版本:1.0.0")
        print("MCOS版本号:100010000")
    else:
        time.sleep(0.0)
    
    if command2 == help1:
        print(" ")
        print("MCOS 命令帮助文档")
        print("cd               - 请输入cd help查看此命令的帮助文档")
        print("chkdsk           - 请输入chkdsk help查看此命令的帮助文档")
        print("cls              - 新页面")
        print("dir              - 列出当前目录的文件")
        print("exit             - 退出MCOS")
        print("help             - 查看MCOS命令帮助文档")
        print("list             - 请输入list help查看此命令的帮助文档")
        print("logoff           - 注销")
        print("mc               - 请安装java8以上版本后输入命令")
        print("OptionalFeatures - 调试命令")
        print("ping             - ping指定ip")
        print("python           - python命令")
        print("start            - 打开某个文件")
        print("tell             - 请输入tell help查看此命令的帮助文档")
        print("test             - 测试命令")
        print("url              - 抓包代码")
        print("ver              - 查看系统版本")
        print(" ")
    else:
        time.sleep(0.0)
    
    if command2 == url:
        print("ERROR:“htps://” is not network, line 1")
        print("执行“url”代码出错:“htps://”不是地址，行:1")
    else:
        time.sleep(0.0)
    
    if command2 == test:
        print("[MCOS]网络连接测试")
        print("[MCOS]括号内内容为线程，不是测试次数")
        time.sleep(2.5)
        print("（10）http://mcserver.xhtml.mom/api/mcos/servertell.py:bad")
        print("（1）http://mcserver.xhtml.mom/api/mcos/client.py:ok")
        print("（1）http://mcserver.xhtml.mom/api/mcos/client.sh:ok")
        print("（1）http://github.com/DESKTOP09N492K/mcos/README.md:bad")
        time.sleep(2.0)
        print("（1）https://mf.iqy.im/qingyun/index.php?id=128&username=admin_password=**********:ok")
        print("（2）https://mf.iqy.im/qingyun/phpmyadmin.php?id=64&username=admin_password=**********:ok")
        print("（1）http://mcserver.xhtml.mom/:ok<223ms>")
        print("（1）https://mcserver.xhtml.mom/:bad<timed out>")
        time.sleep(0.5)
        print("[MCOS]评估中...")
        time.sleep(1.0)
        print("您当前网络较好，延迟:30ms~110ms，多线程:支持，频段:2.4Ghz/5.0Ghz")
    else:
        time.sleep(0.0)
    
    if command2 == cdhelp:
        print(" ")
        print("cd 命令帮助文档")
        print("cd [目录] - 跳转到指定目录")
        print("cd ..     - 返回上级目录")
        print(" ")
    else:
        time.sleep(0.0)
        
    if command2 == startgameexe:
        # 程序代码
        num = random.randint(1, 10)
        # 判断
        while True:
            guess = int(input("猜一个1~100的数字:"))
            if guess == num:
                print("傻逼猜对了")
                break
            elif guess > num:
                print("傻逼猜大了")
            else:
                print("傻逼猜小了")
    else:
        time.sleep(0.0)
        
    if command2 == chkdskhelp:
        print(" ")
        print("chkdsk 命令帮助文档")
        print("chkdsk [盘符]    - 检查指定盘符的错误并修复")
        print("chkdsk [盘符] /t - 在检查指定盘符结束后执行重启命令")
        print(" ")
    else:
        time.sleep(0.0)
        
    if command2 == chkdskc:
        print("正在检查盘符C:/，可能需要1~2分钟")
        print(" ")
        print("调试命令:无")
        time.sleep(67.0)
        print("已成功检测并修复盘符中的错误")
    else:
        time.sleep(0.0)
        
    if command2 == chkdskct:
        print("正在检查盘符C:/，可能需要1~2分钟")
        print(" ")
        print("调试命令:/t")
        time.sleep(71.0)
        print("已成功检测并修复盘符中的错误")
        print("正在重启...")
        time.sleep("5.0")
        os.system("clear")
    else:
        time.sleep(0.0)
        
    if command2 == logoff:
        print("由于MCOS限制，无法使用logoff命令")
    else:
        time.sleep(0.0)
        
    if command2 == OptionalFeatures:
        print("启用或关闭MCOS功能")
        print("NET.fromwork 3.5: 启用")
    else:
        time.sleep(0.0)
        
    if command2 == cls1:
        os.system("clear")
    else:
        time.sleep(0.0)
        
    if command2 == ping:
        sent = 1
        ip = input("请输入ip:")
        print("已测试 %s 次到ip为 %s 的服务器"%(sent,ip))
        time.sleep(1.0)
        sent = sent + 1
        print("已测试 %s 次到ip为 %s 的服务器"%(sent,ip))
        time.sleep(1.0)
        sent = sent + 1
        print("已测试 %s 次到ip为 %s 的服务器"%(sent,ip))
        time.sleep(1.0)
        print("测试完成，网络正常")
    else:
        time.sleep(0.0)
        
    