#!/bin/bash
 #!/bin/bash 
         COUNTER=0
         while [  $COUNTER -lt 1000000 ]; do
             echo $COUNTER
             let COUNTER=COUNTER+1 
         done
#bash count.sh  6.57s user 3.02s system 45% cpu 21.077 total
