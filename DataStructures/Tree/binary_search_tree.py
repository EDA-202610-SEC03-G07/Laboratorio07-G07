

def new_bst():
    return {"root": None}
















def size(bts):
    return size_tree(bts["root"])

def size_tree(my_node):
    if my_node is None:
        return 0
    else:
        return my_node["size"]
    
    