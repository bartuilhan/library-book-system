num = 0
num += 1
name ="name:", input("what is name book:"),
call ="call:" ,input("what call that book:"),
year ="year:", input("what year of this book:")
with open("data\\book.txt","w+") as file:
    file.writelines("book")
    file.writelines(name)
    file.writelines("\n")
    file.writelines(call)
    file.writelines("\n")
    file.writelines(year)
    file.writelines("\n")
    file.close()