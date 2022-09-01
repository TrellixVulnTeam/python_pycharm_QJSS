# -*-coding:utf-8 -*-
import wmi
import pikepdf
from time import sleep
from pyspectator.processor import Cpu
from PIL import Image

# 获取计算机信息
def System_spec():
    Pc = wmi.WMI()
    os_info = Pc.Win32_OperatingSystem()[0]
    processor = Pc.Win32_Processor()[0]
    Gpu = Pc.Win32_VideoController()[0]
    os_name = os_info.Name.encode('utf-8').split(b'|')[0]
    ram = float(os_info.TotalVisibleMemorySize) / 1048576
    print(f'操作系统: {os_name}')
    print(f'CPU: {processor.Name}')
    print(f'内存: {ram} GB')
    print(f'显卡: {Gpu.Name}')

    print("\n计算机信息如上 ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑")

#pdf文件加密
def Encrypt_pdf(filepath):
    pdf = pikepdf.open(filepath)
    pdf.save('encrypt.pdf',encryption=pikepdf.Encryption(owner="your_password", user="your_password", R=4))
    pdf.close()

#pdf文件解密
def Decrypt_pdf():
    pdf = pikepdf.open("encrypt.pdf",password='your_password')
    pdf.save("decrypt.pdf")
    pdf.close()

#获取电脑CPU温度
def Get_temperature_CPU():
    cpu = Cpu(monitoring_latency=1)
    with cpu:
        while True:
            print(f'Temp:{cpu.temperature} °C')
            sleep(2)

# 图片格式转换, Jpg转Png
def Interchange_png():
    img = Image.open('test.jpg')
    img.save('test1.png')


if __name__ =="__main__":
    System_spec()
    Get_temperature_CPU()

