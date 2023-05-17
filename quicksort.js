
function quicksort(arr){
if (arr.length <= 1) {
    return arr
}
 const pivot = arr[arr.length-1]
  let left = []
 let right = []


for ( j=0; j < arr.length -1; j++){
        if(arr[j]< pivot){
            left.push(arr[j])
        }else{
            right.push(arr[j])
        }

}

return [...quicksort(left), pivot, ...quicksort(right)]

}


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
console.log(quicksort(test)) 