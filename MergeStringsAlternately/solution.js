function mergeAlternately(word1, word2){
  let result = [];
  let index = 0;

  while (index < word1.length && index < word2.length) {
    result.push(word1[index]);
    result.push(word2[index]);
    index++;
  }

  if (index < word1.length)
    result.push(...word1.slice(index));
  
  if (index < word2.length)
    result.push(...word2.slice(index));

  return result.join("");
}