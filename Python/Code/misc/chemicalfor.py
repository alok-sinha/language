def countOfAtoms(formula):
        def countAtoms(formula):
            n = len(formula)
            i = 0
            e = None
            counts = {}
            
            while i < n:
                print i
                if formula[i].islower():
                    e = e + formula[i]
                    i += 1
            
                elif formula[i] == '(':
                    if e != None:
                        if e in counts:
                            counts[e]  += 1
                        else:
                            counts[e] = 1
                    
                    ind = formula.rindex(')')
                    d = countAtoms(formula[i+1:ind])
                    i = ind + 1
                    e = None
            
                elif formula[i].isdigit():
                    #print "Found digit"
                    num = formula[i]
                    i += 1
                    while i < n:
                        if formula[i].isdigit():
                            num = num + formula[i]
                            i += 1
                        else:
                            i -= 1
                            break
                        
                    repeat = int(num)
                    #Update count
                    #print repeat,formula[i-1] 
                    if e is None:
                        for el in d:
                            if el in counts:
                                counts[el] += repeat*d[el]
                            else:
                                counts[el] = repeat*d[el]
                    else:
                        if e in counts:
                            counts[e] += repeat
                        else:
                            counts[e] = repeat
                    i += 1
                    e = None
                else:
                    if e != None:
                        if e in counts:
                            counts[e] += 1
                        else:
                            counts[e] = 1
                            
                    e = formula[i]
                    i += 1

            if e != None:
                if e in counts:
                    counts[e] += 1
                else:
                    counts[e] = 1
            
            #print "Returnmomg", counts
            return counts 
            
        """
        :type formula: str
        :rtype: str
        """
        
        counts = countAtoms(formula)
        s = ""
        print counts
        for el,count in sorted(counts.items()):
            if count > 1:
                s += el + str(count)
            else:    
                s += el
        
        return s

print countOfAtoms("((N42)24(OB40Li30CHe3O48LiNN26)33(C12Li48N30H13HBe31)21(BHN30Li26BCBe47N40)15(H5)16)14")        