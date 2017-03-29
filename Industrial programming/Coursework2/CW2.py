__author__ = 'Beni Iyaka'

#!python3.4
import json
import getopt
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk
import operator
from collections import Counter
#--------------------------------------------
#Constants
#--------------------------------------------
data = 'CW2.json'
#--------------------------------------------
#Dict Constants

continents = {
  'AF' : 'Africa',
  'AS' : 'Asia',
  'EU' : 'Europe',
  'NA' : 'North America',
  'SA' : 'South America',
  'OC' : 'Oceania',
  'AN' : 'Antarctica'
}

#--------------------------------------------
cntry_to_cont = {
  'AF' : 'AS',
  'AX' : 'EU',
  'AL' : 'EU',
  'DZ' : 'AF',
  'AS' : 'OC',
  'AD' : 'EU',
  'AO' : 'AF',
  'AI' : 'NA',
  'AQ' : 'AN',
  'AG' : 'NA',
  'AR' : 'SA',
  'AM' : 'AS',
  'AW' : 'NA',
  'AU' : 'OC',
  'AT' : 'EU',
  'AZ' : 'AS',
  'BS' : 'NA',
  'BH' : 'AS',
  'BD' : 'AS',
  'BB' : 'NA',
  'BY' : 'EU',
  'BE' : 'EU',
  'BZ' : 'NA',
  'BJ' : 'AF',
  'BM' : 'NA',
  'BT' : 'AS',
  'BO' : 'SA',
  'BQ' : 'NA',
  'BA' : 'EU',
  'BW' : 'AF',
  'BV' : 'AN',
  'BR' : 'SA',
  'IO' : 'AS',
  'VG' : 'NA',
  'BN' : 'AS',
  'BG' : 'EU',
  'BF' : 'AF',
  'BI' : 'AF',
  'KH' : 'AS',
  'CM' : 'AF',
  'CA' : 'NA',
  'CV' : 'AF',
  'KY' : 'NA',
  'CF' : 'AF',
  'TD' : 'AF',
  'CL' : 'SA',
  'CN' : 'AS',
  'CX' : 'AS',
  'CC' : 'AS',
  'CO' : 'SA',
  'KM' : 'AF',
  'CD' : 'AF',
  'CG' : 'AF',
  'CK' : 'OC',
  'CR' : 'NA',
  'CI' : 'AF',
  'HR' : 'EU',
  'CU' : 'NA',
  'CW' : 'NA',
  'CY' : 'AS',
  'CZ' : 'EU',
  'DK' : 'EU',
  'DJ' : 'AF',
  'DM' : 'NA',
  'DO' : 'NA',
  'EC' : 'SA',
  'EG' : 'AF',
  'SV' : 'NA',
  'GQ' : 'AF',
  'ER' : 'AF',
  'EE' : 'EU',
  'ET' : 'AF',
  'FO' : 'EU',
  'FK' : 'SA',
  'FJ' : 'OC',
  'FI' : 'EU',
  'FR' : 'EU',
  'GF' : 'SA',
  'PF' : 'OC',
  'TF' : 'AN',
  'GA' : 'AF',
  'GM' : 'AF',
  'GE' : 'AS',
  'DE' : 'EU',
  'GH' : 'AF',
  'GI' : 'EU',
  'GR' : 'EU',
  'GL' : 'NA',
  'GD' : 'NA',
  'GP' : 'NA',
  'GU' : 'OC',
  'GT' : 'NA',
  'GG' : 'EU',
  'GN' : 'AF',
  'GW' : 'AF',
  'GY' : 'SA',
  'HT' : 'NA',
  'HM' : 'AN',
  'VA' : 'EU',
  'HN' : 'NA',
  'HK' : 'AS',
  'HU' : 'EU',
  'IS' : 'EU',
  'IN' : 'AS',
  'ID' : 'AS',
  'IR' : 'AS',
  'IQ' : 'AS',
  'IE' : 'EU',
  'IM' : 'EU',
  'IL' : 'AS',
  'IT' : 'EU',
  'JM' : 'NA',
  'JP' : 'AS',
  'JE' : 'EU',
  'JO' : 'AS',
  'KZ' : 'AS',
  'KE' : 'AF',
  'KI' : 'OC',
  'KP' : 'AS',
  'KR' : 'AS',
  'KW' : 'AS',
  'KG' : 'AS',
  'LA' : 'AS',
  'LV' : 'EU',
  'LB' : 'AS',
  'LS' : 'AF',
  'LR' : 'AF',
  'LY' : 'AF',
  'LI' : 'EU',
  'LT' : 'EU',
  'LU' : 'EU',
  'MO' : 'AS',
  'MK' : 'EU',
  'MG' : 'AF',
  'MW' : 'AF',
  'MY' : 'AS',
  'MV' : 'AS',
  'ML' : 'AF',
  'MT' : 'EU',
  'MH' : 'OC',
  'MQ' : 'NA',
  'MR' : 'AF',
  'MU' : 'AF',
  'YT' : 'AF',
  'MX' : 'NA',
  'FM' : 'OC',
  'MD' : 'EU',
  'MC' : 'EU',
  'MN' : 'AS',
  'ME' : 'EU',
  'MS' : 'NA',
  'MA' : 'AF',
  'MZ' : 'AF',
  'MM' : 'AS',
  'NA' : 'AF',
  'NR' : 'OC',
  'NP' : 'AS',
  'NL' : 'EU',
  'NC' : 'OC',
  'NZ' : 'OC',
  'NI' : 'NA',
  'NE' : 'AF',
  'NG' : 'AF',
  'NU' : 'OC',
  'NF' : 'OC',
  'MP' : 'OC',
  'NO' : 'EU',
  'OM' : 'AS',
  'PK' : 'AS',
  'PW' : 'OC',
  'PS' : 'AS',
  'PA' : 'NA',
  'PG' : 'OC',
  'PY' : 'SA',
  'PE' : 'SA',
  'PH' : 'AS',
  'PN' : 'OC',
  'PL' : 'EU',
  'PT' : 'EU',
  'PR' : 'NA',
  'QA' : 'AS',
  'RE' : 'AF',
  'RO' : 'EU',
  'RU' : 'EU',
  'RW' : 'AF',
  'BL' : 'NA',
  'SH' : 'AF',
  'KN' : 'NA',
  'LC' : 'NA',
  'MF' : 'NA',
  'PM' : 'NA',
  'VC' : 'NA',
  'WS' : 'OC',
  'SM' : 'EU',
  'ST' : 'AF',
  'SA' : 'AS',
  'SN' : 'AF',
  'RS' : 'EU',
  'SC' : 'AF',
  'SL' : 'AF',
  'SG' : 'AS',
  'SX' : 'NA',
  'SK' : 'EU',
  'SI' : 'EU',
  'SB' : 'OC',
  'SO' : 'AF',
  'ZA' : 'AF',
  'GS' : 'AN',
  'SS' : 'AF',
  'ES' : 'EU',
  'LK' : 'AS',
  'SD' : 'AF',
  'SR' : 'SA',
  'SJ' : 'EU',
  'SZ' : 'AF',
  'SE' : 'EU',
  'CH' : 'EU',
  'SY' : 'AS',
  'TW' : 'AS',
  'TJ' : 'AS',
  'TZ' : 'AF',
  'TH' : 'AS',
  'TL' : 'AS',
  'TG' : 'AF',
  'TK' : 'OC',
  'TO' : 'OC',
  'TT' : 'NA',
  'TN' : 'AF',
  'TR' : 'AS',
  'TM' : 'AS',
  'TC' : 'NA',
  'TV' : 'OC',
  'UG' : 'AF',
  'UA' : 'EU',
  'AE' : 'AS',
  'GB' : 'EU',
  'US' : 'NA',
  'UM' : 'OC',
  'VI' : 'NA',
  'UY' : 'SA',
  'UZ' : 'AS',
  'UK' : 'EU',
  'VU' : 'OC',
  'VE' : 'SA',
  'VN' : 'AS',
  'WF' : 'OC',
  'EH' : 'AF',
  'YE' : 'AS',
  'ZM' : 'AF',
  'ZW' : 'AF'
}
#--------------------------------------------
#Main Class
#--------------------------------------------
class MainClass:

