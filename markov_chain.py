#This program works with 5 states to compute the stationary distribution along with
#the component wise difference between p_50 and the stationary distribution. Numpy
#will be imported since it provides us with convenient tools to manipulate arrays
#along with computing eigenvalues of matrices.
import numpy 
#We will be using a fixed number of states = 5. We will be using the transition
#rule 50 times. We will use a margin of error of 1e^-5 as a means to determine
#the seperation between p_50 and the stationary distribution.
num_states = 5
num_transrule = 50
margin_error = 1e-5
#From here we create a random 5 by 5 matrix (Matrix P) using the np.random.rand function and normalize it using the
#formula below. (Then print to the user.)
P_matrix = numpy.random.rand(num_states, num_states)
P_matrix = P_matrix/(P_matrix.sum(axis=1)[:,numpy.newaxis])
print("Matrix P with normalized rows: ")
print(P_matrix)
print()
print()
#Then we create a random vector with 5 values. (Vector p) and normalize it using the
#formula below. (Then print to the user.)
p_vector = numpy.random.rand(num_states)
p_vector = p_vector/(p_vector.sum())
print("Normalized vector p: ")
print(p_vector)
print()
print()
#From here we apply the transition rule 50 times to vector p and obtain p_50 to compare
#with the stationary distribution by using a for loop. (For each iteration in the for loop we are using
#the formula P^Tp = p_hat where need to use dot product.)
#P_matrix.T allows us to access the transpose of Matrix P. After computing p_50
#we print it to the user.
for i in range(0,num_transrule):
    p_vector = P_matrix.T.dot(p_vector)
print("p_50: ")
print(p_vector)
print()
print()
#Then we must compute the stationary distribution to compare it with p_50. First we find the eigenvalue and eigenvectors of
#P transpose using the np.linalg.eig function and use these to find the eigenvector v which corresponds to the eigenvalue closest to 1. Then we need to
#normalize this eigenvector to obtain the sstationary distribution. (Which we print to the user.)
eigen_val, eigen_vec = numpy.linalg.eig(P_matrix.T)
stationary_distribution = eigen_vec[:,numpy.argmin(abs(eigen_val - 1.0))].real
stationary_distribution = stationary_distribution/(stationary_distribution.sum())
print("Stationary distribution: ")
print(stationary_distribution)
print()
print()
#Lastly, we compute the componenet wise difference between p_50 and the stationary distribution. If each element difference is less
#than the margin of error of 1e^-5, then we print the statements in the if condition. Otherwise we print the statement
#in the else condition. Regardless of which condition we enter, the differences itself will be printed to the user.
comp_difference = abs(stationary_distribution - p_vector)
if all(comp_difference < margin_error):
    print("The component wise difference between p_50 and the stationary distribution is: " + str(comp_difference))
    print("p_50 and the stationary distribution match with each other within 1e-5.")

else:
    print("The component wise difference between p_50 and the stationary distribution is: " + str(comp_difference))
    print("p_50 and the stationary distribution do not match with each other within 1e-5.")
