# DonLimpioLogCleaner
Search keywords from a list in a big log file and print the matched line. It supports to invert the sense of matching. Now it supports STDIN.

The output prints to STDOUT. The error prints to STERR. It's like a supergrep command.

You can grep GB logs in minutes. For example: 8000 keywords to 35 GB logs in 85 minutes.

  ## Help
  
Check the options:
  
    $ ./donLimpioCleaner.py --help
    usage: donLimpioCleaner.py [-h] [-f LOG_FILE] [-v] KEYWORD_FILE

    positional arguments:
      KEYWORD_FILE          Obtain keywords from FILE, one per line

    optional arguments:
      -h, --help            show this help message and exit
      -f LOG_FILE, --file LOG_FILE
                            Obtain log file to process
      -v, --invert-match    Invert the sense of matching, to select non-matching
                            lines.

Run DonLimpioLogCleaner to match:

    $ ./donLimpioCleaner.py ip_list.txt -f firewall.log

Run DonLimpioLogCleaner to inverted match:

    $ ./donLimpioCleaner.py ip_list.txt -f firewall.log -v

Run DonLimpioLogCleaner to match from STDIN:

    $ cat firewall.log | ./donLimpioCleaner.py ip_list.txt
    
Run DonLimpioLogCleaner to inverted match from STDIN:

    $ cat firewall.log | ./donLimpioCleaner.py ip_list.txt -v

  ## Install
  
       pip3 install flashtext
  
  ## Software
 - Python 3
 - flashtext
 
  ## References
  https://dev.to/vi3k6i5/regex-was-taking-5-days-to-run-so-i-built-a-tool-that-did-it-in-15-minutes-c98