#--------Sub Constructor------------------------------------
    def __init__(self):
        self.records = self.loadJSON()

#---------JSON LOADING-----------------------------------
    def loadJSON(self) -> list:
        records = [ json.loads(line) for line in open(data) ]
        return records

#-----------Task Executer---------------------------------
    def executeTask(self, user, doc, task):
        """Takes a user uuid, doc uuid and a task and returns the output for the specific task """
        if task == "2a":
            if(doc !=""):
                return self.task2a(doc)
            else:
                print( "DOC UUID needs to be specified")
                return "DOC UUID needs to be specified"
        elif task == "2b":
            if(doc !=""):
                return self.task2b(doc)
            else:
                print( "DOC UUID needs to be specified")
                return "DOC UUID needs to be specified"
        elif task == "3a":
            return self.task3a()
        elif task =="3b":
            return self.task3b()
        elif task == "4":
            return self.listToStringFormat(self.task4())
        elif task == "5a":
            if((doc !="")):
                return self.listToStringFormat(self.DocToReaders(doc))
            else:
                print( "Both Doc UUID and visitor UUID need to be specified")
                return "Both Doc UUID and visitor UUID need to be specified"
        elif task == "5b":
                if((user!="")):
                    return self.listToStringFormat(self.ReadersToDoc(user))
                else:
                    print( "Both Doc UUID and visitor UUID need to be specified")
                    return "Both Doc UUID and visitor UUID need to be specified"
        elif task == self.AlsoLike(doc,task):
            if(doc !=""):
                return self.listToStringFormat(self.AlsoLike(doc, task))
            else:
                print( "DOC UUID needs to be specified")
                return "DOC UUID needs to be specified"

    def listToStringFormat(self, list) ->str:
        """Takes a list and returns a string representation of that list"""
        string = ''
        for element in list:
            stringb = string + str(element) + "\n"
        return stringb

