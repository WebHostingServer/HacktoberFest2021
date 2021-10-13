//Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
//If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).
//The replacement must be in place and use only constant extra memory.
class Solution {
public:
    void nextPermutation(vector<int>& a) {
        int n=a.size();
        int x=a[n-1],y=-1,z=-1;       //x keeps track of maximum value from last
			for(int i=n-1;i>=0;i--){
					if(a[i]<x){       //whenever a value is less then x we point it because that will be index from which array will change
					y=i;break;
				}
				x=max(x,a[i]);
        }
        if(y!=-1){        // if y==-1 that means no index got selected in above loop that mean array is in descending order, so we ignore these steps in which we find out which index will get swapped with yth index(i.e. just greater one).
        for(int i=n-1;i>=0;i--){
            if(a[i]>a[y]){
                z=i;break;
            }
        }
        swap(a[y],a[z]);
        }
        for(int i=y+1;i<=(y+n)/2;i++){ //now order the array after yth index in ascending order which was in descending previously
            if(i==n-i+y){continue;}
            swap(a[i],a[n-(i-y)]);
        }
    }
};
