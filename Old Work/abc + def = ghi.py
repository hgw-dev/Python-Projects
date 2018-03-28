import timeit
start = timeit.default_timer()
count = 0
carry_unit = 0

for c in range(1,10):
    carry_unit = 0
    for f in range(1,10):
        if f != c:
            if f + c != 10:
                i = f + c
                if i > 10:
                    i = i - 10
                    carry_unit = 1
                if i != c and i != f:
                    for b in range(1,10):
                        if b != c and b != f and b != i:
                            for e in range(1,10):
                                if e != c and e != f and e != i and e != b:
                                    for h in range(1,10):
                                        if h != c and h != f and h != i and h != b and h != e:
                                            if carry_unit == 1:
                                                if b + e + 1 == h or b + e - 10 == h:
                                                    for a in range(1,9):
                                                        if a != c and a != f and a != i and a != b and a != e and a != h:
                                                            for d in range(1,9):
                                                                if d != c and d != f and d != i and d != b and d != e and d != h and d != a:
                                                                    if a + d < 10 and 10*a + b + 10*d + e < 100:
                                                                        for g in range(3,10):
                                                                            if a + d == g or a + d + 1 == g:
                                                                                if g != c and g != f and g != i and g != b and g != e and g != h and g != a and g != d:
                                                                                    if a*100 + b* 10 + c + d*100 + e*10 + f == g*100 + h*10 + i:
                                                                                        count = count + 1

                                            elif carry_unit == 0:
                                                if b + e == h or b + e - 10 == h:
                                                    for a in range(1,9):
                                                        if a != c and a != f and a != i and a != b and a != e and a != h:
                                                            for d in range(1,9):
                                                                if d != c and d != f and d != i and d != b and d != e and d != h and d != a:
                                                                    if a + d < 10 and 10*a + b + 10*d + e < 100:
                                                                        for g in range(3,10):
                                                                            if a + d == g or a + d + 1 == g:
                                                                                if g != c and g != f and g != i and g != b and g != e and g != h and g != a and g != d:
                                                                                    if a*100 + b* 10 + c + d*100 + e*10 + f == g*100 + h*10 + i:
                                                                                        count = count + 1

time = timeit.default_timer() - start
print("The number of unique solutions is", count)
print("This has been calculated in", time, "seconds")
