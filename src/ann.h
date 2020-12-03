#ifndef ANN_H
#define ANN_H

void bisection(double (*f)(double), double a, double b, int n);
void newton (double (*f)(double), double (*df)(double), double x0, double n);
void secant(double (*f)(double), double x0, double x1, int n);
void false_position(double (*f)(double), double a, double b, int n);
void jacobi(double *guess, int rows, double matrix[rows][rows + 1], int n);

#endif


