import os
import runpy 
from matplotlib import pyplot
import matplotlib
import humanfriendly
matplotlib.use('agg')


def plot_case(alg,trunc):
    title = 'LMS alg=%s trunc=%d'%(alg,trunc)
    pyplot.title(title)
    pyplot.suptitle('Number of signatures: hash blocks vs signature size')
    stats = runpy.run_path('stats.py')['out']
    colors = ['red','blue','green','yellow','brown']
    for number_of_sig in [32,1024,32768,1048576,1073741824]:
        out = []
        def match_number_of_sig(v):
            if 32 == number_of_sig:
                print(v)
            return v[1]['number_of_sig'] == number_of_sig
        d = dict(filter(match_number_of_sig, stats.items()))
        l = []
        for k,v in d.items():
            v['key'] = k
            l.append(v)
        def take_sig_size(a):
            return a['sig_size']
        def take_hash_blocks(a):
            return a['hash_blocks']
        l.sort(key=take_sig_size)
        last_hb=1<<32
        for e in l:
            hb = e['hash_blocks']
            if hb < last_hb:
                last_hb = hb
                out.append(e)

        x = []
        y = [] 
        print("number_of_sig: %d"%number_of_sig)       
        for e in out:
            print(e)
            px = e['sig_size']
            py = e['hash_blocks']
            x.append(px)
            y.append(py)
            #anno = '%d, %d'%(e['sig_size'],e['hash_blocks'])
            #pyplot.annotate(anno, xy = (px, py))

        pyplot.plot(x, y, 
            label = humanfriendly.format_number(e['number_of_sig']), 
            linestyle = ':',
            color = colors[0],
            marker = 'o',
            markersize = 10)
        colors.pop(0)

    pyplot.legend()
    pyplot.yscale("log")
    pyplot.savefig(title+'.png', dpi = 600)
    pyplot.close()

for alg in ['sha256']:
    for trunc in [32]:
        plot_case(alg,trunc)