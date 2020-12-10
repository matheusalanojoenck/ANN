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

void newton(double (*f)(double), double (*df)(double), double x0, double n)
{
    double xn;
    for (int i = 0; i < n; i++)
    {
        xn = x0 - f(x0) / df(x0);
        x0 = xn;
        printf("x%d = %.16f\n", i + 1, xn);
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
        printf("x%d = %.16f\n", i + 2, x2);
    }
}

void false_position(double (*f)(double), double a, double b, int n)
{
    if (f(a) * f(b) < 0)
    {
        for (int i = 0; i < n; i++)
        {
            double fa = f(a);
            double fb = f(b);
            double c;
            c = (a * fb - b * fa) / (fb - fa);
            if (f(c) == 0)
            {
                printf("Raiz de f encontrada =>  %.16f", c);
                return;
            }
            printf("x%d = %.16f\n", i + 1, c);
            if (fa * f(c) < 0)
            {
                b = c;
            }
            else
            {
                a = c;
            }
        }
    }
    else
    {
        printf("O intervalo [%.16f, %.16f] nao serve.", a, b);
    }
}

void jacobi(double *chute, int rows, double matrix[rows][rows + 1], int n)
{
    double temp_arr[rows];
    for (int i = 0; i < n; i++)
    {
        for (int r = 0; r < rows; r++)
        {
            double temp = 0;
            temp += matrix[r][rows];
            for (int c = 0; c < rows; c++)
            {
                if (r != c)
                {
                    temp -= chute[c] * matrix[r][c];
                }
            }
            temp /= matrix[r][r];
            printf("x%d, %d = %.16f\n", r + 1, i + 1, temp);
            temp_arr[r] = temp;
        }
        printf("\n");
        for (int k = 0; k < rows; k++)
        {
            chute[k] = temp_arr[k];
        }
    }
}

void seidel(double *chute, int rows, double matrix[rows][rows + 1], int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int r = 0; r < rows; r++)
        {
            double temp = matrix[r][rows];
            for (int c = 0; c < rows; c++)
            {
                if (r != c)
                {
                    temp -= chute[c] * matrix[r][c];
                }
            }
            temp /= matrix[r][r];
            printf("x%d, %d = %.16f\n", r + 1, i + 1, temp);
            chute[r] = temp;
        }
        printf("\n");
    }  
}

