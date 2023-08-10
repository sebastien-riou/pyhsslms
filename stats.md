# Stats


## --levels=2 --lms=5 --lmots=8 --alg=sha256 --trunc=32
````
Private Key: test.prv
HSS private key
   levels    : 2
   level=0   : LMS private key
   LMS type  : 00000005
   LMOTS type: 00000004
   I         : 6f2159babf5fc95182cdb0e752aeea3c
   SEED      : e02ad7205b486c2b27819bcff6aca55b42093098a95bdcfb713afec9cefc1485
   q         : 00000002
   pub       : 11cffb80177810b4050f59ebf395f845a06f1b324b416172eca48e6ca817a7a1
   level=1   : LMS private key
   LMS type  : 00000005
   LMOTS type: 00000004
   I         : 6b5bf450f09605e5d524899c479dcbc5
   SEED      : 12216ffba170c95007bbbffa027a891d1d64c161d28da5868f05fbccf424a1f7
   q         : 00000000
   pub       : 1eff5d2da58e9931b782517a7387869baf191b7c104ab134f445a4bc5533c0f3
   max signs : 1024

Public Key: test.pub
HSS public key
   levels    : 2
   LMS type  : 00000005
   LMOTS type: 00000004
   I         : 6f2159babf5fc95182cdb0e752aeea3c
   K         : 11cffb80177810b4050f59ebf395f845a06f1b324b416172eca48e6ca817a7a1
   max signs : 1024

````
Signing null ...
   ... Success. Signature saved in null.sig
|      names      | counts | minimums |      averages      | maximums |
|-----------------|--------|----------|--------------------|----------|
|     H_start     | 565731 |          |                    |          |
|    H_update     | 567907 |    22    | 54.91152072434395  |   110    |
|    H_finish     | 565731 |          |                    |          |
| H_blocksPerHash | 565731 |    1     | 1.0020345358483096 |    18    |
|    H_blocks     | 566882 |          |                    |          |

````
-rw-r--r-- 1 sebastien.riou 1049089 68 Apr  8 22:20 test.prv
-rw-r--r-- 1 sebastien.riou 1049089 60 Apr  8 22:19 test.pub
-rw-r--r-- 1 sebastien.riou 1049089 2644 Apr  8 22:20 null.sig
````
Signature in null.sig is valid.
|      names      | counts | minimums |      averages      | maximums |
|-----------------|--------|----------|--------------------|----------|
|     H_start     |  8941  |          |                    |          |
|    H_update     |  9009  |    22    | 54.859251859251856 |   110    |
|    H_finish     |  8941  |          |                    |          |
| H_blocksPerHash |  8941  |    1     | 1.0050329940722513 |    18    |
|    H_blocks     |  8986  |          |                    |          |


## --levels=2 --lms=5 --lmots=8 --alg=shake --trunc=32
````
Private Key: test.prv
HSS private key
   levels    : 2
   level=0   : LMS private key
   LMS type  : 0000000f
   LMOTS type: 0000000c
   I         : 3e5435d4b8c11c6af7440720d67448a6
   SEED      : 8bec8a9b40e9a33367a2d86e6d01d84f8bfaabbc75094e0f9c561feedbd12324
   q         : 00000002
   pub       : ff42a8ed1626da81f5a893aa12823237ca5ffba31b3bf7fed0850eb5f49747a6
   level=1   : LMS private key
   LMS type  : 0000000f
   LMOTS type: 0000000c
   I         : b13c39fc8932946abbf02298c230ca31
   SEED      : 4af2b9d772ce470b4a24d60d9bae0599514e7c85ab2b4afef72d8cd9779f85ac
   q         : 00000000
   pub       : 29709c62f180a0e9e90f4c51330bcc68125bae6e433090d4c7e7003433452745
   max signs : 1024

Public Key: test.pub
HSS public key
   levels    : 2
   LMS type  : 0000000f
   LMOTS type: 0000000c
   I         : 3e5435d4b8c11c6af7440720d67448a6
   K         : ff42a8ed1626da81f5a893aa12823237ca5ffba31b3bf7fed0850eb5f49747a6
   max signs : 1024

````
Signing null ...
   ... Success. Signature saved in null.sig
|      names      | counts | minimums |     averages      | maximums |
|-----------------|--------|----------|-------------------|----------|
|     H_start     | 565476 |          |                   |          |
|    H_update     | 567652 |    22    | 54.91148097778216 |   110    |
|    H_finish     | 565476 |          |                   |          |
| H_blocksPerHash | 565476 |    1     | 1.000905431883935 |    9     |
|    H_blocks     | 565988 |          |                   |          |

````
-rw-r--r-- 1 sebastien.riou 1049089 68 Apr  8 22:19 test.prv
-rw-r--r-- 1 sebastien.riou 1049089 60 Apr  8 22:19 test.pub
-rw-r--r-- 1 sebastien.riou 1049089 2644 Apr  8 22:19 null.sig
````
Signature in null.sig is valid.
|      names      | counts | minimums |      averages      | maximums |
|-----------------|--------|----------|--------------------|----------|
|     H_start     |  9196  |          |                    |          |
|    H_update     |  9264  |    22    | 54.863126079447326 |   110    |
|    H_finish     |  9196  |          |                    |          |
| H_blocksPerHash |  9196  |    1     | 1.001739886907351  |    9     |
|    H_blocks     |  9212  |          |                    |          |


## --levels=1 --lms=5 --lmots=8 --alg=sha256 --trunc=32
````
Private Key: test.prv
HSS private key
   levels    : 1
   level=0   : LMS private key
   LMS type  : 00000005
   LMOTS type: 00000004
   I         : ac3bf7cbacba9e9325aa3b17d3d87dcd
   SEED      : 6dec44ecbce01e972e2c121b44ce33f1cbeaa9e834dddef6104c10052451557c
   q         : 00000000
   pub       : 476e1b984f93c56f8aa00c19a5f3f375813f84bc639f99a95eb2f9b86cda7d7a
   max signs : 32

Public Key: test.pub
HSS public key
   levels    : 1
   LMS type  : 00000005
   LMOTS type: 00000004
   I         : ac3bf7cbacba9e9325aa3b17d3d87dcd
   K         : 476e1b984f93c56f8aa00c19a5f3f375813f84bc639f99a95eb2f9b86cda7d7a
   max signs : 32

````
Signing null ...
   ... Success. Signature saved in null.sig
|      names      | counts | minimums |     averages      | maximums |
|-----------------|--------|----------|-------------------|----------|
|     H_start     | 282993 |          |                   |          |
|    H_update     | 284081 |    22    | 54.91146187179009 |    86    |
|    H_finish     | 282993 |          |                   |          |
| H_blocksPerHash | 282993 |    1     | 1.002031852377974 |    18    |
|    H_blocks     | 283568 |          |                   |          |

````
-rw-r--r-- 1 sebastien.riou 1049089 68 Apr  8 22:17 test.prv
-rw-r--r-- 1 sebastien.riou 1049089 60 Apr  8 22:17 test.pub
-rw-r--r-- 1 sebastien.riou 1049089 1296 Apr  8 22:17 null.sig
````
Signature in null.sig is valid.
|      names      | counts | minimums |     averages      | maximums |
|-----------------|--------|----------|-------------------|----------|
|     H_start     |  4343  |          |                   |          |
|    H_update     |  4377  |    22    | 54.84875485492346 |    86    |
|    H_finish     |  4343  |          |                   |          |
| H_blocksPerHash |  4343  |    1     | 1.005065622841354 |    18    |
|    H_blocks     |  4365  |          |                   |          |


## --levels=3 --lms=5 --lmots=8 --alg=sha256 --trunc=32
````
Private Key: test.prv
HSS private key
   levels    : 3
   level=0   : LMS private key
   LMS type  : 00000005
   LMOTS type: 00000004
   I         : 9a1bc7f600ff7adaac77ac171cbafe7d
   SEED      : 10bdb72852b2d7be31167f9b7eeebde696e99edfceb7360819b6735c55756df4
   q         : 00000002
   pub       : 126625650bb5dc99db506b9861dba1d04ce88d9fa37a730c3174a9db93b069a3
   level=1   : LMS private key
   LMS type  : 00000005
   LMOTS type: 00000004
   I         : 6709b9da0dbb146dd2bdc86602d90225
   SEED      : 545265aabc640d673414939fa8262423c1a427bc21fed8a29d3968f45cd5d13c
   q         : 00000001
   pub       : 0634657311e025519b7bd0a0c4249daa11c6fb969066710555b2c86ebcd00f21
   level=2   : LMS private key
   LMS type  : 00000005
   LMOTS type: 00000004
   I         : 53649f647479d7ab353c68ddb3585465
   SEED      : 15359973cecba8b2a5332320931017f389b9159d66f27767ceb16dc7e2d877c5
   q         : 00000000
   pub       : 87cf5a52df98c7ad6fc2aa10530f36ecfe9b4b93195f728c48f4fda501f5597d
   max signs : 32768

Public Key: test.pub
HSS public key
   levels    : 3
   LMS type  : 00000005
   LMOTS type: 00000004
   I         : 9a1bc7f600ff7adaac77ac171cbafe7d
   K         : 126625650bb5dc99db506b9861dba1d04ce88d9fa37a730c3174a9db93b069a3
   max signs : 32768

````
Signing null ...
   ... Success. Signature saved in null.sig
|      names      | counts | minimums |      averages      | maximums |
|-----------------|--------|----------|--------------------|----------|
|     H_start     | 848724 |          |                    |          |
|    H_update     | 851988 |    22    | 54.91156682957976  |   110    |
|    H_finish     | 848724 |          |                    |          |
| H_blocksPerHash | 848724 |    1     | 1.0020348193287807 |    18    |
|    H_blocks     | 850451 |          |                    |          |

