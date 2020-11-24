#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void bisection(double (*f)(double), double a, double b, int n)
{
    if (f(a) * f(b) < 0)
    {
        double m = 0;
        for (int i = 0; i < n; i++)
        {
            m = (a + b) / 2;
            if (f(m) == 0)
            {
                printf("A raiz procurada e %.16f\n", m);
                return;
            }
            printf("x%d = %.16f\n", i + 1, m);
            if (f(a) * f(m) < 0)
            {
                b = m;
            }
            else
            {
                a = m;
            }
        }
    }
    else
    {
        printf("O Terema de Bolzano nao sabe dizer se existe raiz para f nesse interfalo");
    }
}

double f(double x)
{
    return x*x*x - 2.0;
}

double f2(double x)
{
    return x*x - 7;
}

double f3(double x)
{
    return sqrt(x) - cos(x);
}

double f4(double x)
{
    return 2*(x + 1) * (x - 0.5) * (x - 1);
}

double f5(double x)
{
    return x*x*x - 7*(x*x) + 14*x - 7;
}

double f6(double x)
{
    return pow(x, 4) - 2*pow(x, 3) - 3*(x*x) + 3*x + 2;
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
