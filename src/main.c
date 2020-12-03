#include <stdio.h>
#include <stdlib.h>
#include "ann.c"
#include <math.h>

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
    return exp(x) - 2 * (x * x) + x - 1.5;
}

double f8(double x)
{
    return x * cos(x) - 3 * (x * x) + 4 * x - 1;
}

double f9(double x)
{
    return M_PI * x - exp(x);
}

double f10(double x)
{
    return x * x - 4 * x + 2 - log(x);
}

double f11(double m)
{
    double v, g, c, t, e;
    e = exp(1);
    g = 9.81;
    c = 18.32;
    v = 34.88;
    t = 7.22;

    return ((9.81 * m) / 18.32) * (1 - exp(-(18.32/m)/7.22)) - 34.88;
}

int main(int argc, char const *argv[])
{
    int max_iter = 4;
    double a = 1.16754; 
    double b = 4.42187;

    secant(f10, a, b, max_iter);

    return 0;
}