function setA(ar, len) {
  for (let i = 0; i < len; i++) {
    ar[i] = Math.round(Math.random() * 99 + 1);
  }
}

function sortAr(ar) {
  let box, i, j;
  for (i = 1; i < ar.length; i++) {
    box = ar[i];
    j = i - 1;
    while (j >= 0 && box < ar[j]) {
      ar[j+1] = ar[j];
      j -= 1;
    }
    ar[j+1] = box;
  }
}

let target = new Array();
setA(target, 88);
console.log('Исходный массив:');
console.log(target);
sortAr(target);
console.log('Отсортированный массив:');
console.log(target);