````
-rw-r--r-- 1 sebastien.riou 1049089 68 Apr  8 22:16 test.prv
-rw-r--r-- 1 sebastien.riou 1049089 60 Apr  8 22:16 test.pub
-rw-r--r-- 1 sebastien.riou 1049089 3992 Apr  8 22:16 null.sig
````
Signature in null.sig is valid.
|      names      | counts | minimums |      averages      | maximums |
|-----------------|--------|----------|--------------------|----------|
|     H_start     | 13284  |          |                    |          |
|    H_update     | 13386  |    22    | 54.86000298819663  |   110    |
|    H_finish     | 13284  |          |                    |          |
| H_blocksPerHash | 13284  |    1     | 1.0051189400782896 |    18    |
|    H_blocks     | 13352  |          |                    |          |

## --levels=2 --lms=5 --lmots=8 --alg=sha256 --trunc=32
````
Private Key: test.prv
HSS private key
   levels    : 2
   level=0   : LMS private key
   LMS type  : 00000005
   LMOTS type: 00000004
   I         : 1f3b65938513ea3c7ad5bcf2aea5336e
   SEED      : b077ce0b2762cf106bbcd560de1615eb6632f9184b833f28027e8f7c8efe9e66
   q         : 00000002
   pub       : 5777b967013548ba67e41683eac9c3c864567b13459f5f79ba8e88c3cab05e30
   level=1   : LMS private key
   LMS type  : 00000005
   LMOTS type: 00000004
   I         : 2450aa60b501fc3de70fa1333418c3a0
   SEED      : 9b0ecfb592c9e4b94b3cf356ad0fd27d0b90cf3bc34096b32c714c091ece1e78
   q         : 00000000
   pub       : 2d189ebe82973ebd238e5be9ac9b5035e1dcbc9e5d64d9e3bbb83042907bbde1
   max signs : 1024

Public Key: test.pub
HSS public key
   levels    : 2
   LMS type  : 00000005
   LMOTS type: 00000004
   I         : 1f3b65938513ea3c7ad5bcf2aea5336e
   K         : 5777b967013548ba67e41683eac9c3c864567b13459f5f79ba8e88c3cab05e30
   max signs : 1024

````
Signing null ...
   ... Success. Signature saved in null.sig
|      names      | counts | minimums |      averages      | maximums |
|-----------------|--------|----------|--------------------|----------|
|     H_start     | 565476 |          |                    |          |
|    H_update     | 567652 |    22    | 54.91148097778216  |   110    |
|    H_finish     | 565476 |          |                    |          |
| H_blocksPerHash | 565476 |    1     | 1.0020354533172053 |    18    |
|    H_blocks     | 566627 |          |                    |          |

````
-rw-r--r-- 1 sebastien.riou 1049089 68 Apr  8 22:15 test.prv
-rw-r--r-- 1 sebastien.riou 1049089 60 Apr  8 22:15 test.pub
-rw-r--r-- 1 sebastien.riou 1049089 2644 Apr  8 22:15 null.sig
````
Signature in null.sig is valid.
|      names      | counts | minimums |      averages      | maximums |
|-----------------|--------|----------|--------------------|----------|
|     H_start     |  9196  |          |                    |          |
|    H_update     |  9264  |    22    | 54.863126079447326 |   110    |
|    H_finish     |  9196  |          |                    |          |
| H_blocksPerHash |  9196  |    1     | 1.0048934319269247 |    18    |
|    H_blocks     |  9241  |          |                    |          |

## --levels=2 --lms=5 --lmots=4 --alg=sha256 --trunc=32
````
Private Key: test.prv
HSS private key
   levels    : 2
   level=0   : LMS private key
   LMS type  : 00000005
   LMOTS type: 00000003
   I         : be83823ec7862edd5beaeefbf364b305
   SEED      : a9f6837ff72f5e719a771c84ddca8053953efd610e4b867ca2b526273c70d0a2
   q         : 00000002
   pub       : cfddf5773c8453f08efbf82c84c364da0eeca68afd5f0dc414bbcb92485d600b
   level=1   : LMS private key
   LMS type  : 00000005
   LMOTS type: 00000003
   I         : 90ea9b83259d64bf0a208ad206735164
   SEED      : 7b8577e72147f440e56558fdc52a2f2f9ea03db715b332369b53a83ce275f145
   q         : 00000000
   pub       : 93f5c8f21a900029cb8835d30582902a6fff9cc0916eaa4f3e6bec3ee1be629b
   max signs : 1024

Public Key: test.pub
HSS public key
   levels    : 2
   LMS type  : 00000005
   LMOTS type: 00000003
   I         : be83823ec7862edd5beaeefbf364b305
   K         : cfddf5773c8453f08efbf82c84c364da0eeca68afd5f0dc414bbcb92485d600b
   max signs : 1024

````
Signing null ...
   ... Success. Signature saved in null.sig
|      names      | counts | minimums |      averages      | maximums |
|-----------------|--------|----------|--------------------|----------|
|     H_start     | 69894  |          |                    |          |
|    H_update     | 74182  |    22    | 53.66781699064463  |   110    |
|    H_finish     | 69894  |          |                    |          |
| H_blocksPerHash | 69894  |    1     | 1.0311185509485792 |    34    |
|    H_blocks     | 72069  |          |                    |          |

````
-rw-r--r-- 1 sebastien.riou 1049089 68 Apr  8 22:14 test.prv
-rw-r--r-- 1 sebastien.riou 1049089 60 Apr  8 22:14 test.pub
-rw-r--r-- 1 sebastien.riou 1049089 4756 Apr  8 22:14 null.sig
````
Signature in null.sig is valid.
|      names      | counts | minimums |      averages      | maximums |
|-----------------|--------|----------|--------------------|----------|
|     H_start     |  1066  |          |                    |          |
|    H_update     |  1200  |    22    | 52.678333333333335 |   110    |
|    H_finish     |  1066  |          |                    |          |
| H_blocksPerHash |  1066  |    1     | 1.072232645403377  |    34    |
|    H_blocks     |  1143  |          |                    |          |


## --levels=2 --lms=5 --lmots=1 --alg=sha256 --trunc=32
````
Private Key: test.prv
HSS private key
   levels    : 2
   level=0   : LMS private key
   LMS type  : 00000005
   LMOTS type: 00000001
   I         : 620f65a257cda8969304f4662968d061
   SEED      : 719f1f22623f81e4c92b2d4fd2cd8d60802eddc0b6a7dc7ddf132a118ef0a2ca
   q         : 00000002
   pub       : a270880e731429d1c5a4e025536eca2f4bd61a80786f6440f0e64d8ece6e38ea
   level=1   : LMS private key
   LMS type  : 00000005
   LMOTS type: 00000001
   I         : b57c440411e42ac73c6055a93bae7ef6
   SEED      : 7ec58ca25d754d86d8c89850781a52bbee2edfbdf7824f30436bd8e227990c6f
   q         : 00000000
   pub       : defac37e9305b8e9242e430f985d20cc86b27395094ec96616a756cfff7b0fcc
   max signs : 1024

Public Key: test.pub
HSS public key
   levels    : 2
   LMS type  : 00000005
   LMOTS type: 00000001
   I         : 620f65a257cda8969304f4662968d061
   K         : a270880e731429d1c5a4e025536eca2f4bd61a80786f6440f0e64d8ece6e38ea
   max signs : 1024

````
Signing null ...
   ... Success. Signature saved in null.sig
|      names      | counts | minimums |     averages      | maximums |
|-----------------|--------|----------|-------------------|----------|
|     H_start     | 34904  |          |                   |          |
|    H_update     | 51864  |    22    | 47.47493444393028 |   110    |
|    H_finish     | 34904  |          |                   |          |
| H_blocksPerHash | 34904  |    1     | 1.243840247536099 |   133    |
|    H_blocks     | 43415  |          |                   |          |

````
-rw-r--r-- 1 sebastien.riou 1049089 68 Apr  8 22:13 test.prv
-rw-r--r-- 1 sebastien.riou 1049089 60 Apr  8 22:13 test.pub
-rw-r--r-- 1 sebastien.riou 1049089 17428 Apr  8 22:13 null.sig
````
Signature in null.sig is valid.
|      names      | counts | minimums |      averages      | maximums |
|-----------------|--------|----------|--------------------|----------|
|     H_start     |  284   |          |                    |          |
|    H_update     |  814   |    22    | 40.38820638820639  |   110    |
|    H_finish     |  284   |          |                    |          |
| H_blocksPerHash |  284   |    1     | 1.9683098591549295 |   133    |
|    H_blocks     |  559   |          |                    |          |


## --levels=1 --lms=5 --lmots=1 --alg=sha256 --trunc=32
````
Private Key: test.prv
HSS private key
   levels    : 1
   level=0   : LMS private key
   LMS type  : 00000005
   LMOTS type: 00000001
   I         : 6d5e1abb25b6cfa810dec01399357c1a
   SEED      : 89600ee080c09e505f998dca06d130ecd6a9004e837026e20fbcb27aa26a06d3
   q         : 00000000
   pub       : afe651c59dc2abf4fe6f3e4a8a0adb2e057ade507f26a69e98ae47ce8517e340
   max signs : 32

Public Key: test.pub
HSS public key
   levels    : 1
   LMS type  : 00000005
   LMOTS type: 00000001
   I         : 6d5e1abb25b6cfa810dec01399357c1a
   K         : afe651c59dc2abf4fe6f3e4a8a0adb2e057ade507f26a69e98ae47ce8517e340
   max signs : 32

