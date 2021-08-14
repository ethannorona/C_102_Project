import os
import shutil

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

path = input("Enter the name of the dirctory to be sorted: ")

list_of_files = os.listdir(path)

for file in list_of_files:
    name, ext = os.path.splitext(file)
    ext = ext[1:]
    if ext == '':
        continue
    
    if name.startswith("a"):
        if os.path.exists(path+'/'+"a"): 
            shutil.move(path+'/'+file, path+'/'+"a"+'/'+file)
        else:
            os.makedirs(path+'/'+"a")
            shutil.move(path+'/'+file, path+'/'+"a"+'/'+file)
    
    elif name.startswith("b"):
        if os.path.exists(path+'/'+"b"): 
            shutil.move(path+'/'+file, path+'/'+"b"+'/'+file)
        else:
            os.makedirs(path+'/'+"b")
            shutil.move(path+'/'+file, path+'/'+"b"+'/'+file)
    elif name.startswith("c"):
        if os.path.exists(path+'/'+"c"): 
            shutil.move(path+'/'+file, path+'/'+"c"+'/'+file)
        else:
            os.makedirs(path+'/'+"c")
            shutil.move(path+'/'+file, path+'/'+"c"+'/'+file)
    elif name.startswith("d"):
        if os.path.exists(path+'/'+"d"): 
            shutil.move(path+'/'+file, path+'/'+"d"+'/'+file)
        else:
            os.makedirs(path+'/'+"d")
            shutil.move(path+'/'+file, path+'/'+"d"+'/'+file)
    elif name.startswith("e"):
        if os.path.exists(path+'/'+"e"): 
            shutil.move(path+'/'+file, path+'/'+"e"+'/'+file)
        else:
            os.makedirs(path+'/'+"e")
            shutil.move(path+'/'+file, path+'/'+"e"+'/'+file)
    elif name.startswith("f"):
        if os.path.exists(path+'/'+"f"): 
            shutil.move(path+'/'+file, path+'/'+"f"+'/'+file)
        else:
            os.makedirs(path+'/'+"f")
            shutil.move(path+'/'+file, path+'/'+"f"+'/'+file)
    elif name.startswith("g"):
        if os.path.exists(path+'/'+"g"): 
            shutil.move(path+'/'+file, path+'/'+"g"+'/'+file)
        else:
            os.makedirs(path+'/'+"g")
            shutil.move(path+'/'+file, path+'/'+"g"+'/'+file)
    elif name.startswith("h"):
        if os.path.exists(path+'/'+"h"): 
            shutil.move(path+'/'+file, path+'/'+"h"+'/'+file)
        else:
            os.makedirs(path+'/'+"h")
            shutil.move(path+'/'+file, path+'/'+"h"+'/'+file)
    elif name.startswith("i"):
        if os.path.exists(path+'/'+"i"): 
            shutil.move(path+'/'+file, path+'/'+"i"+'/'+file)
        else:
            os.makedirs(path+'/'+"i")
            shutil.move(path+'/'+file, path+'/'+"i"+'/'+file)
    elif name.startswith("j"):
        if os.path.exists(path+'/'+"j"): 
            shutil.move(path+'/'+file, path+'/'+"j"+'/'+file)
        else:
            os.makedirs(path+'/'+"j")
            shutil.move(path+'/'+file, path+'/'+"j"+'/'+file)
    elif name.startswith("k"):
        if os.path.exists(path+'/'+"k"): 
            shutil.move(path+'/'+file, path+'/'+"k"+'/'+file)
        else:
            os.makedirs(path+'/'+"k")
            shutil.move(path+'/'+file, path+'/'+"k"+'/'+file)
    elif name.startswith("l"):
        if os.path.exists(path+'/'+"l"): 
            shutil.move(path+'/'+file, path+'/'+"l"+'/'+file)
        else:
            os.makedirs(path+'/'+"l")
            shutil.move(path+'/'+file, path+'/'+"l"+'/'+file)
    elif name.startswith("m"):
        if os.path.exists(path+'/'+"m"): 
            shutil.move(path+'/'+file, path+'/'+"m"+'/'+file)
        else:
            os.makedirs(path+'/'+"m")
            shutil.move(path+'/'+file, path+'/'+"m"+'/'+file)
    elif name.startswith("n"):
        if os.path.exists(path+'/'+"n"): 
            shutil.move(path+'/'+file, path+'/'+"n"+'/'+file)
        else:
            os.makedirs(path+'/'+"n")
            shutil.move(path+'/'+file, path+'/'+"n"+'/'+file)
    elif name.startswith("o"):
        if os.path.exists(path+'/'+"o"): 
            shutil.move(path+'/'+file, path+'/'+"o"+'/'+file)
        else:
            os.makedirs(path+'/'+"o")
            shutil.move(path+'/'+file, path+'/'+"o"+'/'+file)
    elif name.startswith("p"):
        if os.path.exists(path+'/'+"p"): 
            shutil.move(path+'/'+file, path+'/'+"p"+'/'+file)
        else:
            os.makedirs(path+'/'+"p")
            shutil.move(path+'/'+file, path+'/'+"p"+'/'+file)
    elif name.startswith("q"):
        if os.path.exists(path+'/'+"q"): 
            shutil.move(path+'/'+file, path+'/'+"q"+'/'+file)
        else:
            os.makedirs(path+'/'+"q")
            shutil.move(path+'/'+file, path+'/'+"q"+'/'+file)
    elif name.startswith("r"):
        if os.path.exists(path+'/'+"r"): 
            shutil.move(path+'/'+file, path+'/'+"r"+'/'+file)
        else:
            os.makedirs(path+'/'+"r")
            shutil.move(path+'/'+file, path+'/'+"r"+'/'+file)
    elif name.startswith("s"):
        if os.path.exists(path+'/'+"s"): 
            shutil.move(path+'/'+file, path+'/'+"s"+'/'+file)
        else:
            os.makedirs(path+'/'+"s")
            shutil.move(path+'/'+file, path+'/'+"s"+'/'+file)
    elif name.startswith("t"):
        if os.path.exists(path+'/'+"t"): 
            shutil.move(path+'/'+file, path+'/'+"t"+'/'+file)
        else:
            os.makedirs(path+'/'+"t")
            shutil.move(path+'/'+file, path+'/'+"t"+'/'+file)
    elif name.startswith("u"):
        if os.path.exists(path+'/'+"u"): 
            shutil.move(path+'/'+file, path+'/'+"u"+'/'+file)
        else:
            os.makedirs(path+'/'+"u")
            shutil.move(path+'/'+file, path+'/'+"u"+'/'+file)
    elif name.startswith("v"):
        if os.path.exists(path+'/'+"v"): 
            shutil.move(path+'/'+file, path+'/'+"v"+'/'+file)
        else:
            os.makedirs(path+'/'+"v")
            shutil.move(path+'/'+file, path+'/'+"v"+'/'+file)
    elif name.startswith("w"):
        if os.path.exists(path+'/'+"w"): 
            shutil.move(path+'/'+file, path+'/'+"w"+'/'+file)
        else:
            os.makedirs(path+'/'+"w")
            shutil.move(path+'/'+file, path+'/'+"w"+'/'+file)
    elif name.startswith("x"):
        if os.path.exists(path+'/'+"x"): 
            shutil.move(path+'/'+file, path+'/'+"x"+'/'+file)
        else:
            os.makedirs(path+'/'+"x")
            shutil.move(path+'/'+file, path+'/'+"x"+'/'+file)
    elif name.startswith("y"):
        if os.path.exists(path+'/'+"y"): 
            shutil.move(path+'/'+file, path+'/'+"y"+'/'+file)
        else:
            os.makedirs(path+'/'+"y")
            shutil.move(path+'/'+file, path+'/'+"y"+'/'+file)
    elif name.startswith("z"):
        if os.path.exists(path+'/'+"z"): 
            shutil.move(path+'/'+file, path+'/'+"z"+'/'+file)
        else:
            os.makedirs(path+'/'+"z")
            shutil.move(path+'/'+file, path+'/'+"z"+'/'+file)
    elif name.startswith("0"):
        if os.path.exists(path+'/'+"0"): 
            shutil.move(path+'/'+file, path+'/'+"0"+'/'+file)
        else:
            os.makedirs(path+'/'+"0")
            shutil.move(path+'/'+file, path+'/'+"0"+'/'+file)
    elif name.startswith("1"):
        if os.path.exists(path+'/'+"1"): 
            shutil.move(path+'/'+file, path+'/'+"1"+'/'+file)
        else:
            os.makedirs(path+'/'+"1")
            shutil.move(path+'/'+file, path+'/'+"1"+'/'+file)
    elif name.startswith("2"):
        if os.path.exists(path+'/'+"2"): 
            shutil.move(path+'/'+file, path+'/'+"2"+'/'+file)
        else:
            os.makedirs(path+'/'+"2")
            shutil.move(path+'/'+file, path+'/'+"2"+'/'+file)
    elif name.startswith("3"):
        if os.path.exists(path+'/'+"3"): 
            shutil.move(path+'/'+file, path+'/'+"3"+'/'+file)
        else:
            os.makedirs(path+'/'+"3")
            shutil.move(path+'/'+file, path+'/'+"3"+'/'+file)
    elif name.startswith("4"):
        if os.path.exists(path+'/'+"4"): 
            shutil.move(path+'/'+file, path+'/'+"4"+'/'+file)
        else:
            os.makedirs(path+'/'+"4")
            shutil.move(path+'/'+file, path+'/'+"4"+'/'+file)
    elif name.startswith("5"):
        if os.path.exists(path+'/'+"5"): 
            shutil.move(path+'/'+file, path+'/'+"5"+'/'+file)
        else:
            os.makedirs(path+'/'+"5")
            shutil.move(path+'/'+file, path+'/'+"5"+'/'+file)
    elif name.startswith("6"):
        if os.path.exists(path+'/'+"6"): 
            shutil.move(path+'/'+file, path+'/'+"6"+'/'+file)
        else:
            os.makedirs(path+'/'+"6")
            shutil.move(path+'/'+file, path+'/'+"6"+'/'+file)
    elif name.startswith("7"):
        if os.path.exists(path+'/'+"7"): 
            shutil.move(path+'/'+file, path+'/'+"7"+'/'+file)
        else:
            os.makedirs(path+'/'+"7")
            shutil.move(path+'/'+file, path+'/'+"7"+'/'+file)
    elif name.startswith("8"):
        if os.path.exists(path+'/'+"8"): 
            shutil.move(path+'/'+file, path+'/'+"8"+'/'+file)
        else:
            os.makedirs(path+'/'+"8")
            shutil.move(path+'/'+file, path+'/'+"8"+'/'+file)
    elif name.startswith("9"):
        if os.path.exists(path+'/'+"9"): 
            shutil.move(path+'/'+file, path+'/'+"9"+'/'+file)
        else:
            os.makedirs(path+'/'+"9")
            shutil.move(path+'/'+file, path+'/'+"9"+'/'+file)
    