/*

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
Example 1: This tree is symmetric. i.e if you were to draw a line down the center, both the left and right
           subtrees would be mirror reflections of each other
          1   
        /   \
       2     2
     /  \   /  \
    3    4 4    3

*/

class TreeNode{
    constructor(val, left, right){
        this.val = (val === undefined ? 0: val);
        this.left = (left === undefined ? null: left);
        this.right = (right === undefined ? null: right);
    }
}

const isSymmetricRecursive = function(left, right){
    if (left === null && right === null){
        console.log('both are null');
        return true;
    }

    if (left === null && right !== null){
        console.log('left === null right: ' + right.val);
        return false;
    }

    if (left !== null && right === null){
        console.log('left: ' + left.val + ' right === null');
        return false;
    }

    if (left.val !== right.val){
        return false;
    }

    return isSymmetricRecursive(left.left, right.right) && isSymmetricRecursive(left.right, right.left);
}

const isSymmetricIterative = function(root){
    if (root === null){
        return false;
    }

    queue = [];
    queue.push(root.left);
    queue.push(root.right);

    while(queue.length !== 0){
        left_node = queue.shift();
        right_node = queue.shift();

        if (left_node === null && right_node === null){
            continue;
        }

        if (left_node === null && right_node !== null){
            return false;
        }

        if (left_node !== null && right_node === null){
            return false;
        }

        if (left_node.val !== right_node.val){
            return false;
        }

        queue.push(left_node.left);
        queue.push(right_node.right);
        queue.push(left_node.right);
        queue.push(right_node.left);
    }

    return true;
}

const isSymmetric = function(root){
    if (root === null){
        return true;
    }

    //return isSymmetricRecursive(root.left, root.right);
    //return isSymmetricIterative(root);
}