````
Signing null ...
   ... Success. Signature saved in null.sig
|      names      | counts | minimums |      averages      | maximums |
|-----------------|--------|----------|--------------------|----------|
|     H_start     | 17447  |          |                    |          |
|    H_update     | 25927  |    22    | 47.47240328614957  |    86    |
|    H_finish     | 17447  |          |                    |          |
| H_blocksPerHash | 17447  |    1     | 1.2438814695936264 |   133    |
|    H_blocks     | 21702  |          |                    |          |

````
-rw-r--r-- 1 sebastien.riou 1049089 68 Apr  8 22:12 test.prv
-rw-r--r-- 1 sebastien.riou 1049089 60 Apr  8 22:12 test.pub
-rw-r--r-- 1 sebastien.riou 1049089 8688 Apr  8 22:12 null.sig
````
Signature in null.sig is valid.
|      names      | counts | minimums |      averages      | maximums |
|-----------------|--------|----------|--------------------|----------|
|     H_start     |  147   |          |                    |          |
|    H_update     |  412   |    22    | 40.49757281553398  |    86    |
|    H_finish     |  147   |          |                    |          |
| H_blocksPerHash |  147   |    1     | 1.9319727891156462 |   133    |
|    H_blocks     |  284   |          |                    |          |


## --levels=1 --lms=10 --lmots=1 --alg=sha256 --trunc=32
````
Private Key: test.prv
HSS private key
   levels    : 1
   level=0   : LMS private key
   LMS type  : 00000006
   LMOTS type: 00000001
   I         : 41d5d8e9a3e8b5d3eadf6172421d980b
   SEED      : baa02c3812e7106ae6857f01d0c3ab0d730a8d08213fbc117c0a4e1ff9a57591
   q         : 00000000
   pub       : 371e878c6854522bf9b947c54ebfaf200905c57f0ee745107f1e9683cab8f9d1
   max signs : 1024

Public Key: test.pub
HSS public key
   levels    : 1
   LMS type  : 00000006
   LMOTS type: 00000001
   I         : 41d5d8e9a3e8b5d3eadf6172421d980b
   K         : 371e878c6854522bf9b947c54ebfaf200905c57f0ee745107f1e9683cab8f9d1
   max signs : 1024

````
Signing null ...
   ... Success. Signature saved in null.sig
|      names      | counts | minimums |      averages      | maximums |
|-----------------|--------|----------|--------------------|----------|
|     H_start     | 546197 |          |                    |          |
|    H_update     | 817557 |    22    | 47.362142333806695 |    86    |
|    H_finish     | 546197 |          |                    |          |
| H_blocksPerHash | 546197 |    1     | 1.249344101121024  |   133    |
|    H_blocks     | 682388 |          |                    |          |

````
-rw-r--r-- 1 sebastien.riou 1049089 68 Apr  8 22:11 test.prv
-rw-r--r-- 1 sebastien.riou 1049089 60 Apr  8 22:11 test.pub
-rw-r--r-- 1 sebastien.riou 1049089 8848 Apr  8 22:11 null.sig
````
Signature in null.sig is valid.
|      names      | counts | minimums |     averages      | maximums |
|-----------------|--------|----------|-------------------|----------|
|     H_start     |  138   |          |                   |          |
|    H_update     |  403   |    22    | 40.55831265508685 |    86    |
|    H_finish     |  138   |          |                   |          |
| H_blocksPerHash |  138   |    1     | 2.028985507246377 |   133    |
|    H_blocks     |  280   |          |                   |          |


## --levels=1 --lms=10 --lmots=1 --alg=shake --trunc=32
````
Private Key: test.prv
HSS private key
   levels    : 1
   level=0   : LMS private key
   LMS type  : 00000010
   LMOTS type: 00000009
   I         : 4f318dcdb18d9e6b1231e31e29694213
   SEED      : ee09fb451fab0e155177a75e75e7d8d3aa6e61f19ab51e2906c0cac7a8b2ae78
   q         : 00000000
   pub       : 497e7d044e665ac83d8aff0b0bd6f32146fa1165461593a5a314a5b3520c21df
   max signs : 1024

Public Key: test.pub
HSS public key
   levels    : 1
   LMS type  : 00000010
   LMOTS type: 00000009
   I         : 4f318dcdb18d9e6b1231e31e29694213
   K         : 497e7d044e665ac83d8aff0b0bd6f32146fa1165461593a5a314a5b3520c21df
   max signs : 1024

````
Signing null ...
   ... Success. Signature saved in null.sig
|      names      | counts | minimums |      averages      | maximums |
|-----------------|--------|----------|--------------------|----------|
|     H_start     | 546194 |          |                    |          |
|    H_update     | 817554 |    22    | 47.36211430682255  |    86    |
|    H_finish     | 546194 |          |                    |          |
| H_blocksPerHash | 546194 |    1     | 1.1162370879211416 |    63    |
|    H_blocks     | 609682 |          |                    |          |

````
-rw-r--r-- 1 sebastien.riou 1049089 68 Apr  8 22:09 test.prv
-rw-r--r-- 1 sebastien.riou 1049089 60 Apr  8 22:09 test.pub
-rw-r--r-- 1 sebastien.riou 1049089 8848 Apr  8 22:09 null.sig
````
Signature in null.sig is valid.
|      names      | counts | minimums |      averages      | maximums |
|-----------------|--------|----------|--------------------|----------|
|     H_start     |  141   |          |                    |          |
|    H_update     |  406   |    22    | 40.66502463054187  |    86    |
|    H_finish     |  141   |          |                    |          |
| H_blocksPerHash |  141   |    1     | 1.4397163120567376 |    63    |
|    H_blocks     |  203   |          |                    |          |

## --levels=3 --lms=10 --lmots=8 --alg=sha256 --trunc=32
````
Private Key: test.prv
HSS private key
   levels    : 3
   level=0   : LMS private key
   LMS type  : 00000006
   LMOTS type: 00000004
   I         : 37c613386c5343ecd8e2492aa57313dc
   SEED      : f18775ab90d5a36504a5753d0a5a93886dd37bf5d443201b7d451ab7667bec01
   q         : 00000002
   pub       : a74313f2722fc34264c29ef22c0a53caa9ce696e7b375c79ed051372f05f1c42
   level=1   : LMS private key
   LMS type  : 00000006
   LMOTS type: 00000004
   I         : 8438f72439b064b78cf29f81ae0235cb
   SEED      : dc4b44aece229d54f37f3825a95b293f432408c1ee5cc7a07a91236d086665b6
   q         : 00000001
   pub       : ec0f340637c607030fab3d600d1d4c9602fdc03e115bd646a87034a6b99d9755
   level=2   : LMS private key
   LMS type  : 00000006
   LMOTS type: 00000004
   I         : 4ca8f96fafc90667d06c356b6b11ec3a
   SEED      : 8179afebdf3255c55a9f41041446afdb2b0ca6e11935a83689f3e207ce16ef7b
   q         : 00000000
   pub       : 28582cc037380398376b9e2cdef470d6a30c7bd0ae651be7a9e541179506bcc5
   max signs : 1073741824

Public Key: test.pub
HSS public key
   levels    : 3
   LMS type  : 00000006
   LMOTS type: 00000004
   I         : 37c613386c5343ecd8e2492aa57313dc
   K         : a74313f2722fc34264c29ef22c0a53caa9ce696e7b375c79ed051372f05f1c42
   max signs : 1073741824

````
Signing null ...
   ... Success. Signature saved in null.sig
|      names      |  counts  | minimums |     averages      | maximums |
|-----------------|----------|----------|-------------------|----------|
|     H_start     | 26760501 |          |                   |          |
|    H_update     | 26864949 |    22    | 54.91023604772151 |   110    |
|    H_finish     | 26760501 |          |                   |          |
| H_blocksPerHash | 26760501 |    1     | 1.00206629165874  |    18    |
|    H_blocks     | 26815796 |          |                   |          |

````
-rw-r--r-- 1 sebastien.riou 1049089 68 Aug  9 14:40 test.prv
-rw-r--r-- 1 sebastien.riou 1049089 60 Aug  9 14:36 test.pub
-rw-r--r-- 1 sebastien.riou 1049089 4472 Aug  9 14:40 null.sig
````
Signature in null.sig is valid.
|      names      | counts | minimums |      averages      | maximums |
|-----------------|--------|----------|--------------------|----------|
|     H_start     | 13554  |          |                    |          |
|    H_update     | 13656  |    22    | 54.89682190978325  |   110    |
|    H_finish     | 13554  |          |                    |          |
| H_blocksPerHash | 13554  |    1     | 1.0061236535340121 |    18    |
|    H_blocks     | 13637  |          |                    |          |

## --levels=3 --lms=10 --lmots=4 --alg=sha256 --trunc=32
````
Private Key: test.prv
HSS private key
   levels    : 3
   level=0   : LMS private key
   LMS type  : 00000006
   LMOTS type: 00000003
   I         : c5ee78072b9f4049022880ae7a42d7b8
   SEED      : efd7d62add092f8c2ed210ca668448437eefecb11595cd405bf58300721e3ee0
   q         : 00000002
   pub       : c1f34af0f9fa959dcd8d25d3870ad5528597da40cd5819ca2cb60319e22c8b9d
   level=1   : LMS private key
   LMS type  : 00000006
   LMOTS type: 00000003
   I         : 5741c3f0f80fcae4606f1296434c9ab6
   SEED      : 29c9c41dd02735431ba631981d121a4d18292e1c497a067e0bef546c8c5a8886
   q         : 00000001
   pub       : c4b6cd92d8593ce72f57562a1e6a5cd09aa9b2c2b19bfbdc174990c2416f0200
   level=2   : LMS private key
   LMS type  : 00000006
   LMOTS type: 00000003
   I         : 73e34f608914446a8ddf69172cd957cd
   SEED      : a8641c99cc08c787a0e93076a9dcdc0d3854bf4c230bd1c3c95f15f81d0363ac
   q         : 00000000
   pub       : 4d291b9de04c11b5f0b92dab926717341c3f0a0cc73ae656753e4a84cf54a74e
   max signs : 1073741824

