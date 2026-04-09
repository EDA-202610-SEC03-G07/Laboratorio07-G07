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