const coinChange = function(coins, amount){
    const dp_array = new Array(amount + 1).fill(amount + 1);
    dp_array[0] = 0;

    for (let i = 1; i <= amount; i++){
        for (const coin of coins){
            if (i - coin >= 0){
                dp_array[i] = Math.min(dp_array[i], dp_array[i - coin] + 1);
            }
        }
    }

    return (dp_array[amount] === amount + 1 ? -1 : dp_array[amount]);
}

console.log(coinChange([1,2,5], 11));