#!/usr/bin/env bash
echo "Content-type: text/html"
echo ""
now="$(date)"
echo '<html><head><title>Hello World - CGI app</title></head>'
echo '<body>'

echo '<h2>Hello World!</h2>'
echo "Computer name : $HOSTNAME<br/>"
echo "The current date and time : ${now}<br/>"
echo '</body>'
echo '</html>'