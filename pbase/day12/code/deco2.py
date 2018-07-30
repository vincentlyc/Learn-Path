

def msg_service(fn):
    def savemoney2(name, x):
        print("歡迎", name, "來原銀銀行,請取號！！")
        fn(name, x)
        print(name, "辦理了存", x, "元錢的業務, 短信發送中")
    return savemoney2


@msg_service
def savemoney(name, x):
    print(name, "存錢", x, "元")

savemoney = msg_service(savemoney)

#(不可取)
# def savemoney2(name, x):
#	print("歡迎", name, "來原銀銀行,請取號！！")
#	savemoney(name, x)
#	print(name, "辦理了存", x, "元錢的業務, 短信發送中")

#savemoney = savemoney2


savemoney("小張", 200)
savemoney("小趙", 500)
