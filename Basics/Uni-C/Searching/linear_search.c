#include "stdio.h"

int main() {
  int arr[] = {10, 69, 50, 84, 765, 00, 164890, 420, 87451, 1};
  int n = sizeof(arr) / sizeof(arr[0]);

  int target = 164890;
  for (int i = 0; i < n; i++) {
    if (arr[i] == target) {
      printf("Target: %d found at index: %d\n", target, i);
      return 0;
    }
  }
  printf("Target: %d not found\n", target);
  return -1;
}