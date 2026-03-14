#include "stdio.h"

int push(int num, int stack_size, int top, int stack[]) {
  // printf("Number to push is %d and size: %d", num, stack_size);
  if (stack_size > top) {
    printf("Top is at: %d\n", top);
    stack[top + 1] = num;
    top++;
  }
  for (int i = 0; i < stack_size; i++) {
    printf("%d\n", i);
  };
  return 0;
}

int main() {
  int n = 10;
  int stack[n] = {};
  int stack_size = sizeof(stack) / sizeof(stack[0]);
  int top = -1;
  // printf("Stack size is: %d\n", stack_size);
  push(69, stack_size, top, stack);
  return 0;
}