Public Key: test.pub
HSS public key
   levels    : 3
   LMS type  : 00000006
   LMOTS type: 00000003
   I         : c5ee78072b9f4049022880ae7a42d7b8
   K         : c1f34af0f9fa959dcd8d25d3870ad5528597da40cd5819ca2cb60319e22c8b9d
   max signs : 1073741824

````
Signing null ...
   ... Success. Signature saved in null.sig
|      names      | counts  | minimums |      averages      | maximums |
|-----------------|---------|----------|--------------------|----------|
|     H_start     | 3304131 |          |                    |          |
|    H_update     | 3509955 |    22    | 53.648657318968475 |   110    |
|    H_finish     | 3304131 |          |                    |          |
| H_blocksPerHash | 3304131 |    1     | 1.0316110347925067 |    34    |
|    H_blocks     | 3408578 |          |                    |          |

````
-rw-r--r-- 1 sebastien.riou 1049089 68 Aug  9 14:48 test.prv
-rw-r--r-- 1 sebastien.riou 1049089 60 Aug  9 14:47 test.pub
-rw-r--r-- 1 sebastien.riou 1049089 7640 Aug  9 14:48 null.sig
````
Signature in null.sig is valid.
|      names      | counts | minimums |      averages      | maximums |
|-----------------|--------|----------|--------------------|----------|
|     H_start     |  1524  |          |                    |          |
|    H_update     |  1725  |    22    |  52.8631884057971  |   110    |
|    H_finish     |  1524  |          |                    |          |
| H_blocksPerHash |  1524  |    1     | 1.0859580052493438 |    34    |
|    H_blocks     |  1655  |          |                    |          |


## --levels=3 --lms=10 --lmots=1 --alg=sha256 --trunc=32
````
Private Key: test.prv
HSS private key
   levels    : 3
   level=0   : LMS private key
   LMS type  : 00000006
   LMOTS type: 00000001
   I         : 73b7d1cc5893b57604d4ca5d0f8fab36
   SEED      : 25376f990488b8a33e18d58ce99df2fe791b44afad071663c234059efe69b489
   q         : 00000002
   pub       : afc7e04f83b885317a17e8a915850b1fb3c54390c739f72dea3ec85a4b342f1f
   level=1   : LMS private key
   LMS type  : 00000006
   LMOTS type: 00000001
   I         : 19612d8fbe0e5b13998bb5b67f93f82c
   SEED      : ec1255a0a38cb68ee3bf40f3c7a9a8faec28c55267a885a31ed0de247032e1d9
   q         : 00000001
   pub       : deedbc16df97c499ef7527f57a3fde956f6c1ce8f99e97f03aa2824c5e760109
   level=2   : LMS private key
   LMS type  : 00000006
   LMOTS type: 00000001
   I         : 827384a9bef8fbf6a038d7ef45cb047f
   SEED      : c39d8228f8ec18798e24dbd8276e733f3a777e5c3098705f0f3fdcfeefa8cd0e
   q         : 00000000
   pub       : 64f6beb0f66273abac46e7fc74350bac23e578cf038e2817608fbdd9aaf2aa22
   max signs : 1073741824

Public Key: test.pub
HSS public key
   levels    : 3
   LMS type  : 00000006
   LMOTS type: 00000001
   I         : 73b7d1cc5893b57604d4ca5d0f8fab36
   K         : afc7e04f83b885317a17e8a915850b1fb3c54390c739f72dea3ec85a4b342f1f
   max signs : 1073741824

````
Signing null ...
   ... Success. Signature saved in null.sig
|      names      | counts  | minimums |      averages      | maximums |
|-----------------|---------|----------|--------------------|----------|
|     H_start     | 1638578 |          |                    |          |
|    H_update     | 2452658 |    22    | 47.36214751506325  |   110    |
|    H_finish     | 1638578 |          |                    |          |
| H_blocksPerHash | 1638578 |    1     | 1.2493472999149262 |   133    |
|    H_blocks     | 2047153 |          |                    |          |

````
-rw-r--r-- 1 sebastien.riou 1049089 68 Aug  9 14:49 test.prv
-rw-r--r-- 1 sebastien.riou 1049089 60 Aug  9 14:49 test.pub
-rw-r--r-- 1 sebastien.riou 1049089 26648 Aug  9 14:49 null.sig
````
Signature in null.sig is valid.
|      names      | counts | minimums |      averages      | maximums |
|-----------------|--------|----------|--------------------|----------|
|     H_start     |  427   |          |                    |          |
|    H_update     |  1222  |    22    | 40.803600654664486 |   110    |
|    H_finish     |  427   |          |                    |          |
| H_blocksPerHash |  427   |    1     | 2.002341920374707  |   133    |
|    H_blocks     |  855   |          |                    |          |


## --levels=3 --lms=5 --lmots=1 --alg=sha256 --trunc=32
````
Private Key: test.prv
HSS private key
   levels    : 3
   level=0   : LMS private key
   LMS type  : 00000005
   LMOTS type: 00000001
   I         : bf1c231395aa0bd402b2d3d5ccb71644
   SEED      : d163adfba4c6b82e8bd2941977684ca34eeab2f3fd77d9974dbf019be027c875
   q         : 00000002
   pub       : 26305aebc2e983e2f753968eef8598c1f0f8d7d588c1f1a7caaa7a88d53d551f
   level=1   : LMS private key
   LMS type  : 00000005
   LMOTS type: 00000001
   I         : 0ca6d6f8e2c577205cce425738641c1a
   SEED      : d5834d4258f998351c3120cbfe7952cb1e2f3ad094f18040137e2b4ffbe2cf64
   q         : 00000001
   pub       : 9488b8caa8c6ff0e91470b9ea78452c12423905fd21a3d87d780418d61e101cf
   level=2   : LMS private key
   LMS type  : 00000005
   LMOTS type: 00000001
   I         : 1477a747f028e843e97235ef6f76cc4f
   SEED      : a085c5dcaee60b705c01a5fe9296409f38ec5b17ae9a6afc605d5e4269bbb03d
   q         : 00000000
   pub       : 792fbe36d983c3f413cb0dd1f8ee317a37c6b9c5effc1fed0c9f000448591eb7
   max signs : 32768

Public Key: test.pub
HSS public key
   levels    : 3
   LMS type  : 00000005
   LMOTS type: 00000001
   I         : bf1c231395aa0bd402b2d3d5ccb71644
   K         : 26305aebc2e983e2f753968eef8598c1f0f8d7d588c1f1a7caaa7a88d53d551f
   max signs : 32768

````
Signing null ...
   ... Success. Signature saved in null.sig
|      names      | counts | minimums |     averages      | maximums |
|-----------------|--------|----------|-------------------|----------|
|     H_start     | 52345  |          |                   |          |
|    H_update     | 77785  |    22    | 47.47423025004821 |   110    |
|    H_finish     | 52345  |          |                   |          |
| H_blocksPerHash | 52345  |    1     | 1.243901041169166 |   133    |
|    H_blocks     | 65112  |          |                   |          |

````
-rw-r--r-- 1 sebastien.riou 1049089 68 Aug  9 14:52 test.prv
-rw-r--r-- 1 sebastien.riou 1049089 60 Aug  9 14:52 test.pub
-rw-r--r-- 1 sebastien.riou 1049089 26168 Aug  9 14:52 null.sig
````
Signature in null.sig is valid.
|      names      | counts | minimums |      averages      | maximums |
|-----------------|--------|----------|--------------------|----------|
|     H_start     |  437   |          |                    |          |
|    H_update     |  1232  |    22    | 40.541396103896105 |   110    |
|    H_finish     |  437   |          |                    |          |
| H_blocksPerHash |  437   |    1     | 1.9450800915331807 |   133    |
|    H_blocks     |  850   |          |                    |          |


## --levels=3 --lms=5 --lmots=4 --alg=sha256 --trunc=32
````
Private Key: test.prv
HSS private key
   levels    : 3
   level=0   : LMS private key
   LMS type  : 00000005
   LMOTS type: 00000003
   I         : 43fb32d640cb181acb620176da50fcac
   SEED      : a0dc1424b3cd4b92f6b1dd86bd6e278c0201b0d7b366588e36e9bfaeb9f8377d
   q         : 00000002
   pub       : 0fadcb3531f13545c092a7f9c1bb8487f7a49c8d84fdd04df6b608135233b6c1
   level=1   : LMS private key
   LMS type  : 00000005
   LMOTS type: 00000003
   I         : baa7e1d454f769fc973daa4daf022c17
   SEED      : b59dfe7af4c3bc4ebd0cfcf1cd123c9f68474f7330e8a3f096f9ece88f0e2404
   q         : 00000001
   pub       : 35ae8ef80c972a5dc1ad5ef860e6b4a9ea75b5b25459536c8fe8179912c0cd14
   level=2   : LMS private key
   LMS type  : 00000005
   LMOTS type: 00000003
   I         : 76b8644f3019c025b0eda1f9e24b837a
   SEED      : 306895766bd15c25b5e4c25581ce3ccb06db857f7cf751da13500d09cbd0fef8
   q         : 00000000
   pub       : 42b3393dbd8d24f9026eb9c03601196f330348762d77cb9bf9d9e82c87f53a35
   max signs : 32768

