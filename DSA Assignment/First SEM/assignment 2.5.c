#include <stdio.h>
#include <stdlib.h>
int main() {
    int n, i;
    printf("Enter the number of elements: ");
    scanf("%d", &n);
    int *arr = (int *)calloc(n, sizeof(int));
    if (arr == NULL) { printf("Memory allocation failed. Exiting...");
        return 1; }
    printf("Enter the elements:\n");
    for (i = 0; i < n; i++) {  scanf("%d", &arr[i]); }
    printf("Elements you entered:\n");
    for (i = 0; i < n; i++) {
        printf("%d ", arr[i]);  }
    free(arr); 
    return 0;
}

