filename = input("Input the Filename: ")
f_extns = filename.split(".")
dict = {"py":"python","c":"C","cpp":"C++","java":"java","txt":"text"}
key = f_extns[-1]
if key in dict.keys():
    print ("The extension of the file is : " + dict[key])
