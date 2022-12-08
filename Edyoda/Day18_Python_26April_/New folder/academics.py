

def learnerPoints(hours):

    return hours*1.6

def feesScholarship(earning,ipoints):

    if(earning<500000 and ipoints >70):
        return True
    else:
        return False


def finalEval(Project,MCQ):

    marks=Project+MCQ

    if(marks>80):
        return True
    else:
        return False