Public Key: test.pub
HSS public key
   levels    : 3
   LMS type  : 00000005
   LMOTS type: 00000003
   I         : 43fb32d640cb181acb620176da50fcac
   K         : 0fadcb3531f13545c092a7f9c1bb8487f7a49c8d84fdd04df6b608135233b6c1
   max signs : 32768

````
Signing null ...
   ... Success. Signature saved in null.sig
|      names      | counts | minimums |      averages      | maximums |
|-----------------|--------|----------|--------------------|----------|
|     H_start     | 104916 |          |                    |          |
|    H_update     | 111348 |    22    | 53.668965764989046 |   110    |
|    H_finish     | 104916 |          |                    |          |
| H_blocksPerHash | 104916 |    1     | 1.0311010713332571 |    34    |
|    H_blocks     | 108179 |          |                    |          |

````
-rw-r--r-- 1 sebastien.riou 1049089 68 Aug  9 14:53 test.prv
-rw-r--r-- 1 sebastien.riou 1049089 60 Aug  9 14:53 test.pub
-rw-r--r-- 1 sebastien.riou 1049089 7160 Aug  9 14:53 null.sig
````
Signature in null.sig is valid.
|      names      | counts | minimums |      averages      | maximums |
|-----------------|--------|----------|--------------------|----------|
|     H_start     |  1524  |          |                    |          |
|    H_update     |  1725  |    22    |  52.5936231884058  |   110    |
|    H_finish     |  1524  |          |                    |          |
| H_blocksPerHash |  1524  |    1     | 1.0761154855643045 |    34    |
|    H_blocks     |  1640  |          |                    |          |


## --levels=2 --lms=10 --lmots=1 --alg=sha256 --trunc=32
````
Private Key: test.prv
HSS private key
   levels    : 2
   level=0   : LMS private key
   LMS type  : 00000006
   LMOTS type: 00000001
   I         : 4f1f61a5422ff723c3f4f2bfc7cf2acd
   SEED      : d82fffdd75c351d8ec10b66e5c4f8238e17b274e41b415399718089f99cf989f
   q         : 00000002
   pub       : e129b0c6b355df03cc4f89b37c4d0f8ff674b7df91d35bf8593ad90b2cfa32bf
   level=1   : LMS private key
   LMS type  : 00000006
   LMOTS type: 00000001
   I         : 2461df52c3053fa9c6ba2bdee521bd1b
   SEED      : 7bbd8d2e4da352d505aebf7c52aeed11360313f31ec2a4847265a02dd0b44d45
   q         : 00000000
   pub       : 328e84e2b31d654336a173fef733a7ff7aedfa9eb95ce4e0fec68fe46855b32c
   max signs : 1048576

Public Key: test.pub
HSS public key
   levels    : 2
   LMS type  : 00000006
   LMOTS type: 00000001
   I         : 4f1f61a5422ff723c3f4f2bfc7cf2acd
   K         : e129b0c6b355df03cc4f89b37c4d0f8ff674b7df91d35bf8593ad90b2cfa32bf
   max signs : 1048576

````
Signing null ...
   ... Success. Signature saved in null.sig
|      names      | counts  | minimums |      averages      | maximums |
|-----------------|---------|----------|--------------------|----------|
|     H_start     | 1092357 |          |                    |          |
|    H_update     | 1635077 |    22    | 47.362003746612544 |   110    |
|    H_finish     | 1092357 |          |                    |          |
| H_blocksPerHash | 1092357 |    1     | 1.2493534622838505 |   133    |
|    H_blocks     | 1364740 |          |                    |          |

````
-rw-r--r-- 1 sebastien.riou 1049089 68 Aug  9 14:58 test.prv
-rw-r--r-- 1 sebastien.riou 1049089 60 Aug  9 14:58 test.pub
-rw-r--r-- 1 sebastien.riou 1049089 17748 Aug  9 14:58 null.sig
````
Signature in null.sig is valid.
|      names      | counts | minimums |      averages      | maximums |
|-----------------|--------|----------|--------------------|----------|
|     H_start     |  313   |          |                    |          |
|    H_update     |  843   |    22    | 41.258600237247926 |   110    |
|    H_finish     |  313   |          |                    |          |
| H_blocksPerHash |  313   |    1     | 1.9105431309904153 |   133    |
|    H_blocks     |  598   |          |                    |          |

## --levels=2 --lms=10 --lmots=4 --alg=sha256 --trunc=32
````
Private Key: test.prv
HSS private key
   levels    : 2
   level=0   : LMS private key
   LMS type  : 00000006
   LMOTS type: 00000003
   I         : 3e43d5a04697106b4059d3e1159f27e4
   SEED      : eb825ba19588a9d2a23b9f372e743c10cfaaa0ab1a987adf0ed153580c7bdce7
   q         : 00000002
   pub       : a6de301590421fc78d85a4f3b4c0bd2502b68ee03dfea143a6a06bec7aa9c497
   level=1   : LMS private key
   LMS type  : 00000006
   LMOTS type: 00000003
   I         : 8ad7873d52c7580b80f921e6b7ce65a9
   SEED      : f06013624e074e8575092b876a1a3499f8cd829865e56f6f7cd28313c0fb4483
   q         : 00000000
   pub       : 31fa789520161d8d77bf09e3b6931fbd5992b4e9d0c9f8719f194e1f191f7711
   max signs : 1048576

Public Key: test.pub
HSS public key
   levels    : 2
   LMS type  : 00000006
   LMOTS type: 00000003
   I         : 3e43d5a04697106b4059d3e1159f27e4
   K         : a6de301590421fc78d85a4f3b4c0bd2502b68ee03dfea143a6a06bec7aa9c497
   max signs : 1048576

````
Signing null ...
   ... Success. Signature saved in null.sig
|      names      | counts  | minimums |      averages      | maximums |
|-----------------|---------|----------|--------------------|----------|
|     H_start     | 2202754 |          |                    |          |
|    H_update     | 2339970 |    22    | 53.64864934165823  |   110    |
|    H_finish     | 2202754 |          |                    |          |
| H_blocksPerHash | 2202754 |    1     | 1.0316108834667874 |    34    |
|    H_blocks     | 2272385 |          |                    |          |

````
-rw-r--r-- 1 sebastien.riou 1049089 68 Aug  9 15:00 test.prv
-rw-r--r-- 1 sebastien.riou 1049089 60 Aug  9 15:00 test.pub
-rw-r--r-- 1 sebastien.riou 1049089 5076 Aug  9 15:00 null.sig
````
Signature in null.sig is valid.
|      names      | counts | minimums |      averages      | maximums |
|-----------------|--------|----------|--------------------|----------|
|     H_start     |  1016  |          |                    |          |
|    H_update     |  1150  |    22    | 52.84695652173913  |   110    |
|    H_finish     |  1016  |          |                    |          |
| H_blocksPerHash |  1016  |    1     | 1.0856299212598426 |    34    |
|    H_blocks     |  1103  |          |                    |          |


## --levels=2 --lms=10 --lmots=8 --alg=sha256 --trunc=32
````
Private Key: test.prv
HSS private key
   levels    : 2
   level=0   : LMS private key
   LMS type  : 00000006
   LMOTS type: 00000004
   I         : 35a22f0278922a3990c693889a665905
   SEED      : d5c3c43b2190862d39ae265d10ee6e79608bc4f2dfdbf47af08ab53c0940a331
   q         : 00000002
   pub       : cf9fefe91ce2ce7d42053e652ab565b0610797344b776500a6b4ccb7e52dcdb2
   level=1   : LMS private key
   LMS type  : 00000006
   LMOTS type: 00000004
   I         : 13182c99f17bdaa7eac12dc936a89b5a
   SEED      : 39ead7c067f5c4411c9de4211b245b0918a5c404164481a468518559c66dcffe
   q         : 00000000
   pub       : 4d0aa612f320437e025de23c4d4fb54ced0ee312c68fd760ad6d46ea5afc5f29
   max signs : 1048576

Public Key: test.pub
HSS public key
   levels    : 2
   LMS type  : 00000006
   LMOTS type: 00000004
   I         : 35a22f0278922a3990c693889a665905
   K         : cf9fefe91ce2ce7d42053e652ab565b0610797344b776500a6b4ccb7e52dcdb2
   max signs : 1048576

````
Signing null ...
   ... Success. Signature saved in null.sig
|      names      |  counts  | minimums |      averages      | maximums |
|-----------------|----------|----------|--------------------|----------|
|     H_start     | 17840419 |          |                    |          |
|    H_update     | 17910051 |    22    |  54.9102354314904  |   110    |
|    H_finish     | 17840419 |          |                    |          |
| H_blocksPerHash | 17840419 |    1     | 1.0020662631298065 |    18    |
|    H_blocks     | 17877282 |          |                    |          |

````
-rw-r--r-- 1 sebastien.riou 1049089 68 Aug  9 15:05 test.prv
-rw-r--r-- 1 sebastien.riou 1049089 60 Aug  9 15:02 test.pub
-rw-r--r-- 1 sebastien.riou 1049089 2964 Aug  9 15:05 null.sig
````
Signature in null.sig is valid.
|      names      | counts | minimums |      averages      | maximums |
|-----------------|--------|----------|--------------------|----------|
|     H_start     |  8951  |          |                    |          |
|    H_update     |  9019  |    22    | 54.893779798203795 |   110    |
|    H_finish     |  8951  |          |                    |          |
| H_blocksPerHash |  8951  |    1     | 1.0061445648530891 |    18    |
|    H_blocks     |  9006  |          |                    |          |


