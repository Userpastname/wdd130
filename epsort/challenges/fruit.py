def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")
    reversed = []
    for f in range(len(fruit_list)):
        #adds to reversed list by reverse order by subtracting from total length counting up
        reversed.append(fruit_list[len(fruit_list)-f-1])
    print(f"reversed: {reversed}")
    
    
    fruit_list.append("orange")
    print(f"with orange{fruit_list}")
    
    for f in range(len(fruit_list)):
        #find where apple is and insert cherry
        if fruit_list[f] == "apple":
            fruit_list.insert(f,"cherry")
            break
    print(f"insert cherry before apple{fruit_list}")

    for f in range(len(fruit_list)):
        if fruit_list[f] == "banana":
            fruit_list.pop(f)
            break
    print(f"kill banana{fruit_list}")
    
    last = fruit_list[len(fruit_list)-1]
    fruit_list.pop()
    print(last)
    print(f"kill last{fruit_list}")

    fruit_list.sort()
    print(fruit_list)
    
    fruit_list.clear()
    print(fruit_list)
    
main()