#---------------------Task 2a-------------------------1--------------------------
    def task2a(self, doc):
        """"Take a document UUID and return a  dictionary in which the keys are the countries in which the document
                has been read in and the values are the number of times the document has been read from that country """
        docCountryList=[]
        for x in self.records:
            if x.get('subject_doc_id') == doc:
                docCountryList.append(x['visitor_country'])
        #Run histogram and return countries list
        x = []
        y = []
        for k,v in Counter(docCountryList).items():
            x.append(k)
            y.append(v)
        print (Counter(docCountryList))
        plt.title('Countries of Viewers')
        plt.bar(range(len(y)), y, align='center')
        plt.xticks(range(len(y)), x, size='small')
        plt.show()
        return docCountryList
#------------------------Task 2b--------------------------------------------------
    def task2b(self, doc):
        """"Take a document UUID and show a histogram of the continents that the document has been read in and
                   the number of times that it has been read for each continent"""
        docCountryList=[]
        for x in self.records:
            if x.get('subject_doc_id') == doc:
                docCountryList.append(x['visitor_country'])
        continentsList = []
        for entry in docCountryList:
            for country, continent in cntry_to_cont.items():
                if entry == country:
                    for contnt,cntntName in continents.items():
                        if contnt == continent:
                            continentsList.append(cntntName)
        x = []
        y = []
        #Insert countries and number of occurences in two seperate lists
        for k,v in Counter(continentsList).items():
            x.append(k)
            y.append(v)
        print(Counter(continentsList))
        plt.title('Continents of Viewers')
        plt.bar(range(len(y)), y, align='center')
        plt.xticks(range(len(y)), x, size='small')
        plt.show()
        return (Counter(continentsList))
