#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        division_result = 0
        try:
            numerator = my_list_1[i]
            denominator = my_list_2[i]
            division_result = numerator / denominator
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        finally:
            new_list.append(division_result)
    return new_list