## --levels=2 --lms=10 --lmots=2 --alg=sha256 --trunc=32
````
Private Key: test.prv
HSS private key
   levels    : 2
   level=0   : LMS private key
   LMS type  : 00000006
   LMOTS type: 00000002
   I         : 3d624fcde15431afa6e701ff1c40692f
   SEED      : e388758cd6a35714f46d4c86106cdfce9ccbf14fb82a22f60050d21469545f70
   q         : 00000002
   pub       : efd43b0a7e30b7a5bf11822c5e31226145d9fe69df73eff63f2b466bbb2cdc61
   level=1   : LMS private key
   LMS type  : 00000006
   LMOTS type: 00000002
   I         : 2df75fb4f72e01b455261f2f6da7da28
   SEED      : c5e62085fb1ce6fa04b7adeaa0f3ea7e3ddff7833104df27793841cdc9344aa3
   q         : 00000000
   pub       : 2c6f31e651b16693fa2737062fbffde36ece4b39ed13a5f6dc958995c6abe737
   max signs : 1048576

Public Key: test.pub
HSS public key
   levels    : 2
   LMS type  : 00000006
   LMOTS type: 00000002
   I         : 3d624fcde15431afa6e701ff1c40692f
   K         : efd43b0a7e30b7a5bf11822c5e31226145d9fe69df73eff63f2b466bbb2cdc61
   max signs : 1048576

````
Signing null ...
   ... Success. Signature saved in null.sig
|      names      | counts  | minimums |      averages      | maximums |
|-----------------|---------|----------|--------------------|----------|
|     H_start     | 1096369 |          |                    |          |
|    H_update     | 1368753 |    22    | 50.418469219793494 |   110    |
|    H_finish     | 1096369 |          |                    |          |
| H_blocksPerHash | 1096369 |    1     | 1.1251540311701627 |    67    |
|    H_blocks     | 1233584 |          |                    |          |

````
-rw-r--r-- 1 sebastien.riou 1049089 68 Aug  9 15:07 test.prv
-rw-r--r-- 1 sebastien.riou 1049089 60 Aug  9 15:07 test.pub
-rw-r--r-- 1 sebastien.riou 1049089 9300 Aug  9 15:07 null.sig
````
Signature in null.sig is valid.
|      names      | counts | minimums |      averages      | maximums |
|-----------------|--------|----------|--------------------|----------|
|     H_start     |  401   |          |                    |          |
|    H_update     |  667   |    22    | 46.73613193403298  |   110    |
|    H_finish     |  401   |          |                    |          |
| H_blocksPerHash |  401   |    1     | 1.3815461346633418 |    67    |
|    H_blocks     |  554   |          |                    |          |


## --levels=1 --lms=10 --lmots=2 --alg=sha256 --trunc=32
````
Private Key: test.prv
HSS private key
   levels    : 1
   level=0   : LMS private key
   LMS type  : 00000006
   LMOTS type: 00000002
   I         : d08a52c33ddefe54c8ebb77260bb5f51
   SEED      : 2992b0210333d52892da31dd02512eb4816cce3010dcd22011fa512eee9dee09
   q         : 00000000
   pub       : 8f1b29817de8b69b90ffb1b8f68f268032fa57f7f7b6601891ce9a5cb0bdd3a2
   max signs : 1024

Public Key: test.pub
HSS public key
   levels    : 1
   LMS type  : 00000006
   LMOTS type: 00000002
   I         : d08a52c33ddefe54c8ebb77260bb5f51
   K         : 8f1b29817de8b69b90ffb1b8f68f268032fa57f7f7b6601891ce9a5cb0bdd3a2
   max signs : 1024

````
Signing null ...
   ... Success. Signature saved in null.sig
|      names      | counts | minimums |      averages      | maximums |
|-----------------|--------|----------|--------------------|----------|
|     H_start     | 548177 |          |                    |          |
|    H_update     | 684369 |    22    | 50.418378097196104 |    86    |
|    H_finish     | 548177 |          |                    |          |
| H_blocksPerHash | 548177 |    1     | 1.1251548313774566 |    67    |
|    H_blocks     | 616784 |          |                    |          |

````
-rw-r--r-- 1 sebastien.riou 1049089 68 Aug  9 15:09 test.prv
-rw-r--r-- 1 sebastien.riou 1049089 60 Aug  9 15:09 test.pub
-rw-r--r-- 1 sebastien.riou 1049089 4624 Aug  9 15:09 null.sig
````
Signature in null.sig is valid.
|      names      | counts | minimums |      averages      | maximums |
|-----------------|--------|----------|--------------------|----------|
|     H_start     |  208   |          |                    |          |
|    H_update     |  341   |    22    | 46.83577712609971  |    86    |
|    H_finish     |  208   |          |                    |          |
| H_blocksPerHash |  208   |    1     | 1.3653846153846154 |    67    |
|    H_blocks     |  284   |          |                    |          |

## --levels=1 --lms=5 --lmots=2 --alg=sha256 --trunc=32
````
Private Key: test.prv
HSS private key
   levels    : 1
   level=0   : LMS private key
   LMS type  : 00000005
   LMOTS type: 00000002
   I         : 211c0327c604e2e5fa837415923aa3f4
   SEED      : 861745f80c8c95aef24dcb28e49161ec6129bb998a2a39a05032dda05bf41a80
   q         : 00000000
   pub       : c2bf35593309af9148e0f293ad5136e35275f6ad1ac6553b819f9870e219d93c
   max signs : 32

Public Key: test.pub
HSS public key
   levels    : 1
   LMS type  : 00000005
   LMOTS type: 00000002
   I         : 211c0327c604e2e5fa837415923aa3f4
   K         : c2bf35593309af9148e0f293ad5136e35275f6ad1ac6553b819f9870e219d93c
   max signs : 32

````
Signing null ...
   ... Success. Signature saved in null.sig
|      names      | counts | minimums |     averages      | maximums |
|-----------------|--------|----------|-------------------|----------|
|     H_start     | 17460  |          |                   |          |
|    H_update     | 21716  |    22    | 50.48646159513723 |    86    |
|    H_finish     | 17460  |          |                   |          |
| H_blocksPerHash | 17460  |    1     | 1.122737686139748 |    67    |
|    H_blocks     | 19603  |          |                   |          |

````
-rw-r--r-- 1 sebastien.riou 1049089 68 Aug  9 15:12 test.prv
-rw-r--r-- 1 sebastien.riou 1049089 60 Aug  9 15:12 test.pub
-rw-r--r-- 1 sebastien.riou 1049089 4464 Aug  9 15:12 null.sig
````
Signature in null.sig is valid.
|      names      | counts | minimums |      averages      | maximums |
|-----------------|--------|----------|--------------------|----------|
|     H_start     |  200   |          |                    |          |
|    H_update     |  333   |    22    | 46.174174174174176 |    86    |
|    H_finish     |  200   |          |                    |          |
| H_blocksPerHash |  200   |    1     |       1.355        |    67    |
|    H_blocks     |  271   |          |                    |          |


## --levels=2 --lms=5 --lmots=2 --alg=sha256 --trunc=32
````
Private Key: test.prv
HSS private key
   levels    : 2
   level=0   : LMS private key
   LMS type  : 00000005
   LMOTS type: 00000002
   I         : 12e7e355b8c507752cea72845e3ae299
   SEED      : c6aa68d10e15ac386c1a18bcfd490fd07773549d5801e68ce7486c26b79f348b
   q         : 00000002
   pub       : 0a40d17741fbf573a951abc870987af6926b521a60d6f8042738922737d58d85
   level=1   : LMS private key
   LMS type  : 00000005
   LMOTS type: 00000002
   I         : 78084beeae1ae12f51f53128cb46c5b5
   SEED      : 954190ac5892da2ef81b806b4e10b3ad85290fce3b8bee79eeeecd3571997478
   q         : 00000000
   pub       : dad1ab80fbe8204039b06cbffae49343c8b67da96fca457e4308f04cefcefddc
   max signs : 1024

Public Key: test.pub
HSS public key
   levels    : 2
   LMS type  : 00000005
   LMOTS type: 00000002
   I         : 12e7e355b8c507752cea72845e3ae299
   K         : 0a40d17741fbf573a951abc870987af6926b521a60d6f8042738922737d58d85
   max signs : 1024

````
Signing null ...
   ... Success. Signature saved in null.sig
|      names      | counts | minimums |      averages      | maximums |
|-----------------|--------|----------|--------------------|----------|
|     H_start     | 34926  |          |                    |          |
|    H_update     | 43438  |    22    | 50.48837423454118  |   110    |
|    H_finish     | 34926  |          |                    |          |
| H_blocksPerHash | 34926  |    1     | 1.1227452327778733 |    67    |
|    H_blocks     | 39213  |          |                    |          |

````
-rw-r--r-- 1 sebastien.riou 1049089 68 Aug  9 15:13 test.prv
-rw-r--r-- 1 sebastien.riou 1049089 60 Aug  9 15:13 test.pub
-rw-r--r-- 1 sebastien.riou 1049089 8980 Aug  9 15:13 null.sig
````
Signature in null.sig is valid.
|      names      | counts | minimums |      averages      | maximums |
|-----------------|--------|----------|--------------------|----------|
|     H_start     |  394   |          |                    |          |
|    H_update     |  660   |    22    | 46.17878787878788  |   110    |
|    H_finish     |  394   |          |                    |          |
| H_blocksPerHash |  394   |    1     | 1.3629441624365481 |    67    |
|    H_blocks     |  537   |          |                    |          |

