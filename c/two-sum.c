#Famous Two Sum Problem Using C language
#Function Solution for above problem

int *twoSum(int numbers[], int n, int target) {
    int array[100000] = {-1};
	int temp = 0;
	int i = 0;
	static int result[2];
	for(i = 0; i < n; i++)
	{
		array[numbers[i] + 5000] = i;
	}
	for(i = 0; i < n; i++)
	{
		temp = array[target - numbers[i] + 5000];
		if(temp)
    		if(temp > i)
    	    {
    	        result[0] = i + 1;
    	        result[1] = temp + 1;
    	        break;
    	    }
	}
	return result;
}
