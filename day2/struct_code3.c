#include<stdio.h>
struct a{
	int z;
	int x;
	char y;
};
int main()
{
	struct a yes;
	printf("%d",sizeof(yes));
	return 0;
}
