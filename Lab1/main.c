#include <stdio.h>

int step = 0;

void monkeyGo(char x,char y)
{
	printf("Step %d：猴子从%c走到%c\n",++step,x,y);
}

void moveBox(char x,char y)
{
	printf("Step %d：猴子把箱子从%c搬到%c\n",++step,x,y);
}

void climbBox()
{
	printf("Step %d：猴子爬上箱子\n",++step);
}

void catchBanana()
{
	printf("Step %d：猴子拿到香蕉\n",++step);
}

int main(void)
{

	char atMonkey = 65; 
    char atBox = 66; 
    char atBanana = 67; 

	if(atMonkey != atBox)
	{
		monkeyGo(atMonkey,atBox);
	}

	if(atBox != atBanana)
	{
		moveBox(atBox,atBanana);
	}

	climbBox();
	catchBanana();

	return 0;
}
