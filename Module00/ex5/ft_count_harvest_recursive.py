def  ft_count_harvest_recursive():
    days = int(input("days until harvest:"))

    def helper(day):
        if day > days:
            print("Harvest time!")
            return
        print("Day", day)
        helper(day + 1)

    helper(1)