import sys

def main():
    global source, new, check, dest
    path = [str(w) for line in sys.stdin.readlines() for w in line.split()]
    case = 1
    i = 0
    length = len(path)
    while (True):
        p = path[i]       
        c = path[i+1]
        check = True
        tree = makeTree(c)
        check = False
        edit = addOne(p, tree)
        theLca = LCA(source, dest)
        lca = tree[theLca]
        s = thePath(lca,source,dest,p)
        print('Case% d: ' % (case) + '\n   P = ' + p +'\n   C = ' 
            + c +'\n' + '   S = ' + s + '\n')
        case = case + 1
        if (i >= length-2):
            break
        i = i+2

def LCA(a,b):
    while (a.level > b.level):
        a = a.parent
    while (b.level > a.level):
        b = b.parent
    while (a.name != b.name):
        if (a.name == "" and b.name != ""):
            b = b.parent
        elif (a.name != "" and b.name == ""):
            a = a.parent
        else:
            a = a.parent
            b = b.parent
    return a.name + str(a.level)

def thePath(lca,sr,dest,p):
    fromSr=""
    fromDest=""
    slash = "/"
    if(lca.name + str(lca.level) == sr.name + str(sr.level) and lca.name 
        + str(lca.level) == dest.name + str(dest.level)):
        return(".")
    while (lca.name + str(lca.level) != sr.name + str(sr.level) or lca.name 
        + str(lca.level) != dest.name + str(dest.level)):
        if (lca.name + str(lca.level) != sr.name + str(sr.level)):
            if(fromSr == ""):
                fromSr = fromSr + ".."
                sr = sr.parent
            else:
                fromSr = fromSr + "/.."
                sr = sr.parent
        else:
            if(fromDest == ""):
                fromDest = dest.name + fromDest
                dest = dest.parent
            else:
                fromDest = dest.name + "/" + fromDest
                dest = dest.parent
    if (fromDest == "" or fromSr == ""):
        slash = ""
    if p[0] != "/":
        return ridOfDots(fromSr + slash + fromDest)
    return (fromSr + slash + fromDest)

def ridOfDots(string):
    noDot = string.split("/")
    array = []
    for i in range(0,(len(noDot)-1)):
        if noDot[i] != "." and noDot[i] != "..":
            if noDot[i+1] == "..":
                continue
            array.append(noDot[i])
    array.append(noDot[len(noDot)-1])
    final = "/".join(array)
    return final

def addOne(p, tree):
    global dest
    return dict(makeTree(p),**tree) 

def makeTree(path):
    global source, dest
    root = Node("", None ,0) 
    level = 1
    tree = dict() 
    tree[root.name + str(root.level)] = root
    j = 1 
    arr = [] 
    arr.append(root) 
    if(len(path) == 1):
        if (check):
            source = root
        else:
            dest = root
        return tree
    for i in range(0,len(path)):
        if (path[i] == "." and i != len(path)):
            if(i+1 == len(path)):
                if (check):
                    source = root
                else:
                    dest = root
                return tree
            elif (path[i]+path[i+1] == ".."):
                level = level - 1
                j = j-1
        elif (path[i] != "/" and path[i] != "."):
            if (i == 0 or i == 1):
                new = Node(path[i],root,level)
                tree[new.name + str(new.level)] = new
                arr.append(new)
            else:
                if (path[i-2] == "." and path[i-3] == "."):
                    j=j+1
                    new = Node(path[i],tree[arr[j-1].name + str(arr[j-1].level)],level)
                    arr.append(new)
                else:
                    new = Node(path[i],tree[arr[len(arr)-1].name + str(arr[len(arr)-1].level)],level)
                    arr.append(new)
                tree[new.name + str(new.level)] = new
                j = j + 1
            level = level + 1
    if (check):
        source = new
    else:
        dest = new
    return tree       

class Node:
   
    def __init__(self, name, parent, level):
        self.parent = parent
        self.name = name
        self.level = level

    def print_Node(self):
        print("Name: " + self.name + "  Parent: " + (self.parent).name + "  Level: " + str(self.level))

    def get_Name(self, name):
        return self.name
main()

