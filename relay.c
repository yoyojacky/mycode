#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <wiringPi.h>
#include <sys/time.h>
#include <limits.h>
#include <wiringPiI2C.h>
#include <fcntl.h>
#include <errno.h>
#include <sys/stat.h>
#include <time.h>
#include <string.h>

#define I2C_ADDR 0x11
#define RELAY_NO_1 0x01
#define RELAY_NO_2 0x02
#define RELAY_NO_3 0x03
#define RELAY_NO_4 0x04
#define R_ON 0x01
#define R_OFF 0x00

static volatile int relay1_state;
static volatile int relay2_state;
static volatile int relay3_state;
static volatile int relay4_state;

int get_i2c_fd = -1; 

int I2C_detect(void)
{
	int fd = -1;
	if((fd = open("/dev/i2c-0", O_RDWR)) < 0)
	{
		if((fd = open("/dev/i2c-1", O_RDWR)) < 0)
		{
			printf("I2C device file can not be accessed!\n");
			return -1;  /* i2c not active */
		}
	}
	
	close(fd);

	if((get_i2c_fd = wiringPiI2CSetup(I2C_ADDR)) < 0)
	{
		close(get_i2c_fd);
		return -2; /* i2c device not found */
	}

	sleep(1);

 	relay1_state = wiringPiI2CReadReg8(get_i2c_fd, 0x01);	
 	relay2_state = wiringPiI2CReadReg8(get_i2c_fd, 0x02);	
 	relay3_state = wiringPiI2CReadReg8(get_i2c_fd, 0x03);	
 	relay4_state = wiringPiI2CReadReg8(get_i2c_fd, 0x04);	

	if( relay1_state == -1 || relay2_state == -1 || relay3_state == -1 || relay4_state == -1)
	{ 
		printf("i2c device is out of work\n");
		return -3;
	}
}
	

int I2C_device_init()
{
	for(int x=0; x<=4; x++)
	{
	wiringPiI2CWriteReg8(get_i2c_fd, RELAY_NO_1, R_OFF);
	sleep(1);
	wiringPiI2CWriteReg8(get_i2c_fd, RELAY_NO_2, R_OFF);
	sleep(1);
	wiringPiI2CWriteReg8(get_i2c_fd, RELAY_NO_3, R_OFF);
	sleep(1);
	wiringPiI2CWriteReg8(get_i2c_fd, RELAY_NO_4, R_OFF);
	}
}

int main(void)
{
	I2C_device_init();
	if((I2C_detect()) > 0)
	{
	for(int i=0; i<1000; i++)
	{
	wiringPiI2CWriteReg8(get_i2c_fd,RELAY_NO_1, R_ON);
        sleep(1);
	wiringPiI2CWriteReg8(get_i2c_fd,RELAY_NO_1, R_OFF);
        sleep(1);
	}
	}
}

