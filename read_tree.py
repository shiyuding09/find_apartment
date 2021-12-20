def read_tree():
    with open("static/data/tree.txt","r") as f:
        tree=tuple(eval(f.read()))
    return tree

if __name__=='__main__':

    read_tree()

