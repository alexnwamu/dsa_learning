// function mergeSort(arr){
// if (arr.length <=1){
//     return arr
// }

// n = Math.floor(arr.length/2)
// left_arr = arr.slice(0,n)
// right_arr = arr.slice(n)

// left = mergeSort(left_arr)  
// right = mergeSort(right_arr) 


// return merge(left,right)

// }
// function merge(left_arr,right_arr){
//     let sortedarr = []
//     let i= 0
//     let j=0
//     while (i < left_arr.length && j < right_arr.length ){
    
//         if(left_arr[i] < right_arr[j] ){
//             sortedarr.push(left_arr[i])
//             i++
//         }else{
//             sortedarr.push(right_arr[i])
//             j++
//         }
//         }
//     while (i < left_arr.length){
//         sortedarr.push(left_arr[i])
//         i++
       
//     }
//     while (j < right_arr.length){
//         sortedarr.push(right_arr[j])
//         j++
//     }
    
//     return sortedarr
//     }

function mergeSort(arr) {
    if (arr.length <= 1) {
      return arr;
    }
  
    // Split the array in half
    const middleIndex = Math.floor(arr.length / 2);
    const leftArr = arr.slice(0, middleIndex);
    const rightArr = arr.slice(middleIndex);
  
    // Recursively call mergeSort on each half
    const sortedLeftArr = mergeSort(leftArr);
    const sortedRightArr = mergeSort(rightArr);
  
    // Merge the two sorted halves
    return merge(sortedLeftArr, sortedRightArr);
  }
  
  function merge(leftArr, rightArr) {
    let resultArr = [];
    let leftIndex = 0;
    let rightIndex = 0;
  
    while (leftIndex < leftArr.length && rightIndex < rightArr.length) {
      if (leftArr[leftIndex] < rightArr[rightIndex]) {
        resultArr.push(leftArr[leftIndex]);
        leftIndex++;
      } else {
        resultArr.push(rightArr[rightIndex]);
        rightIndex++;
      }
    }
  
    // Add the remaining elements of leftArr
    while (leftIndex < leftArr.length) {
      resultArr.push(leftArr[leftIndex]);
      leftIndex++;
    }
  
    // Add the remaining elements of rightArr
    while (rightIndex < rightArr.length) {
      resultArr.push(rightArr[rightIndex]);
      rightIndex++;
    }
  
    return resultArr;
  }
  

test_array = [2,3,6,7,10,1,5,34,2,5,67]

console.log(mergeSort(test_array))
