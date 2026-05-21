
def l_prime(x, theta):
    sum = 0;
    for x_i in x:
        sum += -2*(theta-x_i) / (1+(theta-x_i)**2)
    return sum
    

def l_twoprime(x, theta):
    sum = 0;
    for x_i in x:
        sum += -2 / (1+(theta-x_i)**2)**2
    return sum


x = [-1.94, 0.59, -5.98, -0.08, -0.77]
theta = x[0]

for i in range(10):
    print("iteration #{}:".format(i))
    
    lp = l_prime(x, theta)
    lpp = l_twoprime(x, theta)

    new_theta = theta - lp / lpp
    
    print("theta_{} = {}".format(i, theta))
    print("-> l_prime: {}, l_twoprime: {}".format(lp, lpp))
    print("=> theta_{} = {}\n".format(i+1, new_theta))

    theta = new_theta
    
