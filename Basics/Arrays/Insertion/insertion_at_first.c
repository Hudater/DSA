/*
Q. Add user-given-num at the begining of the array

Approach 1: a new array which stores user-num at 0th index and copies over every
"n" index element at n+1 index of the new array

Approach 2: start with the origional array with a large size and right-shift all
the elements starting at extreme right (say "k"th index and moving it to k+1)
*/

#include <stdio.h>

int approach_one(int temp_num) {
  printf("\nUsing approach 1:\n\n");
  int array_size, element_number = 1;
  int array_num[5] = {6, 7, 8, 9, 10};
  int new_array[6];
  // printf("New number to add at 0th index is: %d\n", temp_num);
  array_size = sizeof(array_num) / sizeof(array_num[0]);
  // printf("Array size is %d\n", array_size);
  for (int i = 0; i < array_size; i++) {
    // new_array[i+1]=array_num[i];
    new_array[element_number] = array_num[i];
    // printf("Element is %d\n", element_number);
    // printf("New number is: %d\n", new_array[element_number]);
    element_number++;
  }
  new_array[0] = temp_num;
  for (int i = 0; i <= array_size; i++) {
    printf("Element at %d is %d\n", i, new_array[i]);
  }
  return 0;
}

int approach_two(int temp_num) {
  printf("\nUsing approach 2:\n\n");
  int array_size, element_number = 1;
  int array_num[20] = {6, 7, 8, 9, 10};
  // printf("New number to add is: %d\n", temp_num);
  array_size = sizeof(array_num) / sizeof(array_num[0]);
  // printf("Array size is: %d\n", array_size);
  for (int i = 0; i <= array_size; i++) {
    // new_array[i+1]=array_num[i];
    // array_num[i + 1] = array_num[i];
    printf("Element at %d is %d\n", i, array_num[i]);
    // printf("Element is %d\n", i + 1);
    // printf("New number is: %d\n", array_num[i + 1]);
    // element_number++;
  }
  // array_num[0]=temp_num;
  return 0;
}

int main() {
  int temp_num;
  printf("Enter num to add at 0th index: ");
  scanf("%d", &temp_num);
  approach_one(temp_num);
  approach_two(temp_num);
  return 0;
}