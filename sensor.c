#include <stdio.h>
#include <stdint.h>
#include <wiringPi.h>
#include <wiringPiI2C.h>

#define TEMP_REG 0x05
#define BMP280_L 0x09
#define BMP280_M 0x0A
#define BMP280_H 0x0B
#define LIGHT_L 0x02
#define LIGHT_H 0x03
#define HUMAN_DETECT 0x0D


uint8_t Result;
uint8_t bmp280_l;
uint8_t bmp280_m;
uint8_t bmp280_h;
uint8_t light_h;
uint8_t light_l;


int main(void)
{
	int fd;
	fd = wiringPiI2CSetup(0x17);
	Result = wiringPiI2CReadReg8(fd, TEMP_REG);
	printf("TEMP: %d\n", Result);
	bmp280_l = wiringPiI2CReadReg8(fd,BMP280_L);
	bmp280_m = wiringPiI2CReadReg8(fd,BMP280_M);
	bmp280_h = wiringPiI2CReadReg8(fd,BMP280_H);
	printf("Pressure: %d pascal\n", (int)bmp280_l | (int)bmp280_m << 8 | (int)bmp280_h << 16 );
	light_h = wiringPiI2CReadReg8(fd,LIGHT_H);
	light_l = wiringPiI2CReadReg8(fd,LIGHT_L);
	printf("Light sensor: %d lux\n", (int)light_l | (int)light_h << 8);
	if (wiringPiI2CReadReg8(fd, HUMAN_DETECT) == 1)
	{
		printf("there is somebody here!\n");
	}
	else
	{
		printf("NO body has been detected!\n");
	}

	return 0;
}

