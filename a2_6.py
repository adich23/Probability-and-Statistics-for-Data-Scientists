import numpy

def rand_walk(init_val, final_high, final_low, prob, N):
    
    nleft = 0
    nright = 0
    csum = 0
    
    left_end = final_low
    right_end = final_high
    p = prob
    n = N
    
    for i in range(0, n):
        
        run_val = init_val
        while(1):
            
            if((run_val == right_end) or (run_val == left_end)):
                break;
            
            u = numpy.random.uniform(0, 1)
            if(u < p):
                run_val = run_val + 1
            else:
                run_val = run_val - 1
        
        csum = csum + run_val
        
        if(run_val == right_end):
            nright = nright + 1
        else:
            nleft = nleft + 1
    
    num = float(n)
    nright = float(nright)
    a = nright / num

    nleft = float(nleft)
    b = nleft / num

    csum = float(csum)
    c = csum / num
    return a, b, c

[a, b, c] = rand_walk(100, 150, 0, 0.5, 10000)
print "TEST CASE 1 >> (answer for 6(a)) ", a, "\t(answer for 6(b)) ", b, "\t(answer for 6(c)) ", c
[a, b, c] = rand_walk(100, 200, 0, 0.52, 10000)
print "TEST CASE 2 >> (answer for 6(a)) ", a, "\t(answer for 6(b)) ", b, "\t(answer for 6(c)) ", c
[a, b, c] = rand_walk(200, 250, 0, 0.54, 10000)
print "TEST CASE 3 >> (answer for 6(a)) ", a, "\t(answer for 6(b)) ", b, "\t(answer for 6(c)) ", c