def rec_num(num):
    if num == 0:
        return
    rec_num(num - 1)
    print("Day :", num)
def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    rec_num(days)
    print("Harvest time!")
