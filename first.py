

int a,b,c;
printf("enter the value of a:");
scanf("%d",&a);
if(a<21)
{
    b=21-a;
    printf("should borrow %d lemon",b);
    }
else if(a==21)
{
    printf("suffficient lemon");
    }
else
{
    c=a-21;
    printf("there are %d extra lemon",c); 
    }
