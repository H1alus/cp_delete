#the script eliminates all the copies of a file listed with '(n)' 
#n as the number of the reached copies in the directory
#to use the script just put it in the directory where the copies are found
#then type in the terminal:
# $python3 copy_delete.py
# if some files have root only access execute it as sudo (if needed)
 
import os
import sys

def n_copy_finder(content = []):
    n_copy = 0
    max_n_cp = 0
    for _ in range(len(content)):
        index_1st_par = content[_].rfind('(')
        index_2nd_par = content[_].rfind(')')
        if index_1st_par != -1 and index_2nd_par != -1:
            diff_pars = index_2nd_par - index_1st_par
            if diff_pars == 2:
                n_copy = int(content[_][index_1st_par + 1])
            elif diff_pars > 2:   
                n_copy = int(content[_][index_1st_par + 1 : index_2nd_par])
        if n_copy > max_n_cp:
            max_n_cp = n_copy
    return max_n_cp

def main():
    content = os.listdir()
    max_copies = n_copy_finder(content) + 1
    for j in range(max_copies):
        for i in range(len(content)):
            if content[i].rfind('({})'.format(j)) != -1:
                original_name = content[i].replace('({})'.format(j), '')
                original_name = original_name.replace(' .', '.', 1)
                for k in range(len(content)):
                    if original_name == content[k] and k != i:
                        os.remove(content[i])
                        break
    print('you may find some copies in the folder because the original was not found\n\
or the notation is not supported')
                
if __name__ == "__main__":
    main()
