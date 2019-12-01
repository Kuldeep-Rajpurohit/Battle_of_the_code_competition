/*
Xenny's is competing in a race and his car has X litres of fuel. There are N milestones in the competition. It takes no fuel at all to travel between gas stations, but at the  gas station,  amount of petrol is drained.

Find the number milestones Xenny crosses before his car gets out of fuel.

Input
The first line of input consists of 2 space-separated integers - N and X.

The second line contains N space-separated integers - 

Output
Print a single integer - the number of milestones Xenny crosses.
*/

#include<stdio.h>

int main()
{
    int i, stones, fuel, count = 0;
    scanf("%d %d", &stones,&fuel);
    int values[stones];
    for(i=0;i<stones;i++)
    {
        scanf("%d",&values[i]);
    }
    for(i=0;i<stones;i++)
    {
        if(fuel>=values[i])
        {
            fuel = fuel-values[i];
            count++;
        }
        else
        break;
    }
    printf("\n%d ", count);
    return 0;
}
