if __name__ == "__main__":
    cost = int(input())
    change = 1000 - cost
    coins = [500, 100, 50, 10, 5, 1]
    ans = 0
    for coin in coins:
        ans += change // coin
        change %= coin
    print(ans)