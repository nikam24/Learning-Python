# f = open("sampleText.txt", "r") 

# # for each in f: 
# #     print(each) 

# print(f.read()) 

with open('sampleText.txt', 'r') as file : 
    for line in file : 
        print(line, end='')

    # content = file.read() 
    # print("Hello out")
    # # print(content)

    # for each in content : 
    #     print(each)
