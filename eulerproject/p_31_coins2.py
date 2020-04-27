def problem_31_dynamic_programming(money, coin_index):
    count = 0
    if coin_index <= 0:
        return 1
    m = money
    if memoiz_list[m][coin_index] > 0:
        return memoiz_list[m][coin_index]
    while money >= 0:
        count += problem_31_dynamic_programming(money, coin_index - 1)
        money -= coin_list[coin_index]
    memoiz_list[m][coin_index] = count
    return count

coin_list = [1,2,5,10,20,50,100,200]
memoiz_list = [[0,0,0,0,0,0,0,0] for i in range(201)]
print(problem_31_dynamic_programming(2,7))
