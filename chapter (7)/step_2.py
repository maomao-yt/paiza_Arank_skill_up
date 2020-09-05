N = int(input())
# 冪剰余(べきじょうよ)を参考
def bits(integer):
    result = 0
    while integer:
        # 右ビットシフト
        integer >>= 1
        result += 1
    return result


def calc(base, exponent, modulo=1000000007):
    result = 1
    if not modulo:
        iteration = bits(exponent)
        while iteration >= 0:
            result *= result
            if (exponent >> iteration) & 1:
                result *= base
            iteration -= 1
    else:
        firstModulus = base % modulo
        iteration = bits(exponent)
        while iteration >= 0:
            result = (result * result) % modulo
            if (exponent >> iteration) & 1:
                result = (result * firstModulus) % modulo
            iteration -= 1
    return result


ans=calc(2, N)
print(ans)
