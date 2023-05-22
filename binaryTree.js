class Node{
constructor(value){
this.value = value;
this.left = null;
this.right = null;
}

}
class Binarytree{
constructor (root){
this.root= new Node(root)
}
search(value){

    return this.postOrderSearch(this.root,value)
}
preOrderSearch(start,find_val){
    if (start){
        if (start.value == find_val){
            return true
        }else{
            return this.preOrderSearch(start.left,find_val) || this.preOrderSearch(start.right,find_val)
        }
    }
    return false
}
postOrderSearch(start,find_val){
    if (start){
        if (start.left && this.postOrderSearch(start.left,find_val)){
            return true
        }
        if (start.right && this.postOrderSearch(start.right,find_val)){
            return true
        }
        if (start.value == find_val){
            return true
        }
    }
    return false
}
}

const tree = new Binarytree(1)
tree.root.left = new Node(2)
tree.root.right = new Node(3)
tree.root.left.left = new Node(4)
tree.root.left.right = new Node(5)

console.log(tree.search())