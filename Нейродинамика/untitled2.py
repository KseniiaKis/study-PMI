import numpy as np 

def rhs(phi,gamma):
    return (10 * (gamma**2 - 1) * (np.arctan((gamma * np.tan(phi/10) - 1)/(gamma**2 - 1)**(1/2))) - np.arctan((gamma * np.tan(np.pi/10) - 1)/(gamma**2 - 1)**(1/2)))/(gamma**2 - 1)**(1/2)

def rhs1(gamma):
    return(10 * np.pi/(gamma**2 - 1)**(1/2))

my_file = open("BabyFile.txt", "w+")

my_file.write("gamma = 0.1\n")
my_file.write("omega = " + str(rhs1(0.1))+"\n")
my_file.write("omega1 = " + str(rhs(3*np.pi,0.1))+"\n")
my_file.write("omega2 = " + str(rhs(5*np.pi,0.1))+"\n")
my_file.write("omega3 = "+ str(rhs(7*np.pi,0.1))+"\n")
my_file.write("omega4 = "+ str(rhs(9*np.pi,0.1))+"\n")
my_file.write("omega5 = "+ str(rhs(11*np.pi,0.1))+"\n")
my_file.write("omega1 + omega2 + omega3 + omega4 + omega5 = "+ str(rhs(11*np.pi,0.1)+rhs(5*np.pi,0.1)-rhs(7*np.pi,0.1)+rhs(9*np.pi,0.1)-rhs(11*np.pi,0.1))+"\n")

my_file.write("\n")

my_file.write("gamma = 0.5\n")
my_file.write("omega = " + str(rhs1(0.5))+"\n")
my_file.write("omega1 = "+ str(rhs(3*np.pi,0.5))+"\n")
my_file.write("omega2 = "+ str(rhs(5*np.pi,0.5))+"\n")
my_file.write("omega3 = "+ str(rhs(7*np.pi,0.5))+"\n")
my_file.write("omega4 = "+ str(rhs(9*np.pi,0.5))+"\n")
my_file.write("omega5 = "+ str(rhs(11*np.pi,0.5))+"\n")
my_file.write("omega1 + omega2 + omega3 + omega4 + omega5 = "+ str(rhs(11*np.pi,0.5)+rhs(5*np.pi,0.5)+rhs(7*np.pi,0.5)+rhs(9*np.pi,0.5)+rhs(11*np.pi,0.5))+"\n")

my_file.write("\n")

my_file.write("gamma = 0.95\n")
my_file.write("omega = " + str(rhs1(0.95))+"\n")
my_file.write("omega1 = "+ str(rhs(3*np.pi,0.95))+"\n")
my_file.write("omega2 = "+ str(rhs(5*np.pi,0.95))+"\n")
my_file.write("omega3 = "+ str(rhs(7*np.pi,0.95))+"\n")
my_file.write("omega4 = "+ str(rhs(9*np.pi,0.95))+"\n")
my_file.write("omega5 = "+ str(rhs(11*np.pi,0.95))+"\n")
my_file.write("omega1 + omega2 + omega3 + omega4 + omega5 = "+ str(rhs(11*np.pi,0.95)+rhs(5*np.pi,0.95)+rhs(7*np.pi,0.95)+rhs(9*np.pi,0.95)+rhs(11*np.pi,0.95))+"\n")

my_file.write("\n")

my_file.write("gamma = 1.05\n")
my_file.write("omega = " + str(rhs1(1.05))+"\n")
my_file.write("omega1 = "+ str(rhs(3*np.pi,1.05))+"\n")
my_file.write("omega2 = "+ str(rhs(5*np.pi,1.05))+"\n")
my_file.write("omega3 = "+ str(rhs(7*np.pi,1.05))+"\n")
my_file.write("omega4 = "+ str(rhs(9*np.pi,1.05))+"\n")
my_file.write("omega5 = "+ str(rhs(11*np.pi,1.05))+"\n")
my_file.write("omega1 + omega2 + omega3 + omega4 + omega5 = "+ str(rhs(11*np.pi,1.05)+rhs(5*np.pi,1.05)+rhs(7*np.pi,1.05)+rhs(9*np.pi,1.05)+rhs(11*np.pi,1.05))+"\n")

my_file.write("\n")

my_file.write("gamma = 5\n")
my_file.write("omega = " + str(rhs1(5))+"\n")
my_file.write("omega1 = "+ str(rhs(3*np.pi,5))+"\n")
my_file.write("omega2 = "+ str(rhs(5*np.pi,5))+"\n")
my_file.write("omega3 = "+ str(rhs(7*np.pi,5))+"\n")
my_file.write("omega4 = "+ str(rhs(9*np.pi,5))+"\n")
my_file.write("omega5 = "+ str(rhs(11*np.pi,5))+"\n")
my_file.write("omega1 + omega2 + omega3 + omega4 + omega5 = "+ str(rhs(11*np.pi,5)+rhs(5*np.pi,5)+rhs(7*np.pi,5)+rhs(9*np.pi,5)+rhs(11*np.pi,5))+"\n")

my_file.close()