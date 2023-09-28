#include<stdio.h>
struct a{
	double z;
	double x;
	char y;
};
int main()
{
	struct a yes;
	printf("%d",sizeof(yes));
	return 0;
}
