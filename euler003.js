var checkfactor = function(bignum, x) {
  return bignum % x == 0;
}

var getfactors = function(x) {
  var compl = 0;
  var factorArr = [];
  for (var i = 2; i < x; i++) {
    if (checkfactor(x, i)) {
      compl = x / i;
      if (factorArr.indexOf(compl) > -1 && factorArr.indexOf(i) > -1) {
        break;
      } else {
        factorArr.push(compl);
        factorArr.push(i);
      }
    }
  }
  factorArr.sort(function(a, b) {
    return b - a;
  });
  return factorArr;
}

var isPrime = function(x) {
  var factor_arr = getfactors(x);
  return factor_arr.length == 0;
}

// The prime factors of 13195 are 5, 7, 13 and 29.
//
// What is the largest prime factor of the number 600851475143 ?

var x = 600851475143;
// var x = 13195;

console.log('Buscando');

var factorArr = getfactors(x);
for (var factor in factorArr) {
  if(isPrime(factorArr[factor])){
    console.log(factorArr[factor]);
    break;
  }
}

console.log('fin');
