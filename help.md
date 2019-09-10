allure generate report/ -o report/html(将xml文件转化为html)
pytest==4.0.1
查看日志：在命令行输入：idevicesyslog
日志重定向：idevicesyslog >> iphone.log &
查看日志：tail -f iphone.log
tail -f iphone.log | grep 'QQ' # 查看包含QQ的行

