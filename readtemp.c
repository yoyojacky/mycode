#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <fcntl.h>

int main(void)
{
        float temp;
        char str[999];
        FILE *file;
        file = fopen("/sys/class/thermal/thermal_zone0/temp", "r");
        if(file){
                while(fscanf(file, "%s", str) !=EOF)
                        printf("%.2fCeicus Degree\n",strtod(str, NULL)/1000);
                fclose(file);
        }
        return 0;
}
