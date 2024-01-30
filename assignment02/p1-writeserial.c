#include <unistd.h>

void writeSerial(unsigned char* data, int size)
{
	unsigned char* port = (unsigned char*)0x10A4;
	unsigned char* status = (unsigned char*)0x10A5;
	while (size > 0)
	{
		if (*status & 0b10000)
		{
			sleep(1);
			continue;
		}
		*port = *data;
		data++;
		size--;
	}
}
