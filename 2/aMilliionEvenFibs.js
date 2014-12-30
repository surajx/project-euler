function* fibGen(){
  var a=1,b=2;
  yield a;
  yield b;
  while (true){
    yield a+b;
    b = a+b;
    a = b-a;
  }
}

var problem2 = function(){
  fib = fibGen();
  var sum = 0;
  var curFib = 0;
  var t = process.hrtime()
  while(curFib<=4000000){
    curFib = fib.next().value;
    if(curFib%2==0) sum += curFib;
  }
  var t1 = process.hrtime(t);
  console.log("%s %d seconds and %d nanoseconds", "Fib using Generators", t1[0], t1[1]);
  console.log(sum);
}

problem2();
