from numpy import *
from numpy import random as rd
import sys, getopt


### instance parameters

path_to_instance_dir= "/home1/djukanovic/lcps/src/srcAugust/lcps/src/rlcs/instances/large-random/"
f_train = open("train_link.txt", "w") # file to save the train link:
f_validation = open("validation_link.txt", "w") # file to save the validation link

## function to generate a train link for training the neural network 

def generate_train_validate_link(n, m, k, len_p, sigma, size_group):
    
    
    for index in range(size_group): 
    
        path_instance = path_to_instance_dir + str(m) + "_" + str(n) + "_" +  str(k) + "_"  + str(int(n * len_p)) + "_" + str(sigma) + "_" + str(index) + ".txt"
        
        if  index in [0, 1]: 
            f_train.write(" -train " + path_instance + " " )
        elif index == 2: #validation instance 
            f_validation.write(" -validation " + path_instance + " " )
        else:
            continue


if __name__ == "__main__":
   
   nx = [200, 500, 1000]
   mx = [3, 5, 10]
   kx = [3, 5, 10]
   lenpx = [0.01, 0.02, 0.05]
   
   
   for n in nx:
      for m in mx:
          for k in kx:
              for lx in lenpx:
                  for sigma in [4, 20]:
                      generate_train_validate_link(n, m, k, lx, sigma, 5) # sigma, size_group)  
        

   # close the stream 
   f_train.close() 
   f_validation.close()
