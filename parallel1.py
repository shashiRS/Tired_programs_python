import sys, os, time
from subprocess import Popen, list2cmdline
def exec_commands(cmds):
    print("Heloo")
    flag1=False
    flag2=False
    strnumber=''
    stremail=''
    print(link[i])

    try:

        time.sleep(5)
        f = urllib.urlopen(link[i])
        s = f.read()
        my_listp=findall(r"\+91[\s-]?\d*[-\s]?\d*[\s-]?\d{3}",s)
        # logging.debug(re.findall(r"(?:(?:\+?1\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?",s))
        my_liste=re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.(?:com|in|co.in|org|edu|gov|uk|net|ca|mil)",s)

        kk=re.findall(r"\+?\d{1,3}?[- .]?\(?(?:\d{2,3})\)?[- .]?\d\d\d[- .]?\d\d\d\d",s)
        kk1 = set(kk)
        content=list(kk1)
        for k in range(1,7):
            content = [x for x in content if not x.startswith(str(k))]
            my_listp.extend(content)
               
                
            domm=link[i].split('/')[2]
                                                
            if 'www' in domm:
                domains.append(domm.split('www.',1)[1])
                domn=domm.split('www.',1)[1]


            else:
                domains.append(domm)
                domn=domm
                #fnd domain using whois 
            for dom in domains:
                domain = whois.whois(dom)
                
            if len(domain.emails)>5:
                for j in range(1):
                     stremail+=domain.emails+','

            else:
                for j in domain.emails:
                    stremail+=j+','
            if domain.phone: 
                for j in domain.phone:
                    strnumber+=j+','

            my_set2 = set(my_liste)
            email=list(my_set2)
            my_set1 = set(my_listp)
            phone_number=list(my_set1)
            lennumber=len(phone_number)
            lenemail=len(email)

            if lenemail==0:
                flag1=True
            if lennumber==0:
                flag2=True
            if flag1 and flag2==True:
                logging.debug(link[i])
                if 'facebook' in link[i]:
                    print("Social media")
                else:
                    s = BeautifulSoup(f.content,'lxml')
                            
                        logging.debug(link[i])
                        url2=link[i].split('/')[2]
                        # print(s.find_all('a', href=True, text=re.compile(r'(\w*)contact(\w*)', flags=re.IGNORECASE)))
                        for lll in s.find_all('a', href=True, text=re.compile(r'(\w*)contact(\w*)', flags=re.IGNORECASE)):
                            print lll['href']
                            time.sleep(5)
                            urll="http://"+url2+lll['href']
                            f = urllib.urlopen(urll)
                            s = f.read()
                                
                            print("Both are empty fetching contact-Us page")
                            print(re.findall(r"\+?\d{1,3}?[- .]?\(?(?:\d{2,3})\)?[- .]?\d\d\d[- .]?\d\d\d\d",s))   
      
                            my_listp=findall(r"\+91[\s-]?\d*[-\s]?\d*[\s-]?\d{3}",s)
                            my_liste=re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.(?:com|in|co.in|org|edu|gov|uk|net|ca|mil)",s)
           
                            kk=re.findall(r"\+?\d{1,3}?[- .]?\(?(?:\d{2,3})\)?[- .]?\d\d\d[- .]?\d\d\d\d",s)
                            kk1 = set(kk)
                            content=list(kk1)
                            for k in range(1,8):
                                content = [x for x in content if not x.startswith(str(k))]
                            my_listp.extend(content)

                            my_set2 = set(my_liste)
                            email=list(my_set2)
                            my_set1 = set(my_listp)
                            phone_number=list(my_set1)
                           
                            for items in phone_number:
                                strnumber+=items+','
                                print strnumber
                            for items in email:
                                stremail+=items+',' 
                                print stremail
                            
                            new=Orgn(name=title[i],link=link[i],orname_desc=orname_des[i],project_id=term+'_'+str(i),domain=domn,Phone_no=strnumber,email_id=stremail)   
                            db.session.add(new)
                            db.session.commit()
                            # new=Contact(contaclink=urll,Phone_no=strnumber,email_id=stremail)
                            # db.session.add(new)
                            # db.session.commit()
             
                else:
                    
                    for items in phone_number:
                        strnumber+=items+','
                    for items in email:
                        stremail+=items+',' 
                    new=Orgn(name=title[i],link=link[i],orname_desc=orname_des[i],project_id=term+'_'+str(i),domain=domn,Phone_no=strnumber,email_id=stremail)   
                    db.session.add(new)
                    db.session.commit()
                    # new=Contact(contaclink=link[i],Phone_no=strnumber,email_id=stremail)
                    # db.session.add(new)
                    # db.session.commit()
            except Exception as e:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                # print(exc_type, fname, exc_tb.tb_lineno)
                # print(str(e))
                db.session.rollback()


commands = [
    ['curl', 'http://www.reddit.com/'],
    ['curl', 'http://en.wikipedia.org/'],
    ['curl', 'http://www.google.com/'],
    ['curl', 'http://www.yahoo.com/'],
    ['curl', 'http://news.ycombinator.com/']
]
exec_commands(commands)
