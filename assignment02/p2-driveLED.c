#define TURN_SIGNAL_DURATION 0.5

void driveTurnSignal()
{
	unsigned char* input = 0x100A;
	unsigned char* output = 0x100B;
	static int state = 0;
	switch (*input & 0b11)
	{
	case 0b00:
		// off
		*output = 0b00000000;
		state = 0;
		break;
	case 0b01:
		// right
		*output = state ? 0b00000000 : 0b00001111;
		state = !state;
		break;
	case 0b10:
		// left
		*output = state ? 0b00000000 : 0b11110000;
		state = !state;
		break;
	case 0b11:
		// hazard
		*output = 0b11111111;
		state = !state;
		break;
	}
}

void driveTurnSignal_Sweep()
{
	unsigned char* input = 0x100A;
	unsigned char* output = 0x100B;
	static unsigned char* state = 0b00000000;
	switch (*input & 0b11)
	{
	case 0b00:
		// off
		state = 0b00000000;
		break;
	case 0b01:
		// right
		if (state & 0b00000001)
			state = 0b00000000;
		else
			state = (state >> 1) | 0b00001000;
		break;
	case 0b10:
		// left
		if (state & 0b10000000)
			state = 0b00000000;
		else
			state = (state << 1) | 0b00001000;
		break;
	case 0b11:
		// hazard
		state ^= 0b11111111;
		break;
	}
	*output = state;
}
