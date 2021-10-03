#include <stdio.h>
/*
Using C's pointer arithmetic, this is a function that receives the as
parameters: an array address and it's number of elements, and it returns
the sum of the even numbers on that array.
by: Tiago Ribeiro (https://github.com/Tiago-S-Ribeiro)
*/
int main(){
	
	int array[] = {23,5,46,12,1,3,10,7,26,94};
	int length = sizeof(array)/sizeof(array[0]);
	int *ptr = array;
	
	printf("The sum of even numbers is: %d\n", sum(ptr, length));
	return 0;	
}

int sum(int *num, int length){
	int i, total = 0;
	
	for(i = 0; i < length; i++){
		if(*(num+i) % 2 == 0){
			total += *(num+i);
		}
    }
	
	return total;
}