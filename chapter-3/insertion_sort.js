function insertionSort(array) {
  for (let i = 1; i < array.length; i++) {
    insertValue = array[i];
    j = i - 1;
    while (j >= 0 && array[j] > insertValue) {
      array[j + 1] = array[j];
      j--;
    }
    array[j + 1] = insertValue;
  }
  return array;
}

const array = [8, 3, 1, 5, 2, 1];
console.log(insertionSort(array));
