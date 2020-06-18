# -*- coding: UTF-8 -*-
from mpi4py import MPI
import linecache
import sys
import json
from collections import Counter
import time
start_time = time.time()
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

size = MPI.COMM_WORLD.Get_size()

file = sys.argv[1]

data = []
language = []
counter=Counter()
counterl=Counter()
with open(file,"r",encoding='utf-8') as f:
    for i,line in enumerate(f):
        try:
            if i==0 or i%size!=rank:
                continue
            if len(data) == 0:
                counter+=Counter(data)
                counterl+=Counter(language)
                language=[]
                data=[]
            line=line[:-2]
            j = json.loads(line)
            for tag in j['doc']['entities']['hashtags']:
                data.append(tag['text'].encode('utf-8').lower())
            language.append(j['doc']['lang'])
        except Exception as e:
            # print(e)
            pass
counter+=Counter(data)
counterl+=Counter(language)
data=[]
language=[]
dl = comm.gather((counter,counterl), root=0)

DICT = {'en': 'English',
        'ar': 'Arabic',
        'bn': 'Bengali',
        'cs': 'Czech',
        'da': 'Danish',
        'de': 'German',
        'el': 'Greek',
        'es': 'Spanish',
        'fa': 'Persian',
        'fi': 'Finnish',
        'fil': 'Filipino',
        'fr': 'French',
        'he': 'Hebrew',
        'hi': 'Hindi',
        'hu': 'Hungarian',
        'id': 'Indonesian',
        'id': 'Indonesian',
        'it': 'Italian',
        'ja': 'Japanese',
        'ko': 'Korean',
        'msa': 'Malay',
        'nl': 'Dutch',
        'no': 'Norwegian',
        'pl': 'Polish',
        'pt': 'Portuguese',
        'ro': 'Romanian',
        'ru': 'Russian',
        'sv': 'Swedish',
        'th': 'Thai',
        'tr': 'Turkish',
        'tl':'Tagalog',
        'uk': 'Ukrainian',
        'ur': 'Urdu',
        'ud':'Undefined',
        'vi': 'Vietnamese',
        'zh-cn': 'Chinese Simplified',
        'zh-tw': 'Chinese Traditional'}
if rank == 0:
    data = [i[0] for i in dl]
    language = [i[1] for i in dl]
    result = []
    counter=Counter()
    for da in data:
        counter+=da
    #counter = Counter(result)
    count = 1
    for tag, times in counter.most_common(12):
        try:
            sys.stdout.write("{} #{} {}\n".format(
                count, tag.decode('utf-8'), times))
            count += 1
        except:
            pass
        if count > 10:
            break
    sys.stdout.write('\n')
    #lang = []
    #for la in language:
    #    for l in la:
    #        lang.append(l)
    #counterl = Counter(la)
    counterl=Counter()
    for lang in language:
	    counterl+=lang
    count = 1
    for langu, times in counterl.most_common(15):
        try:
            sys.stdout.write("{}. {} ({}), {}\n".format(
                count, DICT.get(langu,'Undefined'), langu, times))
            count += 1
            if count > 10:
                break
        except:
            pass
    sys.stdout.write('\n')
    stop_time = time.time()
    sys.stdout.write("time used {}s\n".format(stop_time-start_time))
