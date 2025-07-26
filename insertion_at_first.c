#include <stdio.h>

void main(){
    int temp_num, array_size, element_number=1;
    int array_num[5]={6,7,8,9,10};
    int new_array[6];
    printf("Enter a number: ");
    // scanf("%d", &new_array[0]);
    // printf("New number added at 0th index is: %d\n", new_array[0]);
    scanf("%d", &temp_num);
    printf("New number to add at 0th index is: %d\n", temp_num);
    array_size=sizeof(array_num)/sizeof(array_num[0]);
    // printf("Array size is %d\n", array_size);
    for (int i=0; i<array_size; i++){
        // new_array[i+1]=array_num[i];
        new_array[element_number]=array_num[i];
        // printf("Element is %d\n", element_number);
        // printf("New number is: %d\n", new_array[element_number]);
        element_number++;
    }
    new_array[0]=temp_num;
    for (int i=0; i<=array_size; i++){
        printf("Element at %d is %d\n",i, new_array[i]);
    }
}



// #include <stdio.h>

// void main(){
//     int temp_num, array_size, element_number=1;
//     int array_num[6]={6,7,8,9,10};
//     printf("Enter a number: ");
//     scanf("%d", &temp_num);
//     printf("New number to add is: %d\n", temp_num);
//     array_size=sizeof(array_num)/sizeof(array_num[0]);
//     // printf("Array size is: %d\n", array_size);
//     for (int i=0; i<=array_size; i++){
//         // new_array[i+1]=array_num[i];
//         array_num[i+1]=array_num[i];
//         printf("Element is %d\n", i+1);
//         printf("New number is: %d\n", array_num[i+1]);
//         // element_number++;
//     }
//     // array_num[0]=temp_num;
// }