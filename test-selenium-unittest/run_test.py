
#如何执行多个测试文件呢？
#unittest中的TestLoader类提供的discover()方法可以从多个文件中查找测试用例。
#discover(start_dir，pattern='test*.py'，top_level_dir=None)
#start_dir ：待测试的模块名或测试用例目录。
#pattern='test*.py' ：测试用例文件名的匹配原则。此处匹配文件名以“test”开头
#的“.py”类型的文件，星号“*”表示任意多个字符。
#top_level_dir=None：测试模块的顶层目录，如果没有顶层目录，则默认为 None。


import unittest
import HTMLTestRunner
import time
import yagmail

from certifi import contents


##定义一个发送邮件的方法

def send_mail(attachments):
    yag=yagmail.SMTP('1095531627@qq.com', 'yyjmxnyjqsswicej',host="smtp.qq.com")
    #登录发送人邮箱
    #user: 发件人邮箱地址
    #password: 发件人邮箱是smtp服务的授权码(并非登录密码)
    #host: 发件人邮箱的smtp服务器地址
    to = ['1102147452@qq.com', '1095531627@qq.com']#to: 收件人邮箱地址,多个用list形式，['','','']
    subject = 'unittest自动化测试报告'#subject: 邮件主题
    contents = '<p>各位好</p>&nbsp;&nbsp;&nbsp;&nbsp;本次自动化测试报告如附件所示，请各位查收，谢谢。'#contents: 邮件内容,可以设置为html字符。
    cc = ['1095531627@qq.com']  #cc:抄送,多个用list形式，['','','']
    bcc = ['1095531627@qq.com'] #bcc:秘密抄送,多个用list形式，['','','']

    yag.send(to,subject,contents,attachments,cc,bcc,)#邮件发送
    #attachments:添加附件,多个用list形式，['','','']
    print('邮件已发送成功')

    # 定义测试用例的目录为case目录，运行所有的test*开头的用例


if __name__ == '__main__':
    suits = unittest.defaultTestLoader.discover(start_dir='./case', pattern='test*.py')
    # 调用HTMLTestRunner 生成测试报告
    # runner = unittest.HTMLTestRunner()
    # 生成html格式的测试报告
    now_time = time.strftime("%Y%m%d-%H%M%S")#设置日期格式
    report='./reports/' + now_time + '_result.html'
    fp = open(report, 'wb')#打开文件
    #wb以二进制方式打开，只能写入文件。如果文件不存在，创建该文件； 如果文件存在，会清空，再打开（覆盖）
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='百度搜索测试报告', description="运行环境：Windows 10, Edge浏览器",tester='likaiyan',verbosity=2)#写入报告
    """
    stream：指定生成 HTML 测试报告的文件，必填。
    verbosity：指定日志的级别，默认为 1。如果想得到更详细的日志，则可以将参数 修改为 2。
    title：指定测试用例的标题，默认为 None。
    description：指定测试用例的描述，默认为 None
    """
    runner.run(suits)
    fp.close()#关闭文件
    send_mail(report)


