import bst_node as bst

def new_bst():
    return {"root": None}

def insert_node(root, key, value):
    if root is None:
        root = bst.new_node(key, value)
    else :
        if key < root['key']:
            root['left'] = insert_node(root['left'], key, value)
        elif key > root['key']:
            root['right'] = insert_node(root['right'], key, value)
        else:
            root['value'] = value 
        root["size"]=1+ size_tree(root["left"]) + size_tree(root["right"])
    return root

def put(bst, key, value):

    bst['root'] = insert_node(bst['root'], key, value )
    
    return bst

def size(bst):
    return size_tree(bts["root"])

def size_tree(my_node):
    if my_node is None:
        return 0
    else:
        return 1+size_tree(my_node["left"])+size_tree(my_node["right"])
    
def get(bst,key):
    return get_node(bst["root"],key["value"])

def get_node(root,key):
    if root is None:
        return root
    else:
        if root["key"] ==key:
            return root
        elif root["key"]< key:
            return get_node(root["left"],key)
        else:
            return get_node(root["right"],key)
            
    
    