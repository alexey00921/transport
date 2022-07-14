from cvxopt.modeling import variable, op
import time
start = time.time()
x = variable(9, 'x')
c= [7,3,6,4,8,2,1,5,9]
z=(c[0]*x[0] + c[1]*x[1] +c[2]* x[2] +c[3]*x[3] + c[4]*x[4] +c[5]* x[5]+c[6]*x[6] +c[7]*x[7] +c[8]* x[8])
mass1 = (x[0] + x[1] +x[2] <= 74)

mass2 = (x[3] + x[4] +x[5] <= 40)
mass3 = (x[6] + x[7] + x[8] <= 36)
mass4 = (x[0] + x[3] + x[6] == 20)
mass5 = (x[1] +x[4] + x[7] == 30)
mass6 = (x[2] + x[5] + x[8] == 30)

x_non_negative = (x >= 0)    
problem =op(z,[mass1,mass2,mass3,mass4 ,mass5,mass6,x_non_negative])
problem.solve(solver='glpk')  
print("Результат Xopt:")
for i in x.value:
         print(i)
print("Стоимость доставки:")
print(problem.objective.value()[0])
stop = time.time()
print ("Время :")
print(stop - start)