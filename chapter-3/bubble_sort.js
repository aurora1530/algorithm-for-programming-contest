const bubbleSort = (array) => {
  let shouldSort = true;
  while (shouldSort) {
    shouldSort = false;

    for (let j = array.length; j > 0; j--) {
      if (array[j] < array[j - 1]) {
        [array[j], array[j - 1]] = [array[j - 1], array[j]];
        j--;
        shouldSort = true;
      }
    }
  }
  return array;
};

const array = [5, 4, 3, 2, 1];
console.log(bubbleSort(array));
