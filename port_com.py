import serial  # 导入模块

try:
 portx = "COM1"  # 端口，Windows中通常为COM
 bps = 115200  # 波特率，常用的有：9600，19200，115200
 delay = 10  # 延时，0为立即返回，其余为等待时间（单位为秒）
 ser = serial.Serial(portx, bps, timeout = delay)  # 给串口赋值

 str = "川山越岭一往无前"  # 数据编写
 ser.write((str + '\n').encode("GB2312"))  # 中文编码
 print("发送成功！")
 print(ser.readline())  # 可以接收数据
 ser.close()  # 关闭串口

except Exception as e:  # 如果失败，打印失败
 print("无法发送讯息！", e)