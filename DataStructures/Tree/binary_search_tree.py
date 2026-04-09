

def new_bst():
    return {"root": None}

def insert_node(root, key, value):
    if root is None:
        root = new_node(key, value)
    else :
        if key < root['key']:
            root['left'] = insert_node(root['left'], key, value)
        elif key > root['key']:
            root['right'] = insert_node(root['right'], key, value)
        else:
            root['value'] = value 
    

def put(bst, key, value):

    bst['root'] = insert_node(bst['root'], key, value )
    
    return bst

def size(bts):
    return size_tree(bts["root"])

def size_tree(my_node):
    if my_node is None:
        return 0
    else:
        return 1+size_tree(my_node["left"])+size_tree(my_node["right"])
    
    