## --levels=3 --lms=5 --lmots=2 --alg=sha256 --trunc=32
````
Private Key: test.prv
HSS private key
   levels    : 3
   level=0   : LMS private key
   LMS type  : 00000005
   LMOTS type: 00000002
   I         : 3834e2438a735ca54f0c95844a02773d
   SEED      : a90331eb8a8940fe8fe7f8d95985f2b79a3fe85cae0a3aa52fcc4c7289a9f3c2
   q         : 00000002
   pub       : 82a8b77790614b044a869cbefe58a7b1052241efb79ab437d20835987246d3cd
   level=1   : LMS private key
   LMS type  : 00000005
   LMOTS type: 00000002
   I         : 3568a4199e4665cc6e15100c195a46df
   SEED      : 395fd91f9e9e1b48fbe29032a9d49b8db7650a7ca3cb136532f111bc05e51345
   q         : 00000001
   pub       : d71de3ed41e179a3ce6bea5f7848ffe3ad2f642711390e213ffa9b681280421b
   level=2   : LMS private key
   LMS type  : 00000005
   LMOTS type: 00000002
   I         : 159f3038bed8625eb68911b96d8b9302
   SEED      : e4896c9f30067c8de50d40ffa91a3ac54721416a27d2c3a6895dc8abf495555f
   q         : 00000000
   pub       : 0ece293992aa5463f6de67bb0bc3c7e369871518c4c8a491bc8247b0dcb6ef55
   max signs : 32768

Public Key: test.pub
HSS public key
   levels    : 3
   LMS type  : 00000005
   LMOTS type: 00000002
   I         : 3834e2438a735ca54f0c95844a02773d
   K         : 82a8b77790614b044a869cbefe58a7b1052241efb79ab437d20835987246d3cd
   max signs : 32768

````
Signing null ...
   ... Success. Signature saved in null.sig
|      names      | counts | minimums |      averages      | maximums |
|-----------------|--------|----------|--------------------|----------|
|     H_start     | 52350  |          |                    |          |
|    H_update     | 65118  |    22    | 50.48610215301453  |   110    |
|    H_finish     | 52350  |          |                    |          |
| H_blocksPerHash | 52350  |    1     | 1.1228462273161413 |    67    |
|    H_blocks     | 58781  |          |                    |          |

````
-rw-r--r-- 1 sebastien.riou 1049089 68 Aug  9 15:15 test.prv
-rw-r--r-- 1 sebastien.riou 1049089 60 Aug  9 15:15 test.pub
-rw-r--r-- 1 sebastien.riou 1049089 13496 Aug  9 15:15 null.sig
````
Signature in null.sig is valid.
|      names      | counts | minimums |      averages      | maximums |
|-----------------|--------|----------|--------------------|----------|
|     H_start     |  630   |          |                    |          |
|    H_update     |  1029  |    22    | 46.540330417881435 |   110    |
|    H_finish     |  630   |          |                    |          |
| H_blocksPerHash |  630   |    1     | 1.3412698412698412 |    67    |
|    H_blocks     |  845   |          |                    |          |

## --levels=3 --lms=10 --lmots=2 --alg=sha256 --trunc=32
````
Private Key: test.prv
HSS private key
   levels    : 3
   level=0   : LMS private key
   LMS type  : 00000006
   LMOTS type: 00000002
   I         : 095e207693a52a46c5b626e47d8c7fc1
   SEED      : 8d555bb87e03b2a1a10663bd2ccba1ef45414f6f635709ba45d0e7ef1be0de48
   q         : 00000002
   pub       : 5ef966ddd44a9d3a08c58f7b93ff6770c8a5a40096db0b695d2371d3e4cf0182
   level=1   : LMS private key
   LMS type  : 00000006
   LMOTS type: 00000002
   I         : 3ec793a39e10be61f13bc0da62cce933
   SEED      : cfa8e26c77af28f58dac5ea952e9d9deeb874dd206df53ba70e38a2a8f9c8a06
   q         : 00000001
   pub       : b5f9bd4d66a91ee9c1d854f719ad49a6c1b6673c48c657341d38861c70d26954
   level=2   : LMS private key
   LMS type  : 00000006
   LMOTS type: 00000002
   I         : 10e215e14f728e5a9db3f8412f146d15
   SEED      : 43b9b2fd344e1237c88a4090e177891520a385df760c1a424e860da3ddea7192
   q         : 00000000
   pub       : 53a58e92c3e2958ab1c8f3450f9762bb9de3749f1b3a481d527c46424ee97076
   max signs : 1073741824

Public Key: test.pub
HSS public key
   levels    : 3
   LMS type  : 00000006
   LMOTS type: 00000002
   I         : 095e207693a52a46c5b626e47d8c7fc1
   K         : 5ef966ddd44a9d3a08c58f7b93ff6770c8a5a40096db0b695d2371d3e4cf0182
   max signs : 1073741824

````
Signing null ...
   ... Success. Signature saved in null.sig
|      names      | counts  | minimums |      averages      | maximums |
|-----------------|---------|----------|--------------------|----------|
|     H_start     | 1644525 |          |                    |          |
|    H_update     | 2053101 |    22    | 50.41841925945192  |   110    |
|    H_finish     | 1644525 |          |                    |          |
| H_blocksPerHash | 1644525 |    1     | 1.1251565041577356 |    67    |
|    H_blocks     | 1850348 |          |                    |          |

````
-rw-r--r-- 1 sebastien.riou 1049089 68 Aug  9 15:17 test.prv
-rw-r--r-- 1 sebastien.riou 1049089 60 Aug  9 15:17 test.pub
-rw-r--r-- 1 sebastien.riou 1049089 13976 Aug  9 15:17 null.sig
````
Signature in null.sig is valid.
|      names      | counts | minimums |      averages      | maximums |
|-----------------|--------|----------|--------------------|----------|
|     H_start     |  630   |          |                    |          |
|    H_update     |  1029  |    22    | 46.99222546161322  |   110    |
|    H_finish     |  630   |          |                    |          |
| H_blocksPerHash |  630   |    1     | 1.3650793650793651 |    67    |
|    H_blocks     |  860   |          |                    |          |


## --levels=1 --lms=5 --lmots=4 --alg=sha256 --trunc=32
````
Private Key: test.prv
HSS private key
   levels    : 1
   level=0   : LMS private key
   LMS type  : 00000005
   LMOTS type: 00000003
   I         : 60c78c4e250acbc50fa5b93bf243b296
   SEED      : 6cc19029752c3694ff6f20aaed19feffd07cf47db8f132ebc82e1d7412e95ebd
   q         : 00000000
   pub       : 72f2fc0916bc36a6ed6e2f294c2c17bb55c49cb21e8cd6d9310429290dccf1a1
   max signs : 32

Public Key: test.pub
HSS public key
   levels    : 1
   LMS type  : 00000005
   LMOTS type: 00000003
   I         : 60c78c4e250acbc50fa5b93bf243b296
   K         : 72f2fc0916bc36a6ed6e2f294c2c17bb55c49cb21e8cd6d9310429290dccf1a1
   max signs : 32

````
Signing null ...
   ... Success. Signature saved in null.sig
|      names      | counts | minimums |      averages      | maximums |
|-----------------|--------|----------|--------------------|----------|
|     H_start     | 34902  |          |                    |          |
|    H_update     | 37046  |    22    |  53.665442962803   |    86    |
|    H_finish     | 34902  |          |                    |          |
| H_blocksPerHash | 34902  |    1     | 1.0311443470288235 |    34    |
|    H_blocks     | 35989  |          |                    |          |

````
-rw-r--r-- 1 sebastien.riou 1049089 68 Aug  9 15:19 test.prv
-rw-r--r-- 1 sebastien.riou 1049089 60 Aug  9 15:19 test.pub
-rw-r--r-- 1 sebastien.riou 1049089 2352 Aug  9 15:19 null.sig
````
Signature in null.sig is valid.
|      names      | counts | minimums |      averages      | maximums |
|-----------------|--------|----------|--------------------|----------|
|     H_start     |  578   |          |                    |          |
|    H_update     |  645   |    22    | 52.796899224806204 |    86    |
|    H_finish     |  578   |          |                    |          |
| H_blocksPerHash |  578   |    1     | 1.065743944636678  |    34    |
|    H_blocks     |  616   |          |                    |          |

## --levels=1 --lms=10 --lmots=4 --alg=sha256 --trunc=32
````
Private Key: test.prv
HSS private key
   levels    : 1
   level=0   : LMS private key
   LMS type  : 00000006
   LMOTS type: 00000003
   I         : cb905ef60ae47011a4a4c200b9fcf2a3
   SEED      : 2f287c4ee7dda8323b876bf375b7d104ed716aa3dca0f35064a0b080e3a0df1f
   q         : 00000000
   pub       : fcc016418fcd2e3e676ebc7c63c7d2df9aebb3b72bf504595403665ecceccf60
   max signs : 1024

Public Key: test.pub
HSS public key
   levels    : 1
   LMS type  : 00000006
   LMOTS type: 00000003
   I         : cb905ef60ae47011a4a4c200b9fcf2a3
   K         : fcc016418fcd2e3e676ebc7c63c7d2df9aebb3b72bf504595403665ecceccf60
   max signs : 1024

````
Signing null ...
   ... Success. Signature saved in null.sig
|      names      | counts  | minimums |      averages      | maximums |
|-----------------|---------|----------|--------------------|----------|
|     H_start     | 1101317 |          |                    |          |
|    H_update     | 1169925 |    22    | 53.64855610402376  |    86    |
|    H_finish     | 1101317 |          |                    |          |
| H_blocksPerHash | 1101317 |    1     | 1.0316121516329995 |    34    |
|    H_blocks     | 1136132 |          |                    |          |

