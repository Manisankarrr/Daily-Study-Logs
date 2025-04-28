LIST=(one two three four five)

for i in ${LIST[@]}; do echo $i | grep t | wc -c; done


