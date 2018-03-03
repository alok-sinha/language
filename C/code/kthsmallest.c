#include <stdio.h>
#include <stdlib.h>
#include <time.h>


void swap (int nums[], int i, int j) {
	int tmp = nums[i];
	nums[i] = nums[j];
	nums[i] = tmp;
}

int partition(int nums[], int count) {

	if (count == 1) {
		return 0;
	} else if (count == 2) {

	}

	int pivot = nums[count-1];
	int left = 0, right = count, pivotIndex = count-1;

	while (left < pivotIndex) {
		int num = nums[left];
		if (num < pivot) {
			left += 1;
		} else if (num == pivot) {
			pivotIndex -= 1;
			swap(nums, pivotIndex, left);
		} else {
			right -= 1;
			swap(nums,right, pivotIndex-1);
			pivotIndex -= 1;
			swap(nums,left, right);
		}
	}
	return pivotIndex;
}

int findKthSmallest (int nums[], int count, int k) {
	
	int pivotIndex = partition(nums, count);
	printf("\n PivotIndex = %d", pivotIndex);
	if (pivotIndex == k-1) {
		return nums[pivotIndex];
	}
	if (pivotIndex > k-1) {
		return findKthSmallest(nums, pivotIndex,k);
	} else {
		return findKthSmallest(nums + pivotIndex+1, count-pivotIndex-1, k-pivotIndex-1);
	}
}

int main(int argc, char *args[]) {
	srand(time(0));	
	printf("%d", rand()%100);
	int nums[] = {10,2,4,1,3,9,12,14};
	printf("\n%d\n", findKthSmallest(nums, 8, 1));
	for (int i=0; i < 8; i++) {
		printf(" %d", nums[i]);
	}
}
