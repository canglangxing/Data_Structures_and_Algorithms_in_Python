def the_change(price, pay):
    if price == pay:
        print("不需要找零")
    else:
        change = (pay - price) * 10
        money = [100, 50, 20, 10, 5, 1, 0.5, 0.1]
        cash = {}
        for i in money:
            num = change // (i * 10)
            temp = change % (i * 10)
            cash[i] = int(num)
            if temp == 0:
                break
            else:
                change = temp
        for key, value in cash.items():
            print(f"找零{value}张{key}元人民币")


the_change(100.5, 120)
