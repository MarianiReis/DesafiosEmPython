#Given the participants' score sheet for your University Sports Day, you are required to find the runner-up
#  score. You are given  scores. Store them in a list and find the score of the runner-up.
#Input Format
#The first line contains . The second line contains an array   of  integers each separated by a space.



if __name__ == '__main__':


    n = input()
    arr = list(map(int, n))


    runner_up = list(set(arr))  #converte para um conjunto, remove as duplicatas
    runner_up.sort(reverse=True) #ordena em ordem decrescente


    print(runner_up[1])  


