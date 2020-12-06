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

double df7(double x)
{
    return exp(x) - 4 * x + 1;
}

double f8(double x)
{
    return x * cos(x) - 3 * (x * x) + 4 * x - 1;
}

double df8(double x)
{
    return cos(x) - x * sin(x) - 6 * x + 4;
}

double f9(double x)
{
    return M_PI * x - exp(x);
}

double df9(double x)
{
    return M_PI - exp(x);
}

double f10(double x)
{
    return x * x - 4 * x + 2 - log(x);
}

double df10(double x)
{
    return 2 * x - 4 - (1 / x);
}

double f11(double m)
{
    //double g = 9.81;
    //double c = 18.32;
    //double v = 34.88;
    //double t = 7.22;
    //double e = exp(1);

    return 9.81 * m / 18.32 * (1 - pow(exp(1), (-(18.32/m)/7.22))) - 34.88;
}
/*
    int rows = 3;
    double chute[3] = {-1.11524, -2.49542, -0.24685};
    double matrix[3][4] = {{-2.03177, 0.40818, -0.57744, 2.76515}, 
                           {-0.88368, -4.45015, 2.52032, 0.28211}, 
                           {1.7885, 1.3987, -4.23335, 2.0998}};
    
    int rows = 4;
    double chute[4] = {-2.37917, 2.60325, 2.79379, 1.29619};
    double matrix[4][5] = {{-6.82693, -1.8299, -2.72428, -1.04886, -0.63892}, 
                           {-0.07539, 4.46569, -1.02667, 2.13974, -0.278}, 
                           {-1.61745, 1.86442, 5.29975, 0.59399, -0.87177}, 
                           {1.11451, 1.7397, -0.41972, 4.49783, 0.75046}};
                           
    int rows = 5;
    double chute[5] = {-2.17235, 1.31524, 0.13036, -2.76423, -1.07013};
    double matrix[5][6] = {{8.76212, -2.99902, -2.07349, 1.74435, 0.48242, 2.60548}, 
                           {1.79903, 9.85613, 1.71093, 2.24097, -2.64235, 0.10541}, 
                           {2.41455, -0.37162, 6.16894, -1.37429, -0.54564, -2.94572}, 
                           {2.76312, 2.26258, 1.42194, 10.77037, -2.85989, -2.76762},
                           {-0.68826, -0.58147, 0.6242, 1.41151, -4.76827, 0.44764}};
*/

int main(int argc, char const *argv[])
{
    
    int max_iter = 7;
    /*double a = 40; 
    double b = 200;
    bisection(f11, a, b, max_iter);*/
    

    jacobi(chute, rows, matrix, max_iter);
    return 0;
}