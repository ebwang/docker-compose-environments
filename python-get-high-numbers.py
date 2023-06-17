def birthdayCakeCandles(candles):
    highest_number = max(candles)
    count = candles.count(highest_number)
    return count

if __name__ == '__main__':
    candles_count = 4

    candles = [3,2,1,3,3]

    result = birthdayCakeCandles(candles)

    print(result)

