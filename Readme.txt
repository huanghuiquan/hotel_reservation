前期准备：
1、打开mysql服务
2、mysite/setting.py中设置DATABASE变量，设置为mysql数据库，设置你本机mysql的密码
安装过程：
1、在命令行下进入当前目录（含有manage.py文件的目录）
2、输入命令： python ./manage.py syncdb （这里会要求您设置一个admin用户，根据提示设置，以备进入后台管理）
3、运行命令：python ./manage.py runserver
4、打开浏览器运行输入网址：localhost:8000/hotels/index/ 进入首页

当然你进行查询时是没有结果的，因为数据库还是空的，你需要进入admin（http://localhost:8000/admin/）增加旅馆、房间等信息

End.