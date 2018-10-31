#include <stdio.h>
#include <wiringPiI2C.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>
#include <stdlib.h>
#include <time.h>

#include <wiringPi.h>


#define SOCKET_PORT 12580
#define MAX_CONN 5

int main()
{
	int fd;
	fd = wiringPiI2CSetup(0x15);
	printf("starting nightlight server on port 12580\n");
	//定义socket fd 
	int s_fd = socket(AF_INET, SOCK_STREAM, 0);
	//定义sockaddr_in
	struct sockaddr_in s_saddr;
	s_saddr.sin_family = AF_INET;
	s_saddr.sin_port = htons(SOCKET_PORT);
	s_saddr.sin_addr.s_addr = htonl(INADDR_ANY);
	
	//bind,绑定成功返回0， 失败返回-1
	if(bind(s_fd, (struct sockaddr *)&s_saddr, sizeof(s_saddr)) !=0)
	{
		perror("bind failed, please check your port and ip addr");
		exit(1);
	}
	//listen，成功返回0， 失败返回-1
	if(listen(s_fd, MAX_CONN) !=0)
	{
		perror("listen section is failed, please check s_fd and BACKLOG");
		exit(1);
	}
	//客户端套接字4
	char buffer[1024];
	struct sockaddr_in c_addr;
	socklen_t length; 
        //成功返回非负描述字， 出错返回-1
	int conn = accept(s_fd, (struct sockaddr *)&c_addr, &length);
	if(conn<0)
	{
		perror("Connet failed!");
		exit(1);
	}

		memset(buffer,0, sizeof(buffer));

	for(;;)
	{
		while(conn <= 0){
			sleep(1);
		}

		int len = recv(conn, buffer, sizeof(buffer),0);

	        clock_t start, finish;  
	        double  duration;  
	        start = clock();  


		for(int i=1; i<25; i++)
		{
			wiringPiI2CWriteReg8(fd,i,buffer[i]);
		}
		printf("-------------------");

	        finish = clock();  
        	duration = (double)(finish - start) / CLOCKS_PER_SEC;
		printf("%f \n",duration);

		fflush(stdout);
		if(len <= 0) conn = accept(s_fd, (struct sockaddr *)&c_addr, &length);
	}
	
}
