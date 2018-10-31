#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <string.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>

#define SERVER_IP "192.168.1.109"
#define PORT 12580

int main()
{
	printf("client starting...\n");
	int c_socket;
	struct sockaddr_in addr;
	char buffer[25];
	if((c_socket = socket(AF_INET, SOCK_STREAM, 0))<0)
	{
		perror("socket error");
		exit(1);
	}
	bzero(&addr, sizeof(addr));
	addr.sin_family = AF_INET;
	addr.sin_port = htons(PORT);
	if(inet_pton(AF_INET, (char *)SERVER_IP, &addr.sin_addr) <=0)
	{
		exit(0);
	}
	
	if(connect(c_socket,(struct sockaddr*)&addr, sizeof(addr))<0)
	{
		perror("connect failed\n");
		exit(1);
	}

	
	for(;;)
	{
		int x = 0;
		static unsigned char y = 0;
		memset(buffer, 0, sizeof(buffer));
		for(x=1; x<25; x++)
		{
			y = y + 5;
			 buffer[x] = y;

			 printf("%d\n",y);
		
			 send(c_socket, buffer, sizeof(buffer),0);
			if(send(c_socket,buffer,sizeof(buffer),0) <0)
			{
			perror("send buffer error\n");
			exit(1);
			}
			usleep(1000);
		}
	}
}
