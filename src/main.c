#include <stdio.h>
#include <stdlib.h>
#include "ann.c"

double f(double x)
{
    return x*x*x - 2.0;
}

double f1(double x)
{
    return x*x - 7;
}

double df1(double x)
{
    return 2 * x;
}

double f2(double x)
{
    return sqrt(x) - cos(x);
}

double df2(double x)
{
    return 1/(2*sqrt(x)) + sin(x);
}

double f3(double x)
{
    return 2*(x + 1) * (x - 0.5) * (x - 1);
}

double df3(double x)
{
    return 6*pow(x,2) - 2*x - 2;
}

double f4(double x)
{
    return x*x*x - 7*(x*x) + 14*x - 7;
}

double df4(double x)
{
    return 3*pow(x, 2) - 14*x + 14;
}

double f5(double x)
{
    return pow(x, 4) - 2*pow(x, 3) - 3*(x*x) + 3*x + 2;
}

double df5(double x)
{
    return 4*pow(x, 3) - 6*(x*x) - 6*x + 3;
}

double f6(double x)
{
    return x - pow(2, -x);
}

double df6(double x)
{
    return (pow(2, x) + log(2))/pow(2, x);
}

double f7(double x)
{
    return x - pow(2, -x);
}

int main(int argc, char const *argv[])
{
    int max_iter = 10;
    double a = -0.0695; 
    double b = 1.48019;

    bisection(f7, a, b, max_iter);

    return 0;
}