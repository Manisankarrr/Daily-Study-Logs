#!/usr/bin/bash
if [ ${1,,} = manish ]; then
        echo "Hello manish"
elif [ ${1,,} = help ]; then
        echo "Enter your userName!"
else
        echo "Not manish"
fi