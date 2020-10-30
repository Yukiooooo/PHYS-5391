#!/usr/bin/env python

def offspring_select(target,num_child,mut_rate): 
    """
    This function an implementation of the Weasel Program written in python
    
    This experiment was created by Richard Dawkins,check the link for more info:
    http://en.wikipedia.org/wiki/Weasel_program
    
    Usage:
    in your command line, put this code in your current direction and then:
    $ python weasel_pro.py
    
    you'll get the results on your command window :D
    """
    # import useful modules
    import random # randomly creating characters, digits
    from string import ascii_uppercase as gene # import 'genes' for selection
    
    # initialization: claim variables & parameters
    gene = gene + ' '  # symbols (capital letters + space)
    print ("select gene from here: ", gene)
    new_parent = [] # select the most resemble child to the target in each generation
    
    # Construct random starting string of same length as target
    weasel = [] # used for storing the new created weasels offspring
    # we assume that the genes of the offspring could mutate, but the number of genes will
    # will not change, they always the same as the target
    for i in range(len(target)):
        weasel.append(random.choice(gene)) # randomly select a set of genes
        # get the first generation ==> parents
    
    # Main loop: construct mutated offspring, select best for next generation, stop when target reached
    gen = 0 # initialization of generation
    while new_parent != target: # Judging whether to get the target
        gen += 1 # create new generation
    
        #%% create a new list for storing mutations offspring
        child_list = []
        for i in range(num_child):
            # force the child as new parent
            child = weasel[:]
            # Iterate over digits in child, mutation is allowed any digits
            for digit in range(len(child)): # start the loop of offspring
                # replace the digits with randomly genes 
                if random.random() < mut_rate: # check if below the mutation rate
                    # Randomly select new gene 
                    old_gene = weasel[digit] # find the old gene digit
                    mutation = set(gene) - set(old_gene) # get the new gene library
                    new_gene = random.choice(list(mutation)) # replace the digits with new gene
    
                    # copy the new gene, complete the mutation process for child
                    child[digit] = new_gene
    
            # Add the mutated child to list of current childs
            child_list.append(child)
    
    
        #%% Accoding to the "Monkey Print Shakespeare", compare the offspring with 
        # the target one digit by one digit, then find most fit offspring 
        min_dif = len(target) + 1 # initialization of the minimum difference
        for child in child_list: # start loop of the offspring
    
            # Find number of positions that differ between kid and target
            dif = 0 # initialization of the difference
            for digit in range(len(target)): # start loop of the target
                if child[digit] != target[digit]: # compare every digit 
                    dif = dif + 1 # calculate the number of different digits
    
            # Keep bmost similar offspring
            if dif < min_dif: # find the most simialr one to the target
                min_dif = dif # copy different digits to the minimum difference
                new_parent = child # use the child as the new parent
                
        weasel = new_parent # use most similar offspring for next round of mutation
    
        #%% calculation of the printing info
        fitness = (len(target)-min_dif)/len(target) # check similarity between offspring & target
        output_string = "" # initialization of the output offspring
        for digit in range(len(target)): # compare every digits between offspring & target
            if new_parent[digit] == target[digit]: # keep the same digit 
                output_string += new_parent[digit] # copy the offspring digit to output offspring
            else:
                output_string += '*'  # keep the different digits as '*'
        print ("%s ==> Gen:%4d Dif: %3d Fit: %.4f rate: %.2f" % (output_string, gen, min_dif, fitness,random.random()))
        # when the target reached in offspring ==> stop the program
        if fitness == 1: # means target reached
            break # stop the WHOLE loop
        
    return gen # return the generation we need

#%% use the function for testing
    
# gen = offspring_select("METHINKS IT IS LIKE A WEASEL",5000,0.01) 
# print ("generations needed = ", gen) 



















