#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <wiringPi.h>


int main(void)
{
   char buff[25];
   FILE *thermal;
   int LED = 1;

   wiringPiSetup();
   pinMode(LED, OUTPUT);

   for(;;)
   {
   	thermal = fopen("/sys/class/thermal/thermal_zone0/temp","r");
	memset(buff, 0, sizeof(buff));
	fread(buff, 5, 1, thermal);
      	printf("%s\n", buff);
   	fclose(thermal);
      if ( atoi(buff) > 50000 )
      {
       digitalWrite(LED,HIGH); delay(500);
      } 
      else{
      digitalWrite(LED,LOW); delay(500);
      }
   }
   return 0;
}
