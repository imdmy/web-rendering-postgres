// 定义一个父类 Animal
class Animal {
    constructor(name) {
      this.name = name;
    }
  
    // 父类的方法
    eat() {
      console.log(`${this.name} is eating.`);
    }
  }
  
  // 定义一个子类 Dog，继承自 Animal
  class Dog extends Animal {
    constructor(name, breed) {
      // 使用 super 调用父类的构造函数来初始化继承的属性
      super(name);
      this.breed = breed;
    }
  
    // 子类的方法，重写了父类的方法
    bark() {
      console.log(`${this.name} is barking.`);
    }
  }
  
  // 创建一个 Dog 类的实例
  const myDog = new Dog('Buddy', 'Golden Retriever');
  
  // 访问继承的属性
  console.log(myDog.name); // 输出：Buddy
  
  // 调用继承的方法
  myDog.eat(); // 输出：Buddy is eating.
  
  // 调用子类特有的方法
  myDog.bark(); // 输出：Buddy is barking.
  