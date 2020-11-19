#include <stdio.h>
#include <stdlib.h>

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

int main(int argc, char const *argv[])
{
    int max_iter = 10;
    double a = 0.8027595328839907; 
    double b = 2.4493542821107273;

    bisection(f, a, b, max_iter);
    return 0;
}
