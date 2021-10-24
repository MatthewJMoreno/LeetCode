/*
Given the roots of two binary trees p and q, write a function to 
check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, 
and the nodes have the same value.
*/

class TreeNode{
    constructor(val, left, right){
        this.val = (val===undefined ? 0 : val)
        this.left = (left===undefined ? null : left)
        this.right = (right===undefined ? null : right)
    }
}

// A depth first search approach
const isSameTree = function(p, q){
    if (p===null && q===null){
        return true;
    } else if (p && q && p.val === q.val){
        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    }
    
    return false;
}

// A breadth first search approach
const isSameTreeBredth = function(p, q){
    p_queue = [];
    q_queue = [];

    p_queue.push(p);
    q_queue.push(q);

    while (p_queue.length !== 0 && q_queue.length !== 0){
        p_node = p_queue.shift();
        q_node = q_queue.shift();
        

        if (p_node === null && q_node === null){
            continue;
        }
        if (p_node === null && q_node !== null){
            console.log('p node val: null' + 'q node val: ' + q_node.val);
            return false; 
        }
        if (p_node !== null && q_node === null){
            console.log('p node val: ' + p_node.val + 'q node val: null');
            return false; 
        }
        if (p_node.val !== q_node.val) {
            console.log('p node val: ' + p_node.val + 'q node val: ' + q_node.val);
            return false; 
        }

        p_queue.push(p_node.left);
        p_queue.push(p_node.right);
        q_queue.push(q_node.left);
        q_queue.push(q_node.right);
    }

    return p_queue.length === 0 && q_queue.length === 0;
}