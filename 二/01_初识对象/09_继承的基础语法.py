"""
演示面向对象: 继承的基础语法
"""

# 演示单继承
class Phone:
    IMEI = None        # 序列号
    producer = "ITCAST"    # 厂商

    def call_by_4g(self):
        print("4g通话")

class Phone2026(Phone):
    face_id = "10001"     # 面部识别id

    def call_by_5g(self):
        print("5g通话")

phone = Phone2026()
print(phone.producer)
phone.call_by_4g()
phone.call_by_5g()

# 演示多继承
class NFCReader:
    nfc_type = "第五代"
    producer = "HM"

    def read_card(self):
        print("NFC读卡")

    def write_card(self):
        print("NFC写卡")

class RemoteControl:
    rc_type = "红外遥控"

    def control(self):
        print("红外遥控开启了")

class MyPhone(Phone, NFCReader, RemoteControl):
    pass

phone = MyPhone()
phone.call_by_4g()
phone.read_card()
phone.write_card()
phone.control()

# 演示多继承下, 父类成员名一致的场景
print(phone.producer)            #ITCAST, 先继承的优先级高