class Stack {
  constructor(length = 1000) {
    this.top = 0;
    this.data = Array.from({ length: 1000 });
  }

  #isFull() {
    return this.top >= this.data.length - 1;
  }

  push(value) {
    if (this.#isFull()) {
      throw new RangeError('これ以上スタックに値はpushできません。');
    }
    this.data[++this.top] = value;
  }

  isEmpty() {
    return this.top === 0;
  }

  pop() {
    if (this.isEmpty()) {
      throw new RangeError('空のスタックからpopできません。');
    }
    return this.data[this.top--];
  }
}
