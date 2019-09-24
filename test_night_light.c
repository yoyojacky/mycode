#include <iostream>
#include <unistd.h>
#include <errno.h>
#include <wiringPiI2C.h>

using namespace std;
int press_times = 0;
int interval = 1;
int button_addr = 0x19;
int light_number = 0x01;
int key_times = 0;

int main()
{
	int fd, result;
	fd = wiringPiI2CSetup(0x15);
	cout << "Init result: " << fd << endl;
	result = wiringPiI2CReadReg16(fd, button_addr);
	//printf("data is %d\n", result);
	for(;;){
	result = wiringPiI2CReadReg16(fd, button_addr);
	if (result > 0)
	{	
		if(key_times % 2 == 0 ) 
		{
		wiringPiI2CWriteReg16(fd, light_number, 0xff);
		wiringPiI2CWriteReg16(fd, light_number+3, 0xff);
		}
		else
		{	
		wiringPiI2CWriteReg16(fd, light_number, 0x00);
		wiringPiI2CWriteReg16(fd, light_number+3, 0x00);
		switch(light_number)
		{
			case 0x01: 
			case 0x02:
			case 0x07:
			case 0x08:
			case 0x0d:
			case 0x0e:
			case 0x13:
			case 0x14: light_number++;break;
			case 0x03:
			case 0x09:
			case 0x0F: light_number+=4; break;
			case 0x15: light_number=0x01; break;
		}
		}
		key_times++;
		if(key_times > 1) key_times = 0;
		wiringPiI2CWriteReg16(fd, button_addr, 0x0);
		result = wiringPiI2CReadReg16(fd, button_addr);
		printf("data is %d\n", result);
	}
	else
	{
	 printf("press the button\n");
	 sleep(interval);
	}
	}
}
