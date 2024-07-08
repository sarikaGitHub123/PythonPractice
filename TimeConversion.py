


def validate(in_):
    pattern = r"\d\d:\d\d:\d\d[AaPp][Mm]"
    m = re.match(pattern, in_)
    return m

def timeConversion(s):
        hr=int(s[0:2])
        min=int(s[3:5])
        sec=int(s[6:8])
        dayTime=(s[8:])
        if('am'in s or 'AM' in s):
            if(hr==12):
                hr=0
        elif('pm'in s or 'PM' in s):
            if(hr==12):
                hr=12
            else:   
                hr = int(hr)+12
        if(hr<10):
            hr='0'+str(hr)
        if(min<10):
            min='0'+str(min)
        if(sec<10):
            sec='0'+str(sec)    
        time=str(hr)+':'+str(min)+':'+str(sec)
        return time

    

if __name__ == '__main__':

    s = input()

    result = timeConversion(s)
    print(result)