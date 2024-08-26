#lists that represent folder
#strings that represent files.

file_system = [
    [
        "nothing.txt",
        "dog_pic.png",
        [
            "secret_plan.pdf"
        ]
    ],
    "notion.app",
    "slack.app",
    [
        "fun.txt",
        [
            "meaningless_file.txt",
            "chicken_dinner.txt"
        ],
        "not_fun.txt"
    ],
    "zoom.app"
]

target = "chicken_dinner.txt"
#use a loop to go through the file system
def recursion(file_system):
    for file in file_system:
        if file == target:
            return "HOORAH" #base case
       
        if isinstance(file, list): #check if "file" is a list
            result = recursion(file)  #if file is a list search isnide it
            if result:
                return result
            
    return None

result = recursion(file_system) #save the return as  "HOORAH"
print(result)
        