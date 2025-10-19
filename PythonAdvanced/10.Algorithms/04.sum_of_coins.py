def choose_coins(coins_, target_):
    coins_ = sorted(coins_)
    idx = len(coins_)-1
    coins_chosen = {}
    while target_ > 0 and idx>=0:
        count = target_//coins_[idx]
        target_%=coins_[idx]
        if count>0:
            coins_chosen[coins_[idx]] = count
        idx-=1
    if target_!=0:
        return "Error"


    result = f"Number of coins to take: {sum(coins_chosen.values())}\n"
    for coin, count in coins_chosen.items():
        result += f"{count} coin(s) with value {coin}\n"
    return result

coins = [int(x) for x in input().split(", ")]
target = int(input())
print(choose_coins(coins, target))
