HSE = 14745600
min = 0
min1 = 0
for i in range(2, 64):
    if ((HSE/i) >= 950000) and ((HSE/i) <= 2100000):
        for j in range(50, 433):
            if ((HSE/i*j) >= 100000000) and ((HSE/i*j) <= 432000000):
                for k in range(2, 10, 2):
                    if ((HSE/i*j/k) >= 24000000) and ((HSE/i*j/k) <= 180000000):
                        if not min:
                            min = abs((HSE/i*j/k) - 170666667)
                            print(i, j, k, min)
                        else:
                            if abs((HSE/i*j/k) - 170666667) < min:
                                min = abs((HSE / i * j / k) - 170666667)
                                print(i, j, k, min)
                                
for i1 in range(2, 64):
    if ((HSE/i1) >= 950000) and ((HSE/i1) <= 2100000):
        for j1 in range(50, 433):
            if ((HSE/i1*j1) >= 100000000) and ((HSE/i1*j1) <= 432000000):
                for k1 in range(2, 10, 2):
                    if ((HSE/i1*j1/k1) >= 24000000) and ((HSE/i1*j1/k1) <= 216000000):
                        if not min1:
                            min1 = abs((HSE/i1*j1/k1) - 213333333)
                            print(i1, j1, k1, min1)
                        else:
                            if abs((HSE/i1*j1/k1) - 213333333) < min1:
                                min1 = abs((HSE / i1 * j1 / k1) - 213333333)
                                print(i1, j1, k1, min1)
                        
pass