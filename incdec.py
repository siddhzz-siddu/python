main()
{
	int a=50;
	
	
	int b= ++a - a++ + --a + a++ - --a + a++;
	
	
	printf("a=%d b=%d",a,b);
}