#include <stdio.h>

void main()
{
	for (float y = 2; y > -2; (y -= 0.1) && (putchar('\n')))

		for (float x = -2; x < 2; x += 0.05)

			putchar((x * x + y * y - 1) * (x * x + y * y - 1) * (x * x + y * y - 1) - x * x * y * y * y <= 0 ? '*' : ' ');
}
