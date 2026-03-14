#include "stdio.h"

int main() {
  int arr[] = {66, 10, 69, 50, 84, 765, 00, 164890, 420, 87451, 1};
  int n = sizeof(arr) / sizeof(arr[0]);
  int temp = 0;
  for (int j = 0; j < n; j++) {
    // printf("First for\n");
    for (int i = 1; i < n; i++) {
      // printf("Second for\n");
      // printf("Item at index %d is: %d\n", i, arr[i]);
      if (i > i - 1) {
        printf("Swapping num\n");
        temp = arr[i - 1];
        arr[i - 1] = arr[i];
        arr[i] = temp;
      }
    };
  }
  for (int i = 0; i < n; i++) {
    printf("Item at index %d is: %d\n", i, arr[i]);
  }
}