import math

def float_bin(number):
    # 計算小數從小數點第幾位開始計算(由靈開始)
    start_at = abs(math.floor(math.log2(number))) - 1
    # 開頭不是111的情況
    if start_at < 7:
        num_s = bin(start_at).lstrip("0b").zfill(3) #指數
        num_e = ""                                  #精度
        base = pow(2, -(start_at + 1))              #當前基準值

        n_number = number - base                    #因正規化後，首位數字必為1，因此直接先減掉基準值

        # 填寫接下來的bit
        for i in range(0,7):
            base = base / 2
            if n_number >= base:
                num_e = num_e + "1"
                n_number = n_number - base
            else:
                num_e = num_e + "0"


    #開頭是111的情況
    else:
        start_at = 7                                #指數最多只能填7
        num_s = "111"                               #7的binary = "111"
        num_e = ""

        base = pow(2, -(start_at + 1))               #當前基準值
        n_number = number                            #因可能為非正規化數字，因此不先減掉基準值

        for i in range(0,7):
            if n_number >= base:
                num_e = num_e + "1"
                n_number = n_number - base
            else:
                num_e = num_e + "0"
            base = base / 2


    #比較最接近數
    if num_e == "0000000":
        a_num_e = bin(int(num_e, 2) - 1).lstrip("0b").zfill(7)
        b_num_e = num_e
        c_num_e = num_e
    elif num_e == "1111111":
        a_num_e = bin(int(num_e, 2) - 1).lstrip("0b").zfill(7)
        b_num_e = num_e
        c_num_e = bin(int(num_e, 2) + 1).lstrip("0b").zfill(7)
    else:
        a_num_e = bin(int(num_e, 2) - 1).lstrip("0b").zfill(7)
        b_num_e = num_e
        c_num_e = bin(int(num_e, 2) + 1).lstrip("0b").zfill(7)

    a = bin_float(num_s + a_num_e)
    b = bin_float(num_s + b_num_e)
    c = bin_float(num_s + c_num_e)

    a = abs(number - a)
    b = abs(number - b)
    c = abs(number - c)


    if a < b and a < c:
        answer = num_s + a_num_e
    elif b < a and b < c:
        answer = num_s + b_num_e
    else:
        answer = num_s + c_num_e

    print(answer)
    return answer


def bin_float(val):
    num_s = int(val[:3], 2)
    num_e = val[3:]
    if num_s < 7:
        ans = pow(2, -(num_s + 1))
        base = ans

        for i in num_e:
            base = base / 2
            if i == "1":
                ans = ans + base

        return ans

    else:
        ans = 0
        base = pow(2, -(num_s + 1))

        for i in num_e:
            if i == "1":
                ans = ans + base
            base = base / 2

        return ans



print(bin_float(float_bin(0.000974658)))

# i = 0.0001