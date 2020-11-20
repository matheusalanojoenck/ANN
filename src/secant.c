#include <stdio.h>
#include <stdlib.h>

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

int main(int argc, char const *argv[])
{
    double x0 = 1, x1 = 0;
    int max_iter = 50;
    double f (double x)
    {
        return x*x*x - 2;
    }

    secant(f, x0, x1, max_iter);

    return 0;
}
