/* 初始时 atatMonkey = 1 atBox = 2 atBanana = 3 onBox = 0 holdBanana = 0;
   终止时 atatMonkey = 2 atBox = 2 atBanana = 2 onBox = 1 holdBanana = 1;
   涉及到的谓词：
   goto(a,b) 猴子将从a走到b
   push(a,b) 猴子将箱子从a移到b
   climb(a) 猴子爬上a
   get(a) 猴子拿到a
*/
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