#include <stdio.h>
#include <stdlib.h>

void newton (double (*f)(double), double (*df)(double), double x0, double n)
{
    double xn;
    for (int i = 0; i < n; i++)
    {
        xn = x0 - f(x0) / df(x0);
        x0 = xn;
        printf("x%d = %.16f\n" , i + 1, xn);
    }
}



int main(int argc, char const *argv[])
{
    double x0 = 10;
    int max_iter = 20;

    double f(double x)
    {
        return x*x*x - 2;
    }

    double df(double x)
    {
        return 3 * x*x;
    }

    newton(f, df, x0, max_iter);

    return 0;
}