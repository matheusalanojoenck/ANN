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

double f11(double x)
{
    double g = 9.81;
    double c = 18.32;
    double v = 34.88;
    double t = 7.22;
    double m = x;

    return (g * m / c) * (1 - exp(-(c/m) * t)) - v;
}

double f12(double x)
{
    double g = 9.81;
    double c = x;
    double v = 32.85;
    double t = 9.91;
    double m = 73.81;

    return (g * m / c) * (1 - exp(-(c/m) * t)) - v;
}

double f13(double x)
{
    double g = 9.81;
    double H = x;
    double v = 9.6;
    double t = 4.71;
    double L = 3.73;

    return (sqrt(2*g*H) * tanh((sqrt(2*g*H) / (2 * L)) * t)) - v;
}

double f14(double x)
{
    double g = 9.81;
    double Q = 56.33;
    double y = x;
    double A = 2.38 * y + (pow(y, 2) / 2);
    double B = 2.38 + y;
    return 1 - (pow(Q, 2) / (g * pow(A, 3))) * B;
}

double f15(double x)
{
    double V = 2090.81;
    double h = x;
    double R = 8.74;

    return M_PI * pow(h,2) * ((3 * R - h) / 3) - V;
}

double f16(double x)
{
    double h = x;
    double r = 9.75;
    double vs = ( 4 * M_PI* pow(r, 3)) / 3; //volume total da esfera
    double V = -((320,39*vs/1000)-vs);
    //double V = vs / 1000000 / 67961;
    //V = 2638.53109668631;
    
    return ((M_PI * pow(h, 2)) / 3) * (3 * r - h) - V;
}

double f18(double x)
{
    double P0 = 1520593;
    double v = 193404;
    double P = 3057739;
    double lambda = x;
    double t = 365;

    return P0 * exp(lambda) + (v / lambda) * (exp(lambda) - 1) - P;
}

double f19(double x)
{
    double L = 4.57; 
    double r = 4.32;
    double V = 52.73;
    double h = x;

    return (L * (0.5 * M_PI * pow(r, 2) - pow(r, 2) * asin(h/r) - h * sqrt(pow(r, 2) - pow(h, 2))) - V);
}

double f20(double x)
{
    double g = 9.81;
    double t = 1;
    double w = x;
    return -(g/(2 * pow(w, 2))) * (sinh(w * t) - sin(w * t)) - 2.73;
}

double f21(double x)
{
    double l = x;
    //(17.14 - 2*l) * (9.01 - 2*l) * l
    //(772157/5000) - (523/5)*l + 12*pow(l,2)
    return (772157/5000) - (523/5)*l + 12*pow(l,2); 
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

/*
    int rows = 3;
    double chute[3] = {2.99445, -1.05469, 1.07509};
    double matrix[3][4] = {{-3.78819, -2.369, 0.11237, 2.05096}, 
                           {1.87038, 4.15914, -0.98195, 2.55916}, 
                           {1.5186, -1.68326, -4.50867, -2.46453}};
    
    int rows = 4;
    double chute[4] = {1.51554, 0.59033, 2.59659, -1.36953};
    double matrix[4][5] = {{5.70657, 1.59181, -2.13991, -0.40937, 1.19379}, 
                           {1.22447, 6.43517, -1.55641, -2.0888, -2.31753}, 
                           {-2.7192, 2.62558, -7.80922, -0.89896, -2.27104},
                           {0.00192, -0.49205, 1.87426, 3.93371, -1.12101}};
    int rows = 5;
    double chute[5] = {1.59229, 1.33797, -1.97841, -2.20639, 1.92066};
    double matrix[5][6] = {{-10.27212, -2.91537, -2.10697, -2.76979, -0.65572, -2.89636}, 
                           {2.77604, -8.67127, 1.35991, 0.84817, -1.86289, -1.28347}, 
                           {2.3006, 2.73188, -9.67662, 0.99453, 1.82535, 1.3744},
                           {0.62205, 1.73549, 2.0257, 6.60285, 0.39534, -2.40988},
                           {0.66962, -2.84655, -2.41102, 1.8601, -9.61156, 1.69424}};
*/

/*
    int rows = 4;
    double chute[4] = {-0.78049, 2.71578, 1.48246, -0.07112};
    double matrix[4][5] = {{5.03688, 0.273, -2.16656, -1.39779, -0.76352}, 
                           {2.55879, -7.07872, -0.97733, 2.34307, 0.52657}, 
                           {-0.74143, -2.68448, -4.96284, 0.33741, -2.80993},
                           {-0.13314, -2.83822, 2.465, 6.63589, -2.20213}};

    int rows = 4;
    double chute[4] = {1.72468, -2.31705, 2.46693, 0.25621};
    double matrix[4][5] = {{-5.17612, -1.03448, 2.06267, 0.35472, 1.3848}, 
                           {-1.5565, 7.28045, -1.38478, 2.61492, 0.76509}, 
                           {-1.86749, 0.06341, -5.52904, -1.87389, 1.44258},
                           {-0.08474, -2.79924, 1.46593, 6.07416, -0.56471}};

*/

double f_prova(double x)
{
    return pow(x, 3) - 5.0;
}

double df_prova(double x)
{
    return 3 * pow(x, 2);
}
int main(int argc, char const *argv[])
{
    int max_iter = 4;
    //double a = 2.07515;
    //double b = 2.80285;

    //bisection(f_prova, a, b, max_iter);
    //newton(f_prova, df_prova, a, max_iter);
    //secant(f_prova, a, b, max_iter);
    //false_position(f_prova, a, b, max_iter);

    //jacobi(chute, rows, matrix, max_iter);
    //seidel(chute, rows, matrix, max_iter);
    return 0;
}