#--------------------Task 3a------------------------------------------------------
    def task3a(self):
        """Show a histogram of the browsers used by viewers"""
        userAgentList = []
        for entry in self.records:
            userAgentList.append(entry['visitor_useragent'])

        x = []
        y = []
        #Insert countries and number of occurences in two seperate lists
        for k,v in Counter(userAgentList).items():
            x.append(k)
            y.append(v)
        print(Counter(userAgentList))
        plt.cla()
        plt.title('Viewers User Agents')
        plt.bar(range(len(y)), y, align='center')
        plt.xticks(range(len(y)), x, size='small')
        plt.show()
        return userAgentList
#-------------------Task 3b------------------------------------------------------
    def task3b(self):
        """Show a histogram of the browsers used by viewers - just the browser name"""
        browser_count = {}
        browsersList = []
        for entry in self.records:
            if "Firefox" in entry['visitor_useragent']:
               browsersList.append("Firefox")
            elif "Chrome" in entry['visitor_useragent']:
                browsersList.append("Chrome")
            elif "Safari" in entry['visitor_useragent']:
                browsersList.append("Safari")
            elif "Opera" in entry['visitor_useragent']:
                browsersList.append("Opera")
            elif "MSIE" in entry['visitor_useragent']:
                browsersList.append("Internet Explorer")
            else:
                browsersList.append("Other")
        #Run histogram and return browsersList
        x = []
        y = []
        #Insert countries and number of occurrences in two separate lists
        for k,v in Counter(browsersList).items():
            x.append(k)
            y.append(v)
        print(Counter(browsersList))
        plt.cla()
        plt.bar(range(len(y)), y, align='center')
        plt.xticks(range(len(y)), x, size='small')
        plt.show()
        return browsersList
#----------------------Task 4----------------------------------------------------
    def task4(self) ->list:
        """Return the top 10 readers in the records"""
        user_readTimes = dict()
        #Iterate through the json file
        for entry in self.records:
            #Look for pagereatime occurence
            if(entry['event_type'] == 'pagereadtime'):
                if (entry['visitor_uuid'] in user_readTimes):
                    user_readTimes[entry['visitor_uuid']] += entry['event_readtime']
                else:
                    user_readTimes[entry['visitor_uuid']] = entry['event_readtime']
        readTimes = list(sorted(user_readTimes.items(), key=operator.itemgetter(1), reverse = True))[0:10]
        for times in readTimes:
            print(times)
        return readTimes
#------------------------Task 5a------------------------------------------------
    def DocToReaders(self, doc):
        readersList = []
        for entry in self.records:
            #Search for doc in JSON,if the element doc_id exists
            if entry.get('subject_doc_id') == doc:
                #Insert visitor's ID inside list
                readersList.append(entry['visitor_uuid'])
                #return distinct readers IDs
        return set(readersList)

    def TopReaders(self):
        readTimeDict = dict()
        #Itterate through JSON File
        for entry in self.records:
            userFound = False
            #Look for page read occurrences
            if entry['event_type'] == 'pagereadtime':
                #search for duplicate userID inside dict
                for k,v in readTimeDict .items():
                    if k == entry['visitor_uuid'] and entry['event_readtime'] != None:
                        #Increment existing readtime value
                        readTimeDict[k] = int(entry['event_readtime']) + v
                        userFound = True
                        break;
                #Add new user entry to dictionary
                if userFound == False:
                    readTimeDict[entry['visitor_uuid']] = int(entry['event_readtime'])
        #Returns the dictionary with user_id ---> TotalReadTime
        return readTimeDict

    #5b. Returns DocumentIDs based on a readerID
    def ReadersToDoc(self, user):
        docList = []
        for entry in self.records:
            #Find user ID
            if entry['visitor_uuid'] == user:
                #Check that doc ID exists
                if entry.get('subject_doc_id') != None:
                    #Add document ID to the list
                    docList.append(entry['subject_doc_id'])
        #return distinct values for document IDs
        return set(docList)

    def AlsoLike(self, doc, task):
        readersDocDict = dict()
        #Itterate over readers IDs
        for k in self.DocToReaders(doc):
            #Itterate over Document IDs that each reader has read
            for v in self.ReadersToDoc(k):
                #Insert readerID,docID into Dictionary
                readersDocDict.setdefault(k,[]).append(v)
            #Option 5d for returning a list of documents based on readership profile
            if task == "5d":
                docReadTimeDict = dict()
                #Itterating through Doc -->
                for k,v in self.TopReaders().items():
                    for key,value in readersDocDict.items():
                        if k == key :
                            #Itterate through values
                            for i in value:
                                #Insert DocID -- > readTime into dictionary
                                docReadTimeDict[i] = v
                alsoLikeList = []
                for k,v in sorted(docReadTimeDict.items(), key = lambda x:-x[1])[:10]:
                    #Insert top 10 values on list
                    alsoLikeList.append(k)
                print((alsoLikeList))
                return (alsoLikeList)
        #Option 5e for returning a list of documents based on number of readers
        if task == '5e':
            docList = []
            for k,v in readersDocDict.items():
                #Store each document read, inside a list
                for i in v:
                    docList.append(i)
            countDocDict = dict()
            #Create dictionary with DocumentsRead --> Number of occurrences
            for x in docList:
                if x in countDocDict:
                    countDocDict[x] += 1
                else:
                    countDocDict[x] = 1
            alsoLikeList = []
            #Insert top 10 documents, based on the times they have been read inside a list
            for k,v in sorted(countDocDict.items(), key = lambda x:-x[1])[:10]:
                (alsoLikeList.append(k))
            print(sorted(alsoLikeList))
            return sorted(alsoLikeList)

