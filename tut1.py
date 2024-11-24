import sys 
import json 

def main(): 
    print("Hello json!")
    n = len(sys.argv)
    print("Total arguments : ", n)
    
    for i in range(n):
        print("${i} argument is : ", sys.argv[i])

    print(sys.argv[1])
    json_string = json.loads(sys.argv[1])
    print("Parsed json object : ", json_string)

if __name__ == "__main__":
    main()
