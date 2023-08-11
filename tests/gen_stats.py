import os 
import sys
import subprocess
import logging
import traceback
import shutil
from pathlib import Path 
import runpy
import time

def clean_eol(s):
    s = s.replace('\r\r', '\r')
    return s.replace('\r\n', '\n')


def capture_output(*args):
    out = subprocess.run(*args, stdout=subprocess.PIPE).stdout.decode('utf-8')
    return clean_eol(out)

def params_to_args(levels,lms,lmots,alg,trunc):
    args = []
    args.append('--levels=%d'%levels)
    args.append('--lms=%d'%lms)
    args.append('--lmots=%d'%lmots)
    args.append('--alg=%s'%alg)
    args.append('--trunc=%d'%trunc)
    return args

def eval_parameters(args):
    keyfile = 'test'
    msgfile = 'null'
    Path(keyfile+'.prv').unlink(missing_ok=True)
    Path(keyfile+'.pub').unlink(missing_ok=True)
    Path(msgfile+'.sig').unlink(missing_ok=True)
    exe = 'python'
    cmd = [exe,'-m', 'pyhsslms.hsslms']
    genkey = capture_output(cmd+['genkey',keyfile]+args).rstrip("\n")
    for i in range(0,10):
        if os.path.exists(keyfile+'.prv') and os.path.exists(keyfile+'.pub'):
            break
        time.sleep(0.1)
    sign = capture_output(cmd+['sign',keyfile,msgfile]).rstrip("\n")
    for i in range(0,10):
        if os.path.exists(msgfile+'.sig'):
            break
        time.sleep(0.1)
    verify = capture_output(cmd+['verify_stat',keyfile,msgfile]).rstrip("\n")
    stats = verify.split(' ')
    out = dict()
    out['number_of_sig'] = int(stats[0])
    out['sig_size'] = int(stats[1])
    out['hash_blocks'] = int(stats[2])
    return out


resfile='stats.py'
try:
    done = runpy.run_path(resfile)
except:
    done = dict()
    with open(resfile,'w') as f:
        print('out = dict()',file=f)

with open(resfile,'a') as f:
    for trunc in [32]:
        for alg in ['sha256']:
            for levels in [1,2,3]:
                for lms in [5,10,15]:
                    for lmots in [1,2,4,8]:
                        args = params_to_args(levels,lms,lmots,alg,trunc)
                        key = ' '.join(args)
                        if key not in done['out'].keys():
                            print(key)
                            res = eval_parameters(args)
                            print('out["%s"] = %s'%(key,res),file=f,flush=True)
                        