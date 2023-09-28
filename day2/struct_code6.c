#include<stdio.h>
struct a{
	char y;
	double x;
	int z;	
};
int main()
{
	struct a yes;
	printf("%d",sizeof(yes));
	return 0;
}
