#include<stdio.h>
struct a{
	char y;
	int z;
	double x;
};
int main()
{
	struct a yes;
	printf("%d",sizeof(yes));
	return 0;
}
