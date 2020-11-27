#include "ann.h"
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

void secant(double (*f)(double), double x0, double x1, int n)
{
    for (int i = 0; i < n; i++)
    {
        double fx0 = f(x0);
        double fx1 = f(x1);
        if (fx0 == fx1)
        {
            printf("Divisao por zero");
            return;
        }
        double x2;
        x2 = (x0 * fx1 - x1 * fx0) / (fx1 - fx0);
        x0 = x1;
        x1 = x2;
        printf("x%d = %.16f\n", i + 1, x2);
    }
}

