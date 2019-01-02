#include <wiringPi.h>
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

#define CLOCKWISE 1 
#define COUNTER_CLOCKWISE 2

void delayMS(int x);
void rotate(int* pins, int direction);

int main(int argc,char* argv[]){
	if(argc < 4){
		printf("Usage example: ./motor 0 1 2 3 \n");
		return 1;
		}
	int pinA = atoi(argv[1]);
	int pinB = atoi(argv[2]);
	int pinC = atoi(argv[3]);
	int pinD = atoi(argv[4]);

	int pins[4] = {pinA, pinB, pinC, pinD};

	if(-1 == wiringPiSetup()){
		printf("Setup wiringPi failed!\n");
		return 1;
	}

	pinMode(pinA, OUTPUT);
	pinMode(pinB, OUTPUT);
	pinMode(pinC, OUTPUT);
	pinMode(pinD, OUTPUT);

	delayMS(50);
	for(int i=0; i<500; i++){
		rotate(pins, CLOCKWISE);
		}
	return 0;
	}

void delayMS(int x){
	usleep(x * 1000);
	}	

void rotate(int* pins, int direction){
	for(int i=0;i<4;i++){
		if(CLOCKWISE == direction){
			for(int j=0;j<4;j++){
				if(j==i){
					digitalWrite(pins[3-j],1);
					}
				else{
					digitalWrite(pins[3-j],0);
					}
			} 
		}else if(COUNTER_CLOCKWISE == direction){
				for(int j=0; j<4;j++){
				if(j==i){
					digitalWrite(pins[j],1);
				}
				else{
					digitalWrite(pins[j],0);
				}
			}
		     }
	delayMS(4);
		}
	}
