# import os

# for i in os.listdir(r'c:\Dev-Cpp'):
#     print(i)



2#
# import sys
# import os
# path1 =  os.access(r"c:\Dev-Cpp",os.R_OK)
# print(path1)
# path2 =  os.access(r"c:\Dev-Cpp",os.F_OK)
# print(path2)
# path3 = os.access(r"c:\Dev-Cpp",os.W_OK)
# print(path3)
# path4 = os.access(r"c:\Dev-Cpp",os.X_OK)
# print(path4)



#3
# import sys
# import os
# path1 = os.path.exists(r"c:\Dev-Cpp")
# current_dirextory = os.getcwd()
# print(current_dirextory)
# print(path1)
#file_name = os.path.basename(path1)
#print(f"File name  : {path1})


#4

# import sys
# import os
# with open('txt.txt', 'r') as fp:
#     line_count = len(fp.readlines())
# print(line_count)


#5

# import os 
# import sys
# listok = ["1","2","3","4","5","6","7","8","9","10"]
# with open(r"C:\eldodos\fales.txt","w") as file:
#     for listki in listok :
#         file.write(listki)
#         print()
#     file.close()


# import sys 
# import os
# with open(r"C:\eldodos\fales.txt","w") as file:
#     file.write("HELLO WORLD")
# file.close()

#6
# import string 
# for letter in string.ascii_uppercase:
#     fd = open(letter + ".txt","w")
#     fd.close()



#7
# with open ("A.txt", "r")  as firstfile, open ("Z.txt","a") as secondfile:
#     for line in firstfile:
#         secondfile.write(line)


# with open("eldos.html", "r") as read_page, open("eldos2.html","a") as paste_page:
#     for line in  read_page :
#         paste_page.write(line)


8
# import sys
# import os
# import ctypes

# def is_admin():
#     try:
#         return ctypes.windll.shell32.IsUserAnAdmin()
#     except:
#         return False

# if not is_admin():

#     ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
#     sys.exit()
# path1 =  os.access(r"c:\felix",os.R_OK)
# print(path1)
# path2 =  os.access(r"c:\felix",os.F_OK)
# print(path2)
# path3 = os.access(r"c:\felix",os.W_OK)
# print(path3)
# path4 = os.access(r"c:\felix",os.X_OK)
# print(path4)
# path5 = os.path.exists(r"c:\felix")
# print(path5)
# os.chmod("txt.txt")