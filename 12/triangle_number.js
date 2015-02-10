function* genTriangleNumber(){
  tirangle_number = 1;
  counter = 2;
  while (true){
    yield tirangle_number;
    tirangle_number=counter*(counter+1)/2;
    counter+=1;
  }
}

function getDivisorCount(num){
  if(num!=1) count = 2;
  else return 1;
  //count the number of divisors
}

triangleNum = genTriangleNumber();

while(true){
  var divisorCount = getDivisorCount(triangleNum.next().value);

}
