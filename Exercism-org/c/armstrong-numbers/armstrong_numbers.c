#include "armstrong_numbers.h"
#include "math.h"
bool is_armstrong_number(int candidate)
{
  if (candidate < 10)
  {
    return true;
  }

  int temp = candidate;
  int counter = 0;

  do 
  {
    temp /= 10;
    ++counter;

  } while (temp != 0);

  temp = candidate;
  int sum = 0;
  int unit_number;

  do 
  {
    unit_number = temp % 10;
    sum += pow(unit_number, counter);
    temp /= 10;

  } while (temp != 0);
  return (sum == candidate);

}

