def getgroup(cur_entry, cols):

    d = { 
        "Anamnese":"",
        "Allmennt":"",
        "Svelg":"",
        "Collum":"",
        "Nasalt":"",
        "Otologisk":"",
        "Pulm":"",
        "Lab":""
    }
    
    i=2
    while i<=35:
        if (cur_entry[0][i]!=None):
            lval_in_dict = cols[i].rsplit("_",1)[0]
            if (cur_entry[0][i]=="0"):
                d[lval_in_dict] += "Ikke "
            d[lval_in_dict] += cols[i].split("_",1)[1] + ". "
            for ent in ("Hud","AT","Dager syk","HF","RF"):
                if (cols[i].split("_",1)[1]==ent):
                    d[lval_in_dict] = d[lval_in_dict][:-2] + ": " + str(cur_entry[0][i])+ "."
        i+=1
    return {k: v for k, v in d.items() if v is not ""}

def nicify_group2str(cur_entry,cols):
    datastr = ""
    for obj in getgroup(cur_entry,cols).items():
        datastr += obj[0]
        addspace = 10 - len(str(obj[0]))
        while addspace > 0:
            datastr+= " "
            addspace-=1
        # if (obj[0]=="Anamnese"): addspace = "\t"
        if (obj[1]==""):
            return
        datastr += obj[1] + "\n"
    return datastr