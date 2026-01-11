def ft_harvest_total():
    i = 1
    total_harvest = 0
    while i <= 3:
        total_harvest += int(input(f"Day {i} harvest: "))
        i += 1
    print("Total harvest: ", total_harvest)