#--------------------------------------------
#GUI Class
#--------------------------------------------
class GUI:
    def __init__(self):
        """initialisation of the UI"""
        self.root = Tk()
        self.root.title("Coursework 2")

        mainframe = ttk.Frame(self.root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)

        self.visitor_uuid = StringVar()
        self.document_uuid = StringVar()
        self.task = StringVar()

        visitor_entry = ttk.Entry(mainframe, width=30, textvariable=self.visitor_uuid)
        visitor_entry.grid(column=2, row=1, sticky=(W, E))

        document_entry = ttk.Entry(mainframe, width=30, textvariable=self.document_uuid)
        document_entry.grid(column=2, row=2, sticky=(W, E))

        task_entry = ttk.Entry(mainframe, width=2, textvariable=self.task)
        task_entry.grid(column=2, row=3, sticky=(W, E))

        ttk.Button(mainframe, text="Do Task", command=self.doTask).grid(column=2, row=4, sticky=W)

        ttk.Label(mainframe, text="Visitor UUID").grid(column=1, row=1, sticky=W)
        ttk.Label(mainframe, text="Document UUID").grid(column=1, row=2, sticky=E)
        ttk.Label(mainframe, text="Task").grid(column=1, row=3, sticky=W)
        
        self.output = StringVar()
        self.w = ttk.Label( mainframe, textvariable = self.output)
        self.w.grid(column = 1, row = 5, sticky=S)

        for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

        visitor_entry.focus()
        self.root.bind('<Return>', self.doTask)
        
        self.taskEx = MainClass()
        self.root.mainloop()

    def doTask(self, *args):
        """Does the the task specified by the user and shows the output"""
        taskId = self.task.get()
        document = self.document_uuid.get()
        visitor = self.visitor_uuid.get()
        self.output.set(str(self.taskEx.executeTask(visitor, document, taskId)))


#--------------------------------------------
#Main Method
#--------------------------------------------  
if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], "u:d:t:")
    except getopt.GetoptError as err:
        print(str(err))
        sys.exit(0)
    user = ""
    doc = ""
    task = ""
    for o, a in opts:
        if o == "-u":
            user = a
        elif o == "-d":
            doc = a
        elif o == "-t":
            task = a
        else:
            assert False, "unhandled option"
    if((user == "") and (doc == "") and ( task == "")):
        gui = GUI()
    else:
        taskEx = MainClass()
        taskEx.executeTask(user, doc, task)
