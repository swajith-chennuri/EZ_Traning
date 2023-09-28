#include<stdio.h>
struct a{
	int x;
	char y;
	double z;
};
int main()
{
	struct a yes;
	printf("%d",sizeof(yes));
	return 0;
}
