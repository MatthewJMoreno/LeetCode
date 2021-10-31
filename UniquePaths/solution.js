var uniquePaths = function(m, n) {
    const dp_table = new Array(m).fill(0);
    dp_table[0] = new Array(n).fill(1);
    
    for (let i = 1; i < m; i++){
        dp_table[i] = new Array(n).fill(0);
    }
    
    for (let i = 1; i < m; i++){
        dp_table[i][0] = 1;
    }
    
    for (let i = 1; i < m; i++){
        for (let j = 1; j < n; j++){
            dp_table[i][j] = dp_table[i - 1][j] + dp_table[i][j - 1];
        }
    }
    
    return dp_table[m - 1][n - 1];
};