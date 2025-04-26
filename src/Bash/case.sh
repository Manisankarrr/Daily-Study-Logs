#!/bin/bash

case ${1,,} in
        manish | administrator)
                echo "Hello bro"
                ;;
        help)
                echo "Enter the username"
                ;;
        *)
                echo "Who the hell are you?"
esac