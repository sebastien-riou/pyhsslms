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