````
-rw-r--r-- 1 sebastien.riou 1049089 68 Aug  9 15:25 test.prv
-rw-r--r-- 1 sebastien.riou 1049089 60 Aug  9 15:25 test.pub
-rw-r--r-- 1 sebastien.riou 1049089 2512 Aug  9 15:25 null.sig
````
Signature in null.sig is valid.
|      names      | counts | minimums |      averages      | maximums |
|-----------------|--------|----------|--------------------|----------|
|     H_start     |  568   |          |                    |          |
|    H_update     |  635   |    22    | 53.00629921259843  |    86    |
|    H_finish     |  568   |          |                    |          |
| H_blocksPerHash |  568   |    1     | 1.0757042253521127 |    34    |
|    H_blocks     |  611   |          |                    |          |

## --levels=1 --lms=15 --lmots=4 --alg=sha256 --trunc=32
````
Private Key: test.prv
HSS private key
   levels    : 1
   level=0   : LMS private key
   LMS type  : 00000007
   LMOTS type: 00000003
   I         : e307d511a3a80ede87246a126e59b8b9
   SEED      : e742cec34f324d695bbf5936d261a39063d775406ea74f81aae15a6e52a5f414
   q         : 00000000
   pub       : 6516ac91f6f34c04f804bdf500b4c8f06c94721e7543b60f8f6676f92b51925d
   max signs : 32768

Public Key: test.pub
HSS public key
   levels    : 1
   LMS type  : 00000007
   LMOTS type: 00000003
   I         : e307d511a3a80ede87246a126e59b8b9
   K         : 6516ac91f6f34c04f804bdf500b4c8f06c94721e7543b60f8f6676f92b51925d
   max signs : 32768

````
Signing null ...
   ... Success. Signature saved in null.sig
|      names      |  counts  | minimums |      averages      | maximums |
|-----------------|----------|----------|--------------------|----------|
|     H_start     | 35226162 |          |                    |          |
|    H_update     | 37421618 |    22    | 53.648005438995185 |    86    |
|    H_finish     | 35226162 |          |                    |          |
| H_blocksPerHash | 35226162 |    1     | 1.031627373995498  |    34    |
|    H_blocks     | 36340273 |          |                    |          |

````
-rw-r--r-- 1 sebastien.riou 1049089 68 Aug  9 15:36 test.prv
-rw-r--r-- 1 sebastien.riou 1049089 60 Aug  9 15:31 test.pub
-rw-r--r-- 1 sebastien.riou 1049089 2672 Aug  9 15:36 null.sig
````
Signature in null.sig is valid.
|      names      | counts | minimums |      averages      | maximums |
|-----------------|--------|----------|--------------------|----------|
|     H_start     |  528   |          |                    |          |
|    H_update     |  595   |    22    |  53.1327731092437  |    86    |
|    H_finish     |  528   |          |                    |          |
| H_blocksPerHash |  528   |    1     | 1.0909090909090908 |    34    |
|    H_blocks     |  576   |          |                    |          |

## --levels=1 --lms=15 --lmots=2 --alg=sha256 --trunc=32
````
Private Key: test.prv
HSS private key
   levels    : 1
   level=0   : LMS private key
   LMS type  : 00000007
   LMOTS type: 00000002
   I         : 5a6416b251026c370e8be18aa789313f
   SEED      : 07d75a96ea5b9523d193a98410c81dcc03ff9013cfc7587f97c29067d81549d5
   q         : 00000000
   pub       : 6722d68c4ea488fefc9bcf00bc65ea56c51e555299fdc4d44fa6baa577f5bb8c
   max signs : 32768

Public Key: test.pub
HSS public key
   levels    : 1
   LMS type  : 00000007
   LMOTS type: 00000002
   I         : 5a6416b251026c370e8be18aa789313f
   K         : 6722d68c4ea488fefc9bcf00bc65ea56c51e555299fdc4d44fa6baa577f5bb8c
   max signs : 32768

````
Signing null ...
   ... Success. Signature saved in null.sig
|      names      |  counts  | minimums |      averages      | maximums |
|-----------------|----------|----------|--------------------|----------|
|     H_start     | 17531223 |          |                    |          |
|    H_update     | 21889367 |    22    | 50.416238030090135 |    86    |
|    H_finish     | 17531223 |          |                    |          |
| H_blocksPerHash | 17531223 |    1     | 1.1252311376108786 |    67    |
|    H_blocks     | 19726678 |          |                    |          |

````
-rw-r--r-- 1 sebastien.riou 1049089 68 Aug  9 15:44 test.prv
-rw-r--r-- 1 sebastien.riou 1049089 60 Aug  9 15:41 test.pub
-rw-r--r-- 1 sebastien.riou 1049089 4784 Aug  9 15:44 null.sig
````
Signature in null.sig is valid.
|      names      | counts | minimums |     averages      | maximums |
|-----------------|--------|----------|-------------------|----------|
|     H_start     |  207   |          |                   |          |
|    H_update     |  340   |    22    | 47.26764705882353 |    86    |
|    H_finish     |  207   |          |                   |          |
| H_blocksPerHash |  207   |    1     | 1.391304347826087 |    67    |
|    H_blocks     |  288   |          |                   |          |

## --levels=1 --lms=15 --lmots=1 --alg=sha256 --trunc=32
````
Private Key: test.prv
HSS private key
   levels    : 1
   level=0   : LMS private key
   LMS type  : 00000007
   LMOTS type: 00000001
   I         : 854640e5a3e94389fe2bb5412198027e
   SEED      : a13b668a492357a991af77ebb18aee68780f82f71ed1ae9752d7f138088b7655
   q         : 00000000
   pub       : 8a58ec2789f8a4b31885d9e4040146a51074f3af8389e860d17847e4a73d08a9
   max signs : 32768

Public Key: test.pub
HSS public key
   levels    : 1
   LMS type  : 00000007
   LMOTS type: 00000001
   I         : 854640e5a3e94389fe2bb5412198027e
   K         : 8a58ec2789f8a4b31885d9e4040146a51074f3af8389e860d17847e4a73d08a9
   max signs : 32768

````
Signing null ...
   ... Success. Signature saved in null.sig
|      names      |  counts  | minimums |     averages      | maximums |
|-----------------|----------|----------|-------------------|----------|
|     H_start     | 17465753 |          |                   |          |
|    H_update     | 26149273 |    22    | 47.35851428833222 |    86    |
|    H_finish     | 17465753 |          |                   |          |
| H_blocksPerHash | 17465753 |    1     | 1.249525056262962 |   133    |
|    H_blocks     | 21823896 |          |                   |          |

````
-rw-r--r-- 1 sebastien.riou 1049089 68 Aug  9 16:42 test.prv
-rw-r--r-- 1 sebastien.riou 1049089 60 Aug  9 16:39 test.pub
-rw-r--r-- 1 sebastien.riou 1049089 9008 Aug  9 16:42 null.sig
````
Signature in null.sig is valid.
|      names      | counts | minimums |      averages      | maximums |
|-----------------|--------|----------|--------------------|----------|
|     H_start     |  139   |          |                    |          |
|    H_update     |  404   |    22    | 40.977722772277225 |    86    |
|    H_finish     |  139   |          |                    |          |
| H_blocksPerHash |  139   |    1     | 2.0575539568345325 |   133    |
|    H_blocks     |  286   |          |                    |          |


## --levels=1 --lms=15 --lmots=1 --alg=sha256 --trunc=32
````
Private Key: test.prv
HSS private key
   levels    : 1
   level=0   : LMS private key
   LMS type  : 00000007
   LMOTS type: 00000001
   I         : bd8344e6a669d73046f9ba731a562493
   SEED      : 4b65c3dd3675f86e4b97bf75a101ab1849ac82c0a3b37f6586c6eaa06b96b2d8
   q         : 00000000
   pub       : 519a4c763aaedaf07b0c851bfb58f8ba8e8b48d08a1c6f613ee0ca275e14679e
   max signs : 32768

Public Key: test.pub
HSS public key
   levels    : 1
   LMS type  : 00000007
   LMOTS type: 00000001
   I         : bd8344e6a669d73046f9ba731a562493
   K         : 519a4c763aaedaf07b0c851bfb58f8ba8e8b48d08a1c6f613ee0ca275e14679e
   max signs : 32768

````
Signing null ...
   ... Success. Signature saved in null.sig
|      names      |  counts  | minimums |      averages      | maximums |
|-----------------|----------|----------|--------------------|----------|
|     H_start     | 17465745 |          |                    |          |
|    H_update     | 26149265 |    22    |  47.3585119505271  |    86    |
|    H_finish     | 17465745 |          |                    |          |
| H_blocksPerHash | 17465745 |    1     | 1.2495251705552783 |   133    |
|    H_blocks     | 21823888 |          |                    |          |

````
-rw-r--r-- 1 sebastien.riou 1049089 68 Aug  9 18:16 test.prv
-rw-r--r-- 1 sebastien.riou 1049089 60 Aug  9 18:13 test.pub
-rw-r--r-- 1 sebastien.riou 1049089 9008 Aug  9 18:16 null.sig
````
Signature in null.sig is valid.
|      names      | counts | minimums | averages | maximums |
|-----------------|--------|----------|----------|----------|
|     H_start     |  147   |          |          |          |
|    H_update     |  412   |    22    |  41.25   |    86    |
|    H_finish     |  147   |          |          |          |
| H_blocksPerHash |  147   |    1     |   2.0    |   133    |
|    H_blocks     |  294   |          |          |          |

