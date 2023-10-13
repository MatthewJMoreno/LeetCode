const vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'];

function swap(strArr, p1, p2){
  let temp = strArr[p1];
  strArr[p1] = strArr[p2];
  strArr[p2] = temp;
}

function findP2VowelIndex(strArr, p2){
  for (let i = p2; i > 0; i--){
    if (vowels.includes(strArr[i])){
      return i;
    }
  }

  return -1;
}

function reverseVowels(s) {
  let strArr = s.split('');
  let p1 = 0;
  let p2 = strArr.length - 1;

  while (p1 < p2){
    if (vowels.includes(strArr[p1])){
      p2 = findP2VowelIndex(strArr, p2);

      if (p1 < p2){
        swap(strArr, p1, p2);
        p2--;
      }
    }

    p1++;
  }

  return strArr.join('');
}

let s = 'hello';
console.log(reverseVowels(s));